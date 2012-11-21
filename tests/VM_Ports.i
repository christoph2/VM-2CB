
%module vm_ports

%include "Types.i"

%{
#include "VM.h"

void VM_InitPorts(void);

void    VM_GetSinglePort(void), VM_GetNibblePort(void), VM_GetBytePort(void), VM_GetWordPort(void);
void    VM_SetSinglePort(void), VM_SetNibblePort(void), VM_SetBytePort(void), VM_SetWordPort(void);
void    VM_DeactSinglePort(void), VM_DeactNibblePort(void), VM_DeactBytePort(void), VM_DeactWordPort(void);
void    VM_ToggleSinglePort(void);
void    VM_PulseSinglePort(void), VM_GetCount(void), VM_GetFreq(void);
void    VM_GetAdcPort(void);

%}

void VM_InitPorts(void);

void    VM_GetSinglePort(void), VM_GetNibblePort(void), VM_GetBytePort(void), VM_GetWordPort(void);
void    VM_SetSinglePort(void), VM_SetNibblePort(void), VM_SetBytePort(void), VM_SetWordPort(void);
void    VM_DeactSinglePort(void), VM_DeactNibblePort(void), VM_DeactBytePort(void), VM_DeactWordPort(void);
void    VM_ToggleSinglePort(void);
void    VM_PulseSinglePort(void), VM_GetCount(void), VM_GetFreq(void);
void    VM_GetAdcPort(void);

