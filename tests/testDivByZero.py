#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import vm_al as v

CALC_INT_INT     = 0
CALC_INT_LONG    = 1
CALC_INT_FLOAT   = 2
CALC_LONG_INT    = 3
CALC_LONG_LONG   = 4
CALC_LONG_FLOAT  = 5
CALC_FLOAT_INT   = 6
CALC_FLOAT_LONG  = 7
CALC_FLOAT_FLOAT = 8

ERROR_DIV0       = 0x04 # s. VM_Excp.h

mem = v.byteArray(64)
v.setRAMPointer(mem)


class TestDivByZero(unittest.TestCase):
    def testIntInt(self):
        v.setOperandB(CALC_INT_INT)
        v.VM_PushW(0)
        v.VM_PushW(1)
        v.VM_Div()
        res = v.VM_PopW()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testIntLong(self):
        v.setOperandB(CALC_INT_LONG)
        v.VM_PushW(0)
        v.VM_PushL(1)
        v.VM_Div()
        res = v.VM_PopL()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testIntFloat(self):
        v.setOperandB(CALC_INT_FLOAT)
        v.VM_PushW(0)
        v.VM_PushF(1.0)
        v.VM_Div()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testLongInt(self):
        v.setOperandB(CALC_LONG_INT)
        v.VM_PushL(0)
        v.VM_PushW(1)
        v.VM_Div()
        res = v.VM_PopL()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testLongLong(self):
        v.setOperandB(CALC_LONG_LONG)
        v.VM_PushL(0)
        v.VM_PushL(1)
        v.VM_Div()
        res = v.VM_PopL()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testLongFloat(self):
        v.setOperandB(CALC_LONG_FLOAT)
        v.VM_PushL(0)
        v.VM_PushF(1.0)
        v.VM_Div()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testFloatInt(self):
        v.setOperandB(CALC_FLOAT_INT)
        v.VM_PushF(0.0)
        v.VM_PushW(1)
        v.VM_Div()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testFloatLong(self):
        v.setOperandB(CALC_FLOAT_LONG)
        v.VM_PushF(0.0)
        v.VM_PushL(1)
        v.VM_Div()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testFloatFloat(self):
        v.setOperandB(CALC_FLOAT_FLOAT)
        v.VM_PushF(0.0)
        v.VM_PushF(1.0)
        v.VM_Div()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)


class TestModByZero(unittest.TestCase):
    def testIntInt(self):
        v.setOperandB(CALC_INT_INT)
        v.VM_PushW(0)
        v.VM_PushW(1)
        v.VM_Mod()
        res = v.VM_PopW()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testIntLong(self):
        v.setOperandB(CALC_INT_LONG)
        v.VM_PushW(0)
        v.VM_PushL(1)
        v.VM_Mod()
        res = v.VM_PopL()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testIntFloat(self):
        v.setOperandB(CALC_INT_FLOAT)
        v.VM_PushW(0)
        v.VM_PushF(1.0)
        v.VM_Mod()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testLongInt(self):
        v.setOperandB(CALC_LONG_INT)
        v.VM_PushL(0)
        v.VM_PushW(1)
        v.VM_Mod()
        res = v.VM_PopL()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testLongLong(self):
        v.setOperandB(CALC_LONG_LONG)
        v.VM_PushL(0)
        v.VM_PushL(1)
        v.VM_Mod()
        res = v.VM_PopL()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testLongFloat(self):
        v.setOperandB(CALC_LONG_FLOAT)
        v.VM_PushL(0)
        v.VM_PushF(1.0)
        v.VM_Mod()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testFloatInt(self):
        v.setOperandB(CALC_FLOAT_INT)
        v.VM_PushF(0.0)
        v.VM_PushW(1)
        v.VM_Mod()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testFloatLong(self):
        v.setOperandB(CALC_FLOAT_LONG)
        v.VM_PushF(0.0)
        v.VM_PushL(1)
        v.VM_Mod()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)

    def testFloatFloat(self):
        v.setOperandB(CALC_FLOAT_FLOAT)
        v.VM_PushF(0.0)
        v.VM_PushF(1.0)
        v.VM_Mod()
        res = v.VM_PopF()
        self.assertEquals(v.getLastException(), ERROR_DIV0)


unittest.main()