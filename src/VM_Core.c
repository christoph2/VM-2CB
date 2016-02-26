/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2014 by Christoph Schueler <github.com/Christoph2,
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
#include "VM.h"
#include "Utl.h"

/*
**  Defines.
*/
#define THREAD_INIT_SIZE    ((uint8)8)
#define VMC_TYPE_MASK       ((uint8)0x80)

#define VM_CAN_BUFFER_SIZE  ((uint8)12)
#define VM_NUM_CAN_BUFFERS  ((uint8)15)

#define TESTING             0x1000

/*
**  Function-Like-Macros.
*/
#define BRANCH_TO(loc)      (VM_CurrentThread->T_PC = VM_CurrentThread->T_PC + (loc))
#define THREAD_PTR(i)       (VM_TCBType *)(void *)(VM_SystemRAM + ((i) * TCB_SIZE))
#define THREAD_INIT_PTR(i)  (uint8 *)(VM_UserConstants + 2 + (THREAD_INIT_SIZE * (i)))

#define FETCH(op)                                                               \
    _BEGIN_BLOCK                                                                \
        VM_ProgramCounter = VM_CurrentThread->T_PC++;                           \
        VM_SetCodePage(VM_ProgramCounter);                                      \
        op = (uint16) * ((uint16 *)(FLS_PAGE_ADDR + (VM_ProgramCounter << 1))); \
    _END_BLOCK

#define YIELD()                                     \
    _BEGIN_BLOCK                                    \
        VM_CurrentThread->T_PC    -= ((uint8)1);    \
        VM_OpsToExecute            = ((uint8)0x01); \
    _END_BLOCK

/*
**  Global Variables.
*/
uint16  VM_SysVarYear, VM_SysVarMonth, VM_SysVarDay, VM_SysVarHour, VM_SysVarDow;
uint16  VM_SysVarMinute, VM_SysVarSecond, VM_SysVarDst, VM_SysVarZone, VM_SysVarDcfErrCnt;
uint32  VM_SysVarTimerMS, VM_SysVarCnt1, VM_SysVarCnt2, VM_SysVarCnt3;
uint32  VM_SysVarCnt4, VM_SysVarFreq1, VM_SysVarFreq2;

uint8           VM_OperandB;
uint16          VM_OperandW;
uint16          VM_MemoryUsage;
VM_TCBType *    VM_CurrentThread;

/*
**  Local Variables.
*/
STATIC uint8    VM_CurrentTID;
STATIC uint8    VM_OpsToExecute;
STATIC uint8    VM_NumThreads;
STATIC uint16   VM_ProgramCounter;

STATIC uint8    VM_RAMPool[12000 - TESTING];
uint8 *         VM_UserRAM;
uint8 *         VM_UserCode, * VM_UserConstants;

STATIC const uint8 *    VM_SystemRAM       = &VM_RAMPool[0];
STATIC const uint8 *    VM_CANBufferPool   =
    &VM_RAMPool[sizeof(VM_RAMPool) - ((VM_CAN_BUFFER_SIZE * VM_NUM_CAN_BUFFERS) + (uint16)1)];

STATIC void VM_SetCodePage(uint16 pc);
STATIC void VM_InitThread(uint8 num);
STATIC void VM_RetCleanup(void);


#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CORE_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

/* FUNC(void,VM_CORE_CODE) VM_SysInit2(void){} */

void VM_SysInit(void)
{
    VM_SysVarYear      = ((uint16)0x0000U);
    VM_SysVarMonth     = ((uint16)0x0000U);
    VM_SysVarDay       = ((uint16)0x0000U);
    VM_SysVarHour      = ((uint16)0x0000U);
    VM_SysVarDow       = ((uint16)0x0000U);
    VM_SysVarMinute    = ((uint16)0x0000U);
    VM_SysVarSecond    = ((uint16)0x0000U);
    VM_SysVarDst       = ((uint16)0x0000U);
    VM_SysVarZone      = ((uint16)0x0000U);
    VM_SysVarDcfErrCnt = ((uint16)0x0000U);

    VM_SysVarTimerMS   = ((uint32)0x00000000UL);
    VM_SysVarCnt1      = ((uint32)0x00000000UL);
    VM_SysVarCnt2      = ((uint32)0x00000000UL);
    VM_SysVarCnt3      = ((uint32)0x00000000UL);
    VM_SysVarCnt4      = ((uint32)0x00000000UL);
    VM_SysVarFreq1     = ((uint32)0x00000000UL);
    VM_SysVarFreq2     = ((uint32)0x00000000UL);

    HAL_INIT_PHASE1();

    TMR_Init();
}


