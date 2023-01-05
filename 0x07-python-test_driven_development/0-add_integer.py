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

    if type(a) is float and a != float(NaN):
        a = int(a)
    if type(b) is float and b != float(NaN):
        b = int(b)

    return (a + b)
