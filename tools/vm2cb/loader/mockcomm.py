#!/usr/bin/env python
# -*- coding: utf-8 -*-


__version__ = "0.9.2"
__description__ = "VMC-Downloader for C-Control II."
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

import logging
import unittest
import vm2cb.loader.defs as defs
from vm2cb.loader.commIf import IComm

logger = logging.getLogger("vm2cb.loader")

DATE    = "Jan 9 2013"
VERSION = "2-CB/12  V1.0\r\n"

##
## Communication mock-up for unit-testing.
##
class StateError(Exception): pass

class MockCommunication(IComm):
    CLOSED      = 0
    AWAIT_CMD   = 1
    DATA        = 2
    ID          = 3
    DATE        = 4
    VERSION     = 5

    def __init__(self, *args, **kwargs):
        super(MockCommunication, self).__init__(*args, **kwargs)
        self._state = MockCommunication.CLOSED

    def open(self):
        self._state = MockCommunication.AWAIT_CMD

    def close(self):
        if self._state == MockCommunication.CLOSED:
            raise StateError('Port not open.')

    def write(self, data):
        if self._state == MockCommunication.CLOSED:
            raise StateError('Port not open.')
        if len(data) == 1:
            cmd = data[0]
            if cmd == defs.HM_CMD_SEND_ID:
                self._state = MockCommunication.ID
            elif cmd == defs.HM_CMD_SEND_DATE:
                self._state = MockCommunication.DATE
            elif cmd == defs.HM_CMD_SEND_VERSION:
                self._state = MockCommunication.VERSION
            elif cmd == defs.HM_CMD_START:
                pass
            elif cmd == defs.HM_CMD_LOAD_VMC:
                pass
            elif cmd == defs.HM_CMD_LOAD_HEX:
                pass
            elif cmd == defs.HM_CMD_ERASE_VMC:
                pass
            elif cmd == defs.HM_CMD_ERASE_HEX:
                pass
            elif cmd == defs.HM_CMD_SET_HI_BAUD:
                pass
            elif cmd == defs.HM_CMD_SET_DEF_BAUD:
                pass
            elif cmd == defs.HM_CMD_SET_TURBO_BAUD:
                pass
            elif cmd == defs.HM_CMD_RESET:
                pass

    def read(self, length):
        if self._state == MockCommunication.CLOSED:
            raise StateError('Port not open.')
        if self._state == MockCommunication.ID:
            self._state = MockCommunication.AWAIT_CMD
            return defs.CC2_ID
        elif self._state == MockCommunication.DATE:
            self._state = MockCommunication.AWAIT_CMD
            return DATE
        elif self._state == MockCommunication.VERSION:
            self._state = MockCommunication.AWAIT_CMD
            return VERSION
        else:
            return ''

    def flush(self):
        pass

    def displayName(self):
        return "MockCommunication"


