#!/usr/bin/python3
def safe_print_division(a, b):
    print("Inside result: ", end = "")
    try:
        print("{}".format(a / b))
        return (a / b)
    except ZeroDivisionError:
        print("None")
        return (None)
