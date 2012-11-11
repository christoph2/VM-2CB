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

#include "VM_SysMsg.h"

const uint8 VM_C_VERSION[]     = "2-CB/12  V1.0\r\n";
const uint8 VM_C_CCONTROL[]    = "C-Control II\r\n";
const uint8 VM_C_DATE[]        = __DATE__ "\r\n";

const uint8 VM_C_RUNNING[]     = "RUNNING";
const uint8 VM_C_HOSTMODE[]    = "HOSTMODE";
const uint8 VM_C_LOAD_HEX[]    = "LOAD HEX";
const uint8 VM_C_LOAD_VMC[]    = "LOAD VMC";
const uint8 VM_C_ERAS_HEX[]    = "ERAS HEX";
const uint8 VM_C_ERASE_VMC[]   = "ERAS VMC";
const uint8 VM_C_BURN_ERR[]    = "BURN ERR";
const uint8 VM_C_QUIT[]        = "QUIT VMC";

const uint8 VM_C_UND_OPC[]     = "UND OPC";
const uint8 VM_C_STO_TRAP[]    = "STO TRAP";
const uint8 VM_C_STU_TRAP[]    = "STU TRAP";
const uint8 VM_C_ILL_OPA[]     = "ILL OPA";
const uint8 VM_C_BTRAP[]       = "BTRAP";
const uint8 VM_C_FP_ERR[]      = "FP ERR";
const uint8 VM_C_FPE_DIV0[]    = "FPE DIV0";
const uint8 VM_C_FPE_STOF[]    = "FPE STOF";
const uint8 VM_C_FPE_INOF[]    = "FPE INOF";
const uint8 VM_C_ILL_INA[]     = "ILL INA";
const uint8 VM_C_FPE_CONV[]    = "FPE CONV";
const uint8 VM_C_FPE_UNDF[]    = "FPE UNDF";
const uint8 VM_C_PRT_FLT[]     = "PRT FLT";
const uint8 VM_C_FPE_STUF[]    = "FPE STUF";
const uint8 VM_C_FPE_FLUF[]    = "FPE FLUF";
const uint8 VM_C_ILL_BUS[]     = "ILL BUS";
const uint8 VM_C_FPE_FLOF[]    = "FPE FLOF";
