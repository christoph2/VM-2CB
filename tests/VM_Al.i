
%module vm_al

%include "Types.i"

%{
#include "VM.h"

typedef union tagALType {
    sint16  Int;
    sint32  Long;
    float64 Float;
} ALType;

void VM_Add(void), VM_Sub(void), VM_Mul(void), VM_Div(void), VM_Mod(void);
void VM_And(void), VM_Nand(void), VM_Or(void), VM_Nor(void), VM_Xor(void), VM_Nxor(void);
void VM_Equ(void), VM_Neq(void), VM_Hi(void), VM_His(void), VM_Lo(void), VM_Los(void);
void VM_Shl(void), VM_Shr(void), VM_Asr(void), VM_Rol(void), VM_Ror(void);

void VM_CastLongToInt(void), VM_CastIntToLong(void);
void VM_CastFloatToInt(void), VM_CastFloatToLong(void);
void VM_CastIntToFloat(void), VM_CastLongToFloat(void);

void AddInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void AddLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void AddFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void SubInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void SubLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void SubFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void MulInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void MulLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void MulFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void DivInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void DivLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void DivFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void ModInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void ModLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void ModFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void AndInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void AndLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void NandInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NandLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void OrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void OrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void NorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void XorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void XorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void NxorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NxorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void EquInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void EquLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void EquFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void NeqInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NeqLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void NeqFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void HiInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void HiLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void HiFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void HisInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void HisLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void HisFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void LoInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void LoLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void LoFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void LosInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void LosLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void LosFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void ShlInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void ShlLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void ShrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void ShrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void AsrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void AsrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void RolInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void RolLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void RorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void RorLong(const ALType * Param1, const ALType * Param2, ALType * Result);
%}

void VM_Add(void), VM_Sub(void), VM_Mul(void), VM_Div(void), VM_Mod(void);
void VM_And(void), VM_Nand(void), VM_Or(void), VM_Nor(void), VM_Xor(void), VM_Nxor(void);
void VM_Equ(void), VM_Neq(void), VM_Hi(void), VM_His(void), VM_Lo(void), VM_Los(void);
void VM_Shl(void), VM_Shr(void), VM_Asr(void), VM_Rol(void), VM_Ror(void);

void VM_CastLongToInt(void), VM_CastIntToLong(void);
void VM_CastFloatToInt(void), VM_CastFloatToLong(void);
void VM_CastIntToFloat(void), VM_CastLongToFloat(void);

void AddInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void AddLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void AddFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void SubInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void SubLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void SubFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void MulInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void MulLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void MulFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void DivInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void DivLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void DivFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void ModInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void ModLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void ModFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void AndInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void AndLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void NandInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NandLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void OrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void OrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void NorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void XorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void XorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void NxorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NxorLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void EquInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void EquLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void EquFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void NeqInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void NeqLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void NeqFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void HiInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void HiLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void HiFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void HisInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void HisLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void HisFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void LoInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void LoLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void LoFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void LosInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void LosLong(const ALType * Param1, const ALType * Param2, ALType * Result);
void LosFloat(const ALType * Param1, const ALType * Param2, ALType * Result);

void ShlInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void ShlLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void ShrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void ShrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void AsrInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void AsrLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void RolInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void RolLong(const ALType * Param1, const ALType * Param2, ALType * Result);

void RorInt(const ALType * Param1, const ALType * Param2, ALType * Result);
void RorLong(const ALType * Param1, const ALType * Param2, ALType * Result);
