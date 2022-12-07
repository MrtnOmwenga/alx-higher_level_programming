#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key != "" and key in a_dictionary.keys():
        a_dictionary.pop(key, 0)
    return (a_dictionary)
