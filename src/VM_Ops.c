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
#include "VM_Al.h"
#include "VM_Can.h"
#include "VM_Com.h"
#include "VM_Iic.h"
#include "VM_Lcd.h"
#include "VM_Lpt.h"
#include "VM_Ls.h"
#include "VM_Math.h"
#include "VM_Plm.h"
#include "VM_Ports.h"
#include "VM_Str.h"
#include "VM_Twb.h"

/*root*/ const VM_FunctionType VM_CodeTab[] = {

    /*
    **  VM_Code_A
    */
    VM_Nop,                 VM_Quit,                VM_Yield,               VM_Sleep,               VM_Capture,
    VM_Release,             VM_FastReturn,          VM_MakeGlobalPointer,   VM_LoadRefConstByte,    VM_LoadRefConstInt,
    VM_LoadRefConstLong,    VM_LoadRefConstFloat,   VM_LoadRefByte,         VM_LoadRefInt,          VM_LoadRefLong,
    VM_LoadRefFloat,        VM_IncLoadRefByte,      VM_IncLoadRefInt,       VM_IncLoadRefLong,      VM_IncLoadRefFloat,
    VM_StoreRefByte,        VM_StoreRefInt,         VM_StoreRefLong,        VM_StoreRefFloat,       VM_CastIntToLong,
    VM_CastIntToFloat,      VM_CastLongToInt,       VM_CastLongToFloat,     VM_CastFloatToInt,      VM_CastFloatToLong,
    VM_InvertInt,           VM_InvertLong,          VM_InvertFloat,         VM_NegInt,              VM_NegLong,
    VM_NegFloat,            VM_AbsInt,              VM_AbsLong,             VM_AbsFloat,            VM_PutInt,
    VM_PutLong,             VM_PutFloat,            VM_GetInt,              VM_GetLong,             VM_GetFloat,
    VM_GetSinglePort,       VM_GetNibblePort,       VM_GetBytePort,         VM_GetWordPort,         VM_GetAdcPort,
    VM_SetSinglePort,       VM_SetNibblePort,       VM_SetBytePort,         VM_SetWordPort,         VM_DeactSinglePort,
    VM_DeactNibblePort,     VM_DeactBytePort,       VM_DeactWordPort,       VM_ToggleSinglePort,    VM_PulseSinglePort,
    VM_GetCount,            VM_GetFreq,             VM_Syscall,             VM_Sysjump,

    /*
    **  VM_Code_B
    */
    VM_Nop,                 VM_Reset,               VM_Run,                 VM_Resume,              VM_LoadByteImmidiate,
    VM_Add,                 VM_Sub,                 VM_Mul,                 VM_Div,                 VM_Mod,
    VM_Equ,                 VM_Neq,                 VM_Hi,                  VM_His,                 VM_Lo,
    VM_Los,                 VM_And,                 VM_Nand,                VM_Or,                  VM_Nor,
    VM_Xor,                 VM_Nxor,                VM_Shl,                 VM_Shr,                 VM_Asr,
    VM_Rol,                 VM_Ror,                 VM_Min,                 VM_Max,                 VM_MathFunction,
    VM_LoadSysvarInt,       VM_StoreSysvarInt,      VM_LoadSysvarLong,      VM_StoreSysvarLong,     VM_String,
    VM_Plm,                 HwCom,                  SwCom,                  VM_Lpt,                 VM_Can,
    VM_Iic,                 VM_Twb,                 VM_Lcd,                 VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,

    /*
    ** VM_Code_C
    */
    VM_Nop,                 VM_Call,                VM_Return,              VM_IncSP,               VM_Branch,
    VM_BranchIfZero,        VM_LoadImmidiateInt,    VM_LoadConstByte,       VM_LoadConstInt,        VM_LoadConstLong,
    VM_LoadConstFloat,      VM_LoadByte,            VM_LoadInt,             VM_LoadLong,            VM_LoadFloat,
    VM_LoadLocalByte,       VM_LoadLocalInt,        VM_LoadLocalLong,       VM_LoadLocalFloat,      VM_StoreByte,
    VM_StoreInt,            VM_StoreLong,           VM_StoreFloat,          VM_StoreLocalByte,      VM_StoreLocalInt,
    VM_StoreLocalLong,      VM_StoreLocalFloat,     VM_StoreKeepByte,       VM_StoreKeepInt,        VM_StoreKeepLong,
    VM_StoreKeepFloat,      VM_StoreKeepLocalByte,  VM_StoreKeepLocalInt,   VM_StoreKeepLocalLong,  VM_StoreKeepLocalFloat,
    VM_IncLoadByte,         VM_IncLoadInt,          VM_IncLoadLong,         VM_IncLoadFloat,        VM_IncLoadLocalByte,
    VM_IncLoadLocalInt,     VM_IncLoadLocalLong,    VM_IncLoadLocalFloat,   VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,

    /*
    ** VM_Code_D
    */
    VM_Nop,                 VM_ReturnValue,         VM_LoadAbsoluteByte,    VM_LoadAbsoluteInt,     VM_LoadAbsoluteLong,
    VM_LoadAbsoluteFloat,   VM_StoreAbsoluteByte,   VM_StoreAbsoluteInt,    VM_StoreAbsoluteLong,   VM_StoreAbsoluteFloat,
    VM_InlineSyscall,       VM_InlineSysjump,       VM_Hook,                VM_Save,                VM_Restore,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
    VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,     VM_UndefinedOpcode,
};
