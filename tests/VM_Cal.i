
%module vm_cal

%include "Types.i"


%{
#include "VM.h"

boolean Cal_IsLeapYear(uint16 year);

%}

boolean Cal_IsLeapYear(uint16 year);

