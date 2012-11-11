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

#include "VM_Ports.h"

static const uint8 BitTab8[8] = {
    (uint8)0x01, (uint8)0x02, (uint8)0x04, (uint8)0x08, (uint8)0x10, (uint8)0x20, (uint8)0x40, (uint8)0x80
};

#define SINGLE_PORT_MASK    ((uint8)0x0f)       /* 16 Bit-Ports. */
#define NIBBLE_PORT_MASK    ((uint8)0x03)       /* 4 Nibble-Ports. */
#define BYTE_PORT_MASK      ((uint8)0x01)       /* 2 Byte-Ports. */

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_PORTS_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

static uint8 dummy;

void VM_InitPorts(void)
{

}

void VM_GetSinglePort(void)
{
    uint8 port, data, msk;

    port = LOBYTE(VM_PopW()) & SINGLE_PORT_MASK;

    if (port > ((uint8)7)) {
        msk    = port & ((uint8)0x07);
        data   = HAL_BYTE_PORT1;
    } else {
        msk    = port;
        data   = HAL_BYTE_PORT0;
    }

    msk = BitTab8[msk];

    if ((data & msk) == msk) {
        data = (uint8)CC_TRUE;
    } else {
        data = (uint8)CC_FALSE;
    }

    VM_PushW((uint16)data);
}


void VM_SetSinglePort(void)
{
    uint8               port, data, msk;
    volatile uint8 *    dptr, * pptr;

    data   = LOBYTE(VM_PopW());
    port   = LOBYTE(VM_PopW()) & SINGLE_PORT_MASK;

    if (port > ((uint8)7)) {
        msk    = port & ((uint8)0x07);
        dptr   = &HAL_BYTE_PORT_DDR1;
        pptr   = &HAL_BYTE_PORT1;
    } else {
        msk    = port;
        dptr   = &HAL_BYTE_PORT_DDR0;
        pptr   = &HAL_BYTE_PORT0;
    }

    msk = BitTab8[msk];

    if (data != ((uint8)0)) {
        *pptr |= msk;     /* alle Werte ungleich '0' führen zu Hi-Pegel. */
    } else {
        *pptr &= ~msk;
    }

    *dptr |= msk;         /* Port als Ausgang konfigurieren. */
}


void VM_GetNibblePort(void)
{
    uint8 port, data;

    port = LOBYTE(VM_PopW()) & NIBBLE_PORT_MASK;

    switch (port) {
        case 0: case 1:
            data = HAL_BYTE_PORT0;
            break;
        case 2: case 3:
            data = HAL_BYTE_PORT1;
            break;
        default:
            CC_ASSERT(FALSE, ERROR_ILLOPA);
    }

    if ((port & ((uint8)0x01)) == ((uint8)0x1)) {
        data >>= 4;
    }

    data &= ((uint8)0x0f);

    VM_PushW((uint16)data);
}


void VM_SetNibblePort(void)
{
    uint8 port, data;

    data   = LOBYTE(VM_PopW()) & ((uint8)0x0F);
    port   = LOBYTE(VM_PopW()) & NIBBLE_PORT_MASK;

    switch (port) {
        case 0:
            HAL_BYTE_PORT0   &= ((uint8)0xF0);
            HAL_BYTE_PORT0   |= data;
            HAL_BYTE_PORT_DDR0    |= ((uint8)0x0F);
            break;
        case 1:
            HAL_BYTE_PORT0   &= ((uint8)0x0F);
            HAL_BYTE_PORT0   |= data << 4;
            HAL_BYTE_PORT_DDR0    |= ((uint8)0xF0);
            break;
        case 2:
            HAL_BYTE_PORT1  &= ((uint8)0xF0);
            HAL_BYTE_PORT1  |= data;
            HAL_BYTE_PORT_DDR1 |= ((uint8)0x0F);
            break;
        case 3:
            HAL_BYTE_PORT1  &= ((uint8)0x0F);
            HAL_BYTE_PORT1  |= data << 4;
            HAL_BYTE_PORT_DDR1 |= ((uint8)0xF0);
            break;
        default:
            CC_ASSERT(FALSE, ERROR_ILLOPA);
    }
}


void VM_GetBytePort(void)
{
    uint8 port, data;

    port = LOBYTE(VM_PopW()) & BYTE_PORT_MASK;

    if (port == ((uint8)1)) {
        data = HAL_BYTE_PORT1;
    } else {
        data = HAL_BYTE_PORT0;
    }

    VM_PushW((uint16)data);
}


