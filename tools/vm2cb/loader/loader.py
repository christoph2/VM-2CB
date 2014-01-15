#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vm2cb.loader.defs as defs

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


def showProgress(percentage):
    percentage /= 2
    tail = (" " * (50 - percentage)) + ']' + " %u %%" % (percentage << 1)
    bar = '[ ' + ("=" * (percentage))
    print bar, tail, '\r',


class Loader(object):
    def __init__(self, primitives, vmcFile):
        self._primitives = primitives
        self._vmcFile = vmcFile

    def __call__(self):
        num_consts, num_code = self._vmcFile.numberOfConstantBytes, self._vmcFile.numberOfCodeWords
        const_bytes, code_words = self._vmcFile.constBytes, self._vmcFile.codeWords
        percentTage = 0
        oldPercentage = 0

        print "\nLoading %d Constant-Bytes.\n" % (num_consts)
        for i in range(0, num_consts, defs.BLOCK_SIZE):
            self._primitives.exchangeBytes(const_bytes[i : i + defs.BLOCK_SIZE], defs.BLOCK_SIZE)
            percentage = ((i + 32) * 100) / num_consts
            if percentage != oldPercentage:
                showProgress(percentage)
            oldPercentage = percentage
        print "\n\tOK."

        print "\n\nLoading %d Code-Words.\n" % (num_code)
        for i in range(0, num_code, defs.BLOCK_SIZE / 2):
            arr = []
            for w in code_words[i : i + defs.BLOCK_SIZE / 2]:
                #print hex(w),
                arr.append(w & 0xff)    # Swap Bytes???
                arr.append((w >> 8) & 0xff)
                
            self._primitives.exchangeBytes(arr, defs.BLOCK_SIZE)
            percentage = ((i + 16) * 100) / num_code
            if percentage != oldPercentage:
                showProgress(percentage)
            oldPercentage = percentage

