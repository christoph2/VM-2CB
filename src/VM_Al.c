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
#include "VM_Al.h"

typedef union tagALType {
    sint16  Int;
    sint32  Long;
    float64 Float;
} ALType;

typedef void (*FuncType)(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void ArithmetricOperation(const FuncType * table);
STATIC void ComparationOperation(const FuncType * table);
STATIC void Unimplemented(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Arithmetric Operations.
**
*/
STATIC void AddInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void AddLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void AddFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void SubInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void SubLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void SubFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void MulInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void MulLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void MulFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void DivInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void DivLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void DivFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void ModInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void ModLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void ModFloat(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Logic Operations.
**
*/
STATIC void AndInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void AndLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void NandInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void NandLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void OrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void OrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void NorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void NorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void XorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void XorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void NxorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void NxorLong(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Compare Operations.
**
*/
STATIC void EquInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void EquLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void EquFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void NeqInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void NeqLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void NeqFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void HiInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void HiLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void HiFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void HisInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void HisLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void HisFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void LoInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void LoLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void LoFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void LosInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void LosLong(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void LosFloat(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Compare Operations.
**
*/
STATIC void ShlInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void ShlLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void ShrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void ShrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void AsrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void AsrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void RolInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void RolLong(const ALType * Param1, const ALType * Param2, ALType * Result);

STATIC void RorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
STATIC void RorLong(const ALType * Param1, const ALType * Param2, ALType * Result);


STATIC const FuncType AddTable[] = {
    AddInt, AddLong, AddFloat
};

STATIC const FuncType SubTable[] = {
    SubInt, SubLong, SubFloat
};

STATIC const FuncType MulTable[] = {
    MulInt, MulLong, MulFloat
};

STATIC const FuncType DivTable[] = {
    DivInt, DivLong, DivFloat
};

STATIC const FuncType ModTable[] = {
    ModInt, ModLong, ModFloat
};

STATIC const FuncType AndTable[] = {
    AndInt, AndLong, Unimplemented
};

STATIC const FuncType NandTable[] = {
    NandInt, NandLong, Unimplemented
};

STATIC const FuncType OrTable[] = {
    OrInt, OrLong, Unimplemented
};

STATIC const FuncType NorTable[] = {
    NorInt, NorLong, Unimplemented
};

STATIC const FuncType XorTable[] = {
    XorInt, XorLong, Unimplemented
};

STATIC const FuncType NxorTable[] = {
    NxorInt, NxorLong, Unimplemented
};

STATIC const FuncType EquTable[] = {
    EquInt, EquLong, EquFloat
};

STATIC const FuncType NeqTable[] = {
    NeqInt, NeqLong, NeqFloat
};

STATIC const FuncType HiTable[] = {
    HiInt, HiLong, HiFloat
};

STATIC const FuncType HisTable[] = {
    HisInt, HisLong, HisFloat
};

STATIC const FuncType LoTable[] = {
    LoInt, LoLong, LoFloat
};

STATIC const FuncType LosTable[] = {
    LosInt, LosLong, LosFloat
};

STATIC const FuncType ShlTable[] = {
    ShlInt, ShlLong, Unimplemented
};

STATIC const FuncType ShrTable[] = {
    ShrInt, ShrLong, Unimplemented
};

STATIC const FuncType AsrTable[] = {
    AsrInt, AsrLong, Unimplemented
};

STATIC const FuncType RolTable[] = {
    RolInt, RolLong, Unimplemented
};

STATIC const FuncType RorTable[] = {
    RorInt, RorLong, Unimplemented
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_AL_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

STATIC void ArithmetricOperation(const FuncType * table)
{
    ALType  Param1;
    ALType  Param2;
    ALType  Result;

    switch (VM_OperandB) {
        case CALC_INT_INT:
            Param1.Int = VM_PopW();
            Param2.Int = VM_PopW();
            table[0](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_INT_LONG:
            Param1.Long    = VM_PopL();
            Param2.Long    = (sint32)VM_PopW();
            table[1](&Param1, &Param2, &Result);
            VM_PushL(Result.Long);
            break;
        case CALC_INT_FLOAT:
            Param1.Float   = VM_PopF();
            Param2.Float   = (float64)(sint16)VM_PopW();
            table[2](&Param1, &Param2, &Result);
            VM_PushF(Result.Float);
            break;
        case CALC_LONG_INT:
            Param1.Long    = (sint32)VM_PopW();
            Param2.Long    = VM_PopL();
            table[1](&Param1, &Param2, &Result);
            VM_PushL(Result.Long);
            break;
        case CALC_LONG_LONG:
            Param1.Long    = VM_PopL();
            Param2.Long    = VM_PopL();
            table[1](&Param1, &Param2, &Result);
            VM_PushL(Result.Long);
            break;
        case CALC_LONG_FLOAT:
            Param1.Float   = VM_PopF();
            Param2.Float   = (float64)VM_PopL();
            table[2](&Param1, &Param2, &Result);
            VM_PushF(Result.Float);
            break;
        case CALC_FLOAT_INT:
            Param1.Float   = (float64)(sint16)VM_PopW();
            Param2.Float   = VM_PopF();
            table[2](&Param1, &Param2, &Result);
            VM_PushF(Result.Float);
            break;
        case CALC_FLOAT_LONG:
            Param1.Float   = (float64)(sint32)VM_PopL();
            Param2.Float   = VM_PopF();
            table[2](&Param1, &Param2, &Result);
            VM_PushF(Result.Float);
            break;
        case CALC_FLOAT_FLOAT:
            Param1.Float   = VM_PopF();
            Param2.Float   = VM_PopF();
            table[2](&Param1, &Param2, &Result);
            VM_PushF(Result.Float);
            break;
        default:
            CC_ASSERT(FALSE, ERROR_ILLOPA);
    }
}


STATIC void ComparationOperation(const FuncType * table)
{
    ALType  Param1;
    ALType  Param2;
    ALType  Result;

    switch (VM_OperandB) {
        case CALC_INT_INT:
            Param1.Int = VM_PopW();
            Param2.Int = VM_PopW();
            table[0](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_INT_LONG:
            Param1.Long    = VM_PopL();
            Param2.Long    = (sint32)VM_PopW();
            table[1](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_INT_FLOAT:
            Param1.Float   = VM_PopF();
            Param2.Float   = (float64)(sint16)VM_PopW();
            table[2](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_LONG_INT:
            Param1.Long    = (sint32)VM_PopW();
            Param2.Long    = VM_PopL();
            table[1](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_LONG_LONG:
            Param1.Long    = VM_PopL();
            Param2.Long    = VM_PopL();
            table[1](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_LONG_FLOAT:
            Param1.Float   = VM_PopF();
            Param2.Float   = (float64)VM_PopL();
            table[2](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_FLOAT_INT:
            Param1.Float   = (float64)(sint16)VM_PopW();
            Param2.Float   = VM_PopF();
            table[2](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_FLOAT_LONG:
            Param1.Float   = (float64)(sint32)VM_PopL();
            Param2.Float   = VM_PopF();
            table[2](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        case CALC_FLOAT_FLOAT:
            Param1.Float   = VM_PopF();
            Param2.Float   = VM_PopF();
            table[2](&Param1, &Param2, &Result);
            VM_PushW(Result.Int);
            break;
        default:
            CC_ASSERT(FALSE, ERROR_ILLOPA);
    }
}


void Unimplemented(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    UNREFERENCED_PARAMETER(Param1);
    UNREFERENCED_PARAMETER(Param2);
    UNREFERENCED_PARAMETER(Result);

    CC_ASSERT(FALSE, ERROR_ILLOPA);
}


/*
**
**  Add().
**
*/
void VM_Add(void)
{
    ArithmetricOperation(AddTable);
}


void AddInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = Param1->Int + Param2->Int;
}


void AddLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = Param1->Long + Param2->Long;
}


void AddFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Float = Param1->Float + Param2->Float;
}


/*
**
**  Sub().
**
*/
void VM_Sub(void)
{
    ArithmetricOperation(SubTable);
}


void SubInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = Param1->Int - Param2->Int;
}


void SubLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = Param1->Long - Param2->Long;
}


void SubFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Float = Param1->Float - Param2->Float;
}


/*
**
**  Mul().
**
*/
void VM_Mul(void)
{
    ArithmetricOperation(MulTable);
}


void MulInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = Param1->Int * Param2->Int;
}


void MulLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = Param1->Long * Param2->Long;
}


void MulFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Float = Param1->Float * Param2->Float;
}


/*
**
**  Div().
**
*/
void VM_Div(void)
{
    ArithmetricOperation(DivTable);
}


void DivInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    CC_ASSERT(Param2->Int != (sint16)0, ERROR_DIV0);

    Result->Int = Param1->Int / Param2->Int;
}


void DivLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    CC_ASSERT(Param2->Long != (sint32)0, ERROR_DIV0);

    Result->Long = Param1->Long / Param2->Long;
}


void DivFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    CC_ASSERT(Param2->Float != (float64)0.0, ERROR_DIV0);

    Result->Float = Param1->Float / Param2->Float;
}


/*
**
**  Mod().
**
*/
void VM_Mod(void)
{
    ArithmetricOperation(ModTable);
}


void ModInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    CC_ASSERT(Param2->Int != (sint16)0, ERROR_DIV0);

    Result->Int = Param1->Int % Param2->Int;
}


void ModLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    CC_ASSERT(Param2->Long != (sint32)0, ERROR_DIV0);

    Result->Long = Param1->Long % Param2->Long;
}


void ModFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    CC_ASSERT(Param2->Float != (float64)0.0, ERROR_DIV0);

    Result->Float = fmod(Param1->Float, Param2->Float);
}


/*
**
**  And().
**
*/
void VM_And(void)
{
    ArithmetricOperation(AndTable);
}


void AndInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((uint16)Param1->Int & (uint16)Param2->Int);
}


void AndLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (sint32)((uint32)Param1->Long & (uint32)Param2->Long);
}


/*
**
**  Nand().
**
*/
void VM_Nand(void)
{
    ArithmetricOperation(NandTable);
}


void NandInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((uint16) ~((uint16)Param1->Int & (uint16)Param2->Int));
}


void NandLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (sint32)((uint32) ~((uint32)Param1->Long & (uint32)Param2->Long));
}


/*
**
**  Or().
**
*/
void VM_Or(void)
{
    ArithmetricOperation(OrTable);
}


void OrInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((uint16)Param1->Int | (uint16)Param2->Int);
}


void OrLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (sint32)((uint32)Param1->Long | (uint32)Param2->Long);
}


/*
**
**  Nor().
**
*/
void VM_Nor(void)
{
    ArithmetricOperation(NorTable);
}


void NorInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((uint16) ~((uint16)Param1->Int | (uint16)Param2->Int));
}


void NorLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (sint32)((uint32) ~((uint32)Param1->Long | (uint32)Param2->Long));
}


/*
**
**  Xor().
**
*/
void VM_Xor(void)
{
    ArithmetricOperation(XorTable);
}


void XorInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((uint16)Param1->Int ^ (uint16)Param2->Int);
}


void XorLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (sint32)((uint32)Param1->Long ^ (uint32)Param2->Long);
}


