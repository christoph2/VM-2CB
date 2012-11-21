
%module vm_hm

%include "Types.i"

%{
#include "VM.h"

typedef enum tagHM_CommandType {
    HM_CMD_SEND_ID,
    HM_CMD_SEND_DATE,
    HM_CMD_SEND_VERSION,
    HM_CMD_START,
    HM_CMD_LOAD_VMC,
    HM_CMD_LOAD_HEX,
    HM_CMD_ERASE_VMC,
    HM_CMD_ERASE_HEX,
    HM_CMD_SET_HI_BAUD,
    HM_CMD_SET_DEF_BAUD,
    HM_CMD_SET_TURBO_BAUD,
    HM_CMD_RESET = (uint8) 0xff
} HM_CommandType;

void Hm_Dispatcher(void);

boolean Hm_ButtonBootstrapMode(void);
boolean Hm_ButtonHostMode(void);

uint32   Hm_ReadLong(void);
uint16   Hm_ReadWordLE(void), Hm_ReadWordBE(void);

void Hm_SendID(void), Hm_SendDate(void), Hm_SendVersion(void), Hm_Start(void);
void Hm_LoadVMC(void), Hm_EraseVMC(void), Hm_EraseHEX(void), Hm_LoadHEX(void);
void Hm_SetBaudHi(void), Hm_SetBaudDef(void), Hm_SetBaudTurbo(void), Hm_Reset(void);

uint8    Hm_WriteCode(uint16 addr, uint16 data);
uint8    Hm_WriteConst(uint16 addr, uint16 data);
uint8    Hm_EraseVmcPages(void);
uint8    Hm_EraseAsmPages(void);

%}

typedef enum tagHM_CommandType {
    HM_CMD_SEND_ID,
    HM_CMD_SEND_DATE,
    HM_CMD_SEND_VERSION,
    HM_CMD_START,
    HM_CMD_LOAD_VMC,
    HM_CMD_LOAD_HEX,
    HM_CMD_ERASE_VMC,
    HM_CMD_ERASE_HEX,
    HM_CMD_SET_HI_BAUD,
    HM_CMD_SET_DEF_BAUD,
    HM_CMD_SET_TURBO_BAUD,
    HM_CMD_RESET = (uint8) 0xff
} HM_CommandType;

void Hm_Dispatcher(void);

boolean Hm_ButtonBootstrapMode(void);
boolean Hm_ButtonHostMode(void);

uint32   Hm_ReadLong(void);
uint16   Hm_ReadWordLE(void), Hm_ReadWordBE(void);

void Hm_SendID(void), Hm_SendDate(void), Hm_SendVersion(void), Hm_Start(void);
void Hm_LoadVMC(void), Hm_EraseVMC(void), Hm_EraseHEX(void), Hm_LoadHEX(void);
void Hm_SetBaudHi(void), Hm_SetBaudDef(void), Hm_SetBaudTurbo(void), Hm_Reset(void);

uint8    Hm_WriteCode(uint16 addr, uint16 data);
uint8    Hm_WriteConst(uint16 addr, uint16 data);
uint8    Hm_EraseVmcPages(void);
uint8    Hm_EraseAsmPages(void);

