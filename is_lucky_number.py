def isLucky(n):
    tmp = n 
    int_arr = []
    while(tmp != 0 ):
        int_arr.append( tmp % 10 )
        tmp = int(tmp/10)
    r1 = 0 
    r2 = 0 
    for i in range(0 , len(int_arr)):
        if(i >= int(len(int_arr)/2)):
            r2 += int_arr[i]
        else:
            r1 += int_arr[i]
    if(r1 == r2):
        return True
    else:
        return False

import unittest
class TestFunc(unittest.TestCase):
    def test_n1(self):
        self.assertEqual(True,isLucky(1230))
        self.assertEqual(False,isLucky(239017))

if __name__ == '__main__':
    unittest.main()