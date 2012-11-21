
%module vm_twb

%include "Types.i"

%{
#include "VM.h"

void Twb_Init(void), Twb_Rxd(void), Twb_Io(void);

%}

void Twb_Init(void), Twb_Rxd(void), Twb_Io(void);

