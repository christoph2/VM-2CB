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

SPEED_TAB               = {
    'lo': (19200, HM_CMD_SET_DEF_BAUD),
    'med': (57600, HM_CMD_SET_HI_BAUD),
    'hi': (115200, HM_CMD_SET_TURBO_BAUD)
}

BLOCK_SIZE              = 32

