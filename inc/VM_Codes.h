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
#if !defined(__VMCODES_H)
#define __VMCODES_H

#define VM_CODE_A                       ((uint16)0x0000)
#define VM_CODE_B                       ((uint16)0x0040)
#define VM_CODE_C                       ((uint16)0x0080)
#define VM_CODE_D                       ((uint16)0x00C0)

/* --- VM_CODE_A ----------------------------------------------------- */

#define VM_NOP_A                        ( VM_CODE_A |  0 )

#define VM_QUIT                         ( VM_CODE_A |  1 )
#define VM_YIELD                        ( VM_CODE_A |  2 )
#define VM_SLEEP                        ( VM_CODE_A |  3 )
#define VM_CAPTURE                      ( VM_CODE_A |  4 )
#define VM_RELEASE                      ( VM_CODE_A |  5 )

#define VM_FAST_RETURN                  ( VM_CODE_A |  6 )

#define VM_MAKE_GLOBAL_POINTER          ( VM_CODE_A |  7 )

#define VM_LOAD_REF_CONST_BYTE          ( VM_CODE_A |  8 )
#define VM_LOAD_REF_CONST_INT           ( VM_CODE_A |  9 )
#define VM_LOAD_REF_CONST_LONG          ( VM_CODE_A | 10 )
#define VM_LOAD_REF_CONST_FLOAT         ( VM_CODE_A | 11 )

#define VM_LOAD_REF_BYTE                ( VM_CODE_A | 12 )
#define VM_LOAD_REF_INT                 ( VM_CODE_A | 13 )
#define VM_LOAD_REF_LONG                ( VM_CODE_A | 14 )
#define VM_LOAD_REF_FLOAT               ( VM_CODE_A | 15 )

#define VM_INC_LOAD_REF_BYTE            ( VM_CODE_A | 16 )
#define VM_INC_LOAD_REF_INT             ( VM_CODE_A | 17 )
#define VM_INC_LOAD_REF_LONG            ( VM_CODE_A | 18 )
#define VM_INC_LOAD_REF_FLOAT           ( VM_CODE_A | 19 )

#define VM_STORE_REF_BYTE               ( VM_CODE_A | 20 )
#define VM_STORE_REF_INT                ( VM_CODE_A | 21 )
#define VM_STORE_REF_LONG               ( VM_CODE_A | 22 )
#define VM_STORE_REF_FLOAT              ( VM_CODE_A | 23 )

#define VM_CAST_INT_TO_LONG             ( VM_CODE_A | 24 )
#define VM_CAST_INT_TO_FLOAT            ( VM_CODE_A | 25 )
#define VM_CAST_LONG_TO_INT             ( VM_CODE_A | 26 )
#define VM_CAST_LONG_TO_FLOAT           ( VM_CODE_A | 27 )
#define VM_CAST_FLOAT_TO_INT            ( VM_CODE_A | 28 )
#define VM_CAST_FLOAT_TO_LONG           ( VM_CODE_A | 29 )

#define VM_INVERT_INT                   ( VM_CODE_A | 30 )
#define VM_INVERT_LONG                  ( VM_CODE_A | 31 )
#define VM_INVERT_FLOAT                 ( VM_CODE_A | 32 )
#define VM_NEG_INT                      ( VM_CODE_A | 33 )
#define VM_NEG_LONG                     ( VM_CODE_A | 34 )
#define VM_NEG_FLOAT                    ( VM_CODE_A | 35 )
#define VM_ABS_INT                      ( VM_CODE_A | 36 )
#define VM_ABS_LONG                     ( VM_CODE_A | 37 )
#define VM_ABS_FLOAT                    ( VM_CODE_A | 38 )

#define VM_PUT_INT                      ( VM_CODE_A | 39 )
#define VM_PUT_LONG                     ( VM_CODE_A | 40 )
#define VM_PUT_FLOAT                    ( VM_CODE_A | 41 )
#define VM_GET_INT                      ( VM_CODE_A | 42 )
#define VM_GET_LONG                     ( VM_CODE_A | 43 )
#define VM_GET_FLOAT                    ( VM_CODE_A | 44 )

