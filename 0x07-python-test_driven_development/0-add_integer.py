#!/usr/bin/python3

"""Define an integer addition."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float argument are typecasted to int before addition is perfomed.
    Raises:
        TypeError: if either of a or b is a non-integer and non-float.
        """
        if ((not isinstance(a, int) and not isinstance(a, float))):
            raise TypeError("a must be an integer")
        if ((not isinstance(b, int) and not isinstance(b, float))):
            raise TypeError("b must be an integer")
        return (int(a) + int(b))
