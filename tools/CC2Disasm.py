#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__="0.9.2"
__description__="VMC Disassembler"
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

import VMCFile
import VMCodes
import sys

class CC2Disasm(object):
    def __init__(self,vmcFile):
        self.code=vmcFile.codeWords
        self.consts=vmcFile.constBytes
    def GetCodeWord(self):
        for w in self.code:
            yield w
    def go(self):
        operandw=0
        while True:
            try:
                word=self.code.pop(0)
            except IndexError:
                print "FINISHED"
                break

            typ=(word>>8) & 0xc0
#            print "Word: ",word," Type: ",typ
            opcode=((word & 0xff00) >> 8)
            operandb=word & 0x00ff
            oc=0
            print "0x%04X " % word,
            if typ==VMCodes.VM_CODE_A:
                oc=opcode & ~VMCodes.VM_CODE_A
                print "%s(0x%02X)" % (VMCodes.VmcA[opcode],operandb)
            elif typ==VMCodes.VM_CODE_B:
                oc=opcode & ~VMCodes.VM_CODE_B
                if VMCodes.VmcC.has_key(opcode):
#                    print VMCodes.VmcB[opcode],operandb
                    print "%s(0x%02X)" % (VMCodes.VmcB[opcode],operandb)
                else:
                    print "VMB(0x%02X,0x%02X)" % (oc,operandb)
            elif typ==VMCodes.VM_CODE_C:
                oc=opcode & ~VMCodes.VM_CODE_C
                operandw=self.code.pop(0)
                if VMCodes.VmcC.has_key(opcode):
#                    print VMCodes.VmcC[opcode],operandw
                    print "%s(0x%04X)" % (VMCodes.VmcC[opcode],operandw)
                else:
                    print "VMC(0x%02X,0x%04X)" % (oc,operandw)
            elif typ==VMCodes.VM_CODE_D:
                oc=opcode & ~VMCodes.VM_CODE_D
                operandw=self.code.pop(0)
                if VMCodes.VmcD.has_key(opcode):
#                    print VMCodes.VmcD[opcode],operandb,operandw
                    print "%s(0x%02X,0x%04X)" % (VMCodes.VmcD[opcode],operandb,operandw)
                else:
                    pass



def test():
    if len(sys.argv)!=2:
        sys.exit("usage: CC2Disam vmc-file.\n")

    vmcFile=VMCFile.VMCReader(file(sys.argv[1]))
    d=CC2Disasm(vmcFile)
    d.go()

if __name__=="__main__":
    test()

