#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    result = my_list
    if idx < len(my_list) and idx >= 0:
        #result = my_list[:idx] + my_list[idx + 1:]
        del result[idx]
    return (result)
