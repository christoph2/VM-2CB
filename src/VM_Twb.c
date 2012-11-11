/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 * (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
 *                                      cpu12.gems@googlemail.com>
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

#include "VM_Twb.h"

static void Twb_Init(void), Twb_Rxd(void), Twb_Io(void);


static const VoidFunctionType TwbTab[] = {
    Twb_Init, Twb_Rxd, Twb_Io
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_TWB_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void VM_Twb(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(TwbTab), ERROR_ILLOPA);
    TwbTab[VM_OperandB]();
}


void Twb_Init(void)
{

}


void Twb_Rxd(void)
{
    VM_PushW(CC_TRUE);
}


void Twb_Io(void)
{
    uint16 buf = VM_PopW();

    VM_PushW(CC_TRUE);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_TWB_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
