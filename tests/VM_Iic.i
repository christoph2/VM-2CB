
%module vm_iic

%include "Types.i"

%{
#include "VM.h"

void I2c_Init(void), I2c_Start(void), I2c_Stop(void), I2c_Write(void);
void I2c_Read(void), I2c_ReadLast(void), I2c_Ready(void);

%}

void I2c_Init(void), I2c_Start(void), I2c_Stop(void), I2c_Write(void);
void I2c_Read(void), I2c_ReadLast(void), I2c_Ready(void);

