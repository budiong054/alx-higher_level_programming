#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the max integer function
    """
    def test_max_integer(self):
        """Test max_integer when list contains both positive and
            negative integers/floats
        """
        # when list contains positive integer
        self.assertEqual(max_integer([3, 5, 6, 8]), 8)
        # when list contains negative integer
        self.assertEqual(max_integer([-2, -6, -7, -9, -3]), -2)
        # when list contains both positive and negative integer
        self.assertEqual(max_integer([-2, 3, 1, -3, -1, 0]), 3)
        # when list contains positive and negative float
        self.assertEqual(max_integer([-7.64, -3.09, -3, -1.8, -1]), -1)
        # when an empty list is passed
        self.assertIsNone(max_integer())

    def test_type(self):
        """Test max_integer if it raises an error when a list contains
            a non integer or float
        """
        # when the list contains a string
        self.assertRaises(TypeError, max_integer, [-1, "5", "6", 7, -2])
        # when a list contains a list
        self.assertRaises(TypeError, max_integer, [2, 4, [8, 9], 8])
