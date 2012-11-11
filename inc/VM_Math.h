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
#if !defined(__VM_MATH_H)
#define __VM_MATH_H

#include "VM.h"
#include "VM_Excp.h"
#include <math.h>

void    VM_InvertInt(void), VM_InvertLong(void), VM_InvertFloat(void);
void    VM_NegInt(void), VM_NegLong(void), VM_NegFloat(void);
void    VM_AbsInt(void), VM_AbsLong(void), VM_AbsFloat(void);

void VM_Min(void), VM_Max(void);

void VM_MathFunction(void);


#endif /* __VM_MATH_H */

