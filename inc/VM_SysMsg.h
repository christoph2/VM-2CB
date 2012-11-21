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
#if !defined(__VM_SYSMSG_H)
#define __VM_SYSMSG_H

#include "VM.h"

#if defined(__cplusplus)
extern "C"
{
#endif  /* __cplusplus */

extern const uint8  VM_C_VERSION[];
extern const uint8  VM_C_CCONTROL[];
extern const uint8  VM_C_DATE[];

extern const uint8  VM_C_RUNNING[];
extern const uint8  VM_C_HOSTMODE[];
extern const uint8  VM_C_LOAD_HEX[];
extern const uint8  VM_C_LOAD_VMC[];
extern const uint8  VM_C_ERAS_HEX[];
extern const uint8  VM_C_ERASE_VMC[];
extern const uint8  VM_C_BURN_ERR[];
extern const uint8  VM_C_QUIT[];

extern const uint8  VM_C_UND_OPC[];
extern const uint8  VM_C_STO_TRAP[];
extern const uint8  VM_C_STU_TRAP[];
extern const uint8  VM_C_ILL_OPA[];
extern const uint8  VM_C_BTRAP[];
extern const uint8  VM_C_FP_ERR[];
extern const uint8  VM_C_FPE_DIV0[];
extern const uint8  VM_C_FPE_STOF[];
extern const uint8  VM_C_FPE_INOF[];
extern const uint8  VM_C_ILL_INA[];
extern const uint8  VM_C_FPE_CONV[];
extern const uint8  VM_C_FPE_UNDF[];
extern const uint8  VM_C_PRT_FLT[];
extern const uint8  VM_C_FPE_STUF[];
extern const uint8  VM_C_FPE_FLUF[];
extern const uint8  VM_C_ILL_BUS[];
extern const uint8  VM_C_FPE_FLOF[];

#if defined(__cplusplus)
}
#endif  /* __cplusplus */

#endif /* __VM_SYSMSG_H */

