#!/usr/bin/python3
"""The ``test_base`` module

This contains the test case for the ``Base`` class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase is test class for the Base Class
    """
    def test_base_correct(self):
        """Method test the base class for equality
        """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(20).id, 20)

    def test_base_raise_error(self):
        """Method test if it raises error
        """
        with self.assertRaises(AttributeError):
            Base(2).__nb_objects
            Base().__nb_objects
