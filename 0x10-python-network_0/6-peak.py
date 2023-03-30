#!/usr/bin/python3
"""
Find Peak in unsirted list
"""


def find_peak(list_of_integers):
    """ Find Max """
    if list_of_integers == [] or list_of_integers is None:
        return None

    sort = sorted(list_of_integers)
    return sort[-1]
