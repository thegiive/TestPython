# -*- coding: utf-8 -*-

import unittest
from shape_area import *


class TestShapeAreaFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_n1(self):
        """Test method add(a, b)"""
        self.assertEqual(1, shapeArea(1))
        self.assertEqual(5, shapeArea(2))
        self.assertEqual(13, shapeArea(3))
        self.assertEqual(25, shapeArea(4))
        # self.assertNotEqual(3, add(2, 2))

if __name__ == '__main__':
    unittest.main()