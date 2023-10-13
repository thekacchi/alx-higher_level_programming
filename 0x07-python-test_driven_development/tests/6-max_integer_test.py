#!/usr/bin/python3
"""Unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer"""
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 4, 6, 1]), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_only_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_large_list(self):
        self.assertEqual(max_integer([1000, 0, -1]), 1000)
