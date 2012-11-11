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

void VM_InitPorts(void)
{

}


void VM_GetSinglePort(void)
{
    uint8 port, data, msk;

    port = LOBYTE(VM_PopW()) & SINGLE_PORT_MASK;

    if (port > ((uint8)7)) {
        msk    = port & ((uint8)0x07);
        data   = S12PIM_REG8(PTH);
    } else {
        msk    = port;
        data   = S12MEBI_REG8(PORTB);
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
        dptr   = &S12PIM_REG8(DDRH);
        pptr   = &S12PIM_REG8(PTH);
    } else {
        msk    = port;
        dptr   = &S12MEBI_REG8(DDRB);
        pptr   = &S12MEBI_REG8(PORTB);
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
            data = S12MEBI_REG8(PORTB);
            break;
        case 2: case 3:
            data = S12PIM_REG8(PTH);
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
            S12MEBI_REG8(PORTB)   &= ((uint8)0xF0);
            S12MEBI_REG8(PORTB)   |= data;
            S12MEBI_REG8(DDRB)    |= ((uint8)0x0F);
            break;
        case 1:
            S12MEBI_REG8(PORTB)   &= ((uint8)0x0F);
            S12MEBI_REG8(PORTB)   |= data << 4;
            S12MEBI_REG8(DDRB)    |= ((uint8)0xF0);
            break;
        case 2:
            S12PIM_REG8(PTH)  &= ((uint8)0xF0);
            S12PIM_REG8(PTH)  |= data;
            S12PIM_REG8(DDRH) |= ((uint8)0x0F);
            break;
        case 3:
            S12PIM_REG8(PTH)  &= ((uint8)0x0F);
            S12PIM_REG8(PTH)  |= data << 4;
            S12PIM_REG8(DDRH) |= ((uint8)0xF0);
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
        data = S12PIM_REG8(PTH);
    } else {
        data = S12MEBI_REG8(PORTB);
    }

    VM_PushW((uint16)data);
}


void VM_SetBytePort(void)
{
    uint8 port, data;

    data   = LOBYTE(VM_PopW());
    port   = LOBYTE(VM_PopW()) & BYTE_PORT_MASK;

    if (port == ((uint8)1)) {
        S12PIM_REG8(PTH)   = data;
        S12PIM_REG8(DDRH)  = ((uint8)0xFF);
    } else {
        S12MEBI_REG8(PORTB)    = data;
        S12MEBI_REG8(DDRB)     = ((uint8)0xFF);
    }
}


void VM_GetWordPort(void)
{
    uint8   port;
    uint16  data;

    port   = LOBYTE(VM_PopW()); /* ignorieren. */
    data   = S12PIM_REG8(PTH) << 8;
    data  |= S12MEBI_REG8(PORTB);
    VM_PushW(data);
}


void VM_SetWordPort(void)
{
    uint8   port;
    uint16  data;

    data   = VM_PopW();
    port   = LOBYTE(VM_PopW()); /* ignorieren. */

    S12MEBI_REG8(PORTB)    = LOBYTE(data);
    S12PIM_REG8(PTH)       = HIBYTE(data);
    S12MEBI_REG8(DDRB)     = S12PIM_REG8(DDRH) = ((uint8)0xFF);
}


void VM_DeactSinglePort(void)
{
    uint8 port;

    port = LOBYTE(VM_PopW()) & SINGLE_PORT_MASK;

    if (port > ((uint8)7)) {
        S12PIM_REG8(DDRH) &= ~(BitTab8[port & ((uint8)0x07)]);
    } else {
        S12MEBI_REG8(DDRB) &= ~(BitTab8[port]);
    }
}


void VM_DeactNibblePort(void)
{
    uint8 port;

    port = LOBYTE(VM_PopW()) & NIBBLE_PORT_MASK;

    switch (port) {
        case 0:
            S12MEBI_REG8(DDRB) &= ((uint8)0xF0);
            break;
        case 1:
            S12MEBI_REG8(DDRB) &= ((uint8)0x0F);
            break;
        case 2:
            S12PIM_REG8(DDRH) &= ((uint8)0xF0);
            break;
        case 3:
            S12PIM_REG8(DDRH) &= ((uint8)0x0F);
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
        S12PIM_REG8(DDRH) = ((uint8)0x00);
    } else {
        S12MEBI_REG8(DDRB) = ((uint8)0x00);
    }
}


void VM_DeactWordPort(void)
{
    uint8 port;

    port               = LOBYTE(VM_PopW()); /* ignorieren. */
    S12PIM_REG8(DDRH)  = S12MEBI_REG8(DDRB) = ((uint8)0x00);
}


void VM_ToggleSinglePort(void)
{
    uint8               port, msk;
    volatile uint8 *    dptr, * pptr;

    port = LOBYTE(VM_PopW()) & SINGLE_PORT_MASK;

    if (port > ((uint8)7)) {
        msk    = port & ((uint8)0x07);
        dptr   = &S12PIM_REG8(DDRH);
        pptr   = &S12PIM_REG8(PTH);
    } else {
        msk    = port;
        dptr   = &S12MEBI_REG8(DDRB);
        pptr   = &S12MEBI_REG8(PORTB);
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
    S12Atd_ConfigType const *   base;

    chn = LOBYTE(VM_PopW()) & ((uint8)0x0F);

    if (chn > ((uint8)7)) {
        base = ATD0;
    } else {
        base = ATD1;
    }

    chn &= ((uint8)0x07);

    VM_PushW((sint16)S12Atd_GetChannel(base, chn));
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_?_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
