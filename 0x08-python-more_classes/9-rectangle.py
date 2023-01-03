#!/usr/bin/python3
"""
Creates class Rectangle
Adds Private instance attribute width and height
Class methods Area and Perimeter to calculate
area and perimeter
Public class methods to print the Rectangle
Method to detect deletion of class instance
Adds instance counter
Adds a class attribute print_symbol
Public class method to compare Rectangles
"""


class Rectangle:
    """Class with private attributes width and height"""

    """Instance counter"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize class"""

        Rectangle.number_of_instances += 1
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

    def __str__(self):
        """Prints Rectangle using #"""
        result = ""
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return (result)
        for i in range(self._Rectangle__height):
            for j in range(self._Rectangle__width):
                result = result + str(self.print_symbol)
            result = result + "\n"
        return (result[:-1])

    def __repr__(self):
        """Return string representation of object"""
        result = ""
        result += "Rectangle("
        result += str(self._Rectangle__width)
        result += ", "
        result += str(self._Rectangle__height)
        result += ")"
        return (result)

    def __del__(self):
        """Called when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns rectangle of width = height = size"""
        return (cls(size, size))
