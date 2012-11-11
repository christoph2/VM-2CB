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

#include "VM_Plm.h"

/*
** Oktave von A (220Hz) bis GIS1 (415,4Hz) auf der Zeitbasis 2 (800ns).
*/
static const uint16 __tone_tab[12] = {
    /* 56818,53625,50628,47783,45922,42560,40167,37913,35796,33784,31888,30091 */
    0xDDF2, 0xD179, 0xC5C4, 0xBAA7, 0xB362, 0xA640, 0x9CE7, 0x9419, 0x8BD4, 0x83F8, 0x7C90, 0x758B
};

/*
**  Module-Function-Prototypes.
*/
static void Plm_Init(void), Plm_SetTB(void), Plm_SetPM(void), Plm_SetPL(void), Plm_Out(void), Plm_Beep(void);


/*
**  Sprungtabelle.
*/
static const VoidFunctionType FuncTab[PLM_CODE_MAX + 1] = {
    Plm_Init, Plm_SetTB, Plm_SetPM, Plm_SetPL, Plm_Out, Plm_Beep
};

static void Plm_ToneOut(uint16 tone);

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_PLM_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

void VM_Plm(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(FuncTab), ERROR_ILLOPA);
    FuncTab[VM_OperandB]();
}


static void Plm_Init(void)
{

}


static void Plm_SetTB(void)
{

}


static void Plm_SetPM(void)
{

}


static void Plm_SetPL(void)
{

}


static void Plm_Out(void)
{

}


static void Plm_Beep(void)
{

}


static void Plm_ToneOut(uint16 tone)
{

}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_?_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
