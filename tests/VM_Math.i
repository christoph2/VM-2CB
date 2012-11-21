
%module vm_math

%include "Types.i"

%{
#include "VM.h"

void MinInt(void), MinLong(void), MinFloat(void);
void MaxInt(void), MaxLong(void), MaxFloat(void);

void MF_Sqr(void), MF_Sqrt(void), MF_Curt(void);
void MF_Sin(void), MF_Cos(void), MF_Tan(void);
void MF_Asin(void), MF_Acos(void), MF_Atan(void);
void MF_Log(void), MF_Ln(void), MF_Exp(void);
void MF_Pow(void), MF_Ceil(void), MF_Floor(void);

%}

void MinInt(void), MinLong(void), MinFloat(void);
void MaxInt(void), MaxLong(void), MaxFloat(void);

void MF_Sqr(void), MF_Sqrt(void), MF_Curt(void);
void MF_Sin(void), MF_Cos(void), MF_Tan(void);
void MF_Asin(void), MF_Acos(void), MF_Atan(void);
void MF_Log(void), MF_Ln(void), MF_Exp(void);
void MF_Pow(void), MF_Ceil(void), MF_Floor(void);

