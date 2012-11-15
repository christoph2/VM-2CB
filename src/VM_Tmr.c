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

#include "VM_Tmr.h"

/*
**  REFERENCES
**  ==========
**
**  EB611/D             - HC11 AND HC12 FAMILIES' PULSE ACCUMULATOR
**  S12ECT10B8CV1/D     - HCS12 16BIT 10CHANNEL ENHANCED CAPTURE TMR BLOCK GUIDE
**  S12ECT16B8CV1       - HCS12 16-BIT, 8-CHANNEL ENHANCED CAPTURE TIMER (ECT) BLOCK G
**
*/

STATIC uint32 TMR_TOF_Count;

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_TMR_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void TMR_Init(void)
{
    TMR_TOF_Count = 0UL;
}

uint32 TMR_GetTofCount(void)
{
    return TMR_TOF_Count;
}

void TMR_TimerTick(void)
{
    VM_SysVarTimerMS++; /* TODO: Tick-Granularität (eine MS funktioniert unter Windows nicht wirklich zuverlässig...) */

    if ((((uint16)VM_SysVarTimerMS) % (uint16)1000) == (uint16)0) {
        VM_SysVarFreq1 = Cntr_GetFrequency1();
        VM_SysVarFreq2 = Cntr_GetFrequency2();
        Cntr_Reset();

        if (++VM_SysVarSecond == (uint16)60) {
            VM_SysVarSecond = (uint16)0;

            if (++VM_SysVarMinute == (uint16)60) {
                VM_SysVarMinute = (uint16)0;

                if (++VM_SysVarHour == (uint16)24) {
                    VM_SysVarHour = (uint16)0;
                    /* todo: Calender-Handling, DCF-Err-, LPT-Busy-Handling. */
                }
            }
        }
    }
}


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_TMR_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
