#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    i = 0

    while (i < len(roman_string)):
        s1 = my_dict[roman_string[i]]

        if i + 1 < len(roman_string):
            s2 = my_dict[roman_string[i + 1]]

            if s1 >= s2:
                result = result + s1
                i = i + 1
            else:
                result = result + s2 - s1
                i = i + 2
        else:
            result = result + s1
            i = i + 1
            
    return (result)
        
