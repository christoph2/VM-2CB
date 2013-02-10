%{
#include <stdint.h>
%}

%include <stdint.i>

typedef unsigned char boolean;

typedef /*@signed-integral-type@*/ int8_t       sint8;
typedef /*@unsigned-integral-type@*/ uint8_t    uint8;
typedef /*@signed-integral-type@*/ int16_t      sint16;
typedef /*@unsigned-integral-type@*/ uint16_t   uint16;
typedef /*@signed-integral-type@*/ int32_t      sint32;
typedef /*@unsigned-integral-type@*/ uint32_t   uint32;

typedef /*@signed-integral-type@*/ int_least8_t     sint8_least;
typedef /*@unsigned-integral-type@*/ uint_least8_t  uint8_least;
typedef /*@signed-integral-type@*/ int_least16_t    sint16_least;
typedef /*@unsigned-integral-type@*/ uint_least16_t uint16_least;
typedef /*@signed-integral-type@*/ int_least32_t    sint32_least;
typedef /*@unsigned-integral-type@*/ uint_least32_t uint32_least;

typedef double float64;

%include "carrays.i"
%array_class(unsigned char, byteArray);
%array_class(unsigned short, codeArray);

void setRAMPointer(unsigned char * ptr);
void setCodePointer(unsigned short * ptr);
void setConstPointer(unsigned char * ptr);
void setOperandB(uint8_t b);
void setOperandW(uint16_t w);

extern uint8 VM_OperandB;
extern uint16 VM_OperandW;
extern uint16 VM_SysVarYear, VM_SysVarMonth, VM_SysVarDay, VM_SysVarHour, VM_SysVarDow;
extern uint16 VM_SysVarMinute, VM_SysVarSecond, VM_SysVarDst, VM_SysVarZone, VM_SysVarDcfErrCnt;
extern uint32 VM_SysVarTimerMS, VM_SysVarCnt1, VM_SysVarCnt2, VM_SysVarCnt3;
extern uint32 VM_SysVarCnt4, VM_SysVarFreq1, VM_SysVarFreq2;

%{
uint16_t getSP(void);
void setOperandB(uint8_t b);
void setOperandW(uint16_t w);
extern uint8_t VM_OperandB;
extern uint16_t VM_OperandW;
extern uint16_t VM_SysVarYear, VM_SysVarMonth, VM_SysVarDay, VM_SysVarHour, VM_SysVarDow;
extern uint16_t VM_SysVarMinute, VM_SysVarSecond, VM_SysVarDst, VM_SysVarZone, VM_SysVarDcfErrCnt;
extern uint32_t VM_SysVarTimerMS, VM_SysVarCnt1, VM_SysVarCnt2, VM_SysVarCnt3;
extern uint32_t VM_SysVarCnt4, VM_SysVarFreq1, VM_SysVarFreq2;
uint8_t getLastException(void);
uint8_t getLastStatus(void);
%}

void    VM_PushW(sint16 w);
sint16  VM_PopW(void);
void    VM_PushL(sint32 l);
sint32  VM_PopL(void);
void    VM_PushF(float f);
float64 VM_PopF(void);
uint16 getSP(void);
uint8_t getLastException(void);
uint8_t getLastStatus(void);

