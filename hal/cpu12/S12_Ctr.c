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

#include "S12_Ctr.h"

ISR1(PAOVIHandler)
{
    S12ECT_REG8(PAFLG) = PAOVF;
/*    Frequency1+=ACC_MAX; */
    Frequency1++;
}

ISR1(PBOVIHandler)
{
    S12ECT_REG8(PBFLG) = PBOVF;
    Frequency1        += ACC_MAX;
    /* PACN1 */
}

ISR1(PORTHHandler)
{
    if ((S12PIM_REG8(PIFH) & PIFH0) == PIFH0) {
        S12PIM_REG8(PIFH) &= ~PIFH0;
        VM_SysVarCnt1++;
        /* todo: Hook aufrufen falls installiert. */
    }

    if ((S12PIM_REG8(PIFH) & PIFH1) == PIFH1) {
        S12PIM_REG8(PIFH) &= ~PIFH1;
        VM_SysVarCnt2++;
        /* todo: Hook aufrufen falls installiert. */
    }

    if ((S12PIM_REG8(PIFH) & PIFH2) == PIFH2) {
        S12PIM_REG8(PIFH) &= ~PIFH2;
        VM_SysVarCnt3++;
        /* todo: Hook aufrufen falls installiert. */
    }

    if ((S12PIM_REG8(PIFH) & PIFH3) == PIFH3) {
        S12PIM_REG8(PIFH) &= ~PIFH3;
        VM_SysVarCnt4++;
        /* todo: Hook aufrufen falls installiert. */
    }
}

