/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
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

#include "VM_Hm.h"
#include "VM_Excp.h"

static uint32   Hm_ReadLong(void);
static uint16   Hm_ReadWordLE(void), Hm_ReadWordBE(void);

static void Hm_SendID(void), Hm_SendDate(void), Hm_SendVersion(void), Hm_Start(void);
static void Hm_LoadVMC(void), Hm_EraseVMC(void), Hm_EraseHEX(void), Hm_LoadHEX(void);
static void Hm_SetBaudHi(void), Hm_SetBaudDef(void), Hm_SetBaudTurbo(void), Hm_Reset(void);

static uint8    Hm_WriteCode(uint16 addr, uint16 data);
static uint8    Hm_WriteConst(uint16 addr, uint16 data);
static uint8    Hm_EraseVmcPages(void);
static uint8    Hm_EraseAsmPages(void);


static const uint8  Hm_CodeBanks[]     = FLS_CODE_BANKS;
static const uint8  Hm_ConstBanks[]    = FLS_CONST_BANKS;
#if defined(FLS_USE_ASM_BANKS)
static const uint8 Hm_AsmBanks[] = FLS_ASM_BANKS;
#endif  /* FLS_USE_ASM_BANKS */

/*
**      Jump-Table.
*/
static const VoidFunctionType FuncTab[] = {
    Hm_SendID,   Hm_SendDate, Hm_SendVersion, Hm_Start,      Hm_LoadVMC, Hm_LoadHEX,
    Hm_EraseVMC, Hm_EraseHEX, Hm_SetBaudHi,   Hm_SetBaudDef, Hm_SetBaudTurbo
};

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_HM_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */


static uint8 dummy(void)
{
    return 0;
}


void Hm_Dispatcher(void)
{
    uint8 ch;

    ShowStatus(STATUS_HOSTMODE);

    FOREVER {
        ch = HAL_COM0_GETCHAR();

        if (ch <= (uint8)(SIZEOF_ARRAY(FuncTab))) {
            FuncTab[ch]();
        } else if (ch == HM_CMD_RESET) {
            Hm_Reset();
        } else {

        }
    }
}


static void Hm_SendID(void)
{
    HAL_COM0_PUTSTRING((uint8 *)VM_C_CCONTROL);
}


static void Hm_SendDate(void)
{
    HAL_COM0_PUTSTRING((uint8 *)VM_C_DATE);
}


static void Hm_SendVersion(void)
{
    HAL_COM0_PUTSTRING((uint8 *)VM_C_VERSION);
}


static void Hm_Start(void)
{
    /* Start VM direct. */
    /* IISR_ENTRY_POINT(); */
    HAL_RESET_MCU();
}


static void Hm_LoadVMC(void)
{
    uint32  numConsts, numVMCs;
    uint16  data, idx;

    numConsts  = Hm_ReadLong();
    numVMCs    = Hm_ReadLong();

    for (idx = (uint16)0x0000U; idx < (uint16)(numConsts / (uint16)2); ++idx) {
        data = Hm_ReadWordBE();
        CC_ASSERT((Hm_WriteConst(idx, data) == STD_OK), ERROR_BURN);
        CC_ASSERT((WREF(FLS_PAGE_ADDR, ((idx << 1) % FLS_PAGE_SIZE)) == data), ERROR_BURN);
    }

    for (idx = (uint16)0x0000U; idx < (uint16)numVMCs; ++idx) {
        data = Hm_ReadWordLE();
        CC_ASSERT((Hm_WriteCode(idx, data) == STD_OK), ERROR_BURN);
        CC_ASSERT((WREF(FLS_PAGE_ADDR, ((idx << 1) % FLS_PAGE_SIZE)) == data), ERROR_BURN);
    }
}


static void Hm_LoadHEX(void)
{
    uint16  addr, data;
    uint8   len;

    do {
        addr = Hm_ReadWordBE();
        len = HAL_COM0_GETCHAR();
        HAL_COM0_PUT(len);

        while (len--) {
            data = Hm_ReadWordBE();

            addr += (uint16)2;
        }
    } while (addr != ((uint16)0xffffU));
}


static void Hm_EraseVMC(void)
{
    CC_ASSERT((Hm_EraseVmcPages() == STD_OK), ERROR_BURN);

    HAL_COM0_PUT(HM_CMD_ERASE_VMC);
}