void VM_SchedInit(void)
{
    VM_OpsToExecute    = (uint8)0x00;
    VM_ProgramCounter  = (uint16)0x0000U;
    VM_OperandB        = (uint8)0x00;
    VM_OperandW        = (uint16)0x0000U;

    VM_MemoryUsage = (uint16)0x0000U;

    VM_InitThreads();
}


void VM_InitThreads(void)
{
    uint8 idx;

    VM_CurrentTID  = (uint8)0x00;
    VM_NumThreads  = (uint8) * BPTR_CONST((uint16)0x0000U);
    CC_ASSERT(VM_NumThreads != (uint8)0x00, ERROR_MEMCORRPT);

    VM_UserRAM = VM_RAMPool + (VM_NumThreads * TCB_SIZE);

    for (idx = (uint8)0; idx < VM_NumThreads; ++idx) {
        VM_InitThread(idx);
    }
}


void VM_InitThread(uint8 num)
{
    uint8 *         th_init_ptr;
    STATIC uint16   sp = (uint16)0x0000U; /* keep track of current SP. */
    VM_TCBType *    th_ptr;

    th_init_ptr    = (uint8 *)VM_GetConstantPtr((uint16)(((((uint16)THREAD_INIT_SIZE * num)) + (uint16)2) >> (uint16)1));
    th_ptr         = THREAD_PTR(num);

    th_ptr->T_PC           = WREF(th_init_ptr, 0);
    th_ptr->T_PC           = Utl_Swap16(&th_ptr->T_PC);
    th_ptr->T_BP           = sp;
    th_ptr->T_SP           = sp;
    th_ptr->T_PRIO_CURR    = BREF(th_init_ptr, 6);

    sp = WREF(th_init_ptr, 4);
    sp = Utl_Swap16(&sp);
}


boolean VM_BlankCheck(void)
{
    uint16 addr;

    for (addr = (uint16)0x0000U; addr < (uint16)0xffffU; ++addr) {
        if (*VM_GetCodePtr(addr) != (uint16)0xffffu) {
            return FALSE;
        }
    }

    return TRUE;
}


void VM_Schedule(void)
{
    STATIC uint16 op;

    FOREVER {
#if defined(VM_USE_WATCHDOG)
        (void)S12Crg_TriggerWDG();
#endif  /* VM_USE_WATCHDOG */
        VM_CurrentThread   = THREAD_PTR(VM_CurrentTID);
        VM_OpsToExecute    = VM_CurrentThread->T_PRIO_CURR;

        while (VM_OpsToExecute-- != (uint8)0x00) {
            FETCH(op);
            VM_OperandB = HIBYTE(op);                               /* VM_OperandB=LOBYTE(op); */

            if (((LOBYTE(op) & VMC_TYPE_MASK)) == VMC_TYPE_MASK) {  /* HIBYTE */
                FETCH(VM_OperandW);
            }

            VM_CodeTab[LOBYTE(op)]();   /* HIBYTE */
        }

        if ((++VM_CurrentTID) >= VM_NumThreads) {
            VM_CurrentTID = (uint8)0;
        }
    }
}


void VM_UndefinedOpcode(void)
{
    Exception(ERROR_UNDOPC);
}


void * VM_GetConstantPtr(uint16 addr)
{
    HAL_FLASH_SELECT_PAGE(((uint8)(addr / (FLS_PAGE_SIZE / (uint16)2))) + FLS_PPAGE_BASE_CONST);

    return (void *)((((addr % (FLS_PAGE_SIZE / (uint16)2)) << (uint16)1)) + FLS_PAGE_ADDR);
}


uint16 * VM_GetCodePtr(uint16 addr)
{
    HAL_FLASH_SELECT_PAGE(((uint8)(addr / (FLS_PAGE_SIZE / (uint16)2))) + FLS_PPAGE_BASE_CODE);

    return (uint16 *)((((addr % (FLS_PAGE_SIZE / (uint16)2)) << (uint16)1)) + FLS_PAGE_ADDR);
}


void VM_PushW(sint16 w)
{
    WREF(VM_UserRAM, VM_CurrentThread->T_SP)   = (uint16)w;
    VM_CurrentThread->T_SP                    += (uint16)2;
}


sint16 VM_PopW(void)
{
    return (sint16)WREF(VM_UserRAM, (VM_CurrentThread->T_SP -= (uint16)2));
}


