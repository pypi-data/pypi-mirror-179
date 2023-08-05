"""OptoDAS module from dastools.

This file is part of dastools.

dastools is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

dastools is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If
not, see https://www.gnu.org/licenses/.

   :Copyright:
       2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany
   :License:
       GPLv3
   :Platform:
       Linux

.. moduleauthor:: Javier Quinteros <javier@gfz-potsdam.de>, GEOFON, GFZ Potsdam
"""

import logging
import datetime
import os
from h5py import File
from h5py import Group
from h5py import Dataset
from .das import Das
from obspy import UTCDateTime
from obspy.core.trace import Stats
from obspy.core.util.attribdict import AttribDict
import numpy as np
from math import floor
from math import ceil
from numbers import Number
from .tdms import PotentialGap
from .tdms import NoData


def unwrap(signal, wrapstep=2 * np.pi, axis=-1):
    """
    Unwrap phase phi by changing absolute jumps greater than wrapStep/2 to
    their wrapStep complement along the given axis. By default (if wrapStep is
    None) standard unwrapping is performed with wrapStep=2*np.pi.

    (Note: np.unwrap in the numpy package has an optional "discont" parameter
    which does not give an expected (or useful) behavior when it deviates
    from default. Use this unwrap implementation instead of the numpy
    implementation if your signal is wrapped with discontinuities that deviate
    from 2*pi.)

    Original code from Alcatel Submarine Networks Norway AS!
    """
    scale = 2 * np.pi / wrapstep
    return (np.unwrap(signal * scale, axis=axis) / scale).astype(signal.dtype)


