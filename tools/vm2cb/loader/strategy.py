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


from vm2cb.loader.mockcomm import MockCommunication

comm = MockCommunication()
comm.open()
#print pri.requestID()
#print pri.requestDate()
#print pri.requestVersion()

class ILoadVMCStrategy(object):
    __metaclass__ = abc.ABCMeta


class DefaultLoadVMCStrategy(ILoadVMCStrategy):
    def __init__(self, comm):
        self._comm = comm

    def run(self):
        self.requestID()
        self.eraseVMC()
        self.loadVMC()

    def requestID(self):
        pass

    def eraseVMC(self):
        pass

    def loadVMC(self):
        pass



