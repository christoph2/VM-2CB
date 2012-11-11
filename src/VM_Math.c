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

#include "VM_Math.h"

#define ONE_THIRD ((float64)((float64)1.0 / (float64)3.0))

static void MinInt(void), MinLong(void), MinFloat(void);
static void MaxInt(void), MaxLong(void), MaxFloat(void);

static void MF_Sqr(void), MF_Sqrt(void), MF_Curt(void);
static void MF_Sin(void), MF_Cos(void), MF_Tan(void);
static void MF_Asin(void), MF_Acos(void), MF_Atan(void);
static void MF_Log(void), MF_Ln(void), MF_Exp(void);
static void MF_Pow(void), MF_Ceil(void), MF_Floor(void);


static const VoidFunctionType MinTab[] = {
    MinInt, MinLong, MinFloat
};

static const VoidFunctionType MaxTab[] = {
    MaxInt, MaxLong, MaxFloat
};

static const VoidFunctionType MFTab[] = {
    MF_Sqr,  MF_Sqrt, MF_Curt, MF_Sin,
    MF_Cos,  MF_Tan,  MF_Asin, MF_Acos,
    MF_Atan, MF_Log,  MF_Ln,   MF_Exp,
    MF_Pow,  MF_Ceil, MF_Floor
};


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_?_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void VM_InvertInt(void)
{
    VM_PushW(~VM_PopW());
}


void VM_InvertLong(void)
{
    VM_PushL(~VM_PopL());
}


void VM_InvertFloat(void)
{
    uint16  w;
    float64 t;

    t = VM_PopF();

    if (t == 0.0) {   /* todo: DBL_EPSILON!!! */
        w = CC_TRUE;
    } else {
        w = CC_FALSE;
    }

    VM_PushW((sint16)w);
}


void VM_NegInt(void)
{
    VM_PushW((sint16)(-1 * VM_PopW()));
}


void VM_NegLong(void)
{
    VM_PushL((sint32)(-1L * VM_PopL()));
}


void VM_NegFloat(void)
{
    VM_PushF((float64)(-1.0 * VM_PopF()));
}


void VM_AbsInt(void)
{
    sint16 w;

    w = VM_PopW();
    VM_PushW((sint16)(( w < (sint16)0) ? w * -1 : w));
}


void VM_AbsLong(void)
{
    sint32 w;

    w = VM_PopL();
    VM_PushL((sint32)((w < (sint32)0L) ? w * -1L : w));

}


void VM_AbsFloat(void)
{
    VM_PushF(fabs(VM_PopF()));
}


void VM_Min(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(MinTab), ERROR_ILLOPA);
    MinTab[VM_OperandB]();
}


void VM_Max(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(MaxTab), ERROR_ILLOPA);
    MaxTab[VM_OperandB]();
}


void MinInt(void)
{
    VM_PushW(MIN(VM_PopW(), VM_PopW()));
}


void MinLong(void)
{
    VM_PushL(MIN(VM_PopL(), VM_PopL()));
}


void MinFloat(void)
{
    VM_PushF(MIN(VM_PopF(), VM_PopF()));
}


void MaxInt(void)
{
    VM_PushW(MAX(VM_PopW(), VM_PopW()));
}


void MaxLong(void)
{
    VM_PushL(MAX(VM_PopL(), VM_PopL()));
}


void MaxFloat(void)
{
    VM_PushF(MAX(VM_PopF(), VM_PopF()));
}


void VM_MathFunction(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(MFTab), ERROR_ILLOPA);
    MFTab[VM_OperandB]();

}


void MF_Sqr(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(pow(arg, (float64)2.0));
}


void MF_Sqrt(void)
{
    float64 arg;

    arg = VM_PopF();
    CC_ASSERT(arg >= 0, ERROR_EDOM);
    VM_PushF(sqrt(arg));
}


void MF_Curt(void)
{
    float64 arg;

    arg = VM_PopF();
    CC_ASSERT(arg >= 0, ERROR_EDOM);
    VM_PushF(pow(arg, (float64)ONE_THIRD));
}


void MF_Sin(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(sin(arg));
}


void MF_Cos(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(cos(arg));
}


void MF_Tan(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(tan(arg));
}


void MF_Asin(void)
{
    float64 arg;

    arg = VM_PopF();
    CC_ASSERT(((arg >= (float64) - 1.0) && (arg <= (float64)1.0)), ERROR_EDOM);
    VM_PushF(asin(arg));
}


void MF_Acos(void)
{
    float64 arg;

    arg = VM_PopF();
    CC_ASSERT(((arg >= (float64) - 1.0) && (arg <= (float64)1.0)), ERROR_EDOM);
    VM_PushF(acos(arg));
}


void MF_Atan(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(atan(arg));
}


void MF_Log(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(log10(arg));

}


void MF_Ln(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(log(arg));
}


void MF_Exp(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(exp(arg));

}


void MF_Pow(void)
{
    float64 arg1, arg2;

    arg1   = VM_PopF();
    arg2   = VM_PopF();
    VM_PushF(pow(arg1, (float64)arg2));
}


void MF_Ceil(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(ceil(arg));
}


void MF_Floor(void)
{
    float64 arg;

    arg = VM_PopF();
    VM_PushF(floor(arg));
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_?_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
