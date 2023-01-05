#!/usr/bin/python3
"""
Adds 2 integers / floats and returns integer
Input must be integers or floats
"""


def add_integer(a, b=98):
    """add the 2 integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
