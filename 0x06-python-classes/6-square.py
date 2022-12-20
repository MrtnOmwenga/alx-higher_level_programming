#!/usr/bin/python3
"""Class Square with private instance attribute size"""


class Square:
    """Class Square with private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
        self._Square__position = position

    def area(self):
        """Calculates area of square"""
        return (self._Square__size * self._Square__size)

    @property
    def size(self):
        """Gets size"""
        return (self._Square__size)

    @size.setter
    def size(self, value):
        """Sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    @property
    def position(self):
        """Square position"""
        return (self._Square__position)

    @position.setter
    def position(self, value):
        """Sets square position"""
        if type(value) == tuple and len(value) == 2:
            self._Square__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints square using #"""
        if (self._Square__size) == 0:
            print("")
        for h in range(self._Square__position[1]):
            print("")
        for i in range(self._Square__size):
            for e in range(self._Square__position[0]):
                print(" ", end="")
            for j in range(self._Square__size):
                print("#", end="")
            print("")
