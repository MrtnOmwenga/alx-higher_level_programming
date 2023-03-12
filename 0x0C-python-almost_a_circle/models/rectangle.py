#!/usr/bin/python3
"""
Class Rectangle that inherits from
Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter"""
        return(self.__width)

    @width.setter
    def width(self, width):
        """Setter"""
        self.__width = width

    @property
    def height(self):
        """Getter"""
        return(self.__height)

    @height.setter
    def height(self, height):
        """Setter"""
        self.__height = height

    @property
    def x(self):
        """Getter"""
        return(self.__x)

    @x.setter
    def x(self, x):
        """Setter"""
        self.__x = x

    @property
    def y(self):
        """Getter"""
        return(self.__y)

    @y.setter
    def y(self, y):
        """Setter"""
        self.__y = y
