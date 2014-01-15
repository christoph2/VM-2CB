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

import abc
import os
import sys
import time
import locale
import logging

import vm2cb.vmcfile
import vm2cb.loader.defs as defs

import abc
import os
import sys
import time
import locale
import logging

import vm2cb.vmcfile
import vm2cb.loader.defs as defs
from vm2cb.loader.errors import CommunicationError, TimeoutError
from vm2cb.loader.utils import serializeLong

logger = logging.getLogger("vm2cb.loader")


class Primitives(object):
    logger = logging.getLogger("vm2cb.loader")

    def __init__(self, port, waitTimeAfterErase = 2.5):
        self._port = port
        self._waitTimeAfterErase = waitTimeAfterErase

    def requestString(self, cmd):
        self._port.write(bytearray([cmd]))
        result = self._port.read(128)
        self.checkTimeout(result)
        self._port.flush()
        return result.strip()

    def writeCommand(self, cmd):
        self._port.write(bytearray([cmd]))

    def exchangeBytes(self, data, len):
        self._port.write(bytearray(data))
        result = self._port.read(len)
        self.checkTimeout(result)
        result = [ord(x) for x in result]
        return data == result

    def checkTimeout(self, res):
        if res == '':
            raise TimeoutError("Connection timed out.")

    def requestID(self):
        return self.requestString(defs.HM_CMD_SEND_ID)

    def requestDate(self):
        return self.requestString(defs.HM_CMD_SEND_DATE)

    def requestVersion(self):
        return self.requestString(defs.HM_CMD_SEND_VERSION)

    def targetReset(self):
        self.writeCommand(defs.HM_CMD_RESET)

    def eraseVMC(self):
        self.writeCommand(defs.HM_CMD_ERASE_VMC)
        time.sleep(self._waitTimeAfterErase)
        result = self._port.read(1)
        self.checkTimeout(result)
        if ord(result) != defs.HM_CMD_ERASE_VMC:
            raise CommunicationError()

    def startLoad(self, numConsts, numCode):
        self.writeCommand(defs.HM_CMD_LOAD_VMC)
        if not self.exchangeBytes(serializeLong(numConsts), 4):
            raise CommunicationError()
        if not self.exchangeBytes(serializeLong(numCode), 4):
            raise CommunicationError()

    def SwitchBaudrate(self, speed):
        br = speed[0]
        cmd = speed[1]
        self.writeCommand(cmd)
        time.sleep(0.1)
        self._port.setBaudrate(br)
        ID = self.requestID()
        self.checkTimeout(ID)
        if ID != defs.CC2_ID:
            raise CommunicationError()


