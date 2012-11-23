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
#if !defined(__CCCONFIG_H)
#define __CCCONFIG_H

#if defined(__cplusplus)
extern "C"
{
#endif  /* __cplusplus */

#if defined(_MSC_VER)

#define FLS_PPAGE_OFFSET    ((uint8)0x20)
#define FLS_SECTOR_SIZE     ((uint16)1024U)
#define FLS_NUM_CODE_PAGES  ((uint8)2)
#define FLS_NUM_CONST_PAGES ((uint8)2)
#define FLS_NUM_ASM_PAGES   ((uint8)2)
#define FLS_CODE_BANKS      {(uint8)0x02}
#define FLS_CONST_BANKS     {(uint8)0x03}
#define FLS_ASM_BANKS       {(uint8)0x01}
#define FLS_USE_ASM_BANKS
#define VM_RAM_SIZE         ((uint16)0x3800U

#define VM_RAM_START            (((uint16)0x4000U) - VM_RAM_SIZE)

#define FLS_PPAGE_BASE_CONST    ((uint8)FLS_PPAGE_OFFSET)
#define FLS_PPAGE_BASE_CODE     ((uint8)FLS_PPAGE_OFFSET + FLS_NUM_CONST_PAGES)

#define FLS_NUM_BANKS           ((uint8)1)

#define FLS_PAGE_ADDR           ((uint16)0x8000U)
#define FLS_PAGE_SIZE           ((uint16)0x10000U)  /* NB: MUST MATCH system allocation granularity!!! */

#define EE_BASE                 ((uint16)0x0400U)
#define EE_LEN                  (VM_RAM_START - EE_BASE)

/* #define VM_USE_WATCHDOG */

#define VM_SYSTEM_TIMER_FREQ    ((uint16)1000)        /* µSecs. */

#else
/* #define VM_TARGET_S12_DP512 */
#define VM_TARGET_S12_DP256

#if defined(VM_TARGET_S12_DP512)
/*
**
**  512-Flash-Block-Layout
**  ======================
**
**  Block   Usage
**  ------------------------------------------
**  0       OS (Pages 0x3e+0x3f ==>
**          (32K Unpaged OS+Bootloader) and
**          (96K Paged OS + Reserve))
**  1       128K UserASM    (Pages 0x30-0x37).
**  2       128K UserCode   (Pages 0x28-0x2f).
**  3       128K UserConst  (Pages 0x20-0x27).
**
*/
    #define FLS_PPAGE_OFFSET    ((uint8)0x20)
    #define FLS_SECTOR_SIZE     ((uint16)1024U)
    #define FLS_NUM_CODE_PAGES  ((uint8)8)
    #define FLS_NUM_CONST_PAGES ((uint8)8)
    #define FLS_NUM_ASM_PAGES   ((uint8)8)
    #define FLS_CODE_BANKS      {(uint8)0x02}
    #define FLS_CONST_BANKS     {(uint8)0x03}
    #define FLS_ASM_BANKS       {(uint8)0x01}
    #define FLS_USE_ASM_BANKS
    #define VM_RAM_SIZE         ((uint16)0x3800U
#elif defined(VM_TARGET_S12_DP256)
/*
**
**  256-Flash-Block-Layout
**  ======================
**
**  Block   Usage
**  ------------------------------------------
**  0       OS (Pages 0x3e+0x3f ==>
**          (32K Unpaged OS+Bootloader) and
**          (32K Paged OS + Reserve))
**  1+2     128K UserCode   (Pages 0x34-0x3b).
**  3       64K  UserConst  (Pages 0x30-0x33).
**
*/
    #define FLS_PPAGE_OFFSET    ((uint8)0x30)
    #define FLS_SECTOR_SIZE     ((uint16)512U)
    #define FLS_NUM_CODE_PAGES  ((uint8)8)
    #define FLS_NUM_CONST_PAGES ((uint8)4)
    #define FLS_NUM_ASM_PAGES   ((uint8)0)
    #define FLS_CODE_BANKS      {(uint8)0x01, (uint8)0x02}
    #define FLS_CONST_BANKS     {(uint8)0x03}
/*    #define FLS_USER_ASM_BANKS      {} */
    #define VM_RAM_SIZE         ((uint16)0x3000U
#else
    #error No Target specified.
#endif

#define VM_RAM_START            (((uint16)0x4000U) - VM_RAM_SIZE)

#define FLS_PPAGE_BASE_CONST    ((uint8)FLS_PPAGE_OFFSET)
#define FLS_PPAGE_BASE_CODE     ((uint8)FLS_PPAGE_OFFSET + FLS_NUM_CONST_PAGES)

#define FLS_NUM_BANKS           ((uint8)4)

#define FLS_PAGE_ADDR           ((uint16)0x8000U)
#define FLS_PAGE_SIZE           ((uint16)0x4000U)

#define EE_BASE                 ((uint16)0x0400U)
#define EE_LEN                  (VM_RAM_START - EE_BASE)

/* #define VM_USE_WATCHDOG */

#define VM_SYSTEM_TIMER_FREQ    ((uint16)1000)        /* µSecs. */

#endif /* MSC_VER */

#if defined(__cplusplus)
}
#endif  /* __cplusplus */

#endif /* __CCCONFIG_H */
