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
#if !defined(__PORT_H)
#define __PORT_H

#include "VM.h"

#if defined(__cplusplus)
extern "C"
{
#endif  /* __cplusplus */

#if 0
void InitPorts(void), InitADC(uint8 num);
#endif

void VM_InitPorts(void);

void    VM_GetSinglePort(void), VM_GetNibblePort(void), VM_GetBytePort(void), VM_GetWordPort(void);
void    VM_SetSinglePort(void), VM_SetNibblePort(void), VM_SetBytePort(void), VM_SetWordPort(void);
void    VM_DeactSinglePort(void), VM_DeactNibblePort(void), VM_DeactBytePort(void), VM_DeactWordPort(void);
void    VM_ToggleSinglePort(void);
void    VM_PulseSinglePort(void), VM_GetCount(void), VM_GetFreq(void);
void    VM_GetAdcPort(void);

#if defined(__cplusplus)
}
#endif  /* __cplusplus */

#endif  /* __PORT_H */