#define VM_GET_SINGLE_PORT              ( VM_CODE_A | 45 )
#define VM_GET_NIBBLE_PORT              ( VM_CODE_A | 46 )
#define VM_GET_BYTE_PORT                ( VM_CODE_A | 47 )
#define VM_GET_WORD_PORT                ( VM_CODE_A | 48 )
#define VM_GET_ADC_PORT                 ( VM_CODE_A | 49 )

#define VM_SET_SINGLE_PORT              ( VM_CODE_A | 50 )
#define VM_SET_NIBBLE_PORT              ( VM_CODE_A | 51 )
#define VM_SET_BYTE_PORT                ( VM_CODE_A | 52 )
#define VM_SET_WORD_PORT                ( VM_CODE_A | 53 )

#define VM_DEACT_SINGLE_PORT            ( VM_CODE_A | 54 )
#define VM_DEACT_NIBBLE_PORT            ( VM_CODE_A | 55 )
#define VM_DEACT_BYTE_PORT              ( VM_CODE_A | 56 )
#define VM_DEACT_WORD_PORT              ( VM_CODE_A | 57 )

#define VM_TOGGLE_SINGLE_PORT           ( VM_CODE_A | 58 )
#define VM_PULSE_SINGLE_PORT            ( VM_CODE_A | 59 )

#define VM_GET_COUNT                    ( VM_CODE_A | 60 )
#define VM_GET_FREQ                     ( VM_CODE_A | 61 )

#define VM_SYSCALL                      ( VM_CODE_A | 62 )
#define VM_SYSJUMP                      ( VM_CODE_A | 63 )

/* --- VM_CODE_B ----------------------------------------------------- */

#define VM_NOP_B                        ( VM_CODE_B |  0 )

#define VM_RESET                        ( VM_CODE_B |  1 )
#define VM_RUN                          ( VM_CODE_B |  2 )
#define VM_RESUME                       ( VM_CODE_B |  3 )

#define VM_LOAD_IMMEDIATE_BYTE          ( VM_CODE_B |  4 )

#define VM_ADD                          ( VM_CODE_B |  5 )
#define VM_SUB                          ( VM_CODE_B |  6 )
#define VM_MUL                          ( VM_CODE_B |  7 )
#define VM_DIV                          ( VM_CODE_B |  8 )
#define VM_MOD                          ( VM_CODE_B |  9 )
#define VM_EQU                          ( VM_CODE_B | 10 )
#define VM_NEQU                         ( VM_CODE_B | 11 )
#define VM_HI                           ( VM_CODE_B | 12 )
#define VM_HIS                          ( VM_CODE_B | 13 )
#define VM_LO                           ( VM_CODE_B | 14 )
#define VM_LOS                          ( VM_CODE_B | 15 )
#define VM_AND                          ( VM_CODE_B | 16 )
#define VM_NAND                         ( VM_CODE_B | 17 )
#define VM_OR                           ( VM_CODE_B | 18 )
#define VM_NOR                          ( VM_CODE_B | 19 )
#define VM_XOR                          ( VM_CODE_B | 20 )
#define VM_NXOR                         ( VM_CODE_B | 21 )
#define VM_SHL                          ( VM_CODE_B | 22 )
#define VM_SHR                          ( VM_CODE_B | 23 )
#define VM_ASR                          ( VM_CODE_B | 24 )
#define VM_ROL                          ( VM_CODE_B | 25 )
#define VM_ROR                          ( VM_CODE_B | 26 )
#define VM_MIN                          ( VM_CODE_B | 27 )
#define VM_MAX                          ( VM_CODE_B | 28 )
    #define CALC_INT_INT                ((uint8)0)
    #define CALC_INT_LONG               ((uint8)1)
    #define CALC_INT_FLOAT              ((uint8)2)
    #define CALC_LONG_INT               ((uint8)3)
    #define CALC_LONG_LONG              ((uint8)4)
    #define CALC_LONG_FLOAT             ((uint8)5)
    #define CALC_FLOAT_INT              ((uint8)6)
    #define CALC_FLOAT_LONG             ((uint8)7)
    #define CALC_FLOAT_FLOAT            ((uint8)8)

