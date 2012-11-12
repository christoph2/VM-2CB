#!/usr/bin/env python
# -*- coding: utf-8 -*-


__version__ = "0.9.2"
__description__ = "VMC-Downloader for the C-Control II."
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

NEED_PY_SERIAL="""
    To use this program you need 'pySerial'.

    Get it from
        'http://pyserial.sourceforge.net/'
    or
        '$ easy_install pyserial'
"""

import os
import sys
import time
from optparse import OptionParser,OptionGroup

import locale
locale.setlocale(locale.LC_ALL, '')
coding = locale.getpreferredencoding()

try:
    import serial
except ImportError:
    print "\n*** " + os.path.split(sys.argv[0])[1] + ": INSTALLATION-ERROR ***"
    print NEED_PY_SERIAL
    sys.exit(1)

import vmcfile


HM_CMD_SEND_ID          = 0x00
HM_CMD_SEND_DATE        = 0x01
HM_CMD_SEND_VERSION     = 0x02
HM_CMD_START            = 0x03
HM_CMD_LOAD_VMC         = 0x04
HM_CMD_LOAD_HEX         = 0x05
HM_CMD_ERASE_VMC        = 0x06
HM_CMD_ERASE_HEX        = 0x07
HM_CMD_SET_HI_BAUD      = 0x08
HM_CMD_SET_DEF_BAUD     = 0x09
HM_CMD_SET_TURBO_BAUD   = 0x0a
HM_CMD_RESET            = 0xff

CC2_ID                  = "C-Control II"

SPEED_TAB               = {'lo': (19200, HM_CMD_SET_DEF_BAUD), 'med': (57600, HM_CMD_SET_HI_BAUD), 'hi': (115200, HM_CMD_SET_TURBO_BAUD)}

BLOCK_SIZE              = 32

port                    = None


def portOpen(num):
    global port
    print "Trying to open serial port #" + str(num) + ":"
    try:
        port = serial.Serial(port = num,baudrate = 19200,bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE,
                             stopbits = serial.STOPBITS_ONE, timeout = 0.1
                             )
    except serial.SerialException as e:
        print "\n\t",e
        sys.exit(2)
    print "\tOK, openend as '%s' @ %d Bits/Sec." % (port.portstr, port.baudrate)


def portClose():
    if port.isOpen() == True:
        port.close()


def errorExit(msg):
    print "\tERROR: %s." % (msg)
    portClose()
    sys.exit(1)


def checkTimeout(res):
    if res == '':
        errorExit("Timeout")


def requString(cmd):
    port.write(bytearray([cmd]))
    result = port.read(128)
    port.flush()
    return result.strip()


def requCmd(cmd):
    port.write(bytearray([cmd]))


def SerializeLong(val):
    return [val & 0xff, (val >> 8) & 0xff, (val >> 16) & 0xff, (val >> 24) & 0xff]


def ShowProgress(percentage):
    percentage /= 2
    tail = (" " * (50 - percentage)) + ']'
    bar = '[ ' + ("=" * (percentage))
    print bar, tail, '\r',


def ExchangeBytes(data, len):
    port.write(bytearray(data))
    result = port.read(len)
    checkTimeout(result)
    result = [ord(x) for x in result]
    return data == result


def LoadVMC(vmcFile):
    num_consts, num_code = vmcFile.numberOfConstantBytes, vmcFile.numberOfCodeWords
    const_bytes, code_words = vmcFile.constBytes, vmcFile.codeWords

    print "\nErasing VMC."
    requCmd(HM_CMD_ERASE_VMC)
    time.sleep(2.5)
    result = port.read(1)
    checkTimeout(result)

    if ord(result) == HM_CMD_ERASE_VMC:
        print "\tOK."
    else:
        errorExit("Communication Error")

    print "\nStart loading."
    requCmd(HM_CMD_LOAD_VMC)

    if not ExchangeBytes(SerializeLong(num_consts), 4):
        errorExit("Communication Error")
    if not ExchangeBytes(SerializeLong(num_code), 4):
        errorExit("Communication Error")
    print "\tOK."

    print "\nLoading %d Constant-Bytes.\n" % (num_consts)
    for i in range(0, num_consts, BLOCK_SIZE):
        ExchangeBytes(const_bytes[i : i+BLOCK_SIZE], BLOCK_SIZE)
        ShowProgress(((i + 32) * 100) / num_consts)
    print "\n\n\tOK."

    print "\n\nLoading %d Code-Words.\n" % (num_code)
    for i in range(0, num_code, BLOCK_SIZE / 2):
        arr = []
        for w in code_words[i : i+BLOCK_SIZE / 2]:
            arr.append((w >> 8) & 0xff)
            arr.append(w & 0xff)
        ExchangeBytes(arr, BLOCK_SIZE)
        ShowProgress(((i + 16) * 100) / num_code)
    print "\n\n\tOK."


def requID():
    return requString(HM_CMD_SEND_ID)


def requDate():
    return requString(HM_CMD_SEND_DATE)


def requVersion():
    return requString(HM_CMD_SEND_VERSION)


def requBRSwitch(speed):
    br = speed[0]
    cmd = speed[1]
    print "\nSwitching baudrate to %d Bits/Sec." % (br)
    requCmd(cmd)
    time.sleep(0.1)
    port.baudrate = br
    ID = requID()
    checkTimeout(ID)
    if ID == CC2_ID:
        print "\tOK."
    else:
        errorExit("Communication Error")


def requestID():
    print "\nRequesting Identification:"
    ID = requID()
    checkTimeout(ID)

    Version = requVersion()
    checkTimeout(Version)

    Date = requDate()
    checkTimeout(Date)

    if ID != CC2_ID:
        errorExit("wrong ID - expected '%s', got '%s'" % (CC2_ID, ID))

    print "\tID:\t", ID
    print "\tVer.:\t", Version
    print "\tDate:\t", Date


def printInfo():
    print """\n  %s
  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
                                       cpu12.gems@googlemail.com>
    """ % (__description__)


def main():
    usage = "usage: %prog [options] vmc_file"

    printInfo()
    op = OptionParser(usage = usage, version = "%prog " +__version__)

    op.add_option("-p", "--port", action = "store", type = "int",dest = "comport",
        help = "Com-Port #. This depends on your operating system, e.g.: 1 ==> "
        "COM2 on Microsoft-Systems.", default = 0)
    op.add_option("-s", "--speed", action = "store", type = "choice", dest = "speed",
        choices = ('lo', 'med', 'hi'), default = "med", help = "Communication Speed. "
        "Select one of the folowing: ['lo'|'med'|'hi'] (19200,57600,115200).")

    (options, args) = op.parse_args()
    if len(args) != 1:
        op.print_help()
        exit(1)

    filename = args[0]

    if not os.path.exists(filename):
        print os.getcwd()
        print "\tERROR: File '%s' not found." % (filename)
        sys.exit(1)

    data = vmcfile.VMCReader(file(filename))

    portOpen(options.comport)
    requestID()

    speed = SPEED_TAB[options.speed]

    if port.baudrate != speed[0]:
        requBRSwitch(speed)

    LoadVMC(data)

    print "\nReseting Target.\n"
    requCmd(HM_CMD_RESET)

    portClose()


if __name__ == "__main__":
    main()
