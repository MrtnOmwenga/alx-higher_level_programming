#!/usr/bin/python3
"""
Class MyList that inherits from list
Public method print_sorted that prints
a sorted version of the list
"""


class MyList(list):
    """ Methods: print_sorted"""

    def print_sorted(self):
        """Sorts items in list"""
        self.sort()
        print(self)
