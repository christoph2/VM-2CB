#!/usr/bin/python
# -*- coding: latin-1 -*-

__version__ = "0.9.1"
__description__= ""
__copyright__ = """
   2-CB (C-Control-II kompatible Virtuelle Maschine).

  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
                                       cpu12.gems@googlemail.com>

   All Rights Reserved

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

ReverseDict = lambda d: dict([(value,key) for key,value in d.items()])

VM_CODE_A = 0x0000
VM_CODE_B = 0x0040
VM_CODE_C = 0x0080
VM_CODE_D = 0x00C0


#--- VM_CODE_A -----------------------------------------------------

VM_NOP_A                    = ( VM_CODE_A |  0 )

VM_QUIT                     = ( VM_CODE_A |  1 )
VM_YIELD                    = ( VM_CODE_A |  2 )
VM_SLEEP                    = ( VM_CODE_A |  3 )
VM_CAPTURE                  = ( VM_CODE_A |  4 )
VM_RELEASE                  = ( VM_CODE_A |  5 )

VM_FAST_RETURN              = ( VM_CODE_A |  6 )

VM_MAKE_GLOBAL_POINTER      = ( VM_CODE_A |  7 )

VM_LOAD_REF_CONST_BYTE      = ( VM_CODE_A |  8 )
VM_LOAD_REF_CONST_INT       = ( VM_CODE_A |  9 )
VM_LOAD_REF_CONST_LONG      = ( VM_CODE_A | 10 )
VM_LOAD_REF_CONST_FLOAT     = ( VM_CODE_A | 11 )

VM_LOAD_REF_BYTE            = ( VM_CODE_A | 12 )
VM_LOAD_REF_INT             = ( VM_CODE_A | 13 )
VM_LOAD_REF_LONG            = ( VM_CODE_A | 14 )
VM_LOAD_REF_FLOAT           = ( VM_CODE_A | 15 )

VM_INC_LOAD_REF_BYTE        = ( VM_CODE_A | 16 )
VM_INC_LOAD_REF_INT         = ( VM_CODE_A | 17 )
VM_INC_LOAD_REF_LONG        = ( VM_CODE_A | 18 )
VM_INC_LOAD_REF_FLOAT       = ( VM_CODE_A | 19 )

VM_STORE_REF_BYTE           = ( VM_CODE_A | 20 )
VM_STORE_REF_INT            = ( VM_CODE_A | 21 )
VM_STORE_REF_LONG           = ( VM_CODE_A | 22 )
VM_STORE_REF_FLOAT          = ( VM_CODE_A | 23 )

VM_CAST_INT_TO_LONG         = ( VM_CODE_A | 24 )
VM_CAST_INT_TO_FLOAT        = ( VM_CODE_A | 25 )
VM_CAST_LONG_TO_INT         = ( VM_CODE_A | 26 )
VM_CAST_LONG_TO_FLOAT       = ( VM_CODE_A | 27 )
VM_CAST_FLOAT_TO_INT        = ( VM_CODE_A | 28 )
VM_CAST_FLOAT_TO_LONG       = ( VM_CODE_A | 29 )

VM_INVERT_INT               = ( VM_CODE_A | 30 )
VM_INVERT_LONG              = ( VM_CODE_A | 31 )
VM_INVERT_FLOAT             = ( VM_CODE_A | 32 )
VM_NEG_INT                  = ( VM_CODE_A | 33 )
VM_NEG_LONG                 = ( VM_CODE_A | 34 )
VM_NEG_FLOAT                = ( VM_CODE_A | 35 )
VM_ABS_INT                  = ( VM_CODE_A | 36 )
VM_ABS_LONG                 = ( VM_CODE_A | 37 )
VM_ABS_FLOAT                = ( VM_CODE_A | 38 )

VM_PUT_INT                  = ( VM_CODE_A | 39 )
VM_PUT_LONG                 = ( VM_CODE_A | 40 )
VM_PUT_FLOAT                = ( VM_CODE_A | 41 )
VM_GET_INT                  = ( VM_CODE_A | 42 )
VM_GET_LONG                 = ( VM_CODE_A | 43 )
VM_GET_FLOAT                = ( VM_CODE_A | 44 )

VM_GET_SINGLE_PORT          = ( VM_CODE_A | 45 )
VM_GET_NIBBLE_PORT          = ( VM_CODE_A | 46 )
VM_GET_BYTE_PORT            = ( VM_CODE_A | 47 )
VM_GET_WORD_PORT            = ( VM_CODE_A | 48 )
VM_GET_ADC_PORT             = ( VM_CODE_A | 49 )

VM_SET_SINGLE_PORT          = ( VM_CODE_A | 50 )
VM_SET_NIBBLE_PORT          = ( VM_CODE_A | 51 )
VM_SET_BYTE_PORT            = ( VM_CODE_A | 52 )
VM_SET_WORD_PORT            = ( VM_CODE_A | 53 )

VM_DEACT_SINGLE_PORT        = ( VM_CODE_A | 54 )
VM_DEACT_NIBBLE_PORT        = ( VM_CODE_A | 55 )
VM_DEACT_BYTE_PORT          = ( VM_CODE_A | 56 )
VM_DEACT_WORD_PORT          = ( VM_CODE_A | 57 )

VM_TOGGLE_SINGLE_PORT       = ( VM_CODE_A | 58 )
VM_PULSE_SINGLE_PORT        = ( VM_CODE_A | 59 )

VM_GET_COUNT                = ( VM_CODE_A | 60 )
VM_GET_FREQ                 = ( VM_CODE_A | 61 )

VM_SYSCALL                  = ( VM_CODE_A | 62 )
VM_SYSJUMP                  = ( VM_CODE_A | 63 )


#--- VM_CODE_B -----------------------------------------------------

VM_NOP_B                    = ( VM_CODE_B |  0 )

VM_RESET                    = ( VM_CODE_B |  1 )
VM_RUN                      = ( VM_CODE_B |  2 )
VM_RESUME                   = ( VM_CODE_B |  3 )

VM_LOAD_IMMEDIATE_BYTE      = ( VM_CODE_B |  4 )

VM_ADD                      = ( VM_CODE_B |  5 )
VM_SUB                      = ( VM_CODE_B |  6 )
VM_MUL                      = ( VM_CODE_B |  7 )
VM_DIV                      = ( VM_CODE_B |  8 )
VM_MOD                      = ( VM_CODE_B |  9 )
VM_EQU                      = ( VM_CODE_B | 10 )
VM_NEQU                     = ( VM_CODE_B | 11 )
VM_HI                       = ( VM_CODE_B | 12 )
VM_HIS                      = ( VM_CODE_B | 13 )
VM_LO                       = ( VM_CODE_B | 14 )
VM_LOS                      = ( VM_CODE_B | 15 )
VM_AND                      = ( VM_CODE_B | 16 )
VM_NAND                     = ( VM_CODE_B | 17 )
VM_OR                       = ( VM_CODE_B | 18 )
VM_NOR                      = ( VM_CODE_B | 19 )
VM_XOR                      = ( VM_CODE_B | 20 )
VM_NXOR                     = ( VM_CODE_B | 21 )
VM_SHL                      = ( VM_CODE_B | 22 )
VM_SHR                      = ( VM_CODE_B | 23 )
VM_ASR                      = ( VM_CODE_B | 24 )
VM_ROL                      = ( VM_CODE_B | 25 )
VM_ROR                      = ( VM_CODE_B | 26 )
VM_MIN                      = ( VM_CODE_B | 27 )
VM_MAX                      = ( VM_CODE_B | 28 )

CALC_INT_INT              = 0
CALC_INT_LONG             = 1
CALC_INT_FLOAT            = 2
CALC_LONG_INT             = 3
CALC_LONG_LONG            = 4
CALC_LONG_FLOAT           = 5
CALC_FLOAT_INT            = 6
CALC_FLOAT_LONG           = 7
CALC_FLOAT_FLOAT          = 8


VM_MATH_FUNCTION            = ( VM_CODE_B | 29 )

MATH_SQR                  = 0
MATH_SQRT                 = 1
MATH_CURT                 = 2
MATH_SIN                  = 3
MATH_COS                  = 4
MATH_TAN                  = 5
MATH_ASIN                 = 6
MATH_ACOS                 = 7
MATH_ATAN                 = 8
MATH_LOG                  = 9
MATH_LN                   = 10
MATH_EXP                  = 11
MATH_POW                  = 12
MATH_CEIL                 = 13
MATH_FLOOR                = 14


VM_LOAD_SYSVAR_INT          = ( VM_CODE_B | 30 )
VM_STORE_SYSVAR_INT         = ( VM_CODE_B | 31 )
VM_LOAD_SYSVAR_LONG         = ( VM_CODE_B | 32 )
VM_STORE_SYSVAR_LONG        = ( VM_CODE_B | 33 )

ISYSVAR_YEAR              = 0
ISYSVAR_MONTH             = 1
ISYSVAR_DAY               = 2
ISYSVAR_HOUR              = 3
ISYSVAR_MINUTE            = 4
ISYSVAR_SECOND            = 5
ISYSVAR_DOW               = 6
ISYSVAR_DST               = 7
ISYSVAR_ZONE              = 8
ISYSVAR_DCF_ERRCNT        = 9

LSYSVAR_TIMER_MS          = 0
LSYSVAR_CNT_1             = 1
LSYSVAR_CNT_2             = 2
LSYSVAR_CNT_3             = 3
LSYSVAR_CNT_4             = 4
LSYSVAR_FREQ1             = 5
LSYSVAR_FREQ2             = 6


VM_STRING                   = ( VM_CODE_B | 34 )

STRING_CLEAR               = 0
STRING_GET_LENGTH          = 1
STRING_FILL                = 2
STRING_PUT_CHAR            = 3
STRING_PUT_STRING          = 4
STRING_PUT_CONST_STRING    = 5
STRING_PUT_INT             = 6
STRING_PUT_LONG            = 7
STRING_PUT_FLOAT           = 8
STRING_PUT_FORMATTED_INT   = 9
STRING_PUT_FORMATTED_LONG  = 10
STRING_PUT_FORMATTED_FLOAT = 11
STRING_PUT_BYTE_MASK       = 12


VM_PLM                      = ( VM_CODE_B | 35 )

PLM_INIT                  = 0
PLM_SET_TIMEBASE          = 1
PLM_SET_PORTMODE          = 2
PLM_SET_PERIODLENGTH      = 3
PLM_OUT                   = 4
PLM_BEEP                  = 5

VM_HWCOM                    = ( VM_CODE_B | 36 )

HWCOM_INIT                = 0
HWCOM_SET_SPEED           = 1
HWCOM_SET_BUFFER          = 2
HWCOM_FLUSH               = 3
HWCOM_READY               = 4
HWCOM_PUT                 = 5
HWCOM_SEND                = 6
HWCOM_RXD                 = 7
HWCOM_GET                 = 8

VM_SWCOM                    = ( VM_CODE_B | 37 )

SWCOM_INIT                = 0
SWCOM_SET_SPEED           = 1
SWCOM_SET_BUFFER          = 2
SWCOM_FLUSH               = 3
SWCOM_READY               = 4
SWCOM_PUT                 = 5
SWCOM_SEND                = 6
SWCOM_RXD                 = 7
SWCOM_GET                 = 8

VM_LPT                      = ( VM_CODE_B | 38 )

LPT_INIT                  = 0
LPT_FLUSH                 = 1
LPT_READY                 = 2
LPT_PUT                   = 3
LPT_PRINT                 = 4

VM_CAN                      = ( VM_CODE_B | 39 )

CAN_INIT                  = 0
CAN_READY                 = 1
CAN_GET_ERROR             = 2
CAN_SEND                  = 3
CAN_PUBLISH               = 4
CAN_GET_RTRCOUNT          = 5
CAN_EXPECT                = 6
CAN_REQUEST               = 7
CAN_RXD                   = 8
CAN_GET                   = 9

VM_I2C                      = ( VM_CODE_B | 40 )

I2C_INIT                  = 0
I2C_START                 = 1
I2C_STOP                  = 2
I2C_WRITE                 = 3
I2C_READ                  = 4
I2C_READ_LAST             = 5
I2C_READY                 = 6

VM_TWB                      = ( VM_CODE_B | 41 )

TWB_INIT                  = 0
TWB_IO                    = 1
TWB_RXD                   = 2

VM_LCD                      = ( VM_CODE_B | 42 )

LCD_INIT                  = 0
LCD_SHOW_CURSOR           = 1
LCD_CLEAR                 = 2
LCD_CLREOL                = 3
LCD_GOTO                  = 4
LCD_HOME                  = 5
LCD_SCROLL                = 6
LCD_READY                 = 7
LCD_PUT                   = 8
LCD_PRINT                 = 9


#--- VM_CODE_C -----------------------------------------------------

VM_NOP_C                    = ( VM_CODE_C |  0 )

VM_CALL                     = ( VM_CODE_C |  1 )
VM_RETURN                   = ( VM_CODE_C |  2 )
VM_INC_SP                   = ( VM_CODE_C |  3 )
VM_BRANCH                   = ( VM_CODE_C |  4 )
VM_BRANCH_IF_ZERO           = ( VM_CODE_C |  5 )

VM_LOAD_IMMEDIATE_INT       = ( VM_CODE_C |  6 )

VM_LOAD_CONST_BYTE          = ( VM_CODE_C |  7 )
VM_LOAD_CONST_INT           = ( VM_CODE_C |  8 )
VM_LOAD_CONST_LONG          = ( VM_CODE_C |  9 )
VM_LOAD_CONST_FLOAT         = ( VM_CODE_C | 10 )

VM_LOAD_BYTE                = ( VM_CODE_C | 11 )
VM_LOAD_INT                 = ( VM_CODE_C | 12 )
VM_LOAD_LONG                = ( VM_CODE_C | 13 )
VM_LOAD_FLOAT               = ( VM_CODE_C | 14 )
VM_LOAD_LOCAL_BYTE          = ( VM_CODE_C | 15 )
VM_LOAD_LOCAL_INT           = ( VM_CODE_C | 16 )
VM_LOAD_LOCAL_LONG          = ( VM_CODE_C | 17 )
VM_LOAD_LOCAL_FLOAT         = ( VM_CODE_C | 18 )

VM_STORE_BYTE               = ( VM_CODE_C | 19 )
VM_STORE_INT                = ( VM_CODE_C | 20 )
VM_STORE_LONG               = ( VM_CODE_C | 21 )
VM_STORE_FLOAT              = ( VM_CODE_C | 22 )
VM_STORE_LOCAL_BYTE         = ( VM_CODE_C | 23 )
VM_STORE_LOCAL_INT          = ( VM_CODE_C | 24 )
VM_STORE_LOCAL_LONG         = ( VM_CODE_C | 25 )
VM_STORE_LOCAL_FLOAT        = ( VM_CODE_C | 26 )

VM_STORE_KEEP_BYTE          = ( VM_CODE_C | 27 )
VM_STORE_KEEP_INT           = ( VM_CODE_C | 28 )
VM_STORE_KEEP_LONG          = ( VM_CODE_C | 29 )
VM_STORE_KEEP_FLOAT         = ( VM_CODE_C | 30 )
VM_STORE_KEEP_LOCAL_BYTE    = ( VM_CODE_C | 31 )
VM_STORE_KEEP_LOCAL_INT     = ( VM_CODE_C | 32 )
VM_STORE_KEEP_LOCAL_LONG    = ( VM_CODE_C | 33 )
VM_STORE_KEEP_LOCAL_FLOAT   = ( VM_CODE_C | 34 )

VM_INC_LOAD_BYTE            = ( VM_CODE_C | 35 )
VM_INC_LOAD_INT             = ( VM_CODE_C | 36 )
VM_INC_LOAD_LONG            = ( VM_CODE_C | 37 )
VM_INC_LOAD_FLOAT           = ( VM_CODE_C | 38 )
VM_INC_LOAD_LOCAL_BYTE      = ( VM_CODE_C | 39 )
VM_INC_LOAD_LOCAL_INT       = ( VM_CODE_C | 40 )
VM_INC_LOAD_LOCAL_LONG      = ( VM_CODE_C | 41 )
VM_INC_LOAD_LOCAL_FLOAT     = ( VM_CODE_C | 42 )


#--- VM_CODE_D -----------------------------------------------------

VM_NOP_D                    = ( VM_CODE_D |  0 )

VM_RETURN_VALUE             = ( VM_CODE_D |  1 )

RTYPE_INT                 = 0x0000
RTYPE_LONG                = 0x0100
RTYPE_FLOAT               = 0x0200

VM_LOAD_ABSOLUTE_BYTE       = ( VM_CODE_D |  2 )
VM_LOAD_ABSOLUTE_INT        = ( VM_CODE_D |  3 )
VM_LOAD_ABSOLUTE_LONG       = ( VM_CODE_D |  4 )
VM_LOAD_ABSOLUTE_FLOAT      = ( VM_CODE_D |  5 )

VM_STORE_ABSOLUTE_BYTE      = ( VM_CODE_D |  6 )
VM_STORE_ABSOLUTE_INT       = ( VM_CODE_D |  7 )
VM_STORE_ABSOLUTE_LONG      = ( VM_CODE_D |  8 )
VM_STORE_ABSOLUTE_FLOAT     = ( VM_CODE_D |  9 )

VM_INLINE_SYSCALL           = ( VM_CODE_D | 10 )
VM_INLINE_SYSJUMP           = ( VM_CODE_D | 11 )

VM_HOOK                     = ( VM_CODE_D | 12 )

HOOK_REPLACE              = 0
HOOK_BEFORE               = 1
HOOK_AFTER                = 2

HOOK_EVENT_TIMER          = 0
HOOK_EVENT_IRQPORT1       = 1
HOOK_EVENT_IRQPORT2       = 2
HOOK_EVENT_IRQPORT3       = 3
HOOK_EVENT_IRQPORT4       = 4

VM_SAVE                     = ( VM_CODE_D | 13 )
VM_RESTORE                  = ( VM_CODE_D | 14 )


VM_CODE_INVALID             = ( VM_CODE_D | 63 )


VmcA = {
    VM_NOP_A:                   "NOP_A",
    VM_QUIT:                    "QUIT",
    VM_YIELD:                   "YIELD",
    VM_SLEEP:                   "SLEEP",
    VM_CAPTURE:                 "CAPTURE",
    VM_RELEASE:                 "RELEASE",
    VM_FAST_RETURN:             "FAST_RETURN",
    VM_MAKE_GLOBAL_POINTER:     "MAKE_GLOBAL_POINTER",
    VM_LOAD_REF_CONST_BYTE:     "LOAD_REF_CONST_BYTE",
    VM_LOAD_REF_CONST_INT:      "LOAD_REF_CONST_INT",
    VM_LOAD_REF_CONST_LONG:     "LOAD_REF_CONST_LONG",
    VM_LOAD_REF_CONST_FLOAT:    "LOAD_REF_CONST_FLOAT",
    VM_LOAD_REF_BYTE:           "LOAD_REF_BYTE",
    VM_LOAD_REF_INT:            "LOAD_REF_INT",
    VM_LOAD_REF_LONG:           "LOAD_REF_LONG",
    VM_LOAD_REF_FLOAT:          "LOAD_REF_FLOAT",
    VM_INC_LOAD_REF_BYTE:       "INC_LOAD_REF_BYTE",
    VM_INC_LOAD_REF_INT:        "INC_LOAD_REF_INT",
    VM_INC_LOAD_REF_LONG:       "INC_LOAD_REF_LONG",
    VM_INC_LOAD_REF_FLOAT:      "INC_LOAD_REF_FLOAT",
    VM_STORE_REF_BYTE:          "STORE_REF_BYTE",
    VM_STORE_REF_INT:           "STORE_REF_INT",
    VM_STORE_REF_LONG:          "STORE_REF_LONG",
    VM_STORE_REF_FLOAT:         "STORE_REF_FLOAT",
    VM_CAST_INT_TO_LONG:        "CAST_INT_TO_LONG",
    VM_CAST_INT_TO_FLOAT:       "CAST_INT_TO_FLOAT",
    VM_CAST_LONG_TO_INT:        "CAST_LONG_TO_INT",
    VM_CAST_LONG_TO_FLOAT:      "CAST_LONG_TO_FLOAT",
    VM_CAST_FLOAT_TO_INT:       "CAST_FLOAT_TO_INT",
    VM_CAST_FLOAT_TO_LONG:      "CAST_FLOAT_TO_LONG",
    VM_INVERT_INT:              "INVERT_INT",
    VM_INVERT_LONG:             "INVERT_LONG",
    VM_INVERT_FLOAT:            "INVERT_FLOAT",
    VM_NEG_INT:                 "NEG_INT",
    VM_NEG_LONG:                "NEG_LONG",
    VM_NEG_FLOAT:               "NEG_FLOAT",
    VM_ABS_INT:                 "ABS_INT",
    VM_ABS_LONG:                "ABS_LONG",
    VM_ABS_FLOAT:               "ABS_FLOAT",
    VM_PUT_INT:                 "PUT_INT",
    VM_PUT_LONG:                "PUT_LONG",
    VM_PUT_FLOAT:               "PUT_FLOAT",
    VM_GET_INT:                 "GET_INT",
    VM_GET_LONG:                "GET_LONG",
    VM_GET_FLOAT:               "GET_FLOAT",
    VM_GET_SINGLE_PORT:         "GET_SINGLE_PORT",
    VM_GET_NIBBLE_PORT:         "GET_NIBBLE_PORT",
    VM_GET_BYTE_PORT:           "GET_BYTE_PORT",
    VM_GET_WORD_PORT:           "GET_WORD_PORT",
    VM_GET_ADC_PORT:            "GET_ADC_PORT",
    VM_SET_SINGLE_PORT:         "SET_SINGLE_PORT",
    VM_SET_NIBBLE_PORT:         "SET_NIBBLE_PORT",
    VM_SET_BYTE_PORT:           "SET_BYTE_PORT",
    VM_SET_WORD_PORT:           "SET_WORD_PORT",
    VM_DEACT_SINGLE_PORT:       "DEACT_SINGLE_PORT",
    VM_DEACT_NIBBLE_PORT:       "DEACT_NIBBLE_PORT",
    VM_DEACT_BYTE_PORT:         "DEACT_BYTE_PORT",
    VM_DEACT_WORD_PORT:         "DEACT_WORD_PORT",
    VM_TOGGLE_SINGLE_PORT:      "TOGGLE_SINGLE_PORT",
    VM_PULSE_SINGLE_PORT:       "PULSE_SINGLE_PORT",
    VM_GET_COUNT:               "GET_COUNT",
    VM_GET_FREQ:                "GET_FREQ",
    VM_SYSCALL:                 "SYSCALL",
    VM_SYSJUMP:                 "SYSJUMP"
}

VmcAR = ReverseDict(VmcA)

VmcB = {
    VM_NOP_B:                   "NOP_B",
    VM_RESET:                   "RESET",
    VM_RUN:                     "RUN",
    VM_RESUME:                  "RESUME",
    VM_LOAD_IMMEDIATE_BYTE:     "LOAD_IMMEDIATE_BYTE",
    VM_ADD:                     "ADD",
    VM_SUB:                     "SUB",
    VM_MUL:                     "MUL",
    VM_DIV:                     "DIV",
    VM_MOD:                     "MOD",
    VM_EQU:                     "EQU",
    VM_NEQU:                    "NEQU",
    VM_HI:                      "HI",
    VM_HIS:                     "HIS",
    VM_LO:                      "LO",
    VM_LOS:                     "LOS",
    VM_AND:                     "AND",
    VM_NAND:                    "NAND",
    VM_OR:                      "OR",
    VM_NOR:                     "NOR",
    VM_XOR:                     "XOR",
    VM_NXOR:                    "NXOR",
    VM_SHL:                     "SHL",
    VM_SHR:                     "SHR",
    VM_ASR:                     "ASR",
    VM_ROL:                     "ROL",
    VM_ROR:                     "ROR",
    VM_MIN:                     "MIN",
    VM_MAX:                     "MAX",
    VM_MATH_FUNCTION:           "MATH_FUNCTION",
    VM_LOAD_SYSVAR_INT:         "LOAD_SYSVAR_INT",
    VM_STORE_SYSVAR_INT:        "STORE_SYSVAR_INT",
    VM_LOAD_SYSVAR_LONG:        "LOAD_SYSVAR_LONG",
    VM_STORE_SYSVAR_LONG:       "STORE_SYSVAR_LONG",
    VM_STRING:                  "STRING",
    VM_PLM:                     "PLM",
    VM_HWCOM:                   "HWCOM",
    VM_SWCOM:                   "SWCOM",
    VM_LPT:                     "LPT",
    VM_CAN:                     "CAN",
    VM_I2C:                     "I2C",
    VM_TWB:                     "TWB",
    VM_LCD:                     "LCD",
}

VmcBR = ReverseDict(VmcB)

VmcC = {
    VM_NOP_C:                   "NOP_C",
    VM_CALL:                    "CALL",
    VM_RETURN:                  "RETURN",
    VM_INC_SP:                  "INC_SP",
    VM_BRANCH:                  "BRANCH",
    VM_BRANCH_IF_ZERO:          "BRANCH_IF_ZERO",
    VM_LOAD_IMMEDIATE_INT:      "LOAD_IMMEDIATE_INT",
    VM_LOAD_CONST_BYTE:         "LOAD_CONST_BYTE",
    VM_LOAD_CONST_INT:          "LOAD_CONST_INT",
    VM_LOAD_CONST_LONG:         "LOAD_CONST_LONG",
    VM_LOAD_CONST_FLOAT:        "LOAD_CONST_FLOAT",
    VM_LOAD_BYTE:               "LOAD_BYTE",
    VM_LOAD_INT:                "LOAD_INT",
    VM_LOAD_LONG:               "LOAD_LONG",
    VM_LOAD_FLOAT:              "LOAD_FLOAT",
    VM_LOAD_LOCAL_BYTE:         "LOAD_LOCAL_BYTE",
    VM_LOAD_LOCAL_INT:          "LOAD_LOCAL_INT",
    VM_LOAD_LOCAL_LONG:         "LOAD_LOCAL_LONG",
    VM_LOAD_LOCAL_FLOAT:        "LOAD_LOCAL_FLOAT",
    VM_STORE_BYTE:              "STORE_BYTE",
    VM_STORE_INT:               "STORE_INT",
    VM_STORE_LONG:              "STORE_LONG",
    VM_STORE_FLOAT:             "STORE_FLOAT",
    VM_STORE_LOCAL_BYTE:        "STORE_LOCAL_BYTE",
    VM_STORE_LOCAL_INT:         "STORE_LOCAL_INT",
    VM_STORE_LOCAL_LONG:        "STORE_LOCAL_LONG",
    VM_STORE_LOCAL_FLOAT:       "STORE_LOCAL_FLOAT",
    VM_STORE_KEEP_BYTE:         "STORE_KEEP_BYTE",
    VM_STORE_KEEP_INT:          "STORE_KEEP_INT",
    VM_STORE_KEEP_LONG:         "STORE_KEEP_LONG",
    VM_STORE_KEEP_FLOAT:        "STORE_KEEP_FLOAT",
    VM_STORE_KEEP_LOCAL_BYTE:   "STORE_KEEP_LOCAL_BYTE",
    VM_STORE_KEEP_LOCAL_INT:    "STORE_KEEP_LOCAL_INT",
    VM_STORE_KEEP_LOCAL_LONG:   "STORE_KEEP_LOCAL_LONG",
    VM_STORE_KEEP_LOCAL_FLOAT:  "STORE_KEEP_LOCAL_FLOAT",
    VM_INC_LOAD_BYTE:           "INC_LOAD_BYTE",
    VM_INC_LOAD_INT:            "INC_LOAD_INT",
    VM_INC_LOAD_LONG:           "INC_LOAD_LONG",
    VM_INC_LOAD_FLOAT:          "INC_LOAD_FLOAT",
    VM_INC_LOAD_LOCAL_BYTE:     "INC_LOAD_LOCAL_BYTE",
    VM_INC_LOAD_LOCAL_INT:      "INC_LOAD_LOCAL_INT",
    VM_INC_LOAD_LOCAL_LONG:     "INC_LOAD_LOCAL_LONG",
    VM_INC_LOAD_LOCAL_FLOAT:    "INC_LOAD_LOCAL_FLOAT",
}

VmcCR = ReverseDict(VmcC)

VmcD = {
VM_NOP_D:                       "NOP_D",
VM_RETURN_VALUE:                "RETURN_VALUE",

#  RTYPE_INT
#  RTYPE_LONG
#  RTYPE_FLOAT

VM_LOAD_ABSOLUTE_BYTE:          "LOAD_ABSOLUTE_BYTE",
VM_LOAD_ABSOLUTE_INT:           "LOAD_ABSOLUTE_INT",
VM_LOAD_ABSOLUTE_LONG:          "LOAD_ABSOLUTE_LONG",
VM_LOAD_ABSOLUTE_FLOAT:         "LOAD_ABSOLUTE_FLOAT",
VM_STORE_ABSOLUTE_BYTE:         "STORE_ABSOLUTE_BYTE",
VM_STORE_ABSOLUTE_INT:          "STORE_ABSOLUTE_INT",
VM_STORE_ABSOLUTE_LONG:         "STORE_ABSOLUTE_LONG",
VM_STORE_ABSOLUTE_FLOAT:        "STORE_ABSOLUTE_FLOAT",
VM_INLINE_SYSCALL:              "INLINE_SYSCALL",
VM_INLINE_SYSJUMP:              "INLINE_SYSJUMP",
VM_HOOK:                        "HOOK",

#  HOOK_REPLACE
#  HOOK_BEFORE
#  HOOK_AFTER

#  HOOK_EVENT_TIMER
#  HOOK_EVENT_IRQPORT1
#  HOOK_EVENT_IRQPORT2
#  HOOK_EVENT_IRQPORT3
#  HOOK_EVENT_IRQPORT4

VM_SAVE:                        "SAVE",
VM_RESTORE:                     "RESTORE",
VM_CODE_INVALID:                "CODE_INVALID",
}

VmcDR = ReverseDict(VmcD)

CALC    = 1000
ISYSVAR = 1001
LSYSVAR = 1002

SubFunctions = {
    VM_MATH_FUNCTION: {
        MATH_SQR:                   "SQR",
        MATH_SQRT:                  "SQRT",
        MATH_CURT:                  "CURT",
        MATH_SIN:                   "SIN",
        MATH_COS:                   "COS",
        MATH_TAN:                   "TAN",
        MATH_ASIN:                  "ASIN",
        MATH_ACOS:                  "ACOS",
        MATH_ATAN:                  "ATAN",
        MATH_LOG:                   "LOG",
        MATH_LN:                    "LN",
        MATH_EXP:                   "EXP",
        MATH_POW:                   "POW",
        MATH_CEIL:                  "CEIL",
        MATH_FLOOR:                 "FLOOR",
    },

    VM_STRING:  {
        STRING_CLEAR:               "STRING_CLEAR",
        STRING_GET_LENGTH:          "STRING_GET_LENGTH",
        STRING_FILL:                "STRING_FILL",
        STRING_PUT_CHAR:            "STRING_PUT_CHAR",
        STRING_PUT_STRING:          "STRING_PUT_STRING",
        STRING_PUT_CONST_STRING:    "STRING_PUT_CONST_STRING",
        STRING_PUT_INT:             "STRING_PUT_INT",
        STRING_PUT_LONG:            "STRING_PUT_LONG",
        STRING_PUT_FLOAT:           "STRING_PUT_FLOAT",
        STRING_PUT_FORMATTED_INT:   "STRING_PUT_FORMATTED_INT",
        STRING_PUT_FORMATTED_LONG:  "STRING_PUT_FORMATTED_LONG",
        STRING_PUT_FORMATTED_FLOAT: "STRING_PUT_FORMATTED_FLOAT",
        STRING_PUT_BYTE_MASK:       "STRING_PUT_BYTE_MASK",
    },

    VM_PLM: {
        PLM_INIT:                   "PLM_INIT",
        PLM_SET_TIMEBASE:           "PLM_SET_TIMEBASE",
        PLM_SET_PORTMODE:           "PLM_SET_PORTMODE",
        PLM_SET_PERIODLENGTH:       "PLM_SET_PERIODLENGTH",
        PLM_OUT:                    "PLM_OUT",
        PLM_BEEP:                   "PLM_BEEP",
    },

    VM_HWCOM: {
        HWCOM_INIT:                 "HWCOM_INIT",
        HWCOM_SET_SPEED:            "HWCOM_SET_SPEED",
        HWCOM_SET_BUFFER:           "HWCOM_SET_BUFFER",
        HWCOM_FLUSH:                "HWCOM_FLUSH",
        HWCOM_READY:                "HWCOM_READY",
        HWCOM_PUT:                  "HWCOM_PUT",
        HWCOM_SEND:                 "HWCOM_SEND",
        HWCOM_RXD:                  "HWCOM_RXD",
        HWCOM_GET:                  "HWCOM_GET",
    },

    VM_SWCOM: {
        SWCOM_INIT:                 "SWCOM_INIT",
        SWCOM_SET_SPEED:            "SWCOM_SET_SPEED",
        SWCOM_SET_BUFFER:           "SWCOM_SET_BUFFER",
        SWCOM_FLUSH:                "SWCOM_FLUSH",
        SWCOM_READY:                "SWCOM_READY",
        SWCOM_PUT:                  "SWCOM_PUT",
        SWCOM_SEND:                 "SWCOM_SEND",
        SWCOM_RXD:                  "SWCOM_RXD",
        SWCOM_GET:                  "SWCOM_GET",
    },

    VM_LPT: {
        LPT_INIT:                   "LPT_INIT",
        LPT_FLUSH:                  "LPT_FLUSH",
        LPT_READY:                  "LPT_READY",
        LPT_PUT:                    "LPT_PUT",
    },

    VM_CAN: {
       CAN_INIT:                    "CAN_INIT",
       CAN_READY:                   "CAN_READY",
       CAN_GET_ERROR:               "CAN_GET_ERROR",
       CAN_SEND:                    "CAN_SEND",
       CAN_PUBLISH:                 "CAN_PUBLISH",
       CAN_GET_RTRCOUNT:            "CAN_GET_RTRCOUNT",
       CAN_EXPECT:                  "CAN_EXPECT",
       CAN_REQUEST:                 "CAN_REQUEST",
       CAN_RXD:                     "CAN_RXD",
       CAN_GET:                     "CAN_GET",
    },

    VM_I2C: {
        I2C_INIT:                   "I2C_INIT",
        I2C_START:                  "I2C_START",
        I2C_STOP:                   "I2C_STOP",
        I2C_WRITE:                  "I2C_WRITE",
        I2C_READ:                   "I2C_READ",
        I2C_READ_LAST:              "I2C_READ_LAST",
        I2C_READY:                  "I2C_READY",
    },

    VM_TWB: {
        TWB_INIT:                   "TWB_INIT",
        TWB_IO:                     "TWB_IO",
        TWB_RXD:                    "TWB_RXD",
    },

    VM_LCD: {
       LCD_INIT:                    "LCD_INIT",
       LCD_SHOW_CURSOR:             "LCD_SHOW_CURSOR",
       LCD_CLEAR:                   "LCD_CLEAR",
       LCD_CLREOL:                  "LCD_CLREOL",
       LCD_GOTO:                    "LCD_GOTO",
       LCD_HOME:                    "LCD_HOME",
       LCD_SCROLL:                  "LCD_SCROLL",
       LCD_READY:                   "LCD_READY",
       LCD_PUT:                     "LCD_PUT",
       LCD_PRINT:                   "LCD_PRINT",
    },
    ##
    ##
    ##
    CALC: {
       CALC_INT_INT:                "CALC_INT_INT",
       CALC_INT_LONG:               "CALC_INT_LONG",
       CALC_INT_FLOAT:              "CALC_INT_FLOAT",
       CALC_LONG_INT:               "CALC_LONG_INT",
       CALC_LONG_LONG:              "CALC_LONG_LONG",
       CALC_LONG_FLOAT:             "CALC_LONG_FLOAT",
       CALC_FLOAT_INT:              "CALC_FLOAT_INT",
       CALC_FLOAT_LONG:             "CALC_FLOAT_LONG",
       CALC_FLOAT_FLOAT:            "CALC_FLOAT_FLOAT",
    },

    ISYSVAR: {
        ISYSVAR_YEAR:               "ISYSVAR_YEAR",
        ISYSVAR_MONTH:              "ISYSVAR_MONTH",
        ISYSVAR_DAY:                "ISYSVAR_DAY",
        ISYSVAR_HOUR:               "ISYSVAR_HOUR",
        ISYSVAR_MINUTE:             "ISYSVAR_MINUTE",
        ISYSVAR_SECOND:             "ISYSVAR_SECOND",
        ISYSVAR_DOW:                "ISYSVAR_DOW",
        ISYSVAR_DST:                "ISYSVAR_DST",
        ISYSVAR_ZONE:               "ISYSVAR_ZONE",
        ISYSVAR_DCF_ERRCNT:         "ISYSVAR_DCF_ERRCNT",
    },

    LSYSVAR: {
        LSYSVAR_TIMER_MS:           "LSYSVAR_TIMER_MS",
        LSYSVAR_CNT_1:              "LSYSVAR_CNT_1",
        LSYSVAR_CNT_2:              "LSYSVAR_CNT_2",
        LSYSVAR_CNT_3:              "LSYSVAR_CNT_3",
        LSYSVAR_CNT_4:              "LSYSVAR_CNT_4",
        LSYSVAR_FREQ1:              "LSYSVAR_FREQ1",
        LSYSVAR_FREQ2:              "LSYSVAR_FREQ2",
    },

}

Multiple = {
    VM_ADD:                 CALC,
    VM_SUB:                 CALC,
    VM_MUL:                 CALC,
    VM_DIV:                 CALC,
    VM_MOD:                 CALC,
    VM_EQU:                 CALC,
    VM_NEQU:                CALC,
    VM_HI:                  CALC,
    VM_HIS:                 CALC,
    VM_LO:                  CALC,
    VM_LOS:                 CALC,
    VM_AND:                 CALC,
    VM_NAND:                CALC,
    VM_OR:                  CALC,
    VM_NOR:                 CALC,
    VM_XOR:                 CALC,
    VM_NXOR:                CALC,
    VM_SHL:                 CALC,
    VM_SHR:                 CALC,
    VM_ASR:                 CALC,
    VM_ROL:                 CALC,
    VM_ROR:                 CALC,
    VM_MIN:                 CALC,
    VM_MAX:                 CALC,

    VM_LOAD_SYSVAR_INT:     ISYSVAR,
    VM_STORE_SYSVAR_INT:    ISYSVAR,
    VM_LOAD_SYSVAR_LONG:    LSYSVAR,
    VM_STORE_SYSVAR_LONG:   LSYSVAR,


}

