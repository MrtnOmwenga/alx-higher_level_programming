#!/usr/bin/python3
i = 122
while i >= 97:
    if i % 2 == 1:
        print("{c:c}".format(c=i - 32), end="")
    else:
        print("{c:c}".format(c=i), end="")
    i=i - 1
