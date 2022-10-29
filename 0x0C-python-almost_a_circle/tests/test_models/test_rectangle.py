#!/usr/bin/python3
"""The ``test_rectangle`` module

This module contains the Test class ``TestRectangle``
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle is test class for the Rectangle
        class and methods
    """
    def test_rectangle_id(self):
        """Test the rectangle class id attributes for correct
            output
        """
        self.assertEqual(Rectangle(3, 5, 2, 1, 17).id, 17)
        # self.assertEqual(Rectangle(3, 5).id, 7)
        # self.assertEqual(Rectangle(2, 2).id, 8)

    def test_rectangle_area(self):
        """Test the rectangle area method for correct output
        """
        self.assertEqual(Rectangle(3, 5).area(), 15)
        self.assertEqual(Rectangle(1, 4, 2, 4).area(), 4)

    def test_rectangle_attribute_raises_error(self):
        """Test the rectangle attributes if its raises error
            if given a bad value
        """
        with self.assertRaises(AttributeError):
            r1 = Rectangle(4, 6, 2, 4)
            r1.__width
            r1.__height
            r1.__x
            r1.__y
        with self.assertRaises(ValueError):
            Rectangle(-3, 4, 0, 0)
            Rectangle(1, 0)
            Rectangle(2, 1, -2)
        with self.assertRaises(TypeError):
            Rectangle("3", 2)
            Rectangle(2, True)
            Rectangle(2, 3, {}, 1)
            Rectangle(1, [4])
            Rectangle(4, 2, {x: 2}, {y:3})

    def test_rectangle_area_raises_error(self):
        """Test if the rectangle method area raises error
            if given bad value
        """
        with self.assertRaises(TypeError):
            Rectangle("3", 3).area()
            Rectangle(4, True).area()
            Rectangle(2, 5.5).area()
            Rectangle([3], {2}).area()
