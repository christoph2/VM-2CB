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
#if !defined(__VM_CNTR_H)
#define __VM_CNTR_H

#include "VM.h"
#include "Hal.h"

#if defined(__cplusplus)
extern "C"
{
#endif  /* __cplusplus */

void    Cntr_Init(void);
void    Cntr_Reset(void);
uint32  Cntr_GetFrequency1(void);
uint32  Cntr_GetFrequency2(void);

#if defined(__cplusplus)
}
#endif  /* __cplusplus */


#endif /* __VM_CNTR_H */
