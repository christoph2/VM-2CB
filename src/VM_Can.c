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

void Can_Init(void)
{
    uint16  special_mask;
    uint16  global_mask;
    uint8   speed;

    special_mask   = (uint16)VM_PopW();
    global_mask    = (uint16)VM_PopW();
    speed          = (uint8)VM_PopW();
}


void Can_Ready(void)
{

}


void Can_Error(void)
{

}


void Can_Send(void)
{

}


void Can_Publish(void)
{

}


void Can_RtrCount(void)
{

}


void Can_Expect(void)
{

}


void Can_Request(void)
{

}


void Can_Rxd(void)
{

}


void Can_Get(void)
{

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
