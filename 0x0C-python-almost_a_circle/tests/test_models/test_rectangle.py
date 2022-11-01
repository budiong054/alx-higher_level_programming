#!/usr/bin/python3
"""The ``test_rectangle`` module

This module contains the Test class ``TestRectangle``
"""
import unittest
from models.rectangle import Rectangle


def display_hash(col, row, x=0, y=0):
    """Display # to stdout
    """
    for j in range(y):
        print()
    for i in range(row):
        print(f'{x * " "}{col * "#"}')


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

    def test_rectangle_display(self):
        """Test the rectangle display method for correct output
        """
        self.assertEqual(Rectangle(4, 6).display(), display_hash(4, 6))
        self.assertEqual(Rectangle(2, 2).display(), display_hash(2, 2))
        self.assertEqual(Rectangle(2, 3, 2, 2).display(),
                         display_hash(2, 3, 2, 2))

    def test_rectangle_str(self):
        """Test the rectangle __str__ method
        """
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(4, 6)), "[Rectangle] (22) 0/0 - 4/6")

    def test_rectangle_str_raises(self):
        """Test if __str__ raises error
        """
        with self.assertRaises(ValueError):
            str(Rectangle(4, 8, -1, 2))
            str(Rectangle(0, 2))
        with self.assertRaises(TypeError):
            str(Rectangle(True, 3))
            str(Rectangle(2, 4, "5", 0, 2))

    def test_rectangle_display_raise_error(self):
        """Test rectangle display method for error
        """
        with self.assertRaises(TypeError):
            Rectangle("2", 4).display()
            Rectangle(4, True).display()
        with self.assertRaises(ValueError):
            Rectangle(-4, 5).display()

    def test_rectangle_attribute_raises_error(self):
        """Test the rectangle attributes if its raises error
            if given a bad value
        """
        r1 = Rectangle(4, 6, 2, 4)
        with self.assertRaises(AttributeError):
            r1.__width
        with self.assertRaises(AttributeError):
            r1.__height
        with self.assertRaises(AttributeError):
            r1.__x
        with self.assertRaises(AttributeError):
            r1.__y
        with self.assertRaises(ValueError):
            Rectangle(-3, 4, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(2, 1, -2)
        with self.assertRaises(TypeError):
            Rectangle("3", 2)
        with self.assertRaises(TypeError):
            Rectangle(2, True)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, {}, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, [4])
        with self.assertRaises(TypeError):
            Rectangle(4, 2, {2}, {3})

    def test_rectangle_update(self):
        """Test the rectangle update method for correct output
        """
        r_1 = Rectangle(10, 10, 10, 10)
        r_1.update(89)
        self.assertEqual(str(r_1), "[Rectangle] (89) 10/10 - 10/10")
        r_1.update(20, 3, 4, 5, 6)
        self.assertEqual(str(r_1), "[Rectangle] (20) 5/6 - 3/4")
        r_1.update(height=1)
        self.assertEqual(str(r_1), "[Rectangle] (20) 5/6 - 3/1")
        r_1.update(width=5, id=15, y=4)
        self.assertEqual(str(r_1), "[Rectangle] (15) 5/4 - 5/1")

    def test_rectangle_update_raises(self):
        """Test rectangle update method if its raises the correct
            error
        """
        r_2 = Rectangle(10, 20, 30, 30)
        with self.assertRaises(ValueError):
            r_2.update(67, -3)
        with self.assertRaises(TypeError):
            r_2.update(67, 4, 5, "5")
        with self.assertRaises(TypeError):
            r_2.update(67, True)
        with self.assertRaises(ValueError):
            r_2.update(height=0)
        with self.assertRaises(ValueError):
            r_2.update(height=2, x=-1)
        with self.assertRaises(TypeError):
            r_2.update(height=True)

    def test_rectangle_area_raises_error(self):
        """Test if the rectangle method area raises error
            if given bad value
        """
        with self.assertRaises(TypeError):
            Rectangle("3", 3).area()
        with self.assertRaises(TypeError):
            Rectangle(4, True).area()
        with self.assertRaises(TypeError):
            Rectangle(2, 5.5).area()
        with self.assertRaises(TypeError):
            Rectangle([3], {2}).area()
