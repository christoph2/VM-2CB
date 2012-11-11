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
#if !defined(__VM_LS_H)
#define __VM_LS_H

#include "VM.h"

void VM_LoadByteImmidiate(void), VM_LoadImmidiateInt(void);

void    VM_LoadLocalByte(void), VM_LoadLocalInt(void), VM_LoadLocalLong(void), VM_LoadLocalFloat(void);
void    VM_StoreLocalByte(void), VM_StoreLocalInt(void), VM_StoreLocalLong(void), VM_StoreLocalFloat(void);

void    VM_StoreKeepByte(void), VM_StoreKeepInt(void), VM_StoreKeepLong(void), VM_StoreKeepFloat(void);
void    VM_StoreKeepLocalByte(void), VM_StoreKeepLocalInt(void), VM_StoreKeepLocalLong(void), VM_StoreKeepLocalFloat(void);

void    VM_LoadByte(void), VM_LoadInt(void), VM_LoadLong(void), VM_LoadFloat(void);
void    VM_StoreByte(void), VM_StoreInt(void), VM_StoreLong(void), VM_StoreFloat(void);

void    VM_LoadRefByte(void), VM_LoadRefInt(void), VM_LoadRefLong(void), VM_LoadRefFloat(void);
void    VM_StoreRefByte(void), VM_StoreRefInt(void), VM_StoreRefLong(void), VM_StoreRefFloat(void);

void    VM_IncLoadByte(void), VM_IncLoadInt(void), VM_IncLoadLong(void), VM_IncLoadFloat(void);
void    VM_IncLoadRefByte(void), VM_IncLoadRefInt(void), VM_IncLoadRefLong(void), VM_IncLoadRefFloat(void);
void    VM_IncLoadLocalByte(void), VM_IncLoadLocalInt(void), VM_IncLoadLocalLong(void), VM_IncLoadLocalFloat(void);

void VM_LoadSysvarInt(void), VM_LoadSysvarLong(void), VM_StoreSysvarInt(void), VM_StoreSysvarLong(void);

void    VM_LoadConstByte(void), VM_LoadConstInt(void), VM_LoadConstLong(void), VM_LoadConstFloat(void);
void    VM_LoadRefConstByte(void), VM_LoadRefConstInt(void), VM_LoadRefConstLong(void), VM_LoadRefConstFloat(void);

void    VM_StoreAbsoluteByte(void), VM_StoreAbsoluteInt(void), VM_StoreAbsoluteLong(void), VM_StoreAbsoluteFloat(void);
void    VM_LoadAbsoluteByte(void), VM_LoadAbsoluteInt(void), VM_LoadAbsoluteLong(void), VM_LoadAbsoluteFloat(void);

void    VM_PutInt(void), VM_PutLong(void), VM_PutFloat(void);
void    VM_GetInt(void), VM_GetLong(void), VM_GetFloat(void);


#endif  /* __VM_LS_H */

