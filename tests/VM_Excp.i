
%module vm_excp

%include "Types.i"

%{
#include "VM.h"

void    Exception(uint8 code);
void    ShowStatus(uint8 code);

%}

#define STATUS_RUNNING      0x08
#define STATUS_HOSTMODE     0x09
#define STATUS_BOOTMODUS    0x0a

#define ERROR_UNDOPC        0x01
#define ERROR_ILLOPA        0x02
#define ERROR_FPE           0x03
#define ERROR_DIV0          0x04
#define ERROR_BURN          0x05
#define ERROR_MEMCORRPT     0x06
#define ERROR_OOM           0x07
#define ERROR_NULLPTR       0x08

#define ERROR_EDOM          0x09

void    Exception(uint8 code);
void    ShowStatus(uint8 code);


