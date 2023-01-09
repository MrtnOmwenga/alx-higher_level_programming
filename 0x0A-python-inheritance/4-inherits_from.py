#!/usr/bin/python3
"""
Checks if object is a subclass of class
"""


def inherits_from(obj, a_class):
    """ Uses issubclass function """
    return issubclass(type(obj), a_class)
