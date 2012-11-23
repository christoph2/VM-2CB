/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 * (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
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

#include "VM_Iic.h"

STATIC void I2c_Init(void), I2c_Start(void), I2c_Stop(void), I2c_Write(void);
STATIC void I2c_Read(void), I2c_ReadLast(void), I2c_Ready(void);


STATIC const VoidFunctionType I2cTab[] = {
    I2c_Init, I2c_Start,    I2c_Stop, I2c_Write,
    I2c_Read, I2c_ReadLast, I2c_Ready
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_IIC_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */


void VM_Iic(void)
{
    CC_ASSERT(VM_OperandB < SIZEOF_ARRAY(I2cTab), ERROR_ILLOPA);
    I2cTab[VM_OperandB]();
}


void I2c_Init(void)
{
    HAL_I2C_INIT();
}


void I2c_Start(void)
{
    uint8   device = LOBYTE(VM_PopW());
    boolean res;

    HAL_I2C_START();
    res = HAL_I2C_WRITE(device);

    VM_PushW((res == TRUE) ? CC_TRUE : CC_FALSE);

}


void I2c_Stop(void)
{
    HAL_I2C_STOP();
}


void I2c_Write(void)
{
    uint8   b = LOBYTE(VM_PopW());
    boolean res;

    res = HAL_I2C_WRITE(b);

    VM_PushW((res == TRUE) ? CC_TRUE : CC_FALSE);
}


void I2c_Read(void)
{
    uint8 b;

    b = HAL_I2C_READ(TRUE);

    VM_PushW((uint16)b);
}


void I2c_ReadLast(void)
{
    uint8 b;

    b = HAL_I2C_READ(FALSE);

    VM_PushW((uint16)b);
}


void I2c_Ready(void)
{
    VM_PushW(HAL_I2C_READY());
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_IIC_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
