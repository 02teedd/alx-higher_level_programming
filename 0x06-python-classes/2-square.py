#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represent a rectanglr."""

    def __init__(self, width=0, height=0):
        """Initiatlize a new REctangle.

        args:
        width (int): The width of the new recttangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinsrance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """Get/set the height of the Rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
