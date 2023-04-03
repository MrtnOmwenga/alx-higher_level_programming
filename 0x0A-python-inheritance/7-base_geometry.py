#!/usr/bin/python3
"""
Public instance method area
Public instance method integer
validator
"""


class BaseGeometry:
    """Methods: area
                integer validator"""
    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integer """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
