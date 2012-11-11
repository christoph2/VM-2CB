/*
 *  Grundfos GENIBus Library.
 *
 *  (C) 2007-2012 by Christoph Schueler <cpu12.gems@googlemail.com>
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
 *
 */


#if !defined(__TYPES_H)
#define __TYPES_H

#if defined(__cplusplus)
extern "C"
{
#endif  /* __cplusplus */


/* check for C99-Compiler */
#if defined(__STDC_VERSION__)
    #if __STDC_VERSION__ >= 199901L
        #define C99_COMPILER
    #endif
#endif

/* check for C++-Compiler */
#if defined(__cplusplus)
    #define CPP_COMPILER
#endif

#if (defined(__IAR_SYSTEMS_ICC__) && defined(_DLIB_ADD_C99_SYMBOLS)) || (defined(_C99_COMPILER)) || (defined(_CPP_COMPILER))
#include <stdint.h>
#include <stdbool.h>

typedef unsigned char boolean;

typedef /*@signed-integral-type@*/ int8_t       sint8;
typedef /*@unsigned-integral-type@*/ uint8_t    uint8;
typedef /*@signed-integral-type@*/ int16_t      sint16;
typedef /*@unsigned-integral-type@*/ uint16_t   uint16;
typedef /*@signed-integral-type@*/ int32_t      sint32;
typedef /*@unsigned-integral-type@*/ uint32_t   uint32;

typedef /*@signed-integral-type@*/ int_least8_t     sint8_least;
typedef /*@unsigned-integral-type@*/ uint_least8_t  uint8_least;
typedef /*@signed-integral-type@*/ int_least16_t    sint16_least;
typedef /*@unsigned-integral-type@*/ uint_least16_t uint16_least;
typedef /*@signed-integral-type@*/ int_least32_t    sint32_least;
typedef /*@unsigned-integral-type@*/ uint_least32_t uint32_least;

#if !defined(TRUE)
    #define TRUE    ((boolean)true)
#endif

#if !defined(FALSE)
    #define FALSE   ((boolean)false)
#endif

#else
/* Types  */
typedef unsigned char   boolean;
typedef signed char     sint8;
typedef unsigned char   uint8;
typedef signed short    sint16;
typedef unsigned short  uint16;
typedef signed long     sint32;
typedef unsigned long   uint32;

typedef signed char     sint8_least;
typedef unsigned char   uint8_least;
typedef signed short    sint16_least;
typedef unsigned short  uint16_least;
typedef signed long     sint32_least;
typedef unsigned long   uint32_least;

#if !defined(TRUE)
    #define TRUE    ((boolean)1)
#endif

#if !defined(FALSE)
    #define FALSE   ((boolean)0)
#endif

#endif

#if !defined(NULL)
#define NULL        0
#endif

typedef float           float32;
typedef double          float64;
typedef void *          pvoid;
typedef unsigned int    SizeType;
typedef int             PtrDiffType;

/* Static  (compile time) Assertion. */
#if defined(_C1x_COMPILER)
#define STATIC_ASSERT(cond, msg) _Static_assert((cond), (msg))
#else
#define STATIC_ASSERT(cond, msg)                       \
    struct  GLUE2 (__NEVER_USED_BY_ISO_C_, __LINE__) { \
        uint8 x[(cond) ? 1 : -1];                      \
    }
#endif

#define RETURN_VALUE_IF_FALSE(expr, value) \
    _BEGIN_BLOCK                           \
    if (!(expr)) {                         \
        return (value);                    \
    }                                      \
    _END_BLOCK                             

typedef void (*VoidFunctionType)(void);

#define FOREVER         while(TRUE)

#define NOT_ADDRESSABLE register

#define WAIT_FOR(cond) \
    while (!(cond))    \
        _BEGIN_BLOCK   \
        _END_BLOCK

#define _BEGIN_BLOCK    do {
#define _END_BLOCK      } while (0)

typedef void (*VoidFunctionType)(void);

#define TO_STRING_2(s)          # s
#define TO_STRING(s)            TO_STRING_2(s)

#define GLUE2_2(a, b)           a ## b
#define GLUE2(a, b)             GLUE2_2(a, b)

#define GLUE3_2(a, b, c)        a ## b ## c
#define GLUE3(a, b, c)          GLUE3_2(a, b, c)

#define BREF(b, o)              (*(((uint8 *)(b) + (o))))
#define BPTR(b, o)              ((((uint8 *)(b) + (o))))

#define WREF(w, o)              (*((uint16 *)((uint8 *)(w) + (o))))
#define WPTR(w, o)              (((uint16 *)((uint8 *)(w) + (o))))

#define LREF(l, o)              (*((uint32 *)((uint8 *)(l) + (o))))
#define LPTR(l, o)              (((uint32 *)((uint8 *)(l) + (o))))

#define FREF(f, o)              (*((float64 *)((uint8 *)(f) + (o))))
#define FPTR(f, o)              (((float64 *)((uint8 *)(f) + (o))))

#define BYTE_REG(base, offs)    *(volatile uint8 *)BPTR((base), (offs))
#define WORD_REG(base, offs)    *(volatile uint16 *)WPTR((base), (offs))

#define BIT(n, type)            ((type)(1 << (n)))

#define BIT0    ((uint16)0x01)
#define BIT1    ((uint16)0x02)
#define BIT2    ((uint16)0x04)
#define BIT3    ((uint16)0x08)
#define BIT4    ((uint16)0x10)
#define BIT5    ((uint16)0x20)
#define BIT6    ((uint16)0x40)
#define BIT7    ((uint16)0x80)
#define BIT8    ((uint16)0x0100)
#define BIT9    ((uint16)0x0200)
#define BIT10   ((uint16)0x0400)
#define BIT11   ((uint16)0x0800)
#define BIT12   ((uint16)0x1000)
#define BIT13   ((uint16)0x2000)
#define BIT14   ((uint16)0x4000)
#define BIT15   ((uint16)0x8000)

#define TENARY_COMPARE(id1, id2, mask)  (~((id1) ^ (id2)) | (~(mask)))

#if defined(_C99_COMPILER)
    #define INLINE      inline
    #define RESTRICT    restrict
#elif defined(_CPP_COMPILER)
    #define INLINE      inline
    #define RESTRICT
#else
#if !defined(INLINE)
    #define INLINE
#endif
    #define RESTRICT
#endif

#if !defined(PROGRAM_STARTUP)
#define PROGRAM_STARTUP int main        /* ISO-C only requires 'int main()'-signatures for hosted environments !!! */
#endif /* PROGRAM_STARTUP */

#define VOID_EXPRESSION()           ((void)0)

#if !defined(UNREFERENCED_PARAMETER)
#define UNREFERENCED_PARAMETER(p)   ((p) = (p))
#endif

#define MIN(a, b)                   (((a) > (b)) ? (b) : (a))
#define MAX(a, b)                   (((a) > (b)) ? (a) : (b))

#define BETWEEN(x, min, max)        (((x) >= (min)) && ((x) <= (max)))

#define ABS(i)                      (((i) < 0) ? ((i) * -1) : ((i)))

#define SWAP_INPLACE(a, b)  \
    _BEGIN_BLOCK            \
        (a)    = (a) ^ (b); \
    (b)        = (a) ^ (b); \
    (a)        = (a) ^ (b); \
    _END_BLOCK

#if !defined(LOBYTE)
#define LOBYTE(w)                   ((uint8)((uint16)((uint16)(w) & 0x00ffU)))
#endif

#if !defined(HIBYTE)
#define HIBYTE(w)                   ((uint8)((uint16)(((uint16)(w ) >> 8) & 0x00ffU)))
#endif

#if !defined(LOWORD)
#define LOWORD(dw)                  ((uint16)((uint32)((uint32)(dw) & 0xffffU)))
#endif

#if !defined(HIWORD)
#define HIWORD(dw)                  ((uint16)((uint32)(((uint32)(dw) >> 16) & 0xffffU)))
#endif

#define MAKEWORD(h, l)              ((((uint16)((h) & ((uint8)0xff))) <<  (uint16)8) | ((uint16)((l) & ((uint8)0xff))))
#define MAKEDWORD(h, l)             ((((uint32)((h) & ((uint16)0xffffu))) << (uint32)16) | ((uint32)((l) & ((uint16)0xffffu))))

#define INVERT_NIBBLE(b)            ((uint8)(((uint8) ~(b)) & ((uint8)0x0f)))

#define SIZEOF_ARRAY(arr)           (sizeof((arr)) / sizeof((arr[0])))
#define BEYOND_ARRAY(arr)           ((arr) + SIZE_OF_ARRAY((arr)))

#if !defined(_countof)
#define _countof(arr)		    SIZEOF_ARRAY(arr)
#endif


#if defined(__cplusplus)
}
#endif  /* __cplusplus */

#endif /* __TYPES_H */
