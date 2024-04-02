#!/usr/bin/python3
"""define a class square."""


class Square:
    """Reprent a square."""
    def __init__(self, size = 0):
        """Initialize a new square.
        args:
        size (int): the size of the new square.
        """
        if not isinstance(size, int):
            raise typeError("size must be an integer")
        elif size < 0:
             raise valueError("size must be >= 0")
        self.__size = size

