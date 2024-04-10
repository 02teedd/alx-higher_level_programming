#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, height=0, width=0):
        """initialize a new Rectangle.

        args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise valueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        return f"{{'_Rectangle__height': {self.__height}, '_Rectangle__width': {self.__width}}}"


rectangle1 = Rectangle(4, 2)
rectangle2 = Rectangle(3, 10)

"""print(rectangle1.__dict__)"""
"""print(rectangle2.__dict__)"""

