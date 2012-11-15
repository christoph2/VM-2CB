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

#include "VM_Ls.h"

#define LS_LOCAL(type)          (type(VM_UserRAM, VM_CurrentThread->T_BP + VM_OperandW))
#define LS_KEEP(type, offs) \
    (type(VM_UserRAM, VM_OperandW) = type(VM_UserRAM, (VM_CurrentThread->T_SP - offs)))
#define LS_KEEPLOCAL(type, offs) \
    (type(VM_UserRAM, VM_CurrentThread->T_BP + VM_OperandW) = type(VM_UserRAM, (VM_CurrentThread->T_SP - offs)))
#define LS_ABSOLUTE(type)       (type(VM_OperandW, ((uint16)0x0000u)))
#define LS_DIRECT(type)         (type(VM_UserRAM, VM_OperandW))
#define LS_REF(type)            (type(VM_UserRAM, VM_PopW()))

/* todo: Codepage auswählen!!! */
#define LS_CONST_DIRECT(type)   (type(VM_UserConstants, (((uint16)VM_OperandW) << 1)))
#define LS_CONST_REF(type)      (type(VM_UserConstants, (((uint16)VM_PopW()) << 1)))

/*
**  Local Variables.
*/
STATIC uint16  * const VM_SysVars16[] = {
    &VM_SysVarYear,   &VM_SysVarMonth, &VM_SysVarDay, &VM_SysVarHour, &VM_SysVarMinute,
    &VM_SysVarSecond, &VM_SysVarDow,   &VM_SysVarDst, &VM_SysVarZone, &VM_SysVarDcfErrCnt
};

STATIC uint32 * const VM_SysVars32[] = {
    &VM_SysVarTimerMS, &VM_SysVarCnt1,  &VM_SysVarCnt2, &VM_SysVarCnt3,
    &VM_SysVarCnt4,    &VM_SysVarFreq1, &VM_SysVarFreq2
};


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_LS_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void VM_LoadByteImmidiate(void)
{
    VM_PushW((sint16)VM_OperandB);
}


void VM_LoadImmidiateInt(void)
{
    VM_PushW((sint16)VM_OperandW);
}


void VM_LoadLocalByte(void)
{
    VM_PushW((sint16)LS_LOCAL(BREF));
}


void VM_LoadLocalInt(void)
{
    VM_PushW((sint16)LS_LOCAL(WREF));
}


void VM_LoadLocalLong(void)
{
    VM_PushL((sint32)LS_LOCAL(LREF));
}


void VM_LoadLocalFloat(void)
{
    VM_PushF(LS_LOCAL(FREF));
}


void VM_StoreLocalByte(void)
{
    LS_LOCAL(BREF) = LOBYTE(VM_PopW());
}


void VM_StoreLocalInt(void)
{
    LS_LOCAL(WREF) = (uint16)VM_PopW();
}


void VM_StoreLocalLong(void)
{
    LS_LOCAL(LREF) = (uint32)VM_PopL();
}


void VM_StoreLocalFloat(void)
{
    LS_LOCAL(FREF) = VM_PopF();
}


void VM_StoreKeepByte(void)
{
    LS_KEEP(BREF, sizeof(uint16));
}


void VM_StoreKeepInt(void)
{
    LS_KEEP(WREF, sizeof(uint16));
}


void VM_StoreKeepLong(void)
{
    LS_KEEP(WREF, sizeof(uint32));
}


void VM_StoreKeepFloat(void)
{
    LS_KEEP(FREF, FLOAT_SIZE);
}


void VM_StoreKeepLocalByte(void)
{
    LS_KEEPLOCAL(BREF, sizeof(uint16));
}


void VM_StoreKeepLocalInt(void)
{
    LS_KEEPLOCAL(BREF, sizeof(uint16));
}


void VM_StoreKeepLocalLong(void)
{
    LS_KEEPLOCAL(LREF, sizeof(uint32));
}


void VM_StoreKeepLocalFloat(void)
{
    LS_KEEPLOCAL(LREF, FLOAT_SIZE);
}


void VM_LoadByte(void)
{
    VM_PushW((sint16)LS_DIRECT(BREF));
}