#define VM_MATH_FUNCTION                ( VM_CODE_B | 29 )
    #define MATH_SQR                    ((uint8)0)
    #define MATH_SQRT                   ((uint8)1)
    #define MATH_CURT                   ((uint8)2)
    #define MATH_SIN                    ((uint8)3)
    #define MATH_COS                    ((uint8)4)
    #define MATH_TAN                    ((uint8)5)
    #define MATH_ASIN                   ((uint8)6)
    #define MATH_ACOS                   ((uint8)7)
    #define MATH_ATAN                   ((uint8)8)
    #define MATH_LOG                    ((uint8)9)
    #define MATH_LN                     ((uint8)10)
    #define MATH_EXP                    ((uint8)11)
    #define MATH_POW                    ((uint8)12)
    #define MATH_CEIL                   ((uint8)13)
    #define MATH_FLOOR                  ((uint8)14)

#define VM_LOAD_SYSVAR_INT              ( VM_CODE_B | 30 )
#define VM_STORE_SYSVAR_INT             ( VM_CODE_B | 31 )
#define VM_LOAD_SYSVAR_LONG             ( VM_CODE_B | 32 )
#define VM_STORE_SYSVAR_LONG            ( VM_CODE_B | 33 )
    #define ISYSVAR_YEAR                ((uint8)0)
    #define ISYSVAR_MONTH               ((uint8)1)
    #define ISYSVAR_DAY                 ((uint8)2)
    #define ISYSVAR_HOUR                ((uint8)3)
    #define ISYSVAR_MINUTE              ((uint8)4)
    #define ISYSVAR_SECOND              ((uint8)5)
    #define ISYSVAR_DOW                 ((uint8)6)
    #define ISYSVAR_DST                 ((uint8)7)
    #define ISYSVAR_ZONE                ((uint8)8)
    #define ISYSVAR_DCF_ERRCNT          ((uint8)9)
    #define ISYSVAR_MAX                 ISYSVAR_DCF_ERRCNT

    #define LSYSVAR_TIMER_MS            ((uint8)0)
    #define LSYSVAR_CNT_1               ((uint8)1)
    #define LSYSVAR_CNT_2               ((uint8)2)
    #define LSYSVAR_CNT_3               ((uint8)3)
    #define LSYSVAR_CNT_4               ((uint8)4)
    #define LSYSVAR_FREQ1               ((uint8)5)
    #define LSYSVAR_FREQ2               ((uint8)6)
    #define LSYSVAR_MAX                 LSYSVAR_FREQ2

#define VM_STRING                       ( VM_CODE_B | 34 )
    #define STRING_CLEAR                ((uint8)0)
    #define STRING_GET_LENGTH           ((uint8)1)
    #define STRING_FILL                 ((uint8)2)
    #define STRING_PUT_CHAR             ((uint8)3)
    #define STRING_PUT_STRING           ((uint8)4)
    #define STRING_PUT_CONST_STRING     ((uint8)5)
    #define STRING_PUT_INT              ((uint8)6)
    #define STRING_PUT_LONG             ((uint8)7)
    #define STRING_PUT_FLOAT            ((uint8)8)
    #define STRING_PUT_FORMATTED_INT    ((uint8)9)
    #define STRING_PUT_FORMATTED_LONG   ((uint8)10)
    #define STRING_PUT_FORMATTED_FLOAT  ((uint8)11)
    #define STRING_PUT_BYTE_MASK        ((uint8)12)
    #define STRING_CODE_MAX             STRING_PUT_BYTE_MASK

