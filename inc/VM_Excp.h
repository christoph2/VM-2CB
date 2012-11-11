/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
 *                                       cpu12.gems@googlemail.com>
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
#if !defined(__VM_EXCP_H)
#define __VM_EXCP_H

#include "VM.h"

#define STATUS_RUNNING      ((uint8)0x08)
#define STATUS_HOSTMODE     ((uint8)0x09)
#define STATUS_BOOTMODUS    ((uint8)0x0a)

#define ERROR_UNDOPC        ((uint8)0x01)
#define ERROR_ILLOPA        ((uint8)0x02)
#define ERROR_FPE           ((uint8)0x03)
#define ERROR_DIV0          ((uint8)0x04)
#define ERROR_BURN          ((uint8)0x05)
#define ERROR_MEMCORRPT     ((uint8)0x06)   /* (Flash-)Memory corrupted. */
#define ERROR_OOM           ((uint8)0x07)   /* out of memory. */
#define ERROR_NULLPTR       ((uint8)0x08)   /* NULL-pointer. */

#define ERROR_EDOM          ((uint8)0x08)   /* Domain-Error, e.g. '5 % 0' .*/

#define CC_ASSERT(expr, code) \
    _BEGIN_BLOCK              \
    if (!(expr)) {            \
        Exception((code));    \
    }                         \
    _END_BLOCK

void    Exception(uint8 code);
void    ShowStatus(uint8 code);


#endif  /* __VM_EXCP_H */

