#!/usr/bin/python3
"""Class Square with private instance attribute size"""


class Square:
    """Class Square with private instance attribute"""
    def __init__(self, size=0):
        """Initializes class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
