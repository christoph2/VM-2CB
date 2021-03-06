#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

__version__ = "0.9.2"
__description__ = "VMC-File-Parser for the C-Control II."

__copyright__ = """
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

import sys
import vm2cb.vmcfile as vmcfile

def main():
    if len(sys.argv) != 2:
        print "usage: vmcinfo vmcfile"
        sys.exit()
    vmcFile = vmcfile.VMCReader(file(sys.argv[1]))
    print
    print "Anzahl / Konstanten (Bytes):", vmcFile.numberOfConstantBytes
    print "Anzahl / Codewoerter       :", vmcFile.numberOfCodeWords

if __name__ == "__main__":
    main()

