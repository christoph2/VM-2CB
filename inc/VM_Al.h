/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *  (C) 2007-2012 by Christoph Schueler <chris@konnex-tools.de,
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
#if !defined(__VM_AL_H)
#define __VM_AL_H

#include "VM.h"
#include "VM_Excp.h"
#include <math.h>

void    VM_Add(void), VM_Sub(void), VM_Mul(void), VM_Div(void), VM_Mod(void);
void    VM_And(void), VM_Nand(void), VM_Or(void), VM_Nor(void), VM_Xor(void), VM_Nxor(void);
void    VM_Equ(void), VM_Neq(void), VM_Hi(void), VM_His(void), VM_Lo(void), VM_Los(void);
void    VM_Shl(void), VM_Shr(void), VM_Asr(void), VM_Rol(void), VM_Ror(void);

void    VM_CastLongToInt(void), VM_CastIntToLong(void);
void    VM_CastFloatToInt(void), VM_CastFloatToLong(void);
void    VM_CastIntToFloat(void), VM_CastLongToFloat(void);


#endif  /* __VM_AL_H */