void VM_PushL(sint32 l)
{
    LREF(VM_UserRAM, VM_CurrentThread->T_SP)   = (uint32)l;
    VM_CurrentThread->T_SP                    += (uint16)0x0004U;
}


sint32 VM_PopL(void)
{
    return (sint32)LREF(VM_UserRAM, (VM_CurrentThread->T_SP -= (uint16)0x0004U));
}


void VM_PushF(float64 f)
{
    FREF(VM_UserRAM, VM_CurrentThread->T_SP)   = (float64)f;
    VM_CurrentThread->T_SP                    += FLOAT_SIZE;
}


float64 VM_PopF(void)
{
    return FREF(VM_UserRAM, (VM_CurrentThread->T_SP -= FLOAT_SIZE));
}


void VM_Nop(void)
{
}


void VM_Yield(void)
{
    VM_OpsToExecute = (uint8)0x01;
}


void VM_IncSP(void)
{
    if ((sint16)VM_OperandW >= (sint16)0x0000) {
        VM_CurrentThread->T_SP += VM_OperandW;
    } else {
        VM_CurrentThread->T_SP -= VM_OperandW;
    }
}


void VM_Quit(void)
{

}


void VM_Reset(void)
{
    uint8 num;

    if (VM_OperandB == (uint8)0x00) {
        num = VM_CurrentTID;
    } else {
        num = VM_OperandB - (uint8)0x01;
    }

    VM_InitThread(num);
}


void VM_Sleep(void)
{

    if (VM_CurrentThread->T_STATE == STATE_NOT_SLEEPING) {
        CPU_DISABLE_ALL_INTERRUPTS();
        VM_CurrentThread->T_SLEEP_TIME     = VM_SysVarTimerMS;
        VM_CurrentThread->T_WAKEUP_TIME    = VM_SysVarTimerMS + (uint32)(uint16)VM_PopW();
        CPU_ENABLE_ALL_INTERRUPTS();
        VM_CurrentThread->T_STATE = STATE_SLEEPING;
    } else {
        CPU_DISABLE_ALL_INTERRUPTS();

        if (VM_SysVarTimerMS >= VM_CurrentThread->T_WAKEUP_TIME) {
            VM_CurrentThread->T_STATE = STATE_NOT_SLEEPING;
            CPU_ENABLE_ALL_INTERRUPTS();
            return;
        }

        CPU_ENABLE_ALL_INTERRUPTS();
    }

    VM_CurrentThread->T_PC    -= (uint16)0x0001U;
    VM_OpsToExecute            = (uint8)0x01;
}


void VM_Capture(void)
{
    if (VM_CurrentThread->T_SEMA == VM_SEMA_FREE) {
        VM_CurrentThread->T_SEMA = (uint16)VM_PopW();
    }

    if (BREF(VM_UserRAM, VM_CurrentThread->T_SEMA) == VM_SEMA_FREE) {
        BREF(VM_UserRAM, VM_CurrentThread->T_SEMA) = VM_CurrentTID++;
    } else {
        VM_CurrentThread->T_PC    -= (uint16)0x0001U;               /* Yield. */
        VM_OpsToExecute            = (uint8)0x01;
    }
}


void VM_Release(void)
{
    if ((VM_CurrentThread->T_SEMA) != VM_SEMA_FREE) {
        BREF(VM_UserRAM, VM_CurrentThread->T_SEMA) = (uint8)0x00;
        VM_CurrentThread->T_SEMA                   = VM_SEMA_FREE;

        VM_CurrentThread->T_PC    -= (uint16)0x0001U;
        VM_OpsToExecute            = (uint8)0x01;
    }
}


void VM_Call(void)
{
    VM_PushW((sint16)VM_CurrentThread->T_BP);
    VM_PushW((sint16)VM_CurrentThread->T_PC);

    VM_CurrentThread->T_PC = VM_OperandW;
    VM_CurrentThread->T_BP = VM_CurrentThread->T_SP;
}


void VM_FastReturn(void)
{
    VM_CurrentThread->T_PC = (uint16)VM_PopW();
    VM_CurrentThread->T_BP = (uint16)VM_PopW();
}


void VM_Return(void)
{
    uint16 * fp;

    fp = (uint16 *)(VM_UserRAM + VM_CurrentThread->T_BP);

    VM_CurrentThread->T_PC = *(fp - 1);
    VM_CurrentThread->T_SP = VM_CurrentThread->T_BP - VM_OperandW;       /* Stack-Cleanup. */
    VM_CurrentThread->T_BP = *(fp - 2);
}


