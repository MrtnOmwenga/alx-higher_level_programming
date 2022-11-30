#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 65:
            result = result.join(chr(ord(char) - 32))
        else:
            result = result.join(char)
    print("{result}".format(result=result))
