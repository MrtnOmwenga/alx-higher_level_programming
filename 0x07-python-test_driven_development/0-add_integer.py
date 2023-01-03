#!usr/bin/python3
"""
Adds 2 integers / floats and returns integer
Input must be integers or floats
"""


def add_integer(a, b=98):
    """add the 2 integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a is None:
        return

    a = int(a)
    b = int(b)

    return (a + b)
