#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

__version__="0.9.2"
__description__="VMC-File-Parser for the C-Control II."

__copyright__="""
   2-CB (C-Control-II kompatible Virtuelle Maschine).

  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
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

import cStringIO
import re


class InvalidVMCFile(Exception): pass

VMC_FILE = re.compile(r'''CC2VMC\s(?P<numberOfConstantBytes>\d+)\s(?P<numberOfCodeWords>\d+)[\n]{2}
    (?P<constBytes>(\d+\s)+.*?)[\n]{2}(?P<codeWords>(\d+\s)+.*)''', re.VERBOSE | re.M | re.DOTALL)

def bswap(value):
    hi = (value & 0xff00) >> 8
    lo = value & 0xff

    return lo << 8 | hi

class VMCReader(object):
    def __init__(self, infFile):
        data=infFile.read()

        match = VMC_FILE.match(data)
        if match:
            gd = match.groupdict()
            self.codeWords = map(bswap, map(int, gd['codeWords'].split()))
            self.constBytes = map(int, gd['constBytes'].split())
            self.numberOfConstantBytes = int(gd['numberOfConstantBytes'])
            self.numberOfCodeWords = int(gd['numberOfCodeWords'])

            assert self.numberOfConstantBytes == len(self.constBytes)
            assert self.numberOfCodeWords == len(self.codeWords)
        else:
            pass # todo: Error-Handling.


def test():
    vmcFile=VMCReader(file(r"demo.c2p.vmc"))
    print "Number of Constant Bytes:",vmcFile.numberOfConstantBytes
    print "Number of Code Words:",vmcFile.numberOfCodeWords

if __name__=="__main__":
    test()

