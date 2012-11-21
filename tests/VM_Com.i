
%module vm_com

%include "Types.i"

%{
#include "VM.h"

void Hwcom_Init(void), Hwcom_SetSpeed(void), Hwcom_SetBuffer(void);
void Hwcom_Flush(void), Hwcom_Ready(void), Hwcom_Put(void);
void Hwcom_Send(void), Hwcom_Rxd(void), Hwcom_Get(void);
void Hwcom_SetFormat(void), Hwcom_SendBreak(void);

void Swcom_Init(void), Swcom_SetSpeed(void), Swcom_SetBuffer(void);
void Swcom_Flush(void), Swcom_Ready(void), Swcom_Put(void);
void Swcom_Send(void), Swcom_Rxd(void), Swcom_Get(void);
void Swcom_SetFormat(void), Swcom_SendBreak(void);

%}

void Hwcom_Init(void), Hwcom_SetSpeed(void), Hwcom_SetBuffer(void);
void Hwcom_Flush(void), Hwcom_Ready(void), Hwcom_Put(void);
void Hwcom_Send(void), Hwcom_Rxd(void), Hwcom_Get(void);
void Hwcom_SetFormat(void), Hwcom_SendBreak(void);

void Swcom_Init(void), Swcom_SetSpeed(void), Swcom_SetBuffer(void);
void Swcom_Flush(void), Swcom_Ready(void), Swcom_Put(void);
void Swcom_Send(void), Swcom_Rxd(void), Swcom_Get(void);
void Swcom_SetFormat(void), Swcom_SendBreak(void);

