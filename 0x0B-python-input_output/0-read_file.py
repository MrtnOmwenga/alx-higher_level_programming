#!/usr/bin/python3
"""
Funstion to read a file
No permmissions
No file avilability checks
"""


def read_file(filename=""):
    with open(filename) as file:
        read_data = file.read()
        print(read_data)
