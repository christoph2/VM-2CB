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
import logging

class IComm(object):
    __metaclass__ = abc.ABCMeta
    _logger = logging.getLogger('vm2cb.loader')

    @classmethod
    def getRegisteredClasses(cls):
        return cls.__subclasses__()

    @abc.abstractmethod
    def open(self): pass

    @abc.abstractmethod
    def close(self): pass

    @abc.abstractmethod
    def write(self, data): pass

    @abc.abstractmethod
    def read(self, length): pass

    @abc.abstractmethod
    def flush(self): pass

    @abc.abstractproperty
    def displayName(self):
        pass

