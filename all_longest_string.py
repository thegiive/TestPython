import unittest

def allLongestStrings(inputArray):
    max_length = 0 
    for ele in inputArray:
        if( max_length< len(ele)):
            max_length = len(ele)
    result = []
    for ele in inputArray:
        if(len(ele) == max_length):
            result.append(ele)
    return result


class TestShapeAreaFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_n1(self):
        """Test method add(a, b)"""
        self.assertEqual(["aba", "vcd", "aba"], allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
        self.assertEqual(["aba"], allLongestStrings(["aba"]))

if __name__ == '__main__':
    unittest.main()