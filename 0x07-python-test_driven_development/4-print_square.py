#!/usr/bin/python3
"""
Prints a square using #
size is the length of the square
size must be an integer greater than 0
"""

def print_square(size):
    """Prints a square using #"""

    """Check size"""
    if size is None or type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    """Print square"""
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