class OptoDAS(Das):
    """Class to read, process and export seismic waveforms in OptoDAS format

.. note::
    FIXME THIS!
    Some examples with PDN_1km show that for 16 files of 44 MB (704 MB) we see the following
    With simple encoding of I16 and a record of 4096 bytes we use 720MB
    With STEIM2, a data type of I32 and a record of 4096 bytes we use 504 MB
    With STEIM2, a data type of I32, a decimation factor of 5, and a record of 4096 bytes we use 109 MB

    """

    def __enter__(self):
        """Method which allows to use the syntax 'with object:' and use it inside

        Create a buffer space to store the signal coefficients to be convoluted during the decimation
        """
        for channel in self.channels:
            logging.debug('Create empty buffer for channel %s' % channel)
            self.__buffer[channel] = None

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Method which close open resources after using the syntax 'with object:' and use it inside"""
        if self.__fi is not None:
            self.__fi.close()

    def __iter__(self):
        """Iterate through data (or metadata) and filter and decimate if requested

        :returns: Data and attributes for the header, or metadata
        :rtype: tuple(numpy.array, obspy.core.trace.Stats) or dict
        """
        # Create logger
        logs = logging.getLogger('__iter__')

        if self.iterate == 'M':
            for info in self.__iter_metadata__():
                yield info

        else:
            # In the case that we iterate to get data
            # If no decimation is needed
            if self.__decimate == 1:
                for data, stats in self.__iter_data__():
                    # yield data.astype(self.__outdatatype), stats
                    yield data, stats
            else:
                # Use an input buffer to store the data coming in chunks from __iter_data__
                inbuf = dict()
                # Keep values in a buffer before returning them to be packed in miniSEED records
                # Otherwise, the chunks could be too short and the final size of the mSEED
                # would be too large
                outbuf = dict()
                # Keep filtered values which should be later decimated
                nodecimation = dict()
                # Time of the first sample in the next file
                expectedtime = dict()
                # Flag to know if we are at the beginning of the chunk
                # There should be one entry per channel with a default value of True
                startofchunk = dict()

                for data, stats in self.__iter_data__():
                    ch = int(stats['station'])

                    # Check expected time for each channel
                    if ch in expectedtime:
                        if expectedtime[ch] != stats['starttime']:
                            logs.warning('GAP! Expected: %s ; Current: %s' % (expectedtime[ch], stats['starttime']))
                            # Gap!
                            if ch in inbuf:
                                logs.debug('Remove last %s components of previous chunk' % len(inbuf[ch]['data']))
                                del inbuf[ch]

                            # Flush outbuf?
                            if ch in outbuf:
                                if 'data' in outbuf[ch]:
                                    # Set number of points
                                    outbuf[ch]['stats']['npts'] = len(outbuf[ch]['data'])
                                    # outbuf[ch]['stats']['starttime'] += 1/outbuf[ch]['stats']['sampling_rate']
                                    # outbuf[ch]['stats']['npts'] = 1
                                    logs.debug('Flushing: %s %s' % (outbuf[ch]['stats'], outbuf[ch]['data']))
                                    yield outbuf[ch]['data'], outbuf[ch]['stats']
                                # Remove all data and stats from the output buffer after a GAP
                                del outbuf[ch]
                            else:
                                logs.debug('Nothing to flush after GAP')
                            # self.__buffer[ch] = None
                            del expectedtime[ch]
                            # Start the processing of a new chunk after the gap
                            startofchunk[ch] = True

                    expectedtime[ch] = stats['starttime'] + stats['npts']/self.sampling_rate

                    # Store values coming from __iter_data__
                    if ch not in inbuf:
                        # Initialize an idx and array with the first chunk of data
                        inbuf[ch] = {'data': np.array(data),
                                     'stats': stats}
                        # print('inbuf: %s' % inbuf[ch]['stats'])
                    else:
                        inbuf[ch]['data'] = np.append(inbuf[ch]['data'], data)

                    # Set values of stats for the output buffer resulting from the convolution
                    if ch not in outbuf:
                        # Initialize an idx and array with the first chunk of data
                        outbuf[ch] = {'stats': inbuf[ch]['stats'].copy()}

                        # Modify the starting time only if it is the beginning of the signal
                        if (ch not in startofchunk) or startofchunk[ch]:
                            outbuf[ch]['stats']['starttime'] += (len(self.__filter)-1)/(2 * outbuf[ch]['stats']['sampling_rate'])
                            startofchunk[ch] = False

                        # Change the headers to reflect the decimation
                        # Reduce the sampling rate by the decimation factor
                        outbuf[ch]['stats']['sampling_rate'] = stats['sampling_rate']/self.__decimate
                        # print('outbuf new: %s' % outbuf[ch]['stats'])

                    # If there are not enough components move to the next chunk
                    if len(inbuf[ch]['data']) < len(self.__filter):
                        continue

                    # Convolution of inbuf with filter and then leave the last 234 values (len(filter)-1)
                    # This convolution is performed on a long array (inbuf) and a default filter with 235 components
                    # We save the result of the convolution as int32 to be able to use STEIM2 later
                    nodecimation[ch] = np.convolve(inbuf[ch]['data'], self.__filter, 'valid').astype(self.__outdatatype)
                    logs.debug('filtered: %d components' % len(nodecimation[ch]))
                    logs.debug('filtered[%d][:11] %s' % (ch, nodecimation[ch][:11]))
                    logs.debug('filtered[%d][-11:] %s' % (ch, nodecimation[ch][-11:]))

                    # Check if we can copy as many components as a multiple of the decimation factor
                    leftover = len(nodecimation[ch]) % self.__decimate
                    logs.debug('filtered: leave %d components for next iteration %s' %
                               (leftover, nodecimation[ch][-leftover:]))

                    if leftover:
                        if 'data' not in outbuf[ch]:
                            # Take samples each "self.__decimate" components
                            outbuf[ch]['data'] = nodecimation[ch][:-leftover:self.__decimate]
                        else:
                            # Add samples each "self.__decimate" components
                            outbuf[ch]['data'] = np.append(outbuf[ch]['data'],
                                                           nodecimation[ch][:-leftover:self.__decimate])
                    else:
                        if 'data' not in outbuf[ch]:
                            # Take samples each "self.__decimate" components
                            outbuf[ch]['data'] = nodecimation[ch][::self.__decimate]
                        else:
                            # Add samples each "self.__decimate" components
                            outbuf[ch]['data'] = np.append(outbuf[ch]['data'], nodecimation[ch][::self.__decimate])

                    # Remove filtered signal after copying it to the output buffer
                    del nodecimation[ch]

                    logs.debug('outbuf[%d][:11] %s' % (ch, outbuf[ch]['data'][:11]))
                    logs.debug('outbuf[%d][-11:] %s' % (ch, outbuf[ch]['data'][-11:]))

                    # Keep values which will be needed to start again in the next file
                    # to avoid boundary effects. leftover comes from the extra values we already calculated
                    # but we could not use because of decimation. Therefore, we will put them in the beginning
                    # and calculate again
                    valuesprocessed = len(inbuf[ch]['data']) - len(self.__filter) + 1 - leftover
                    logs.debug('values processed: %d' % valuesprocessed)
                    inbuf[ch]['data'] = inbuf[ch]['data'][-len(self.__filter)+1-leftover:]
                    inbuf[ch]['stats']['starttime'] += valuesprocessed / inbuf[ch]['stats']['sampling_rate']

                    # If there is enough data
                    if len(outbuf[ch]['data']) > 2000:
                        outbuf[ch]['stats']['npts'] = len(outbuf[ch]['data'])
                        logs.debug('Sending: %s %s' % (outbuf[ch]['stats'], outbuf[ch]['data']))
                        yield outbuf[ch]['data'], outbuf[ch]['stats']
                        # Reset outbuf with an empty array and the next starttime (in headers)
                        outbuf[ch]['stats']['starttime'] += len(outbuf[ch]['data']) / outbuf[ch]['stats']['sampling_rate']
                        del outbuf[ch]['data']

                # Do I need here to flush all remaining components from outbuf?
                for ch in outbuf:
                    if ('data' in outbuf[ch]) and len(outbuf[ch]['data']):
                        outbuf[ch]['stats']['npts'] = len(outbuf[ch]['data'])
                        logs.debug('Sending: %s %s' % (outbuf[ch]['stats'], outbuf[ch]['data']))
                        yield outbuf[ch]['data'], outbuf[ch]['stats']
                        outbuf[ch]['stats']['starttime'] += len(outbuf[ch]['data']) / outbuf[ch]['stats']['sampling_rate']
                        del outbuf[ch]['data']

    def __init__(self, filename: str, directory: str = '.', chstart: int = 0, chstop: int = None,
                 chstep: int = 1, channels: list = None, starttime: datetime.datetime = None,
                 endtime: datetime.datetime = None, iterate: str = 'D', decimate: int = 1,
                 firfilter: str = 'fir235', networkcode: str = 'XX', channelcode: str = 'HSF',
                 loglevel: str = 'INFO'):
        """Initialize the OptaDAS object selecting the data, channels and decimation

        :param filename: Experiment to read and process. Usually the name of the root directory
        :type filename: str
        :param directory: Directory where experiment is stored
        :type directory: str
        :param chstart: First channel to select
        :type chstart: int
        :param chstop: Last channel to select
        :type chstop: int
        :param chstep: Step between channels in the selection
        :type chstep: int
        :param channels: Selection of channels to work with (list of integers)
        :type channels: list or NoneType
        :param starttime: Start of the selected time window
        :type starttime: datetime.datetime or NoneType
        :param endtime: End of the selected time window
        :type endtime: datetime.datetime or NoneType
        :param iterate: Select either Data (D) or Metadata (M)
        :type iterate: str
        :param decimate: Factor by which the sampling rate is lowered by decimation
        :type decimate: int
        :param firfilter: Filter to apply in case of decimation (fir235 is the only option)
        :type firfilter: str
        :param networkcode: Network code of the experiment. It has to be two alphanumeric characters
        :type networkcode: str
        :param channelcode: Channel code of the experiment. It has to be three alphanumeric characters
        :type channelcode: str
        :param loglevel: Verbosity in the output
        :type loglevel: str
        :raise TypeError: If chstart, or chstop, or chstep are not int. If channels is not a list, or networkcode is
        not a 2 characters code, or channelcode is not a 3 characters code.
        :raise Exception: If channels is empty.
        :raise NoData: If there is no more data available
        """

        # Log level
        self.__loglevel = loglevel
        logs = logging.getLogger('Init OptoDAS')
        logs.setLevel(loglevel)

        project_dir = os.path.dirname(__file__)

        # Decimation factor
        self.__decimate = decimate

        # Selection of channels
        if not isinstance(chstart, Number) or not isinstance(chstep, Number):
            logs.error('chstart and chstep must be ints')
            raise TypeError('chstart and chstep must be ints')

        if not isinstance(chstop, Number) and chstop is not None:
            logs.error('chstop must be an int or None')
            raise TypeError('chstop must be an int or None')

        if not isinstance(channels, list) and channels is not None:
            logs.error('channels must be a list of numbers or None')
            raise TypeError('channels must be a list of numbers or None')

        if not isinstance(networkcode, str) or len(networkcode) != 2:
            logs.error('Network code has to be two alphanumeric characters')
            raise TypeError('Network code has to be two alphanumeric characters')

        if not isinstance(channelcode, str) or len(channelcode) != 3:
            logs.error('Channel code has to be three alphanumeric characters')
            raise TypeError('Channel code has to be three alphanumeric characters')

        self.__chstart = chstart
        self.__chstop = chstop
        self.__chstep = chstep
        self.__networkcode = networkcode
        self.__channelcode = channelcode

        # channels has priority. Otherwise, chstart, chstop and chstep are used
        if channels is not None and isinstance(channels, list):
            self.channels = channels
            # List of channels cannot be empty
            if not len(self.channels):
                raise Exception('Channel list is empty!')

        else:
            # If chstart, chstop and chstep will define the selected channels we need to keep the three
            #  values (start, stop, step) and define the channels later in readmetadata
            self.channels = None
            # self.channels = list(range(chstart, chstop+1, chstep))

        # Time window selection
        self.__twstart = starttime
        self.__twend = endtime

        # Available time window
        self.starttime = None
        self.endtime = None

        # Sampling Rate
        self.sampling_rate = None

        # File currently being processed
        self.__currentfile = None

        # Name of file
        self.__filename = filename
        self.__directory = directory

        # List of available files in the directory
        self.__available = list()

        # Loop through files and load them in __available as 'YYYYMMDD/TTmmSS'
        experimentdir = os.path.join(directory, filename)
        logs.debug('Experiment directory: %s' % experimentdir)
        # Sort based on the name of the Direntry
        for day in sorted(os.scandir(experimentdir), key=lambda x: x.name):  # type: os.DirEntry
            # Entry must be a directory
            if not day.is_dir():
                continue

            logs.debug('Checking day: %s' % day.name)
            # Check format of the directory name (YYYYMMDD)
            try:
                dt = datetime.datetime.strptime(day.name, '%Y%m%d')
            except ValueError:
                logs.warning('Unexpected format in directory name! Date expected... (%s)' % day.name)
                continue

            daydir = os.path.join(experimentdir, day.name)

            for file in sorted(os.scandir(daydir), key=lambda x: x.name):  # type: os.DirEntry
                # Entry must be a file
                if file.is_dir():
                    continue

                logs.debug('Checking time: %s' % day.name)
                # Entry must be a hdf5 file
                if not file.name.endswith('.hdf5'):
                    continue

                # Check that the format of the filename is exactly as expected. Otherwise, send a warning
                try:
                    dt = datetime.datetime.strptime(day.name + file.name[:-5], '%Y%m%d%H%M%S')
                except ValueError:
                    logs.warning('Unexpected format in file name! Time expected... (%s)' % file.name)
                    continue
                self.__available.append({'dt': dt, 'name': os.path.join(experimentdir, day.name, file.name),
                                         'samples': None})
                if self.__twstart is None:
                    self.__twstart = dt

        if not len(self.__available):
            logs.warning('No files found with proper filename.')
            raise NoData()

        # Set the time window selection to the minimum datetime found
        if self.__twstart < self.__available[0]['dt']:
            self.__twstart = self.__available[0]['dt']

        # Keep the values in case we need to reset them
        self.__origstarttime = self.__twstart
        self.__origendtime = self.__twend

        # What should we iterate? D: Data; M: Metadata
        self.iterate = iterate

        # Define a buffer to store the window over the signal to be
        # convoluted with the FIR filter wile decimating
        # Keys will be channel number and the values will be np.arrays
        self.__buffer = dict()

        # Dictionary to save the metadata defined in the file
        self.metadata = dict()

        # Read filter to decimate
        auxfilter = list()
        with open(os.path.join(project_dir, 'data/filters/%s.txt' % firfilter)) as fin:
            for line in fin.readlines():
                auxfilter.append(float(line))

        self.__filter = np.array(auxfilter)
        logs.debug('FIR filter: %s' % self.__filter)

        # Other variables to be read from the headers
        # self.__hasInterleavedData = None
        self.__endian = None
        self.__datatype = None
        self.__datatypesize = None
        self.__outdatatype = 'i4'
        self.numchannels = None
        self.__samples = None
        self.__samplestart = None
        self.__sampleend = None
        self.__samplecur = None

        try:
            self.__search_data()
        except IndexError:
            raise NoData()

    def __select_file(self):
        """Select a file from the experiment based on the status of the object

        :raise Exception: If data not available in the specified time window. If the header does not
        indicate that the file is a TDMS format
        :raise IndexError: If the last file has already been processed or the start is greater than end
        """
        logs = logging.getLogger('Select file')
        logs.setLevel(self.__loglevel)

        # print('select', self.__twstart, self.starttime, self.__currentfile)

        if self.__currentfile is None:
            for idx, fi in enumerate(self.__available):
                # print(self.__twstart, fi['dt'])
                if self.__twstart < fi['dt']:
                    if not idx:
                        raise Exception('Data not available in the specified time window')
                    filename = os.path.join(self.__directory, self.__available[idx-1]['name'])
                    self.__currentfile = idx-1
                    # print(self.__currentfile, filename)
                    logs.debug(
                        'Opening %s; Starttime: %s' % (self.__available[self.__currentfile]['name'], self.__twstart))
                    break
            else:
                raise Exception('Data not available in the specified time window')
        elif self.__currentfile >= len(self.__available):
            logs.debug('Last file already processed')
            # No more data to iterate
            raise IndexError
        else:
            filename = os.path.join(self.__directory, self.__available[self.__currentfile]['name'])
            self.__twstart = self.__available[self.__currentfile]['dt']
            if (self.__twend is not None) and (self.__twstart > self.__twend):
                logs.debug('Start is greater than end. %s %s' % (self.__twstart, self.__twend))
                raise IndexError
            logs.debug('Opening %s; Starttime: %s' % (self.__available[self.__currentfile]['name'], self.__twstart))

        # print(self.__twstart)
        # Reset some properties before opening the new file
        self.starttime = self.__available[self.__currentfile]['dt']
        # print(self.starttime)
        self.endtime = None
        self.metadata = dict()

        # Read with h5py
        self.__fi = File(filename)

        # TODO All input from now on will be formatted by this
        # self.__endian = '>' if blah else '<'

    def __search_data(self):
        """
        Select a file to work with, read its metadata and calculate samples to read

        :raise IndexError: If the last file has already been processed or the start is greater than end
        """

        while True:
            # Loop through files until there is nothing else (IndexError)
            try:
                self.__select_file()
            except IndexError:
                raise
            except Exception as e:
                logging.warning('Skipping file because of %s' % str(e))
                self.__currentfile += 1
                continue

            # Read the metadata and calculate samples to read
            # Skip to the next file if there is a gap
            try:
                self.__readmetadata()
                return
            except NoData:
                logging.error('No Data was found in the metadata definition')
                self.__currentfile += 1
            except PotentialGap:
                logging.warning('Potential gap detected!')
                self.__currentfile += 1

    # Read all metadata from the HDF5 file
    def __readgroup(self, grp: Group):
        grpdict = dict()
        for k, v in grp.items():
            # print(v.name)
            if isinstance(v, Dataset) and v.name != '/data':
                grpdict[k] = v[()]
            elif isinstance(v, Group):
                grpdict[k] = self.__readgroup(v)
        return grpdict

    # Loads all metadata from the file in an attribute
    def __readmetadata(self):
        logs = logging.getLogger('Read metadata')
        logs.setLevel(self.__loglevel)

        self.metadata = self.__readgroup(self.__fi)

        # Check version and signature of the file
        if self.metadata['fileVersion'] != 7:
            logs.warning('File version is not 7!')

        if self.sampling_rate is None:
            self.sampling_rate = 1.0/self.metadata['header']['dt']
            # Check for decimation and take into account the filter length
            if self.__decimate != 1:
                tap = (len(self.__filter) - 1) / (2.0 * self.sampling_rate)
                # If there is decimation adjust the start and end times to include the tapering
                # and later keep exactly what user requests
                self.__twstart -= datetime.timedelta(seconds=tap)
                if self.__twend is not None:
                    self.__twend += datetime.timedelta(seconds=tap)
                logs.debug('Readjust start and end time to accommodate the filter length: %s - %s' %
                           (self.__twstart, self.__twend))

        curstarttime = datetime.datetime.utcfromtimestamp(self.metadata['header']['time'])
        if self.starttime is None:
            self.starttime = curstarttime
        # print(type(curstarttime), curstarttime)
        self.numchannels = self.metadata['header']['nChannels']
        # print(self.numchannels)

        # If channels was not defined at creation time
        if self.channels is None:
            # If first channel is not selected rewrite with minimum
            if self.__chstart is None:
                self.__chstart = min(self.metadata['header']['channels'])
            # If last channel is not selected rewrite with maximum
            if self.__chstop is None:
                self.__chstop = max(self.metadata['header']['channels'])
            # Define list of selected channels
            chin = list(range(self.__chstart, self.__chstop + 1, self.__chstep))
            print('chin', chin)
            self.channels = [ch for ch in chin if ch in self.metadata['header']['channels']]
            # print(self.channels)
            if not len(self.channels):
                raise Exception('No valid channel IDs selected!')
        # print(self.channels)
        # Keep the indexes of where the channels really are (column in 2D array)
        self.__channelsidx = [self.metadata['header']['channels'].tolist().index(ch) for ch in self.channels]

        self.__samples = self.metadata['header']['nSamples']

        # Calculate endtime based on the number of samples declared and the sampling rate
        self.endtime = self.starttime + datetime.timedelta(seconds=(self.__samples-1) * self.metadata['header']['dt'])

        # Sample to start extraction from based on the initial datetime of the file (__twstart)
        # print(self.__twstart, self.starttime)
        self.__samplestart = max(floor((self.__twstart - self.starttime).total_seconds() / self.metadata['header']['dt']), 0)
        if self.__samplestart >= self.__samples:
            raise PotentialGap('Start reading at %s, but only %s samples' % (self.__samplestart, self.__samples))

        # Should I readjust __twstart to align it exactly with the time of the samples?
        # print(self.__twstart, self.starttime + datetime.timedelta(seconds=self.__samplestart/self.sampling_rate))
        self.__twstart = self.starttime + datetime.timedelta(seconds=self.__samplestart * self.metadata['header']['dt'])
        # print(self.__twstart, self.starttime, self.__samplestart)

        self.__samplecur = self.__samplestart

        # Open end or beyond this file: read until the last sample
        if (self.__twend is None) or (self.__twend >= self.endtime):
            self.__sampleend = self.__samples-1
        else:
            # Otherwise calculate which one is the last sample to read
            self.__sampleend = ceil((self.__twend - self.starttime).total_seconds() / self.metadata['header']['dt'])
            # print(self.__twend, self.starttime, (self.__twend - self.starttime).total_seconds(), self.__sampleend)

        logs.debug('Samples: %s' % self.__samples)
        logs.debug('Samples selected: %s-%s' % (self.__samplestart, self.__sampleend))
        # print('Samples: %s' % self.__samples)
        # print('Samples selected: %s-%s' % (self.__samplestart, self.__sampleend))

    def reset(self):
        """Reset the status of the object and start the read again

        :raise IndexError: If the last file has already been processed or the start is greater than end
        """
        self.__twstart = self.__origstarttime
        self.__twend = self.__origendtime
        self.__currentfile = None
        self.__search_data()

    def __iter_data__(self):
        """Read data from files based on channel selection

        :return: Data and attributes for the header
        :rtype: tuple(numpy.array, obspy.core.trace.Stats)
        """

        # Multiply by dataScale and Unwrap
        auxdata = unwrap(self.__fi['data'] * self.metadata['header']['dataScale'],
                         self.metadata['header']['spatialUnwrRange'], axis=1)
        auxdata2 = auxdata[self.__samplestart:self.__sampleend + 1, self.__channelsidx]
        del auxdata

        # Data
        logs = logging.getLogger('Iterate Data')

        while (self.__twend is None) or (self.__twstart < self.__twend):
            # data = self.__readdata(channels=self.channels)
            # Loop through channels
            for idx, ch in enumerate(self.channels):
                # Get the real position as column in 2D array
                # data = self.__fi['data'][self.__samplestart:self.__sampleend + 1, self.__channelsidx[idx]]
                data = auxdata2[:, idx]
                # data = data * self.metadata['header']['dataScale']
                # Unwrap signal
                # data=unwrap(data, self.metadata['header']['spatialUnwrRange'], axis=1)
                # Integrate in time
                data = np.cumsum(data, axis=0) * self.metadata['header']['dt']
                # Use the sensitivity
                data /= self.metadata['header']['sensitivity']

                stats = Stats()
                stats.network = self.__networkcode
                stats.station = '%05d' % ch
                stats.location = ''
                stats.channel = self.__channelcode
                stats.sampling_rate = self.sampling_rate
                stats.npts = len(data)
                stats.starttime = UTCDateTime(self.__twstart)
                stats.mseed = AttribDict()
                stats.mseed.byteorder = self.__endian
                stats.mseed.dataquality = 'D'
                stats.mseed.record_length = 4096
                stats.mseed.blkt1001 = AttribDict()
                stats.mseed.blkt1001.timing_quality = 100

                logs.debug('Data length: %d; First component: %s' % (len(data), data[0]))
                logs.debug('Stats: %s' % (stats,))
                yield data, stats

            # No more data in this file. Skip to the next one.
            self.__currentfile += 1
            try:
                logs.debug('Moving to next file...')
                self.__search_data()
                # Multiply by dataScale and Unwrap
                auxdata = unwrap(self.__fi['data'] * self.metadata['header']['dataScale'],
                                 self.metadata['header']['spatialUnwrRange'], axis=1)
                auxdata2 = auxdata[self.__samplestart:self.__sampleend + 1, self.__channelsidx]
                del auxdata
            except IndexError:
                break

    def __iter_metadata__(self):
        """Read metadata from files based on channel selection

        :return: Metadata from selected channels
        :rtype: dict
        """
        # Metadata
        logs = logging.getLogger('Iterate Metadata')

        # channels = list(range(self.__chstart, self.__chstop+1, self.__chstep))

        while (self.__twend is None) or (self.__twstart < self.__twend):
            for obj in self.metadata:
                # TODO Check if this is needed
                # if 'id' in self.metadata[obj] and self.metadata[obj]['id'] not in self.channels:
                #     continue
                yield obj, self.metadata[obj]

            # No more data in this file. Skip to the next one.
            self.__currentfile += 1
            try:
                self.__search_data()
            except IndexError:
                break

    def chunks(self) -> int:
        """Estimate number of chunks to iterate"""
        estimatedfiles = 0

        dts = [fi['dt'] for fi in self.__available]
        for idx in range(len(dts)):
            if self.__twstart <= dts[idx]:
                if (self.__twend is None) or (dts[idx] < self.__twend):
                    estimatedfiles += 1
                    continue
            if dts[idx] <= self.__twstart < dts[idx+1]:
                estimatedfiles += 1

        return len(self.channels)*estimatedfiles