#define VM_PLM                          ( VM_CODE_B | 35 )
    #define PLM_INIT                    ((uint8)0)
    #define PLM_SET_TIMEBASE            ((uint8)1)
    #define PLM_SET_PORTMODE            ((uint8)2)
    #define PLM_SET_PERIODLENGTH        ((uint8)3)
    #define PLM_OUT                     ((uint8)4)
    #define PLM_BEEP                    ((uint8)5)
    #define PLM_CODE_MAX                PLM_BEEP

#define VM_HWCOM                        ( VM_CODE_B | 36 )
    #define HWCOM_INIT                  ((uint8)0)
    #define HWCOM_SET_SPEED             ((uint8)1)
    #define HWCOM_SET_BUFFER            ((uint8)2)
    #define HWCOM_FLUSH                 ((uint8)3)
    #define HWCOM_READY                 ((uint8)4)
    #define HWCOM_PUT                   ((uint8)5)
    #define HWCOM_SEND                  ((uint8)6)
    #define HWCOM_RXD                   ((uint8)7)
    #define HWCOM_GET                   ((uint8)8)
    #define HWCOM_CODE_MAX              HWCOM_GET

#define VM_SWCOM                        ( VM_CODE_B | 37 )
    #define SWCOM_INIT                  ((uint8)0)
    #define SWCOM_SET_SPEED             ((uint8)1)
    #define SWCOM_SET_BUFFER            ((uint8)2)
    #define SWCOM_FLUSH                 ((uint8)3)
    #define SWCOM_READY                 ((uint8)4)
    #define SWCOM_PUT                   ((uint8)5)
    #define SWCOM_SEND                  ((uint8)6)
    #define SWCOM_RXD                   ((uint8)7)
    #define SWCOM_GET                   ((uint8)8)
    #define SWCOM_CODE_MAX              SWCOM_GET

    #define BAUD_300                    ((uint8)0)
    #define BAUD_600                    ((uint8)1)
    #define BAUD_1200                   ((uint8)2)
    #define BAUD_2400                   ((uint8)3)
    #define BAUD_4800                   ((uint8)4)
    #define BAUD_9600                   ((uint8)5)
    #define BAUD_19200                  ((uint8)6)
    #define BAUD_38400                  ((uint8)7)
    #define BAUD_57600                  ((uint8)8)
    #define BAUD_115200                 ((uint8)9)
    #define BAUD_MAX                    BAUD_115200

#define VM_LPT                          ( VM_CODE_B | 38 )
    #define LPT_INIT                    ((uint8)0)
    #define LPT_FLUSH                   ((uint8)1)
    #define LPT_READY                   ((uint8)2)
    #define LPT_PUT                     ((uint8)3)
    #define LPT_PRINT                   ((uint8)4)
    #define LPT_CODE_MAX                LPT_PRINT

#define VM_CAN                          ( VM_CODE_B | 39 )
    #define CAN_INIT                    ((uint8)0)
    #define CAN_READY                   ((uint8)1)
    #define CAN_GET_ERROR               ((uint8)2)
    #define CAN_SEND                    ((uint8)3)
    #define CAN_PUBLISH                 ((uint8)4)
    #define CAN_GET_RTRCOUNT            ((uint8)5)
    #define CAN_EXPECT                  ((uint8)6)
    #define CAN_REQUEST                 ((uint8)7)
    #define CAN_RXD                     ((uint8)8)
    #define CAN_GET                     ((uint8)9)
    #define CAN_CODE_MAX                CAN_GET

#define VM_I2C                          ( VM_CODE_B | 40 )
    #define I2C_INIT                    ((uint8)0)
    #define I2C_START                   ((uint8)1)
    #define I2C_STOP                    ((uint8)2)
    #define I2C_WRITE                   ((uint8)3)
    #define I2C_READ                    ((uint8)4)
    #define I2C_READ_LAST               ((uint8)5)
    #define I2C_READY                   ((uint8)6)
    #define I2C_CODE_MAX                I2C_READY

