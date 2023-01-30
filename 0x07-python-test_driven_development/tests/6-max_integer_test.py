#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    
    def test_unorderd_list(self):
        self.assertEqual(max_integer([22, 12, 1024, 98]), 1024)

    def test_single_member(self):
        self.assertEqual(max_integer([98]), 98)

    def test_max_float(self):
        self.assertEqual(max_integer([5.2, 3.6, 8.9, 9.8, 2.0]), 9.8)

    def test_max_alpha(self):
        self.assertEqual(max_integer(['s', 'c', 'h', 'o', 'o', 'l']), 's')

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_matrix(self):
        self.assertEqual(max_integer([[1, 2, 3, 4], [5, 6, 7, 8]]), [5, 6, 7, 8])

    def test_mixed_list(self):
        self.assertEqual(max_integer(['A', 'L', 'X', '9', '8']), 'X')

if __name__ == "__main__":
    unittest.main()
