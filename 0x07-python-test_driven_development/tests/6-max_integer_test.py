#!/usr/bin/python3
"""Unittests for max_integer([...])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_sorted_list(self):
        """Test a sorted list of integers"""

        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unsorted_list(self):
        """Test unsorted list of integers"""

        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test an empty list"""

        result = max_integer([])
        self.assertIsNone(result)

    def test_max_at_beginning(self):
        """Test when max is first element"""

        result = max_integer([8, 3, 4, 7])
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        """Test negative numbers"""

        result = max_integer([-3, -8, -2, -7])
        self.assertEqual(result, -2)

    def test_one_element(self):
        """Test Only one element"""

        result = max_integer([7])
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
