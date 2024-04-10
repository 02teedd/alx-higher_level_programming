#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers and returns the sum.
    

    Args:
        a: The first number (int or float).
        b: The second number (int or float, default is 98).
        
    Raises:
        TypeError: If either a or b is not an int or float.

    Returns:
        int: The sum of a and b, converted to an integer.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must an integer")

    return int(a) + int(b)
