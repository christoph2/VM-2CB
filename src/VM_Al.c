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

static void ArithmetricOperation(const FuncType * table);
static void ComparationOperation(const FuncType * table);
static void Unimplemented(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Arithmetric Operations.
**
*/
static void AddInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void AddLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void AddFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void SubInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void SubLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void SubFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void MulInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void MulLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void MulFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void DivInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void DivLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void DivFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void ModInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void ModLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void ModFloat(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Logic Operations.
**
*/
static void AndInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void AndLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void NandInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void NandLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void OrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void OrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void NorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void NorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void XorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void XorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void NxorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void NxorLong(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Compare Operations.
**
*/
static void EquInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void EquLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void EquFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void NeqInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void NeqLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void NeqFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void HiInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void HiLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void HiFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void HisInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void HisLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void HisFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void LoInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void LoLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void LoFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

static void LosInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void LosLong(const ALType * Param1, const ALType * Param2, ALType * Result);
static void LosFloat(const ALType * Param1, const ALType * Param2, ALType * Result);


/*
**
**  Compare Operations.
**
*/
static void ShlInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void ShlLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void ShrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void ShrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void AsrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void AsrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void RolInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void RolLong(const ALType * Param1, const ALType * Param2, ALType * Result);

static void RorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
static void RorLong(const ALType * Param1, const ALType * Param2, ALType * Result);


static const FuncType AddTable[] = {
    AddInt, AddLong, AddFloat
};

static const FuncType SubTable[] = {
    SubInt, SubLong, SubFloat
};

static const FuncType MulTable[] = {
    MulInt, MulLong, MulFloat
};

static const FuncType DivTable[] = {
    DivInt, DivLong, DivFloat
};

static const FuncType ModTable[] = {
    ModInt, ModLong, ModFloat
};

static const FuncType AndTable[] = {
    AndInt, AndLong, Unimplemented
};

static const FuncType NandTable[] = {
    NandInt, NandLong, Unimplemented
};

static const FuncType OrTable[] = {
    OrInt, OrLong, Unimplemented
};

static const FuncType NorTable[] = {
    NorInt, NorLong, Unimplemented
};

static const FuncType XorTable[] = {
    XorInt, XorLong, Unimplemented
};

static const FuncType NxorTable[] = {
    NxorInt, NxorLong, Unimplemented
};

static const FuncType EquTable[] = {
    EquInt, EquLong, EquFloat
};

static const FuncType NeqTable[] = {
    NeqInt, NeqLong, NeqFloat
};

static const FuncType HiTable[] = {
    HiInt, HiLong, HiFloat
};

static const FuncType HisTable[] = {
    HisInt, HisLong, HisFloat
};

static const FuncType LoTable[] = {
    LoInt, LoLong, LoFloat
};

static const FuncType LosTable[] = {
    LosInt, LosLong, LosFloat
};

static const FuncType ShlTable[] = {
    ShlInt, ShlLong, Unimplemented
};

static const FuncType ShrTable[] = {
    ShrInt, ShrLong, Unimplemented
};

static const FuncType AsrTable[] = {
    AsrInt, AsrLong, Unimplemented
};

static const FuncType RolTable[] = {
    RolInt, RolLong, Unimplemented
};

static const FuncType RorTable[] = {
    RorInt, RorLong, Unimplemented
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_AL_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

static void ArithmetricOperation(const FuncType * table)
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


static void ComparationOperation(const FuncType * table)
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