#define VM_TWB                          ( VM_CODE_B | 41 )
    #define TWB_INIT                    ((uint8)0)
    #define TWB_IO                      ((uint8)1)
    #define TWB_RXD                     ((uint8)2)
    #define TWB_CODE_MAX                TWB_RXD

#define VM_LCD                          ( VM_CODE_B | 42 )
    #define LCD_INIT                    ((uint8)0)
    #define LCD_SHOW_CURSOR             ((uint8)1)
    #define LCD_CLEAR                   ((uint8)2)
    #define LCD_CLREOL                  ((uint8)3)
    #define LCD_GOTO                    ((uint8)4)
    #define LCD_HOME                    ((uint8)5)
    #define LCD_SCROLL                  ((uint8)6)
    #define LCD_READY                   ((uint8)7)
    #define LCD_PUT                     ((uint8)8)
    #define LCD_PRINT                   ((uint8)9)
    #define LCD_CODE_MAX                LCD_PRINT

/* !!!  ERWEITERUNGEN !!! */

#define VM_EEPROM                       ( VM_CODE_B | 43 )
    #define EEPROM_WRITE_BYTE           ((uint8)1)
    #define EEPROM_WRITE_INT            ((uint8)2)
    #define EEPROM_WRITE_LONG           ((uint8)3)
    #define EEPROM_WRITE_FLOAT          ((uint8)4)
    #define EEPROM_READ_BYTE            ((uint8)5)
    #define EEPROM_READ_INT             ((uint8)6)
    #define EEPROM_READ_LONG            ((uint8)7)
    #define EEPROM_READ_FLOAT           ((uint8)8)
    #define EEPROM_CODE_MAX             EEPROM_READ_FLOAT

#define VM_DEBUG                        (VM_CODE_B | 44)
    #define DEBUG_STOP                  ((uint8)1)
    #define DEBUG_MEMORY_USAGE          ((uint8)2)
#define DEBUG_CODE_MAX                  DEBUG_MEMORY_USAGE

/* --- VM_CODE_C ----------------------------------------------------- */

#define VM_NOP_C                        ( VM_CODE_C |  0 )

#define VM_CALL                         ( VM_CODE_C |  1 )
#define VM_RETURN                       ( VM_CODE_C |  2 )
#define VM_INC_SP                       ( VM_CODE_C |  3 )
#define VM_BRANCH                       ( VM_CODE_C |  4 )
#define VM_BRANCH_IF_ZERO               ( VM_CODE_C |  5 )

#define VM_LOAD_IMMEDIATE_INT           ( VM_CODE_C |  6 )

#define VM_LOAD_CONST_BYTE              ( VM_CODE_C |  7 )
#define VM_LOAD_CONST_INT               ( VM_CODE_C |  8 )
#define VM_LOAD_CONST_LONG              ( VM_CODE_C |  9 )
#define VM_LOAD_CONST_FLOAT             ( VM_CODE_C | 10 )

#define VM_LOAD_BYTE                    ( VM_CODE_C | 11 )
#define VM_LOAD_INT                     ( VM_CODE_C | 12 )
#define VM_LOAD_LONG                    ( VM_CODE_C | 13 )
#define VM_LOAD_FLOAT                   ( VM_CODE_C | 14 )
#define VM_LOAD_LOCAL_BYTE              ( VM_CODE_C | 15 )
#define VM_LOAD_LOCAL_INT               ( VM_CODE_C | 16 )
#define VM_LOAD_LOCAL_LONG              ( VM_CODE_C | 17 )
#define VM_LOAD_LOCAL_FLOAT             ( VM_CODE_C | 18 )

#define VM_STORE_BYTE                   ( VM_CODE_C | 19 )
#define VM_STORE_INT                    ( VM_CODE_C | 20 )
#define VM_STORE_LONG                   ( VM_CODE_C | 21 )
#define VM_STORE_FLOAT                  ( VM_CODE_C | 22 )
#define VM_STORE_LOCAL_BYTE             ( VM_CODE_C | 23 )
#define VM_STORE_LOCAL_INT              ( VM_CODE_C | 24 )
#define VM_STORE_LOCAL_LONG             ( VM_CODE_C | 25 )
#define VM_STORE_LOCAL_FLOAT            ( VM_CODE_C | 26 )

