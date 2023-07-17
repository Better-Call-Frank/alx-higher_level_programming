#!/usr/bin/python3

"""
This module contains a Square class that inherits from the Rectangle class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square.

        Args:
            value (int): The size of the Square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square attributes.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents the id attribute.
                - 2nd argument represents the size attribute.
                - 3rd argument represents the x attribute.
                - 4th argument represents the y attribute.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return the string representation of the Square."""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)
