#!/usr/bin/python3

#test_square.py
#Frank M Leoh <375@holbertonschool.com>
"""Defines unittests for models/square.py.

Unittest classes:
TestSquareInstantiation - line 24
TestSquareSize - line 88
TestSquareX - line 166
TestSquareY - line 238
TestSquareOrderOfInitialization - line 306
TestSquareArea - line 322
TestSquareStdout - line 343
TestSquareUpdateArgs - line 426
TestSquareUpdateKwargs - line 538
TestSquareToDictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square

class TestSquareInstantiation(unittest.TestCase):
"""Unittests for testing instantiation of the Square class."""

def test_is_base(self):
    self.assertIsInstance(Square(10), Base)

def test_is_rectangle(self):
    self.assertIsInstance(Square(10), Square)

def test_no_args(self):
    with self.assertRaises(TypeError):
        Square()

def test_one_arg(self):
    s1 = Square(10)
    s2 = Square(11)
    self.assertEqual(s1.id, s2.id - 1)

def test_two_args(self):
    s1 = Square(10, 2)
    s2 = Square(2, 10)
    self.assertEqual(s1.id, s2.id - 1)

def test_three_args(self):
    s1 = Square(10, 2, 2)
    s2 = Square(2, 2, 10)
    self.assertEqual(s1.id, s2.id - 1)

def test_four_args(self):
    self.assertEqual(7, Square(10, 2, 2, 7).id)

def test_more_than_four_args(self):
    with self.assertRaises(TypeError):
        Square(1, 2, 3, 4, 5)

def test_size_private(self):
    with self.assertRaises(AttributeError):
        print(Square(10, 2, 3, 4).__size)

def test_size_getter(self):
    self.assertEqual(5, Square(5, 2, 3, 9).size)

def test_size_setter(self):
    s = Square(4, 1, 9, 2)
    s.size = 8
    self.assertEqual(8, s.size)

def test_width_getter(self):
    s = Square(4, 1, 9, 2)
    s.size = 8
    self.assertEqual(8, s.width)

def test_height_getter(self):
    s = Square(4, 1, 9, 2)
    s.size = 8
    self.assertEqual(8, s.height)

def test_x_getter(self):
    self.assertEqual(0, Square(10).x)

def test_y_getter(self):
    self.assertEqual(0, Square(10).y)
