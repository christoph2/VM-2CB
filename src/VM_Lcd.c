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

#include "VM_Lcd.h"

STATIC void Lcd_init(void), Lcd_show_cursor(void), Lcd_clear(void);
STATIC void Lcd_clreol(void), Lcd_goto(void), Lcd_home(void);
STATIC void Lcd_scroll(void), Lcd_ready(void), Lcd_put(void), Lcd_print(void);


STATIC const VoidFunctionType LcdTab[] = {
    Lcd_init, Lcd_show_cursor, Lcd_clear, Lcd_clreol, Lcd_goto,
    Lcd_home, Lcd_scroll,      Lcd_ready, Lcd_put,    Lcd_print
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_LCD_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

STATIC int dummy(void)
{
    return 1;
}

void VM_Lcd(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(LcdTab), ERROR_ILLOPA);
    LcdTab[VM_OperandB]();
}


void Lcd_init(void)
{
    HAL_LCD_INIT();
}


void Lcd_show_cursor(void)
{
    uint8 yesno = (uint8)VM_PopW();

    HAL_LCD_SHOWCURSOR(yesno);
}


void Lcd_clear(void)
{
    HAL_LCD_CLEAR();
}


void Lcd_clreol(void)
{
    HAL_LCD_CLREOL();
}


void Lcd_goto(void)
{
    uint8   pos  = (uint8)VM_PopW();
    uint8   line = (uint8)VM_PopW();

    HAL_LCD_GOTO(pos, line);
}


void Lcd_home(void)
{
    HAL_LCD_HOME();
}


void Lcd_scroll(void)
{
    uint8 pos = (uint8)VM_PopW();

    HAL_LCD_SCROLL(pos);
}


void Lcd_ready(void)
{
    VM_PushW(HAL_LCD_READY());
}


void Lcd_put(void)
{
    uint8 ch = (uint8)VM_PopW();

    HAL_LCD_PUT(ch);
}


void Lcd_print(void)
{
    uint8   length = (uint8)VM_PopW();              /* length */
    uint8 * buf    = BPTR(VM_UserRAM, VM_PopW());   /* buf[] */

    HAL_LCD_PRINT(buf, length);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_LCD_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