void VM_LoadInt(void)
{
    VM_PushW((sint16)LS_DIRECT(WREF));
}


void VM_LoadLong(void)
{
    VM_PushL((sint32)LS_DIRECT(LREF));
}


void VM_LoadFloat(void)
{
    VM_PushF(LS_DIRECT(FREF));
}


void VM_StoreByte(void)
{
    LS_DIRECT(BREF) = LOBYTE(VM_PopW());
}


void VM_StoreInt(void)
{
    LS_DIRECT(WREF) = (uint16)VM_PopW();
}


void VM_StoreLong(void)
{
    LS_DIRECT(LREF) = (uint32)VM_PopL();
}


void VM_StoreFloat(void)
{
    LS_DIRECT(FREF) = VM_PopF();
}


void VM_LoadSysvarInt(void)
{
    VM_PushW(((VM_OperandB <= ISYSVAR_MAX) ? ((sint16) * VM_SysVars16[VM_OperandB]) : ((sint16)0x0000u)));
}


void VM_LoadSysvarLong(void)
{
    VM_PushL(((VM_OperandB <= LSYSVAR_MAX) ? ((sint32) * VM_SysVars32[VM_OperandB]) : ((sint32)0x00000000L)));
}


void VM_StoreSysvarInt(void)
{
    uint16 w = (uint16)VM_PopW();

    if (VM_OperandB <= ISYSVAR_MAX) {
        *VM_SysVars16[VM_OperandB] = w;
    } else {
        CC_ASSERT(FALSE, ERROR_ILLOPA);
    }
}


void VM_StoreSysvarLong(void)
{
    uint32 l = (uint32)VM_PopL();

    if (VM_OperandB <= LSYSVAR_MAX) {
        *VM_SysVars32[VM_OperandB] = l;
    } else {
        CC_ASSERT(FALSE, ERROR_ILLOPA);
    }
}


void VM_LoadRefByte(void)
{
    VM_PushW((sint16)LS_REF(BREF));
}


void VM_LoadRefInt(void)
{
    VM_PushW((sint16)LS_REF(WREF));
}


void VM_LoadRefLong(void)
{
    VM_PushL((sint32)LS_REF(LREF));
}


void VM_LoadRefFloat(void)
{
    VM_PushF(LS_REF(FREF));
}


void VM_StoreRefByte(void)
{
    LS_REF(BREF) = LOBYTE(VM_PopW());
}


void VM_StoreRefInt(void)
{
    LS_REF(WREF) = (uint16)VM_PopW();
}


void VM_StoreRefLong(void)
{
    LS_REF(LREF) = (uint32)VM_PopL();
}


void VM_StoreRefFloat(void)
{
    LS_REF(FREF) = VM_PopF();
}


void VM_IncLoadByte(void)
{
    VM_PushW((sint16)(LS_DIRECT(BREF) += (uint8)1));
}


void VM_IncLoadInt(void)
{
    VM_PushW((sint16)(LS_DIRECT(WREF) += ((uint16)1)));
}


void VM_IncLoadLong(void)
{
    VM_PushL((sint32)(LS_DIRECT(LREF) += (uint32)1L));
}


void VM_IncLoadFloat(void)
{
    VM_PushF(LS_DIRECT(FREF) += (float64)1.0);
}


void VM_IncLoadRefByte(void)
{
    VM_PushW((sint16)(LS_REF(BREF) += ((uint8)1)));
}


void VM_IncLoadRefInt(void)
{
    VM_PushW((sint16)(LS_REF(WREF) += ((uint16)1)));
}


void VM_IncLoadRefLong(void)
{
    VM_PushL((sint32)(LS_REF(LREF) += ((uint32)1L)));
}


void VM_IncLoadRefFloat(void)
{
    VM_PushF(LS_REF(FREF) += (float64)1.0);
}


void VM_IncLoadLocalByte(void)
{
    VM_PushW((sint16)(LS_LOCAL(BREF) += ((uint8)1)));
}


void VM_IncLoadLocalInt(void)
{
    VM_PushW((sint16)(LS_LOCAL(WREF) += ((uint16)1)));
}


