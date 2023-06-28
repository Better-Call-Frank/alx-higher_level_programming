#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares the square area with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compares the square area with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compares the square area with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compares the square area with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Compares the square area with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is smaller, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compares the square area with another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area is smaller or equal, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)
