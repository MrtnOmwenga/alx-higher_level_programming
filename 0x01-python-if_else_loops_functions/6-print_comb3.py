#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            if i != 8:
                print("{num1:d}{num2:d}".format(num1=i, num2=j), end=", ")
            else:
                print("{num1:d}{num2:d}".format(num1=i, num2=j))
