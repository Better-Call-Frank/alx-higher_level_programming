#!/usr/bin/python3

"""
This module contains a Rectangle class that inherits from the Base class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        
        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
            TypeError: If either x or y is not an integer.
            ValueError: If either x or y is less than 0.
        """
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The width of the Rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x coordinate of the Rectangle.

        Args:
            value (int): The x coordinate of the Rectangle.

        Raises:
            TypeError: If the x coordinate is not an integer.
            ValueError: If the x coordinate is less than 0.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y coordinate of the Rectangle.

        Args:
            value (int): The y coordinate of the Rectangle.

        Raises:
            TypeError: If the y coordinate is not an integer.
            ValueError: If the y coordinate is less than 0.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Update the Rectangle attributes.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents the id attribute.
                - 2nd argument represents the width attribute.
                - 3rd argument represents the height attribute.
                - 4th argument represents the x attribute.
                - 5th argument represents the y attribute.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
