#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    if count == 1:
        print("{:d} arguments.".format(0))
    else:
        if count == 2:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(count - 1))
        for i in range(1, count):
            print("{:d}: {}".format(i, sys.argv[i]))
