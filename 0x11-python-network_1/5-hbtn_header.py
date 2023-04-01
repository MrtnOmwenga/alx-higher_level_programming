#!/usr/bin/python3
""" Get header using request """


if __name__ == '__main__':
    import requests
    import sys

    data = requests.get(sys.argv[1])
    print(data.headers['X-Request-Id'])
