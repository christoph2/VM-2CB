
%module vm_core

%include "Types.i"

%{
#include "VM.h"

extern uint16   VM_SysVarYear, VM_SysVarMonth, VM_SysVarDay, VM_SysVarHour, VM_SysVarDow;
extern uint16   VM_SysVarMinute, VM_SysVarSecond, VM_SysVarDst, VM_SysVarZone, VM_SysVarDcfErrCnt;
extern uint32   VM_SysVarTimerMS, VM_SysVarCnt1, VM_SysVarCnt2, VM_SysVarCnt3;
extern uint32   VM_SysVarCnt4, VM_SysVarFreq1, VM_SysVarFreq2;

extern uint8    VM_OperandB;
extern uint16   VM_OperandW;

extern uint8 * VM_UserRAM;

extern uint16                   VM_MemoryUsage;
extern VM_TCBType *             VM_CurrentThread;
extern const VM_FunctionType    VM_CodeTab[];

void    VM_Schedule(void);
void    VM_SchedInit(void);
void    VM_SysInit(void);
void    VM_InitThreads(void);
boolean VM_BlankCheck(void);

void *      VM_GetConstantPtr(uint16 addr);
uint16 *    VM_GetCodePtr(uint16 addr);

void    VM_PushW(sint16 w);
sint16  VM_PopW(void);
void    VM_PushL(sint32 l);
sint32  VM_PopL(void);
void    VM_PushF(float64 f);
float64 VM_PopF(void);

void    VM_IncSP(void);
void    VM_Nop(void);
void    VM_Yield(void);
void    VM_Quit(void);
void    VM_Sleep(void);
void    VM_Capture(void);
void    VM_Release(void);
void    VM_Call(void);
void    VM_FastReturn(void);
void    VM_Return(void);
void    VM_ReturnValue(void);
void    VM_MakeGlobalPointer(void);
void    VM_UndefinedOpcode(void);
void    VM_Branch(void);
void    VM_BranchIfZero(void);
void    VM_Syscall(void);
void    VM_Sysjump(void);
void    VM_InlineSyscall(void);
void    VM_InlineSysjump(void);
void    VM_Run(void);
void    VM_Resume(void);
void    VM_Save(void);
void    VM_Restore(void);
void    VM_Hook(void);
void    VM_Reset(void);
void    VM_Debug(void);

%}

extern uint16   VM_SysVarYear, VM_SysVarMonth, VM_SysVarDay, VM_SysVarHour, VM_SysVarDow;
extern uint16   VM_SysVarMinute, VM_SysVarSecond, VM_SysVarDst, VM_SysVarZone, VM_SysVarDcfErrCnt;
extern uint32   VM_SysVarTimerMS, VM_SysVarCnt1, VM_SysVarCnt2, VM_SysVarCnt3;
extern uint32   VM_SysVarCnt4, VM_SysVarFreq1, VM_SysVarFreq2;

extern uint8    VM_OperandB;
extern uint16   VM_OperandW;

extern uint8 * VM_UserRAM;

extern uint16                   VM_MemoryUsage;
extern VM_TCBType *             VM_CurrentThread;
extern const VM_FunctionType    VM_CodeTab[];

void    VM_Schedule(void);
void    VM_SchedInit(void);
void    VM_SysInit(void);
void    VM_InitThreads(void);
boolean VM_BlankCheck(void);

void *      VM_GetConstantPtr(uint16 addr);
uint16 *    VM_GetCodePtr(uint16 addr);

void    VM_PushW(sint16 w);
sint16  VM_PopW(void);
void    VM_PushL(sint32 l);
sint32  VM_PopL(void);
void    VM_PushF(float64 f);
float64 VM_PopF(void);

void    VM_IncSP(void);
void    VM_Nop(void);
void    VM_Yield(void);
void    VM_Quit(void);
void    VM_Sleep(void);
void    VM_Capture(void);
void    VM_Release(void);
void    VM_Call(void);
void    VM_FastReturn(void);
void    VM_Return(void);
void    VM_ReturnValue(void);
void    VM_MakeGlobalPointer(void);
void    VM_UndefinedOpcode(void);
void    VM_Branch(void);
void    VM_BranchIfZero(void);
void    VM_Syscall(void);
void    VM_Sysjump(void);
void    VM_InlineSyscall(void);
void    VM_InlineSysjump(void);
void    VM_Run(void);
void    VM_Resume(void);
void    VM_Save(void);
void    VM_Restore(void);
void    VM_Hook(void);
void    VM_Reset(void);
void    VM_Debug(void);


