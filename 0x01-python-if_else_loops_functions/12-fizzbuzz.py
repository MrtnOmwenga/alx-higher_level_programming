#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 100):
        if i %3 == 0 and i % 5 == 0:
            print("FizzBuzz", end="")
            if i != 99:
                print(" ", end="")
            else:
                print("\n")
        if i % 3 == 0:
            print("Fizz", end="")
            if i != 99:
                print(" ", end="")
            else:
                print("\n")
        elif i % 5 == 0:
            print("Buzz", end = "")
            if i != 99:
                print(" ", end="")
            else:
                print("\n")
        else:
            print(i, end="")
            if i != 99:
                print(" ", end="")
            else:
                print("\n")
