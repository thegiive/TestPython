def sortByHeight(a):
    tmp_arr = []
    for index in range(0,len(a)):
        if(a[index] != -1):
            tmp_arr.append(a[index])
            a[index] = 0 
    sorted_arr = list(reversed(sorted(tmp_arr)))
    for index in range(0,len(a)):
        if(a[index] != -1):
            a[index] = sorted_arr.pop()
    return a

import unittest
class TestFunc(unittest.TestCase):
    def test_n1(self):
        self.assertEqual([-1, 150, 160, 170, -1, -1, 180, 190],sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))

if __name__ == '__main__':
    unittest.main()