#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary
    for key, dict_value in list(a_dictionary.items()):
        if value == dict_value:
            new_dict.pop(key, 0)
    return (a_dictionary)
