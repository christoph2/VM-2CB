/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *  (C) 2007-2012 by Christoph Schueler <chris@konnex-tools.de,
 *                                       cpu12.gems@googlemail.com>
 *
 *   All Rights Reserved
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License along
 *  with this program; if not, write to the Free Software Foundation, Inc.,
 *  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */
#if !defined(__VM_HM_H)
#define __VM_HM_H

#include "VM.h"
#include "mcu/s12/inc/S12_Sci.h"
#include "mcu/s12/inc/S12_Fls.h"

typedef enum tagHM_CommandType {
    HM_CMD_SEND_ID,
    HM_CMD_SEND_DATE,
    HM_CMD_SEND_VERSION,
    HM_CMD_START,
    HM_CMD_LOAD_VMC,
    HM_CMD_LOAD_HEX,
    HM_CMD_ERASE_VMC,
    HM_CMD_ERASE_HEX,
    HM_CMD_SET_HI_BAUD,
    HM_CMD_SET_DEF_BAUD,
    HM_CMD_SET_TURBO_BAUD,
    HM_CMD_RESET = (uint8) 0xff
} HM_CommandType;

void Hm_Dispatcher(void);

boolean Hm_ButtonBootstrapMode(void);
boolean Hm_ButtonHostMode(void);


#endif  /* __VM_HM_H */

