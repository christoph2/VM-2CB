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

#include "VM_Cal.h"

/*
**
** Calender-Functions.
**
*/

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CAL_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

boolean Cal_IsLeapYear(uint16 year)
{
    return ((year % 0x0004u) == 0x0000u) && ((year % 0x0064u) != 0x0000u )  || ((year % 0x0190u) == 0x0000u );
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CAL_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
