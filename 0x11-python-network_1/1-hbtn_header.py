#!/usr/bin/python3
""" Return variable in header response """


if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        data = response.headers['X-Request-Id']
        print(data)
