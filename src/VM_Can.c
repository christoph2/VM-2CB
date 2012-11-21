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

#include "VM_Can.h"

STATIC void Can_Init(void), Can_Ready(void), Can_Error(void);
STATIC void Can_Send(void), Can_Publish(void), Can_RtrCount(void);
STATIC void Can_Expect(void), Can_Request(void), Can_Rxd(void);
STATIC void Can_Get(void), Can_SetParameter(void);
STATIC void Can_GetID(void), Can_RequestX(void);


STATIC const VoidFunctionType CanTab[] = {
    Can_Init,         Can_Ready,  Can_Error,   Can_Send, Can_Publish,
    Can_RtrCount,     Can_Expect, Can_Request, Can_Rxd,  Can_Get,
    Can_SetParameter, Can_GetID,  Can_RequestX
};

void VM_Can(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(CanTab), ERROR_ILLOPA);
    CanTab[VM_OperandB]();
}


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CAN_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

static int dummy(void)
{
    return 0;
}

void Can_Init(void)
{
    uint16  special_mask;
    uint16  global_mask;
    uint8   speed;

    special_mask   = (uint16)VM_PopW();
    global_mask    = (uint16)VM_PopW();
    speed          = (uint8)VM_PopW();

    HAL_CAN_INIT(speed, global_mask, special_mask);
}


void Can_Ready(void)
{
    uint8  channel = (uint8)VM_PopW();              /*channel */
   
    VM_PushW((sint16)HAL_CAN_READY(channel));
}


void Can_Error(void)
{
    VM_PushW((sint16)HAL_CAN_ERROR());
}


void Can_Send(void)
{
    uint8 length   = (uint8)VM_PopW();              /* length */
    uint8 * buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[]  */
    uint16 id      = (uint16)VM_PopW();             /* id */
    uint8  channel = (uint8)VM_PopW();              /*channel */

    HAL_CAN_SEND(channel, id, buf, length);
}


void Can_Publish(void)
{
    uint8 length   = (uint8)VM_PopW();              /* length */
    uint8 * buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[]  */
    uint16 id      = (uint16)VM_PopW();             /* id */
    uint8  channel = (uint8)VM_PopW();              /*channel */

    HAL_CAN_PUBLISH(channel, id, buf, length);
}


void Can_RtrCount(void)
{
    uint8  channel = (uint8)VM_PopW();              /*channel */
    
    VM_PushW((sint16)HAL_CAN_RTRCOUNT());
}


void Can_Expect(void)
{
    uint16 id      = (uint16)VM_PopW();             /* id */
    uint8  channel = (uint8)VM_PopW();              /*channel */

    HAL_CAN_EXPECT(channel, id);
}


void Can_Request(void)
{
    uint8  channel = (uint8)VM_PopW();              /*channel */

    HAL_CAN_REQUEST(channel);

}


void Can_Rxd(void)
{
    uint8  channel = (uint8)VM_PopW();              /*channel */

    VM_PushW((sint16)HAL_CAN_RXD(channel));
}


void Can_Get(void)
{
    uint8 * buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[]  */
    uint8  channel = (uint8)VM_PopW();              /*channel */

    HAL_CAN_GET(channel, buf);
}


void Can_SetParameter(void)
{

}


void Can_GetID(void)
{

}


void Can_RequestX(void)
{

}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CAN_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
