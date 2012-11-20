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

#define  _CRT_SECURE_NO_WARNINGS    1

#include "VM_Str.h"
#include <stdio.h>
#include <string.h>


#define MAX_STR_LEN ((uint8)30)


typedef struct tagStr {
    uint8   data[MAX_STR_LEN];
    uint8   len;
} Str;


STATIC void Str_Clear(void), Str_GetLength(void), Str_Fill(void);
STATIC void Str_PutChar(void), Str_PutString(void), Str_PutConstString(void);
STATIC void Str_PutInt(void), Str_PutLong(void), Str_PutFloat(void);
STATIC void Str_PutFormattedInt(void), Str_PutFormattedLong(void);
STATIC void Str_PutFormattedFloat(void), Str_PutByteMask(void);

STATIC void Str_Copy(Str * dst, Str * src);
STATIC void putMask(uint8 value, uint8 c0, uint8 c1, uint8 * str);

STATIC const VoidFunctionType FuncTab[] = {
    Str_Clear,            Str_GetLength,         Str_Fill,            Str_PutChar,
    Str_PutString,        Str_PutConstString,    Str_PutInt,
    Str_PutLong,          Str_PutFloat,          Str_PutFormattedInt,
    Str_PutFormattedLong, Str_PutFormattedFloat,
    Str_PutByteMask
};

STATIC uint8 Str_ScratchBuffer[MAX_STR_LEN + 1];

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_STR_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void VM_String(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(FuncTab), ERROR_ILLOPA);
    FuncTab[VM_OperandB]();
}


STATIC void Str_Clear(void)
{
    Str * str = (Str *)BPTR(VM_UserRAM, VM_PopW());

    if (str->len != (uint8)0x00) {
        str->len = (uint8)0x000;
        Utl_MemSet((void *)str->data, (uint8)0, (SizeType)MAX_STR_LEN);
    }
}


STATIC void Str_GetLength(void)
{
    VM_PushW((sint16)((Str *)BPTR(VM_UserRAM, VM_PopW()))->len);
}


STATIC void Str_Fill(void)
{
    uint8   filler = (uint8)VM_PopW();
    uint8   offset = (uint8)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, VM_PopW());

    if (offset < MAX_STR_LEN) {
        str->len = MAX_STR_LEN;
        Utl_MemSet((void *)(str->data + offset), filler, (SizeType)(MAX_STR_LEN - (SizeType)offset));
    }
}


STATIC void Str_PutChar(void)
{
    uint8   ch     = (uint8)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, VM_PopW());

    if (str->len < MAX_STR_LEN) {
        str->data[str->len++] = ch;
    }
}


STATIC void Str_PutString(void)
{
    Str *   src    = (Str *)BPTR(VM_UserRAM, VM_PopW());
    Str *   dst    = (Str *)BPTR(VM_UserRAM, VM_PopW());

    Str_Copy(dst, src);
}


STATIC void Str_PutConstString(void)
{
    Str *   src    = (Str *)VM_GetConstantPtr((uint16)VM_PopW());
    Str *   dst    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());

    Str_Copy(dst, src);
}


STATIC void Str_PutInt(void)
{
    sint16  value  = VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;
    uint8   byteCount;

    if (len < MAX_STR_LEN) {
        byteCount = MAX_STR_LEN - len;
        sprintf((char * )Str_ScratchBuffer, "%d", value);
        strncpy((char * )str->data[str->len], (char *)Str_ScratchBuffer, byteCount);
        len += byteCount;
    }
}


STATIC void Str_PutLong(void)
{
    uint32  value  = (uint32)VM_PopL();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;
    uint8   byteCount;

    if (len < MAX_STR_LEN) {
        byteCount = MAX_STR_LEN - len;
        sprintf((char * )Str_ScratchBuffer, "%ld", value);
        strncpy((char * )str->data[str->len], (char *)Str_ScratchBuffer, byteCount);
        len += byteCount;

    }
}


STATIC void Str_PutFloat(void)
{
    float64  value  = VM_PopF();
    Str *    str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8    len    = str->len;
    uint8    byteCount;

    if (len < MAX_STR_LEN) {
        byteCount = MAX_STR_LEN - len;
        sprintf((char * )Str_ScratchBuffer, "%f", value);
        strncpy((char * )str->data[str->len], (char *)Str_ScratchBuffer, byteCount);
        len += byteCount;

    }
}


STATIC void Str_PutFormattedInt(void)
{
    sint16  format = VM_PopW();
    uint16  value  = (uint16)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;
    uint8   byteCount;
    
    if (len < MAX_STR_LEN) {
        byteCount = MAX_STR_LEN - len;
    }
}


STATIC void Str_PutFormattedLong(void)
{
    sint16  format = VM_PopW();
    uint32  value  = (uint32)VM_PopL();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;
    uint8   byteCount;
    
    if (len < MAX_STR_LEN) {
        byteCount = MAX_STR_LEN - len;
    }
}


STATIC void Str_PutFormattedFloat(void)
{
    sint16   format = VM_PopW();
    float64  value  = VM_PopF();
    Str *    str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8    len    = str->len;
    uint8    byteCount;
    
    if (len < MAX_STR_LEN) {
        byteCount = MAX_STR_LEN - len;
    }

}


STATIC void Str_PutByteMask(void)
{
    uint8  c0     = (uint8)VM_PopW();
    uint8  c1     = (uint8)VM_PopW();
    uint8  value  = (uint8)VM_PopW();
    Str *  str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8  len    = str->len;
    uint8  byteCount, idx;
    
    putMask(value, c0, c1, (uint8 *)Str_ScratchBuffer);

    if (len < MAX_STR_LEN) {
        byteCount = MIN((MAX_STR_LEN - len), (Utl_StrLen(Str_ScratchBuffer) - 1));

        idx = len;
        while (byteCount) {
            str->data[idx++] = Str_ScratchBuffer[byteCount--];
        }
        str->len = idx;
    }
}


/*
**
**      Helper-Functions.
**
*/
STATIC void Str_Copy(Str * dst, Str * src)
{
    uint8 i, j;

    if ((src->len != (uint8)0x00) && (dst->len < MAX_STR_LEN)) {
        i  = dst->len;
        j  = (uint8)0x00;

        while ((i < MAX_STR_LEN) && (j < src->len)) {
            dst->data[i++] = src->data[j++];
            dst->len++;
        }
    }
}

STATIC void putMask(uint8 value, uint8 c0, uint8 c1, uint8 * str)
{
    uint8 q;
    uint16 r;
    uint16 s;
    uint8 idx;
 
    idx = (uint8)0x00;
  
    s = value;
    while (s) {
        q = s >> 1;
        r = s % 2;

        if (r == (uint8)0x01) {
            Str_ScratchBuffer[idx] = c1;
        } else {
            Str_ScratchBuffer[idx] = c0;    
        }
  
        s = q;
        ++idx;
    }
    str[idx] = '\x0';
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_STR_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
