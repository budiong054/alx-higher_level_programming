#!/usr/bin/python3
"""The ``test_square`` module

This module contains the Test class ``TestRectangle``
"""
import unittest
from models.square import Square
from test_models.test_rectangle import display_hash


class TestSquare(unittest.TestCase):
    """TestSquare is test class for the Square class and methods
    """
    def test_square_id(self):
        """Test the square class id attributes for correct output
        """
        self.assertEqual(Square(5, 2, 4, 5).id, 5)

    def test_square_area(self):
        """Test the square area method for correct output
        """
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(3, 4, 5).area(), 9)
        self.assertEqual(Square(6, 2).area(), 36)

    def test_square_raises(self):
        """Test the square area method incase of bad values
        """
        with self.assertRaises(TypeError):
            Square("5").area()
        with self.assertRaises(TypeError):
            Square(True, 3, 5).area()
        with self.assertRaises(TypeError):
            Square([3], 3, 5).area()
        with self.assertRaises(TypeError):
            Square((4,), 3, 5).area()
        with self.assertRaises(TypeError):
            Square({}, 3, 5).area()
        with self.assertRaises(ValueError):
            Square(-4).area()
        with self.assertRaises(ValueError):
            Square(0, 4, 2).area()

    def test_square_display(self):
        """Test the square display method
        """
        self.assertEqual(Square(4, 3, 2).display(), display_hash(4, 4, 3, 2))
        self.assertEqual(Square(6).display(), display_hash(6, 6))

    def test_square_display_raises(self):
        """Test the square display method for bad value
        """
        with self.assertRaises(TypeError):
            Square("5").display()
        with self.assertRaises(TypeError):
            Square(True, 3, 5).display()
        with self.assertRaises(TypeError):
            Square([3], 3, 5).display()
        with self.assertRaises(TypeError):
            Square((4,), 3, 5).display()
        with self.assertRaises(TypeError):
            Square({}, 3, 5).display()
        with self.assertRaises(ValueError):
            Square(-4).display()
        with self.assertRaises(ValueError):
            Square(0, 4, 2).display()

    def test_square_size(self):
        """Test the square size attribute
        """
        s1 = Square(4, 4, 2)
        self.assertEqual(s1.size, 4)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_square_size_raises(self):
        """Test the square size against bad values
        """
        s2 = Square(4, 5, 6)
        with self.assertRaises(TypeError):
            s2.size = "4"
        with self.assertRaises(TypeError):
            s2.size = True
        with self.assertRaises(TypeError):
            s2.size = (4,)
        with self.assertRaises(ValueError):
            s2.size = -2
        with self.assertRaises(ValueError):
            s2.size = 0

    def test_square_update(self):
        """Test the square update method for correct output
        """
        s3 = Square(3, 3, 5, 12)
        s3.update(14)
        self.assertEqual(s3.id, 14)
        s3.update(19, 7, 9, 4)
        self.assertEqual(s3.size, 7)
        self.assertEqual(s3.x, 9)
        self.assertEqual(s3.y, 4)
        s3.update(size=8, y=5)
        self.assertEqual(s3.size, 8)
        self.assertEqual(s3.y, 5)

    def test_square_update_raises(self):
        """Test the square method against bad values
        """
        s4 = Square(3, 4, 5, 6)
        with self.assertRaises(TypeError):
            s4.update(5, "9")
        with self.assertRaises(TypeError):
            s4.update(5, True)
        with self.assertRaises(TypeError):
            s4.update(5, 7.3)
        with self.assertRaises(ValueError):
            s4.update(x=-1)
        with self.assertRaises(ValueError):
            s4.update(size=0)
        with self.assertRaises(ValueError):
            s4.update(x=3, y=-1)
