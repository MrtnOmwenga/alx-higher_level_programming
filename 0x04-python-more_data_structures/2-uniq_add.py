#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    result = 0
    if my_list == []:
        return (0)
    else:
        for i in my_list:
            if i not in uniq:
                result = result + i
                uniq.append(i)
    return (result)
