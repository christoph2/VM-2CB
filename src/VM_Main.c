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

#include "mcu/s12/inc/S12_Mebi.h"
#include "mcu/s12/inc/S12_Mmc.h"

void    Init_Basic(void);
void    Init_Full(void);


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_MAIN_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

int main(void)
{
    CPU_DISABLE_ALL_INTERRUPTS();

    Init_Basic();

    TMR_Init();

    if (Hm_ButtonBootstrapMode()) {

    }  else if (Hm_ButtonHostMode() || VM_BlankCheck()) {
        Hm_Dispatcher();
    }  else {
        VM_SchedInit();
        VM_SysInit();
        Init_Full();    /* todo: nach Sys_Init. */
        CPU_ENABLE_ALL_INTERRUPTS();
        VM_Schedule();
    }

    return 0;
}


void Init_Basic(void)
{
    S12Mmc_Init();
    S12Mebi_Init(&MEBI);
    S12Crg_Init();
    S12Pim_Init(&PIM);
    S12Fls_Init();
    S12Sci_Init(SCI0);
}


void Init_Full(void)
{
    S12Ect_Init(&ECT_CFG);
    S12Pwm_Init();
    S12Iic_Init(&IIC0);
    S12Atd_Init(ATD0);
    S12Atd_Init(ATD1);
    S12Sci_Init(SCI1);
    S12Iic_Init(&IIC0);
    S12Spi_Init(SPI0);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_MAIN_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