void VM_IncLoadLocalLong(void)
{
    VM_PushL((sint32)(LS_LOCAL(LREF) += ((uint32)1L)));
}


void VM_IncLoadLocalFloat(void)
{
    VM_PushF(LS_LOCAL(FREF) += (float64)1.0);
}


void VM_LoadConstByte(void)
{
    VM_PushW((sint16)LS_CONST_DIRECT(BREF));
}


void VM_LoadConstInt(void)
{
    VM_PushW((sint16)LS_CONST_DIRECT(WREF));
}


void VM_LoadConstLong(void)
{
    VM_PushL((sint32)LS_CONST_DIRECT(LREF));
}


void VM_LoadConstFloat(void)
{
    VM_PushF(LS_CONST_DIRECT(FREF));
}


void VM_LoadRefConstByte(void)
{
    VM_PushW((sint16)LS_CONST_REF(BREF));
}


void VM_LoadRefConstInt(void)
{
    VM_PushW((sint16)LS_CONST_REF(WREF));
}


void VM_LoadRefConstLong(void)
{
    VM_PushL((sint32)LS_CONST_REF(LREF));
}


void VM_LoadRefConstFloat(void)
{
    VM_PushF(LS_CONST_REF(FREF));
}


void VM_PutInt(void)
{
    uint16 dest, pos, value;

    value  = (uint16)VM_PopW();
    pos    = (uint16)VM_PopW();
    dest   = (uint16)VM_PopW();

    WREF(VM_UserRAM, dest + pos) = value;
}


void VM_PutLong(void)
{
    uint16  dest, pos;
    uint32  value;

    value  = (uint32)VM_PopL();
    pos    = (uint16)VM_PopW();
    dest   = (uint16)VM_PopW();

    LREF(VM_UserRAM, dest + pos) = value;
}


void VM_PutFloat(void)
{
    uint16  dest, pos;
    float64 value;

    value  = VM_PopF();
    pos    = (uint16)VM_PopW();
    dest   = (uint16)VM_PopW();

    FREF(VM_UserRAM, dest + pos) = value;
}


void VM_GetInt(void)
{
    uint16 src, pos;

    pos    = (uint16)VM_PopW();
    src    = (uint16)VM_PopW();

    VM_PushW((sint16)WREF(VM_UserRAM, src + pos));
}


void VM_GetLong(void)
{
    uint16 src, pos;

    pos    = (uint16)VM_PopW();
    src    = (uint16)VM_PopW();

    VM_PushL((sint32)LREF(VM_UserRAM, src + pos));
}


void VM_GetFloat(void)
{
    uint16 src, pos;

    pos    = (uint16)VM_PopW();
    src    = (uint16)VM_PopW();

    VM_PushF(FREF(VM_UserRAM, src + pos));
}


void VM_StoreAbsoluteByte(void)
{
    uint8 data;

    data                   = LOBYTE((uint16)VM_PopW());
    BREF(VM_OperandW, 0)   = data;
}


void VM_StoreAbsoluteInt(void)
{
    uint16 data;

    data                   = (uint16)VM_PopW();
    WREF(VM_OperandW, 0)   = data;
}


void VM_StoreAbsoluteLong(void)
{
    uint32 data;

    data                   = (uint32)VM_PopL();
    LREF(VM_OperandW, 0)   = data;
}


void VM_StoreAbsoluteFloat(void)
{
    float64 data;

    data                   = VM_PopF();
    FREF(VM_OperandW, 0)   = data;
}


void VM_LoadAbsoluteByte(void)
{
    uint8 data;

    data = BREF(VM_OperandW, 0);
    VM_PushW((sint16)data);
}


void VM_LoadAbsoluteInt(void)
{
    uint16 data;

    data = WREF(VM_OperandW, 0);
    VM_PushW((sint16)data);
}


void VM_LoadAbsoluteLong(void)
{
    uint32 data;

    data = LREF(VM_OperandW, 0);
    VM_PushL((sint32)data);
}


void VM_LoadAbsoluteFloat(void)
{
    float64 data;

    data = FREF(VM_OperandW, 0);
    VM_PushF(data);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_LS_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
