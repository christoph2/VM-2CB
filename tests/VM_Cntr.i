
%module vm_cntr

%include "Types.i"

%{
#include "VM.h"

void    Cntr_Init(void);
void    Cntr_Reset(void);
uint32  Cntr_GetFrequency1(void);
uint32  Cntr_GetFrequency2(void);

%}

void    Cntr_Init(void);
void    Cntr_Reset(void);
uint32  Cntr_GetFrequency1(void);
uint32  Cntr_GetFrequency2(void);

