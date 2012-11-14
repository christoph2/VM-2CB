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

#include "VM_Str.h"

#define MAX_STR_LEN ((uint8)30)

static void it(uint8 * buf, sint16 num);


typedef struct tagStr {
    uint8   data[MAX_STR_LEN];
    uint8   len;
} Str;

static void Str_Clear(void), Str_GetLength(void), Str_Fill(void);
static void Str_PutChar(void), Str_PutString(void), Str_PutConstString(void);
static void Str_PutInt(void), Str_PutLong(void), Str_PutFloat(void);
static void Str_PutFormattedInt(void), Str_PutFormattedLong(void);
static void Str_PutFormattedFloat(void), Str_PutByteMask(void);

static void Str_Copy(Str * dst, Str * src);


static const VoidFunctionType FuncTab[] = {
    Str_Clear,            Str_GetLength,         Str_Fill,            Str_PutChar,
    Str_PutString,        Str_PutConstString,    Str_PutInt,
    Str_PutLong,          Str_PutFloat,          Str_PutFormattedInt,
    Str_PutFormattedLong, Str_PutFormattedFloat,
    Str_PutByteMask
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_STR_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void VM_String(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(FuncTab), ERROR_ILLOPA);
    FuncTab[VM_OperandB]();
}


static void Str_Clear(void)
{
    Str * str = (Str *)BPTR(VM_UserRAM, VM_PopW());

    if (str->len != (uint8)0x00) {
        str->len = (uint8)0x000;
        Utl_MemSet((void *)str->data, (uint8)0, (SizeType)MAX_STR_LEN);
    }
}


static void Str_GetLength(void)
{
    VM_PushW((sint16)((Str *)BPTR(VM_UserRAM, VM_PopW()))->len);
}


static void Str_Fill(void)
{
    uint8   filler = (uint8)VM_PopW();
    uint8   offset = (uint8)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, VM_PopW());

    if (offset < MAX_STR_LEN) {
        str->len = MAX_STR_LEN;
        Utl_MemSet((void *)(str->data + offset), filler, (SizeType)(MAX_STR_LEN - (SizeType)offset));
    }
}


static void Str_PutChar(void)
{
    uint8   ch     = (uint8)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, VM_PopW());

    if (str->len < MAX_STR_LEN) {
        str->data[str->len++] = ch;
    }
}


static void Str_PutString(void)
{
    Str *   src    = (Str *)BPTR(VM_UserRAM, VM_PopW());
    Str *   dst    = (Str *)BPTR(VM_UserRAM, VM_PopW());

    Str_Copy(dst, src);
}


static void Str_PutConstString(void)
{
    Str *   src    = (Str *)VM_GetConstantPtr((uint16)VM_PopW());
    Str *   dst    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());

    Str_Copy(dst, src);
}


static void Str_PutInt(void)
{
    uint16  value  = (uint16)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;

    if (len < MAX_STR_LEN) {

    }
}


static void Str_PutLong(void)
{
    uint32  value  = (uint32)VM_PopL();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;

    if (len < MAX_STR_LEN) {

    }
}


static void Str_PutFloat(void)
{
    float64  value  = (float64)VM_PopF();
    Str *    str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8    len    = str->len;

    if (len < MAX_STR_LEN) {

    }
}


static void Str_PutFormattedInt(void)
{
    uint16  format = (uint16)VM_PopW();
    uint16  value  = (uint16)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;

}


static void Str_PutFormattedLong(void)
{
    uint16  format = (uint16)VM_PopW();
    uint32  value  = (uint32)VM_PopL();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;

}


static void Str_PutFormattedFloat(void)
{
    uint16   format = (uint16)VM_PopW();
    float64  value  = (float64)VM_PopF();
    Str *    str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8    len    = str->len;

}


static void Str_PutByteMask(void)
{
    uint16  c0     = (uint16)VM_PopW();
    uint16  c1     = (uint16)VM_PopW();
    uint16  value  = (uint16)VM_PopW();
    Str *   str    = (Str *)BPTR(VM_UserRAM, (uint16)VM_PopW());
    uint8   len    = str->len;

}


/*
**
**      Helper-Functions.
**
*/
static void Str_Copy(Str * dst, Str * src)
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

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_STR_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
