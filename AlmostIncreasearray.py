def almostIncreasingSequence1(sequence):
    last_element = -1000001
    reduce_number = 0 
    for element in sequence:
        if(last_element > element):
            reduce_number += 1 
        last_element = element
    if(reduce_number > 1):
        return False
    else:
        return True

def almostIncreasingSequence(sequence):
    remove_number = 0 
    for i in range(1,len(sequence)):
        if(sequence[i] <= sequence[i-1]):
            # print(str(sequence[i])+" "+str(sequence[i-1])+" "+str(remove_number))
            if(remove_number == 0):
                if(i < len(sequence) -1):
                    if(sequence[i-1] < sequence[i+1]):
                        remove_number += 1 
                    elif((i==1) and (sequence[i] < sequence[i+1])):
                        remove_number += 1
                    elif((i >= 2) and (sequence[i] < sequence[i+1]) and (sequence[i-2] < sequence[i])):
                        remove_number += 1
                    else:
                        return False
            else:
                return False
    return True


import unittest

class TestShapeAreaFunc(unittest.TestCase):
    def test_n1(self):
        self.assertEqual(True, almostIncreasingSequence([1,3,2]))
        self.assertEqual(False, almostIncreasingSequence([1,3,2,1]))
        self.assertEqual(False , almostIncreasingSequence([1, 2, 1, 2]))
        self.assertEqual(False , almostIncreasingSequence([1, 4, 10, 4, 2]))
        self.assertEqual(False , almostIncreasingSequence([1, 1, 1, 2, 3]))
        self.assertEqual(False , almostIncreasingSequence([1, 2, 5, 5, 5]))
        self.assertEqual(True , almostIncreasingSequence([1, 2, 3, 4, 3, 6]))
        self.assertEqual(True , almostIncreasingSequence([3, 5, 67, 98, 3]))

    def test_n2(self):
        self.assertEqual(True , almostIncreasingSequence([10, 1, 2, 3, 4, 5]))
        self.assertEqual(True , almostIncreasingSequence([1,2,5,3,5]))
        

if __name__ == '__main__':
    unittest.main()
