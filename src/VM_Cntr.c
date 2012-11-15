/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
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

#include "VM_Cntr.h"

/*#define ACC_MAX ((uint32)0x00010000)*/
#define ACC_MAX ((uint16)0xffff)

STATIC uint8 Frequency1, Frequency2;

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CNTR_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void Cntr_Init(void)
{
    Cntr_Reset();

}

void Cntr_Reset(void)
{
    Frequency1 = (uint8)0;
    Frequency2 = (uint8)0;
}


uint32 Cntr_GetFrequency1(void)
{
    return (uint32)HAL_GET_FREQUENCY1();
}


uint32 Cntr_GetFrequency2(void)
{
    return (uint32)HAL_GET_FREQUENCY2();
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CNTR_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
