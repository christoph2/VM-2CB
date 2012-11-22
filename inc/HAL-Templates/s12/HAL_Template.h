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

#define HAL_RESET_MCU()         ((void)S12Crg_ResetMCU())

#define HAL_GET_FREQUENCY1()    S12ECT_REG16(PACN3) + ((uint32)Frequency1 * ACC_MAX)
#define HAL_GET_FREQUENCY2()    S12ECT_REG16(PACN1) + ((uint32)Frequency2 * ACC_MAX)
#define HAL_BYTE_PORT0          S12MEBI_REG8(PORTB)
#define HAL_BYTE_PORT1          S12PIM_REG8(PTH)
#define HAL_BYTE_PORT_DDR0      
#define HAL_BYTE_PORT_DDR1              

#define HAL_INIT_PHASE0()               \
    _BEGIN_BLOCK                        \
        S12Mmc_Init();                  \
        S12Mebi_Init(&MEBI);            \
        S12Crg_Init();                  \
        S12Pim_Init(&PIM);              \
        S12Fls_Init();                  \
        S12Sci_Init(SCI0);              \
    _END_BLOCK

#define HAL_INIT_PHASE1()               \
    _BEGIN_BLOCK                        \
        (void)S12Iic_Init(&IIC0);       \
        (void)S12Atd_Init(ATD0);        \
        (void)S12Atd_Init(ATD1);        \
        (void)S12Ect_Init(&ECT_CFG);    \
        (void)S12Pwm_Init();            \
        (void)S12Sci_Init(SCI1);        \
        (void)S12Spi_Init(SPI0);        \
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

#define HAL_COM0_INIT()                             ((void)S12Sci_Init(SCI0))
#define HAL_COM0_SETBAUDRATE(rate)                  ((void)S12Sci_SetBaud(SCI0, (rate)))
#define HAL_COM0_SETBUFFER(buffer, length)          ((void)S12Sci_SetRxBuffer(SCI0, (buffer), (length)))
#define HAL_COM0_FLUSH()                            ((void)S12Sci_RxBufFlush(SCI0))
#define HAL_COM0_RXD()                              (S12Sci_RxBufIsEmpty(SCI0))
#define HAL_COM0_GETCHAR()                          (S12Sci_RxBufGetCh(SCI0))
#define HAL_COM0_READY()                            (S12Sci_TxReady(SCI0))
#define HAL_COM0_PUT(ch)                            ((void)S12Sci_Put(SCI0, (ch)))
#define HAL_COM0_SEND(buffer, length)               ((void)S12Sci_SendBuffer(SCI0, (buffer), (length)))
#define HAL_COM0_SETFORMAT(baudrate, parity, nbits) ((void)S12Sci_SetFormat(SCI0, (baudrate), (parity), (nbits)))
#define HAL_COM0_SENDBREAK()                        ((void)S12Sci_SendBreak(SCI0))
#define HAL_COM0_PUTSTRING(str)                     ((void)S12Sci_PutString(SCI0, (str)))

#define HAL_COM1_INIT()                             ((void)S12Sci_Init(SCI1))
#define HAL_COM1_SETBAUDRATE(rate)                  ((void)S12Sci_SetBaud(SCI1, (rate)))
#define HAL_COM1_SETBUFFER(buffer, length)          ((void)S12Sci_SetRxBuffer(SCI1, (buffer), (length)))
#define HAL_COM1_FLUSH()                            ((void)S12Sci_RxBufFlush(SCI1))
#define HAL_COM1_RXD()                              (S12Sci_RxBufIsEmpty(SCI1))
#define HAL_COM1_GETCHAR()                          (S12Sci_RxBufGetCh(SCI1))
#define HAL_COM1_READY()                            (S12Sci_TxReady(SCI1))
#define HAL_COM1_PUT(ch)                            ((void)S12Sci_Put(SCI1, (ch)))
#define HAL_COM1_SEND(buffer, length)               ((void)S12Sci_SendBuffer(SCI1, (buffer), (length)))
#define HAL_COM1_SETFORMAT(baudrate, parity, nbits) ((void)S12Sci_SetFormat(SCI1, (baudrate), (parity), (nbits)))
#define HAL_COM1_SENDBREAK()                        ((void)S12Sci_SendBreak(SCI1))

#define HAL_I2C_INIT()                              (S12Iic_Init(&IIC0))
#define HAL_I2C_START()                             (S12Iic_Start(&IIC0))
#define HAL_I2C_STOP()                              (S12Iic_Stop(&IIC0))
#define HAL_I2C_WRITE(ch)                           (S12Iic_Write(&IIC0, (ch)))   
#define HAL_I2C_READ(ack)                           (S12Iic_Read(&IIC0, (ack)))
#define HAL_I2C_READY()                             (CC_TRUE)

#define HAL_FLASH_ERASE_BANK(bank)                  (S12Fls_MassErase((bank)))
#define HAL_FLASH_ERASE_PROGRAM_WORD(page, addr, data)  (S12Fls_ProgramWord((page), (addr), (data)))
#define HAL_FLASH_SELECT_PAGE(page)                 ((void)S12Mmc_SetPPage((page)))

#define HAL_PLM_INIT()
#define HAL_PLM_SETTB(channel, timebase)
#define HAL_PLM_SETPM(channel, mode)
#define HAL_PLM_SETPL(channel, length)
#define HAL_PLM_OUT(channel, value)
#define HAL_PLM_BEEP(tone)
#define HAL_PLM_TONEOUT(tone)

#define HAL_PORTS_INIT()


#define HAL_CAN_INIT(speed, global_mask, special_mask)
#define HAL_CAN_READY(channel)                          (dummy())
#define HAL_CAN_ERROR()                                 (dummy())
#define HAL_CAN_SEND(channel, id, buf, lengt)
#define HAL_CAN_PUBLISH(channel, id, buf, length)
#define HAL_CAN_RTRCOUNT()                              (dummy())
#define HAL_CAN_EXPECT(channel, id)
#define HAL_CAN_REQUEST(channel)
#define HAL_CAN_RXD(channel)                            (dummy())
#define HAL_CAN_GET(channel, buf)

#endif /* __HAL_TEMPLATE_H */
