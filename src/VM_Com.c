/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2016 by Christoph Schueler <github.com/Christoph2,
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
#include "VM_Com.h"
#include "Hal.h"

STATIC void Hwcom_Init(void), Hwcom_SetSpeed(void), Hwcom_SetBuffer(void);
STATIC void Hwcom_Flush(void), Hwcom_Ready(void), Hwcom_Put(void);
STATIC void Hwcom_Send(void), Hwcom_Rxd(void), Hwcom_Get(void);
STATIC void Hwcom_SetFormat(void), Hwcom_SendBreak(void);

STATIC void Swcom_Init(void), Swcom_SetSpeed(void), Swcom_SetBuffer(void);
STATIC void Swcom_Flush(void), Swcom_Ready(void), Swcom_Put(void);
STATIC void Swcom_Send(void), Swcom_Rxd(void), Swcom_Get(void);
STATIC void Swcom_SetFormat(void), Swcom_SendBreak(void);


STATIC const VoidFunctionType HwComTab[] = {
    Hwcom_Init,      Hwcom_SetSpeed, Hwcom_SetBuffer, Hwcom_Flush,
    Hwcom_Ready,     Hwcom_Put,      Hwcom_Send,      Hwcom_Rxd,  Hwcom_Get,
    Hwcom_SetFormat, Hwcom_SendBreak
};

STATIC const VoidFunctionType SwComTab[] = {
    Swcom_Init,      Swcom_SetSpeed, Swcom_SetBuffer, Swcom_Flush,
    Swcom_Ready,     Swcom_Put,      Swcom_Send,      Swcom_Rxd,  Swcom_Get,
    Swcom_SetFormat, Swcom_SendBreak
};

STATIC const uint32 BaudLookupTable[] = {
    (uint32)300,  (uint32)600,   (uint32)1200,  (uint32)2400,  (uint32)4800,
    (uint32)9600, (uint32)19200, (uint32)38400, (uint32)57600, (uint32)115200
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_COM_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

/*
**
**  HwCom
**
*/
void HwCom(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(HwComTab), ERROR_ILLOPA);
    HwComTab[VM_OperandB]();
}


void Hwcom_Init(void)
{
    HAL_COM0_INIT();
}


void Hwcom_SetSpeed(void)
{
    uint8 speed;

    speed = (uint8)VM_PopW();         /* speed */
    CC_ASSERT(speed < SIZEOF_ARRAY(BaudLookupTable), ERROR_ILLOPA);

    HAL_COM0_SETBAUDRATE(BaudLookupTable[speed]);
}


void Hwcom_SetBuffer(void)
{
    uint8   length;
    uint8 * buf;

    length = (uint8)VM_PopW();              /* length */
    buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[]  */

    /* TODO: assertion */
    HAL_COM0_SETBUFFER(buf, length);
}


void Hwcom_Flush(void)
{
    HAL_COM0_FLUSH();
}


void Hwcom_Rxd(void)
{
    boolean empty;

    empty = HAL_COM0_RXD();

    VM_PushW((sint16)(empty == TRUE ? CC_FALSE : CC_TRUE));
}


void Hwcom_Get(void)
{
    uint8 ch;

    ch = HAL_COM0_GETCHAR();

    VM_PushW((sint16)ch);
}


void Hwcom_Ready(void)
{
    boolean ready;

    ready = HAL_COM0_READY();

    (void)VM_PushW((sint16)(ready == TRUE ? CC_TRUE : CC_FALSE));
}


void Hwcom_Put(void)
{
    uint8 ch;

    ch = (uint8)VM_PopW();
    HAL_COM0_PUT(ch);
}


void Hwcom_Send(void)
{
    uint8   length;
    uint8 * buf;

    length = (uint8)VM_PopW();              /* length */
    buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[] */

    HAL_COM0_SEND(buf, length);
}


void Hwcom_SetFormat(void)
{
    uint8   nbits;
    uint8   parity;
    uint32  baudrate;

    nbits      = (uint8)VM_PopW();          /* nbits */
    parity     = (uint8)VM_PopW();          /* parity */
    baudrate   = (uint32)(uint16)VM_PopW(); /* baudrate */

    HAL_COM0_SETFORMAT(baudrate, parity, nbits);
}


void Hwcom_SendBreak(void)
{
    HAL_COM0_SENDBREAK();
}


/*
**
**  SwCom
**
*/
void SwCom(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(SwComTab), ERROR_ILLOPA);
    SwComTab[VM_OperandB]();
}


void Swcom_Init(void)
{
    HAL_COM1_INIT();
}


void Swcom_SetSpeed(void)
{
    uint8 speed;

    speed = (uint8)VM_PopW();         /* speed */
    CC_ASSERT(speed < SIZEOF_ARRAY(BaudLookupTable), ERROR_ILLOPA);

    HAL_COM1_SETBAUDRATE(BaudLookupTable[speed]);
}


void Swcom_SetBuffer(void)
{
    uint8   length;
    uint8 * buf;

    length = (uint8)VM_PopW();              /* length */
    buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[]  */

    /* todo: assertion */
    HAL_COM1_SETBUFFER(buf, length);
}


void Swcom_Flush(void)
{
    HAL_COM1_FLUSH();
}


void Swcom_Rxd(void)
{
    boolean empty;

    empty = HAL_COM1_RXD();
    VM_PushW((sint16)(empty == TRUE ? CC_FALSE : CC_TRUE));
}


void Swcom_Get(void)
{
    uint8 ch;

    ch = HAL_COM1_GETCHAR();
    VM_PushW((sint16)ch);
}


void Swcom_Ready(void)
{
    boolean ready;

    ready = HAL_COM1_READY();
    (void)VM_PushW((sint16)(ready == TRUE ? CC_TRUE : CC_FALSE));
}


void Swcom_Put(void)
{
    uint8 ch;

    ch = (uint8)VM_PopW();            /* c */
    HAL_COM1_PUT(ch);
}


void Swcom_Send(void)
{
    uint8   length;
    uint8 * buf;

    length = (uint8)VM_PopW();              /* length */
    buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[] */

    HAL_COM1_SEND(buf, length);
}


void Swcom_SetFormat(void)
{
    uint8   nbits;
    uint8   parity;
    uint32  baudrate;

    nbits      = (uint8)VM_PopW();          /* nbits */
    parity     = (uint8)VM_PopW();          /* parity */
    baudrate   = (uint32)(uint16)VM_PopW(); /* baudrate */

    HAL_COM1_SETFORMAT(baudrate, parity, nbits);
}


void Swcom_SendBreak(void)
{
    HAL_COM1_SENDBREAK();
}


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_COM_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
