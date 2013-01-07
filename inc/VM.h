/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
 *                                       cpu12.gems@googlemail.com>
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
#if !defined(__VM_H)
#define __VM_H

#include "Types.h"
#include "Hal.h"
#include "VM_Cfg.h"
#include "VM_Codes.h"
#include "VM_Cntr.h"
#include "VM_Excp.h"
#include "VM_SysMsg.h"
#include "VM_Tmr.h"

#if defined(__cplusplus)
extern "C"
{
#endif  /* __cplusplus */


#define FLOAT_SIZE  ((uint16)sizeof(float64))
STATIC_ASSERT(FLOAT_SIZE == (uint16)8, "Floating-Point-Type must be 8 Bytes!!!");

extern uint8 * VM_UserCode, * VM_UserConstants;

#define CC_TRUE     ((uint16)0xffffU)
#define CC_FALSE    ((uint16)0x0000U)

typedef enum tagThr_StateType {
    STATE_NOT_SLEEPING,
    STATE_SLEEPING
} Thr_StateType;

#define VM_SEMA_FREE ((uint16)0x0000U)

typedef struct tagVM_TCBType {
    uint16          T_PC;           /*!< Program-Counter */
    uint16          T_BP;           /*!< Base-Pointer */
    uint16          T_SP;           /*!< Stack-Pointer */
    uint16          T_SEMA;         /*!< Semaphore */
    uint32          T_SLEEP_TIME;   /*!< Sleep-Time */
    uint32          T_WAKEUP_TIME;  /*!< Wakeuptime */
    uint8           T_PRIO_CURR;    /*!< aktuelle Priorität */
    uint8           T_PRIO_SAVE;    /*!< vorherige Priorität */
    Thr_StateType   T_STATE;        /*!< Status */
} VM_TCBType;

#define TCB_SIZE (sizeof(VM_TCBType))

/* todo: Bei diesen Funktionen muss eine Byte-Order-Korrektur vorgenommen werden!!! */
#define BPTR_CONST(addr)    (uint8 *)VM_GetConstantPtr((addr))
#define WPTR_CONST(addr)    (uint16 *)VM_GetConstantPtr((addr))
#define LPTR_CONST(addr)    (uint32 *)VM_GetConstantPtr((addr))
#define FPTR_CONST(addr)    (float64 *)VM_GetConstantPtr((addr))

typedef void (*VM_FunctionType)(void);

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

#if defined(_MSC_VER)
/* Functions needed for testing. */
void setRAMPointer(unsigned char * ptr);
void setCodePointer(unsigned short * ptr);
void setConstPointer(unsigned char * ptr);
#endif /* _MSC_VER */


/*
**  Stack-Operations.
*/
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

int dummy(void);

#if defined(__cplusplus)
}
#endif  /* __cplusplus */

#endif  /* __VM_H */

