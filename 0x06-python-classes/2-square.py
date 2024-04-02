#!/usr/bin/python3

"""
this is simply our class square
"""


class Square:
    """
    we defining size
    """


    def __init__(self, size=0):
        self.__size = size
        """
        this is our conditions
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """
        property and inside we define self
        """
        @property
        def size(self):
            return self.__size
        """
        and size.setter
        """
        @size.setter
        def size(self, value):
            self.__size = value
           """
           lastly where we define area and return self.__size ** 2
           """
            def area(self):
                return self.__size ** 2
