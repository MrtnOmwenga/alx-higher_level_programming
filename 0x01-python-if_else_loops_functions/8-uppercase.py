#!/usr/bin/python3
def uppercase(str):
    result =''
    result.join([chr(ord(char) - 32) for char in str_data if ord(char) >= 65])
    print("{result}".format(result=result))