#define VM_STORE_KEEP_BYTE              ( VM_CODE_C | 27 )
#define VM_STORE_KEEP_INT               ( VM_CODE_C | 28 )
#define VM_STORE_KEEP_LONG              ( VM_CODE_C | 29 )
#define VM_STORE_KEEP_FLOAT             ( VM_CODE_C | 30 )
#define VM_STORE_KEEP_LOCAL_BYTE        ( VM_CODE_C | 31 )
#define VM_STORE_KEEP_LOCAL_INT         ( VM_CODE_C | 32 )
#define VM_STORE_KEEP_LOCAL_LONG        ( VM_CODE_C | 33 )
#define VM_STORE_KEEP_LOCAL_FLOAT       ( VM_CODE_C | 34 )

#define VM_INC_LOAD_BYTE                ( VM_CODE_C | 35 )
#define VM_INC_LOAD_INT                 ( VM_CODE_C | 36 )
#define VM_INC_LOAD_LONG                ( VM_CODE_C | 37 )
#define VM_INC_LOAD_FLOAT               ( VM_CODE_C | 38 )
#define VM_INC_LOAD_LOCAL_BYTE          ( VM_CODE_C | 39 )
#define VM_INC_LOAD_LOCAL_INT           ( VM_CODE_C | 40 )
#define VM_INC_LOAD_LOCAL_LONG          ( VM_CODE_C | 41 )
#define VM_INC_LOAD_LOCAL_FLOAT         ( VM_CODE_C | 42 )

/* -- VM_CODE_D ----------------------------------------------------- */

#define VM_NOP_D                        ( VM_CODE_D |  0 )

#define VM_RETURN_VALUE                 ( VM_CODE_D |  1 )
    #define RTYPE_INT                   ((uint8)0)
    #define RTYPE_LONG                  ((uint8)1)
    #define RTYPE_FLOAT                 ((uint8)2)

#define VM_LOAD_ABSOLUTE_BYTE           ( VM_CODE_D |  2 )
#define VM_LOAD_ABSOLUTE_INT            ( VM_CODE_D |  3 )
#define VM_LOAD_ABSOLUTE_LONG           ( VM_CODE_D |  4 )
#define VM_LOAD_ABSOLUTE_FLOAT          ( VM_CODE_D |  5 )

#define VM_STORE_ABSOLUTE_BYTE          ( VM_CODE_D |  6 )
#define VM_STORE_ABSOLUTE_INT           ( VM_CODE_D |  7 )
#define VM_STORE_ABSOLUTE_LONG          ( VM_CODE_D |  8 )
#define VM_STORE_ABSOLUTE_FLOAT         ( VM_CODE_D |  9 )

#define VM_INLINE_SYSCALL               ( VM_CODE_D | 10 )
#define VM_INLINE_SYSJUMP               ( VM_CODE_D | 11 )

#define VM_HOOK                         ( VM_CODE_D | 12 )
    #define HOOK_REPLACE                ((uint8)0)
    #define HOOK_BEFORE                 ((uint8)1)
    #define HOOK_AFTER                  ((uint8)2)

    #define HOOK_EVENT_TIMER            ((uint8)0)
    #define HOOK_EVENT_IRQPORT1         ((uint8)1)
    #define HOOK_EVENT_IRQPORT2         ((uint8)2)
    #define HOOK_EVENT_IRQPORT3         ((uint8)3)
    #define HOOK_EVENT_IRQPORT4         ((uint8)4)

#define VM_SAVE                         ( VM_CODE_D | 13 )
#define VM_RESTORE                      ( VM_CODE_D | 14 )

#define VM_CODE_INVALID                 ( VM_CODE_D | 63 )

#endif  /* __VMCODES_H */

