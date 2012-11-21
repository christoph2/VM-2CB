
%module vm_lpt

%include "Types.i"

%{
#include "VM.h"

void Lpt_Init(void), Lpt_Flush(void), Lpt_Ready(void);
void Lpt_Put(void), Lpt_Print(void);

%}

void Lpt_Init(void), Lpt_Flush(void), Lpt_Ready(void);
void Lpt_Put(void), Lpt_Print(void);

