#!/usr/bin/python3
"""Define a MagicClass matching exactly the bytecode provided by Holberton."""

import math

class MagicClass:
    """
    A class that represents a magic circle with radius.

    Attributes:
        __radius (float or int): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (float or int): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number (float or int).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
