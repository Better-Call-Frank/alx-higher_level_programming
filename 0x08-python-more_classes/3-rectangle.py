#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Gets or sets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets or sets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return self._width * 2 + self._height * 2

    def __str__(self):
        """Returns the printable representation of the rectangle.

        The rectangle is represented using the '#' character.
        """
        if self._width == 0 or self._height == 0:
            return ""

        rect = []
        for i in range(self._height):
            rect.extend(["#"] * self._width)
            if i != self._height - 1:
                rect.append("\n")
        return "".join(rect)
