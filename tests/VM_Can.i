
%module vm_can

%include "Types.i"



%{
#include "VM.h"

void Can_Init(void), Can_Ready(void), Can_Error(void);
void Can_Send(void), Can_Publish(void), Can_RtrCount(void);
void Can_Expect(void), Can_Request(void), Can_Rxd(void);
void Can_Get(void), Can_SetParameter(void);
void Can_GetID(void), Can_RequestX(void);

%}

void Can_Init(void), Can_Ready(void), Can_Error(void);
void Can_Send(void), Can_Publish(void), Can_RtrCount(void);
void Can_Expect(void), Can_Request(void), Can_Rxd(void);
void Can_Get(void), Can_SetParameter(void);
void Can_GetID(void), Can_RequestX(void);


