#!/usr/bin/python3
"""
Class square that inherits from Rectangle
Private instance size
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Private instance attribute size"""

    def __init__(self, size):
        """ Initializes class """
        self.__size = size
        super().__init__(size, size)
