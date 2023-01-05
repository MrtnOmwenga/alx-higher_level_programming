#!/usr/bin/python3
"""
Adds 2 integers / floats and returns integer
Input must be integers or floats
"""


def add_integer(a, b=98):
    """add the 2 integers"""
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if b is None or type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a is None:
        return

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return (89)

    return (int(a) + int(b))
