
%module vm_str

%include "Types.i"

%{
#include "VM.h"

#define MAX_STR_LEN     30

typedef struct tagStr {
    uint8   data[MAX_STR_LEN];
    uint8   len;
} Str;

void Str_Clear(void), Str_GetLength(void), Str_Fill(void);
void Str_PutChar(void), Str_PutString(void), Str_PutConstString(void);
void Str_PutInt(void), Str_PutLong(void), Str_PutFloat(void);
void Str_PutFormattedInt(void), Str_PutFormattedLong(void);
void Str_PutFormattedFloat(void), Str_PutByteMask(void);
void Str_Copy(Str * dst, Str * src);
void putMask(uint8 value, uint8 c0, uint8 c1, uint8 * str);

extern uint8 Str_ScratchBuffer[MAX_STR_LEN + 1];
%}

#define MAX_STR_LEN     30

%constant double BLAH = 42.37;

void Str_Clear(void), Str_GetLength(void), Str_Fill(void);
void Str_PutChar(void), Str_PutString(void), Str_PutConstString(void);
void Str_PutInt(void), Str_PutLong(void), Str_PutFloat(void);
void Str_PutFormattedInt(void), Str_PutFormattedLong(void);
void Str_PutFormattedFloat(void), Str_PutByteMask(void);
void Str_Copy(Str * dst, Str * src);
void putMask(uint8 value, uint8 c0, uint8 c1, uint8 * str);

extern uint8 Str_ScratchBuffer[MAX_STR_LEN + 1];

