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
#define CPU_NO_OPERATION()

/* TODO: CriticalSections und 'Vm_Intr' Modul! */
#define CPU_DISABLE_ALL_INTERRUPTS()
#define CPU_ENABLE_ALL_INTERRUPTS()

#define HAL_RESET_MCU()

#define HAL_GET_FREQUENCY1()    23
#define HAL_GET_FREQUENCY2()    42
#define HAL_BYTE_PORT0          dummy
#define HAL_BYTE_PORT1          dummy
#define HAL_BYTE_PORT_DDR0      dummy
#define HAL_BYTE_PORT_DDR1      dummy

#define HAL_INIT_PHASE0()
#define HAL_INIT_PHASE1()

#define HAL_GET_ADC_CHANNEL(channel, value)

#define HAL_COM0_INIT()
#define HAL_COM0_SETBAUDRATE(rate)
#define HAL_COM0_SETBUFFER(buffer, length)
#define HAL_COM0_FLUSH()
#define HAL_COM0_RXD()                                  (dummy())
#define HAL_COM0_GETCHAR()                              (dummy())
#define HAL_COM0_READY()                                (dummy())
#define HAL_COM0_PUT(ch)
#define HAL_COM0_SEND(buffer, length)
#define HAL_COM0_SETFORMAT(baudrate, parity, nbits)
#define HAL_COM0_SENDBREAK()
#define HAL_COM0_PUTSTRING(str)                         

#define HAL_COM1_INIT()
#define HAL_COM1_SETBAUDRATE(rate)
#define HAL_COM1_SETBUFFER(buffer, length)
#define HAL_COM1_FLUSH()
#define HAL_COM1_RXD()                                  (dummy())
#define HAL_COM1_GETCHAR()                              (dummy())
#define HAL_COM1_READY()                                (dummy())
#define HAL_COM1_PUT(ch)
#define HAL_COM1_SEND(buffer, length)
#define HAL_COM1_SETFORMAT(baudrate, parity, nbits)
#define HAL_COM1_SENDBREAK()

#define HAL_I2C_INIT()
#define HAL_I2C_START()
#define HAL_I2C_STOP()
#define HAL_I2C_WRITE(ch)                               (dummy())
#define HAL_I2C_READ(ack)                               (dummy())
#define HAL_I2C_READY()                                 (CC_TRUE)

#define HAL_FLASH_ERASE_BANK(bank)                      (dummy())
#define HAL_FLASH_ERASE_PROGRAM_WORD(page, addr, data)  (dummy())
#define HAL_FLASH_SELECT_PAGE(page)


#endif /* __HAL_TEMPLATE_H */
