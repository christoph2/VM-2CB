/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2013 by Christoph Schueler <github.com/Christoph2,
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

#include "VM.h"
#include <stdio.h>

uint16 VM_SysVarYear, VM_SysVarMonth, VM_SysVarDay, VM_SysVarHour, VM_SysVarDow;
uint16 VM_SysVarMinute, VM_SysVarSecond, VM_SysVarDst, VM_SysVarZone, VM_SysVarDcfErrCnt;
uint32 VM_SysVarTimerMS, VM_SysVarCnt1, VM_SysVarCnt2, VM_SysVarCnt3;
uint32 VM_SysVarCnt4, VM_SysVarFreq1, VM_SysVarFreq2;


uint8 * VM_UserRAM;
uint8 * VM_UserConstants;
uint8 * VM_UserCode;
uint8 VM_OperandB;
uint16 VM_OperandW;
uint16 VM_MemoryUsage;
VM_TCBType * VM_CurrentThread;
uint16 VM_SP = (uint16)0x0000;


void VM_PushW(sint16 w)
{
    WREF(VM_UserRAM, VM_SP) = (uint16)w;
    VM_SP += 2U;
}


sint16 VM_PopW(void)
{
    return (sint16)WREF(VM_UserRAM, (VM_SP -= 2U));
}


void VM_PushL(sint32 l)
{
    LREF(VM_UserRAM, VM_SP)   = (uint32)l;
    VM_SP += 4U;
}


sint32 VM_PopL(void)
{
    return (sint32)LREF(VM_UserRAM, (VM_SP-= 4U));
}


void VM_PushF(float64 f)
{
    FREF(VM_UserRAM, VM_SP)   = (float64)f;
    VM_SP += sizeof(float64);
}


float64 VM_PopF(void)
{
    return FREF(VM_UserRAM, (VM_SP -= sizeof(float64)));
}

void setRAMPointer(unsigned char * ptr)
{
    VM_UserRAM = ptr;
}

void setCodePointer(uint16 * ptr)
{
    VM_UserCode = (uint8*)ptr;
}

void setConstPointer(uint8 * ptr)
{
    VM_UserConstants = ptr;
}