void VM_SetBytePort(void)
{
    uint8 port, data;

    data   = LOBYTE(VM_PopW());
    port   = LOBYTE(VM_PopW()) & BYTE_PORT_MASK;

    if (port == ((uint8)1)) {
        HAL_BYTE_PORT1   = data;
        HAL_BYTE_PORT_DDR1  = ((uint8)0xFF);
    } else {
        HAL_BYTE_PORT0    = data;
        HAL_BYTE_PORT_DDR0     = ((uint8)0xFF);
    }
}


void VM_GetWordPort(void)
{
    uint8   port;
    uint16  data;

    port   = LOBYTE(VM_PopW()); /* ignorieren. */
    data   = HAL_BYTE_PORT1 << 8;
    data  |= HAL_BYTE_PORT0;
    VM_PushW(data);
}


void VM_SetWordPort(void)
{
    uint8   port;
    uint16  data;

    data   = VM_PopW();
    port   = LOBYTE(VM_PopW()); /* ignorieren. */

    HAL_BYTE_PORT0    = LOBYTE(data);
    HAL_BYTE_PORT1       = HIBYTE(data);
    HAL_BYTE_PORT_DDR0     = HAL_BYTE_PORT_DDR1 = ((uint8)0xFF);
}


void VM_DeactSinglePort(void)
{
    uint8 port;

    port = LOBYTE(VM_PopW()) & SINGLE_PORT_MASK;

    if (port > ((uint8)7)) {
        HAL_BYTE_PORT_DDR1 &= ~(BitTab8[port & ((uint8)0x07)]);
    } else {
        HAL_BYTE_PORT_DDR0 &= ~(BitTab8[port]);
    }
}


void VM_DeactNibblePort(void)
{
    uint8 port;

    port = LOBYTE(VM_PopW()) & NIBBLE_PORT_MASK;

    switch (port) {
        case 0:
            HAL_BYTE_PORT_DDR0 &= ((uint8)0xF0);
            break;
        case 1:
            HAL_BYTE_PORT_DDR0 &= ((uint8)0x0F);
            break;
        case 2:
            HAL_BYTE_PORT_DDR1 &= ((uint8)0xF0);
            break;
        case 3:
            HAL_BYTE_PORT_DDR1 &= ((uint8)0x0F);
            break;
        default:
            CC_ASSERT(FALSE, ERROR_ILLOPA);
    }
}


void VM_DeactBytePort(void)
{
    uint8 port;

    port = LOBYTE(VM_PopW()) & BYTE_PORT_MASK;

    if (port == ((uint8)1)) {
        HAL_BYTE_PORT_DDR1 = ((uint8)0x00);
    } else {
        HAL_BYTE_PORT_DDR0 = ((uint8)0x00);
    }
}


void VM_DeactWordPort(void)
{
    uint8 port;

    port               = LOBYTE(VM_PopW()); /* ignorieren. */
    HAL_BYTE_PORT_DDR1  = HAL_BYTE_PORT_DDR0 = ((uint8)0x00);
}


void VM_ToggleSinglePort(void)
{
    uint8               port, msk;
    volatile uint8 *    dptr, * pptr;

    port = LOBYTE(VM_PopW()) & SINGLE_PORT_MASK;

    if (port > ((uint8)7)) {
        msk    = port & ((uint8)0x07);
        dptr   = &HAL_BYTE_PORT_DDR1;
        pptr   = &HAL_BYTE_PORT1;
    } else {
        msk    = port;
        dptr   = &HAL_BYTE_PORT_DDR0;
        pptr   = &HAL_BYTE_PORT0;
    }

    msk = BitTab8[msk];

    *pptr ^= msk;
    *dptr |= msk;
}


void VM_PulseSinglePort(void)
{
/*
**	XOR()
**	Delay()
**	XOR()
*/
    CPU_NO_OPERATION();
}


void VM_GetCount(void)
{

}


void VM_GetFreq(void)
{

}


void VM_GetAdcPort(void)
{
    uint8                       chn;
    sint16                      value;

    chn = LOBYTE(VM_PopW()) & ((uint8)0x0F);

    HAL_GET_ADC_CHANNEL(chn, value);

    VM_PushW(value);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_PORTS_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
