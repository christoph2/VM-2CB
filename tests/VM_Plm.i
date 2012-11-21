
%module vm_plm

%include "Types.i"

%{
#include "VM.h"

void Plm_Init(void), Plm_SetTB(void), Plm_SetPM(void), Plm_SetPL(void), Plm_Out(void), Plm_Beep(void);
void Plm_ToneOut(uint16 tone);
%}

void Plm_Init(void), Plm_SetTB(void), Plm_SetPM(void), Plm_SetPL(void), Plm_Out(void), Plm_Beep(void);
void Plm_ToneOut(uint16 tone);