static void Hm_EraseHEX(void)
{
    CC_ASSERT((Hm_EraseAsmPages() == STD_OK), ERROR_BURN);

    HAL_COM0_PUT(HM_CMD_ERASE_HEX);
}


static void Hm_SetBaudHi(void)
{
    HAL_COM0_SETBAUDRATE(57600UL);
}


static void Hm_SetBaudDef(void)
{
    HAL_COM0_SETBAUDRATE(19200UL);
}


static void Hm_SetBaudTurbo(void)
{
    HAL_COM0_SETBAUDRATE(115200UL);
}


static void Hm_Reset(void)
{
/*  IISR_ENTRY_POINT(); */
    HAL_RESET_MCU();
}


uint32 Hm_ReadLong(void)
{
    uint8 ch[4], i;

    for (i = (uint8)0x00; i < (uint8)4; ++i) {
        ch[i] = HAL_COM0_GETCHAR();
        HAL_COM0_PUT(ch[i]);
    }

    /* LE==>BE Conversion.*/
    return MAKEDWORD((MAKEWORD(ch[3], ch[2])), (MAKEWORD(ch[1], ch[0])));
}


uint16 Hm_ReadWordLE(void)
{
    uint8 ch[2];

    ch[0] = HAL_COM0_GETCHAR();
    HAL_COM0_PUT(ch[0]);

    ch[1] = HAL_COM0_GETCHAR();
    HAL_COM0_PUT(ch[1]);

    /* LE==>BE Conversion.*/
    return MAKEWORD(ch[1], ch[0]);
}


uint16 Hm_ReadWordBE(void)
{
    uint8 ch[2];

    ch[0] = HAL_COM0_GETCHAR();
    HAL_COM0_PUT(ch[0]);

    ch[1] = HAL_COM0_GETCHAR();
    HAL_COM0_PUT(ch[1]);

    return MAKEWORD(ch[0], ch[1]);
}


boolean Hm_ButtonBootstrapMode(void)
{
    return FALSE;
}


boolean Hm_ButtonHostMode(void)
{
    return FALSE;
}


uint8 Hm_EraseVmcPages(void)
{
    uint8   i;
    uint8   stat;

    for (i = (uint8)0x00; i < (uint8)(sizeof(Hm_CodeBanks)); ++i) {
        stat = HAL_FLASH_ERASE_BANK(Hm_CodeBanks[i]);

        if (stat != STD_OK) {
            return stat;
        }
    }

    for (i = (uint8)0x00; i < (uint8)(sizeof(Hm_ConstBanks)); ++i) {
        stat = HAL_FLASH_ERASE_BANK(Hm_ConstBanks[i]);

        if (stat != STD_OK) {
            return stat;
        }
    }

    return STD_OK;
}


uint8 Hm_EraseAsmPages(void)
{
#if defined(FLS_USE_ASM_BANKS)
    uint8   i;
    uint8   stat;

    for (i = (uint8)0x00; i < (uint8)(sizeof(Hm_AsmBanks)); ++i) {
        stat = S12Fls_MassErase(Hm_AsmBanks[i]);

        if (stat != S12FLS_ERR_OK) {
            return stat;
        }
    }

#endif  /* FLS_USE_ASM_BANKS */

    return STD_OK;
}


/*
**  Flash-Wrapper.
*/
uint8 Hm_WriteCode(uint16 addr, uint16 data)
{
    return HAL_FLASH_ERASE_PROGRAM_WORD((uint8)((addr / (FLS_PAGE_SIZE / (uint16)2)) + FLS_PPAGE_BASE_CODE),
                              (((addr % (FLS_PAGE_SIZE / (uint16)2)) << 1) + FLS_PAGE_ADDR), data);
}


uint8 Hm_WriteConst(uint16 addr, uint16 data)
{
    return HAL_FLASH_ERASE_PROGRAM_WORD((uint8)((addr / (FLS_PAGE_SIZE / (uint16)2)) + FLS_PPAGE_BASE_CONST),
                              (((addr % (FLS_PAGE_SIZE / (uint16)2)) << 1) + FLS_PAGE_ADDR), data);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_HM_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
