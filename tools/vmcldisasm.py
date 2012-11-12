#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = "0.9.2"
__description__ = "VMC Disassembler"
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

import vm2cb.vmcfile as vmcfile
import vm2cb.vmcodes as vmcodes
import os
import sys

class CC2Disasm(object):
    def __init__(self,vmcFile):
        self.code = vmcFile.codeWords
        self.consts = vmcFile.constBytes

    def getCodeWord(self):
        for w in self.code:
            yield w

    def go(self):
        operandw = 0
        while True:
            try:
                word = self.code.pop(0)
            except IndexError:
                break

            typ = (word >> 8) & 0xc0
            opcode = ((word & 0xff00) >> 8)
            operandb = word & 0x00ff
            oc = 0
            sys.stdout.write("%04x" % word)
            if typ == vmcodes.VM_CODE_A:
                oc = opcode & ~vmcodes.VM_CODE_A
                sys.stdout.write("        %s(0x%02X)\n" % (vmcodes.VmcA[opcode], operandb))
            elif typ == vmcodes.VM_CODE_B:
                oc = opcode & ~vmcodes.VM_CODE_B
                if vmcodes.VmcB.has_key(opcode):
                    if opcode in vmcodes.SubFunctions:
                        sys.stdout.write("        %s(%s)\n" % (vmcodes.VmcB[opcode], vmcodes.SubFunctions[opcode][operandb] ))
                    elif opcode in vmcodes.Multiple:
                        tmp = vmcodes.Multiple[opcode]
                        sys.stdout.write("        %s(%s)\n" % (vmcodes.VmcB[opcode], vmcodes.SubFunctions[tmp][operandb] ))
                    else:
                        sys.stdout.write("        %s(0x%02X)\n" % (vmcodes.VmcB[opcode], operandb))
                else:
                    print "VMB(0x%02X, 0x%02X)" % (oc,operandb)
            elif typ == vmcodes.VM_CODE_C:
                oc = opcode & ~vmcodes.VM_CODE_C
                operandw = self.code.pop(0)
                sys.stdout.write("%04x" % operandw)
                if vmcodes.VmcC.has_key(opcode):
                    sys.stdout.write("    %s(0x%04X)\n" % (vmcodes.VmcC[opcode], operandw))
                else:
                    sys.stdout.write("    VMC(0x%02X, 0x%04X)\n" % (oc, operandw))
            elif typ == vmcodes.VM_CODE_D:
                oc = opcode & ~vmcodes.VM_CODE_D
                operandw = self.code.pop(0)
                sys.stdout.write("%04x" % operandw)
                if vmcodes.VmcD.has_key(opcode):
                    sys.stdout.write("    %s(0x%02X, 0x%04X)\n" % (vmcodes.VmcD[opcode], operandb, operandw))
                else:
                    pass

def main():
    sys.stderr.write("cc2ldisasm -- C-Control II low-level disassembler.\n\n")
    if len(sys.argv)!=2:
        sys.exit("usage: cc2ldisasm vmc-file.\n")

    vmcFile = vmcfile.VMCReader(file(sys.argv[1]))
    d = CC2Disasm(vmcFile)
    d.go()

if __name__ == "__main__":
    main()

