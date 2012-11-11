#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__="0.9.1"
__description__=""
__copyright__="""VMC to S19 Converter
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

BASE_ADDR_CONST = 0xC0000   # Page #30
BASE_ADDR_CODE  = 0xE0000   # Page #38

PAGE_WINDOW_START   = 0x8000
PAGE_WINDOW_END     = 0xC000 # 0xbfff
PAGE_WINDOW_LEN     = PAGE_WINDOW_END-PAGE_WINDOW_START

#   Code-Pages  = {0x38,0x39,0x3A,0x3B,0x3C,0x3D,0x3E,0x3F}.
#   Const_Pages = {0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37}.
CONST_PPAGE_OFFSET  = 0x30
CODE_PPAGE_OFFSET   = 0x38


## todo: 'binascii.b2a_hex()' / 'binascii.a2b_hex()' !!!

def Addr2Checksum(w):
    return ((w & 0xff0000)>>16) + ((w & 0xff00)>>8) + (w & 0xff)

class VMC2S19(object):
    def __init__(self,data,file_name):
        self.code=data[3]
        self.consts=data[2]
        self.num_code=data[1]
        self.num_consts=data[0]
        self.file=open(file_name,'w')

    @staticmethod
    def GetLinearAddress(base,count):
        return base+count

    @staticmethod
    def GetBankedAddress(base,count):
        if base==BASE_ADDR_CONST:
            base=CONST_PPAGE_OFFSET
        elif base==BASE_ADDR_CODE:
            base=CODE_PPAGE_OFFSET
        else:
            return None
        page=(count/(PAGE_WINDOW_LEN/2))+base
        offs=(((count % (PAGE_WINDOW_LEN/2))<<1)+PAGE_WINDOW_START)
        addr=page<<16 | offs
        return addr

    def go(self,banked):
        count=0
        if banked==True:
            GetAddress=self.GetLinearAddress
        else:
            GetAddress=self.GetBankedAddress
        addr=GetAddress(BASE_ADDR_CONST,count)

        checksum=36+Addr2Checksum(addr)
        self.file.write("S0030000FC\n")
        self.file.write("S224%06X" % addr)

        print "%06X %02X" % (addr,checksum)

        for c in self.consts:
            self.file.write("%02X" % c)
            checksum=(checksum+c)
            count+=1
            if count % 32==0:
                checksum= (~checksum) & 0xff
                self.file.write("%02X\n" % checksum)
                if (count-BASE_ADDR_CONST)<self.num_consts:
                    addr=GetAddress(BASE_ADDR_CONST,count)

                    checksum=36+Addr2Checksum(addr)
                    if count!=self.num_consts:
                        self.file.write("S224%06X" % (addr))

        count=0
        addr=GetAddress(BASE_ADDR_CODE,count)

        checksum=36+Addr2Checksum(addr)
        self.file.write("S224%06X" % addr)

        print "%06X %02X" % (addr,checksum)

        for c in self.code:
            lobyte=(c & 0xff)
            hibyte=(c >> 8)
            self.file.write("%02X%02X" % (hibyte,lobyte))
            count+=2
            checksum=checksum+hibyte+lobyte
            if count % 32 == 0:
                checksum= (~checksum) & 0xff
                self.file.write("%02X\n" % checksum)
                if (count-BASE_ADDR_CODE)<(self.num_code*2):
                    addr=GetAddress(BASE_ADDR_CODE,count)

                    checksum=36+Addr2Checksum(addr)
                    if count!=(self.num_code*2):
                        self.file.write("S224%06X" % (addr))

        self.file.write("S804000000FB")
        self.file.close()

def test():
    r=VMCFile.VMCReader(r'demo.c2p.vmc')
    data=r.parse()
    d=VMC2S19(data,r'demo.s19')
    d.go(False)

if __name__=="__main__":
    test()
