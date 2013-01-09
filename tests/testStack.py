
import unittest
import vm_al as v

class StackTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(StackTest, self).__init__(*args, **kwargs)
		self.arr = v.byteArray(64)
		v.setRAMPointer(self.arr)

	def testOrder(self):
		values = (1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999)
		for w in values:
    			v.VM_PushW(w)
		result = []
		while v.getSP():
			result.append(v.VM_PopW())
		result.reverse()
		self.assertEquals(values, tuple(result))
  
if __name__ == '__main__':
  unittest.main()
 
