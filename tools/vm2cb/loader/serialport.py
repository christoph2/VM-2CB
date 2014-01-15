#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.9.2"
__description__ = "VMC-Downloader for the C-Control II."
__copyright__ = """
   2-CB (C-Control-II kompatible Virtuelle Maschine).

  (C) 2007-2014 by Christoph Schueler <github.com/Christoph2,
                                       cpu12.gems@googlemail.com>

   All Rights Reserved

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""


import os
import sys
import time
import threading
from optparse import OptionParser,OptionGroup
from vm2cb.loader.commIf import IComm

import locale
locale.setlocale(locale.LC_ALL, '')
coding = locale.getpreferredencoding()

try:
    import serial
except ImportError:
    print "pySerial not installed.\nExiting."
    sys.exit(1)



class SerialPort(IComm):
    _lock = threading.Lock()

    def __init__(self, portNum, baudrate = 19200, bytesize = serial.EIGHTBITS,
                 parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, timeout = 0.1):
        self._portNum = portNum
        self._baudrate = baudrate
        self._bytesize = bytesize
        self._parity = parity
        self._stopbits = stopbits
        self._timeout = timeout

    def open(self):
        self._logger.debug("Trying to open serial port #%u.", self._portNum)
        try:
            self._port = serial.Serial(self._portNum, self._baudrate , self._bytesize, self._parity,
                self._stopbits, self._timeout
            )
        except serial.SerialException as e:
            self._logger.error("%s", e)
            #self._logger.exception(e)
            raise
        self._logger.info("Serial port openend as '%s' @ %d Bits/Sec.", self._port.portstr, self._port.baudrate)

    def write(self, data):
        #self._logger.debug("Tx bytes: %s", list(data))
        self._port.write(bytearray(list(data)))

    def read(self, length):
        result = self._port.read(length)
        #self._logger.debug("Rx bytes: %s", list(result))
        return result

    def flush(self):
        self._port.flush()

    def close(self):
        if self._port.isOpen() == True:
            self._port.close()

    def setBaudrate(self, speed):
        self._port.setBaudrate(speed)

    @property
    def displayName(self):
        return "Serial port"

    @property
    def baudrate(self):
        return self._baudrate


#print "REG:", IComm.getRegisteredClasses()

