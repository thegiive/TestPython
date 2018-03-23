def commonCharacterCount(s1, s2):
    dict_s1 = {}
    dict_s2 = {}
    for c in s1:
        if(dict_s1.get(c)):
            dict_s1[c] += 1 
        else:
            dict_s1[c] = 1 
    for c in s2:
        if(dict_s2.get(c)):
            dict_s2[c] += 1 
        else:
            dict_s2[c] = 1 
    result = 0 
    for key in dict_s1:
        if(dict_s2.get(key)):
            result += min(dict_s1[key] , dict_s2[key])
    return result


import unittest
class TestFunc(unittest.TestCase):
    def test_n1(self):
        self.assertEqual(3,commonCharacterCount("aabcc", "adcaa"))
        self.assertEqual(4,commonCharacterCount("zzzzzzzz", "zzzz"))

if __name__ == '__main__':
    unittest.main()