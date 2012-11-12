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
#include "VM_Hm.h"

/*
    TODO: Endianess als Cfg.-Parameter!
*/

void Vm_Init_Phase0(void);

void Fls_Test(void);

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_MAIN_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

int main(void)
{
    CPU_DISABLE_ALL_INTERRUPTS();

    Fls_Test();
    Vm_Init_Phase0();

    TMR_Init();

    if (Hm_ButtonBootstrapMode()) {

    }  else if (Hm_ButtonHostMode() || VM_BlankCheck()) {
        Hm_Dispatcher();
    }  else {
        VM_SchedInit();
        VM_SysInit();
        CPU_ENABLE_ALL_INTERRUPTS();
        VM_Schedule();
    }

    return 0;
}


void Vm_Init_Phase0(void)
{
    HAL_INIT_PHASE0();
}


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_MAIN_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
