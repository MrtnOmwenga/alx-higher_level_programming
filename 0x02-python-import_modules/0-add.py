#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as add
    a = 1
    b = 2
    print("{a:d} + {b:d} = {num:d}".format(a=a, b=b, num=add.add(a, b)))
