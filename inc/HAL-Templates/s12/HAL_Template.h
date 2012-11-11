/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
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
#if !defined(__HAL_TEMPLATE_H)
#define __HAL_TEMPLATE_H

#include "HAL_Defines.h"

#define CPU_BREAKPOINT()
#define CPU_NO_OPERATION
#define CPU_DISABLE_ALL_INTERRUPTS()
#define CPU_ENABLE_ALL_INTERRUPTS()

#define HAL_GET_FREQUENCY1()    S12ECT_REG16(PACN3) + ((uint32)Frequency1 * ACC_MAX)
#define HAL_GET_FREQUENCY2()    S12ECT_REG16(PACN1) + ((uint32)Frequency2 * ACC_MAX)
#define HAL_BYTE_PORT0          S12MEBI_REG8(PORTB)
#define HAL_BYTE_PORT1          S12PIM_REG8(PTH)
#define HAL_BYTE_PORT_DDR0      
#define HAL_BYTE_PORT_DDR1              

#define HAL_INIT()                      \
    _BEGIN_BLOCK                        \
        (void)S12Iic_Init(&IIC0);       \
        (void)S12Atd_Init(ATD0);        \
        (void)S12Atd_Init(ATD1);        \
        (void)S12Ect_Init(&ECT_CFG);    \
        (void)S12Pwm_Init();            \
    _END_BLOCK

#define HAL_GET_ADC_CHANNEL(channel, value)                     \
    _BEGIN_BLOCK                                                \
        S12Atd_ConfigType const *   base;                       \
                                                                \
        if ((channel) > ((uint8)7)) {                           \
            base = ATD0;                                        \
        } else {                                                \
            base = ATD1;                                        \
        }                                                       \
        (channel) &= ((uint8)0x07);                             \
        (value) = (sint16)S12Atd_GetChannel(base, (channel));   \
    _END_BLOCK

#endif /* __HAL_TEMPLATE_H */