/*
   _Return::
    ldd         T_BP,x
    addd        _UserStackStart
    tfr d,y
    ldd         -2,y
    std         T_PC,x
    ldd         T_BP,x
    subd        _operandw       ; Stack-Cleanup
    std         T_SP,x
    ldd         -4,y
    std         T_BP,x
    rts
 */

void VM_ReturnValue(void)
{
    union {
        sint16  w;
        sint32  d;
        float64 f;
    } RetValue;

    switch (VM_OperandB) {
        case RTYPE_INT:
            RetValue.w = VM_PopW();
            VM_RetCleanup();
            VM_PushW(RetValue.w);
            break;
        case RTYPE_LONG:
            RetValue.d = VM_PopL();
            VM_RetCleanup();
            VM_PushL(RetValue.d);
            break;
        case RTYPE_FLOAT:
            RetValue.f = VM_PopF();
            VM_RetCleanup();
            VM_PushF(RetValue.f);
            break;
        default:
            CC_ASSERT(FALSE, ERROR_ILLOPA);
    }

/*
   _ReturnValue::
    ldab        _operandb       ; 0=Int, 1=long; 2=float;
    cmpb        #0
    beq         rv_int
    cmpb        #1
    beq rv_long
    cmpb        #2
    beq         rv_float

   rv_int:
    jsr         _popw
    pshd
    bsr         _RetCleanup
    puld
    jsr         _pushw
    bra         rv_exit
   rv_long:
    jsr         _popl
    bsr         _RetCleanup
    jsr         _pushl
    bra         rv_exit
   rv_float:
    jsr         _popl
    bsr         _RetCleanup
    jsr         _pushl
   rv_exit:
    rts
 */
}


STATIC void VM_RetCleanup(void)
{
    uint16 * fp;

    fp = (uint16 *)(VM_UserRAM + VM_CurrentThread->T_BP);

    VM_CurrentThread->T_PC = *(fp - 1);
    VM_CurrentThread->T_SP = VM_CurrentThread->T_BP - VM_OperandW;       /* Stack-Cleanup. */
    VM_CurrentThread->T_BP = *(fp - 2);
    /*
       _RetCleanup:
       ldd              T_BP,x
       addd     _UserStackStart
       tfr              d,y
       ldd              -2,y
       std              T_PC,x
       ldd              T_BP,x
       subd     _operandw       ; Stack-Cleanup
       std              T_SP,x
       ldd              -4,y
       std              T_BP,x
       rts

     */
}


void VM_MakeGlobalPointer(void)
{
    uint16 * fp;

    fp     = (uint16 *)(VM_UserRAM + (VM_CurrentThread->T_SP - (uint16)0x0002U));
    *fp    = (*fp) + VM_CurrentThread->T_BP;
}


void VM_Branch(void)
{
    BRANCH_TO(VM_OperandW);
}


void VM_BranchIfZero(void)
{
    if (VM_PopW() == 0) {
        BRANCH_TO(VM_OperandW);
    }
}


void VM_Syscall(void)
{

}


void VM_Sysjump(void)
{
}


void VM_InlineSyscall(void)
{
}


void VM_InlineSysjump(void)
{
}


void VM_Run(void)
{
    VM_TCBType * tcb;

    if (VM_OperandB != (uint8)0x00) {
        tcb = VM_CurrentThread;
    } else {
        tcb = THREAD_PTR(VM_OperandB - (uint8)0x01);
    }

    tcb->T_PRIO_SAVE   = tcb->T_PRIO_CURR;
    tcb->T_PRIO_CURR   = LOBYTE(VM_PopW());

    if (tcb->T_PRIO_CURR == (uint8)0x00) {
        VM_OpsToExecute = (uint8)0x01;
    }
}


void VM_Resume(void)
{
    VM_TCBType * tcb;

    if (VM_OperandB != (uint8)0x00) {
        tcb = VM_CurrentThread;
    } else {
        tcb = THREAD_PTR(VM_OperandB - (uint8)0x01);
    }

    tcb->T_PRIO_CURR = tcb->T_PRIO_SAVE;
}


void VM_Save(void)
{

}


void VM_Restore(void)
{

}


void VM_Hook(void)
{

}


void VM_SetCodePage(uint16 pc)
{
    HAL_FLASH_SELECT_PAGE((uint8)((pc / (FLS_PAGE_SIZE / (uint16)2)) + FLS_PPAGE_BASE_CODE));
}

#if defined(_MSC_VER)
int dummy(void)
{
    return 0;
}
#endif /* _MSC_VER */

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_CORE_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

