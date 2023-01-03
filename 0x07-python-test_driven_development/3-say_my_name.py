#!/usr/bin/python3
"""
prints "My name is <first name> <last name>
Both first and last names must be strings
"""


def say_my_name(first_name, last_name=""):
    """Prints first name and last name"""

    """Check first name"""
    if first_name is None or type(first_name) is not str:
        raise TypeError("first_name must be a string")

    """Chack last name"""
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    """Print statement"""
    print("My name is {:s} {:s}".format(first_name, last_name))
