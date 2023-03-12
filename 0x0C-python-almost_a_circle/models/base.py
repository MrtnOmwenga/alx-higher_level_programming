#!/usr/bin/python3
"""
Class Base
"""


class Base:
    """
    Class Base
    Private class attr __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor
        instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
