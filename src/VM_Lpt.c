/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2016 by Christoph Schueler <github.com/Christoph2,
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

#include "VM_Lpt.h"

STATIC void Lpt_Init(void), Lpt_Flush(void), Lpt_Ready(void);
STATIC void Lpt_Put(void), Lpt_Print(void);


STATIC const VoidFunctionType LptTab[] = {
    Lpt_Init, Lpt_Flush, Lpt_Ready,
    Lpt_Put,  Lpt_Print
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_LPT_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void VM_Lpt(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(LptTab), ERROR_ILLOPA);
    LptTab[VM_OperandB]();
}


void Lpt_Init(void)
{
    HAL_LPT_INIT();
}


void Lpt_Flush(void)
{
    HAL_LPT_FLUSH();
}


void Lpt_Ready(void)
{
    VM_PushW(HAL_LPT_READY());
}


void Lpt_Put(void)
{
    uint8 ch = (uint8)VM_PopW();

    HAL_LPT_PUT(ch);
}


void Lpt_Print(void)
{
    uint8   length = (uint8)VM_PopW();              /* length */
    uint8 * buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[] */
    
    HAL_LPT_PRINT(buf, length);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_LPT_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
