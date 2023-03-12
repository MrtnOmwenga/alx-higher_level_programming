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
        items = {1: "width", 2: "height", 3: "x", 4: "y"}
        i = 1
        for item in [width, height, x, y]:
            if type(item) is not int:
                raise TypeError("{} must be an integer".format(items[i]))
            i += 1
        i = 1
        for item in [width, height]:
            if item <= 0:
                raise ValueError("{} must be > 0".format(items[i]))
            i += 1
        i = 3
        for item in [x, y]:
            if item < 0:
                raise ValueError("{} must be >= 0".format(items[i]))
            i += 1

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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Getter"""
        return(self.__height)

    @height.setter
    def height(self, height):
        """Setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Getter"""
        return(self.__x)

    @x.setter
    def x(self, x):
        """Setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Getter"""
        return(self.__y)

    @y.setter
    def y(self, y):
        """Setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Returns area of rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """Displays the rectangle"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str___(self):
        """Overrides __str__"""
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width,
            self.height))