/*
**
**  Nxor().
**
*/
void VM_Nxor(void)
{
    ArithmetricOperation(NxorTable);
}


void NxorInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((uint16) ~((uint16)Param1->Int ^ (uint16)Param2->Int));
}


void NxorLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (sint32)((uint32) ~((uint32)Param1->Long ^ (uint32)Param2->Long));
}


/*
**
**  Equ().
**
*/
void VM_Equ(void)
{
    ComparationOperation(EquTable);
}


void EquInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Int == Param2->Int) ? CC_TRUE : CC_FALSE);
}


void EquLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Long == Param2->Long) ? CC_TRUE : CC_FALSE);
}


void EquFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((fabs(Param1->Float - Param2->Float) < 0.00001) ? CC_TRUE : CC_FALSE);
}


/*
**
**  Neq().
**
*/
void VM_Neq(void)
{
    ComparationOperation(NeqTable);
}


void NeqInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Int == Param2->Int) ? CC_FALSE : CC_TRUE);
}


void NeqLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Long == Param2->Long) ? CC_FALSE : CC_TRUE);
}


void NeqFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((fabs(Param1->Float - Param2->Float) < 0.00001) ? CC_FALSE : CC_TRUE);
}


/*
**
**  Hi().
**
*/
void VM_Hi(void)
{
    ComparationOperation(HiTable);
}


void HiInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Int > Param2->Int) ? CC_TRUE : CC_FALSE);
}


void HiLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Long > Param2->Long) ? CC_TRUE : CC_FALSE);
}


void HiFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Float > Param2->Float) ? CC_TRUE : CC_FALSE);
}


/*
**
**  His().
**
*/
void VM_His(void)
{
    ComparationOperation(HisTable);
}


void HisInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Int >= Param2->Int) ? CC_TRUE : CC_FALSE);
}


void HisLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Long >= Param2->Long) ? CC_TRUE : CC_FALSE);
}


void HisFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Float >= Param2->Float) ? CC_TRUE : CC_FALSE);
}


/*
**
**  Lo().
**
*/
void VM_Lo(void)
{
    ComparationOperation(LoTable);
}


void LoInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Int < Param2->Int) ? CC_TRUE : CC_FALSE);
}


void LoLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Long < Param2->Long) ? CC_TRUE : CC_FALSE);
}


void LoFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Float < Param2->Float) ? CC_TRUE : CC_FALSE);
}


/*
**
**  Los().
**
*/
void VM_Los(void)
{
    ComparationOperation(LosTable);
}


void LosInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Int <= Param2->Int) ? CC_TRUE : CC_FALSE);
}


void LosLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Long <= Param2->Long) ? CC_TRUE : CC_FALSE);
}


void LosFloat(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)((Param1->Float <= Param2->Float) ? CC_TRUE : CC_FALSE);
}


/*
**
**  Shl().
**
*/
void VM_Shl(void)
{
    ArithmetricOperation(ShlTable);
}


void ShlInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = Param1->Int << (Param2->Int & (uint8)0x0f);
}


void ShlLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = Param1->Long << (Param2->Long & (uint8)0x1f);
}


/*
**
**  Shr().
**
*/
void VM_Shr(void)
{
    ArithmetricOperation(ShrTable);
}


void ShrInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (uint16)Param1->Int >> (uint8)(Param2->Int & (uint8)0x0f);
}


void ShrLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (uint32)Param1->Long >> (uint8)(Param2->Long & (uint8)0x1f);
}


/*
**
**  Asr().
**
*/

/*
**
**  !!! WARNING !!!: The 'ASR'-Functions are exploiting undefined behaviour
**                   ('right shift of signed quantity') to simulate CC2.
**
*/
void VM_Asr(void)
{
    ArithmetricOperation(AsrTable);
}


void AsrInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (sint16)Param1->Int >> (uint8)(Param2->Int & (uint8)0x0f);
}


void AsrLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (sint32)Param1->Long >> (uint8)(Param2->Long & (uint8)0x1f);
}


/*
**
**  Rol().
**
*/
void VM_Rol(void)
{
    ArithmetricOperation(RolTable);
}


void RolInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = Param1->Int << Param2->Int;
}


void RolLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = Param1->Long << Param2->Long;
}


/*
**
**  Ror().
**
*/
void VM_Ror(void)
{
    ArithmetricOperation(RorTable);
}


void RorInt(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Int = (uint16)Param1->Int >> (uint16)Param2->Int;
}


void RorLong(const ALType * Param1, const ALType * Param2, ALType * Result)
{
    Result->Long = (uint32)Param1->Long >> (uint32)Param2->Long;
}


void VM_CastLongToInt(void)
{
    VM_PushW((sint16)(VM_PopL() & ((uint32)0x0000ffffL)));
}


void VM_CastIntToLong(void)
{
    VM_PushL((sint32)VM_PopW());
}


void VM_CastFloatToInt(void)
{
    VM_PushW((sint16)VM_PopF());
}


void VM_CastFloatToLong(void)
{
    VM_PushL((sint32)VM_PopF());
}


void VM_CastIntToFloat(void)
{
    VM_PushF((float64)VM_PopW());
}


void VM_CastLongToFloat(void)
{
    VM_PushF((float64)VM_PopL());
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_AL_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
