
%module vm_tmr

%include "Types.i"

%{
#include "VM.h"

void    TMR_Init(void);
uint32  TMR_GetTofCount(void);
void    TMR_TimerTick(void);

%}

void    TMR_Init(void);
uint32  TMR_GetTofCount(void);
void    TMR_TimerTick(void);

