
import unittest
import vm_al as v


values = (1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999)

def main():
  arr = v.byteArray(64)
  v.setRAMPointer(arr)
  for w in values:
    v.VM_PushW(w)
    
  while v.getSP():
    x = v.VM_PopW()
    print x

  
if __name__ == '__main__':
  main()
  unittest.main()
