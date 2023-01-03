#!/usr/bin/python3
"""
Creates class Rectangle
Adds Private instance attribute width and height
Class methods Area and Perimeter to calculate 
area and perimeter
"""


class Rectangle:
    """Class with private attributes width and height"""
    
    def __init__(self, width=0, height=0):
        """Initialize class"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height

    @property
    def width(self):
        """Gets width"""
        return (self._Rectangle__width)

    @width.setter
    def width(self, value):
        """Sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self._Rectangle__width = value

    @property
    def height(self):
        """Gets height"""
        return(self._Rectangle__height)

    @height.setter
    def height(self, value):
        """Sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self._Rectangle__height = value

    def area(self):
        """Returns area of rectangle"""
        return (self._Rectangle__width * self._Rectangle__height)

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return (0)
        return (2 * (self._Rectangle__width + self._Rectangle__height))
