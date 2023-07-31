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


if __name__ == '__main__':
    unittest.main()
