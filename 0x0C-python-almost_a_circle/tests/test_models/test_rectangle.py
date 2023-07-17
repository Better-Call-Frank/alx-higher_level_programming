#!/usr/bin/python3
# test_rectangle.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangleInstantiation - line 25
    TestRectangleWidth - line 114
    TestRectangleHeight - line 190
    TestRectangleX - line 262
    TestRectangleY - line 334
    TestRectangleOrderOfInitialization - line 402
    TestRectangleArea - line 430
    TestRectangleUpdateArgs - line 538
    TestRectangleUpdateKwargs - line 676
    TestRectangleToDictionary - line 788
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    # ... (rest of the tests remain unchanged)
    # ...
    # ...
