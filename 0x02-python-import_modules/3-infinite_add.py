#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    result = 0
    for i in range(1, count):
        result = result + int(sys.argv[i])
    print("{:d}".format(result))
