#!/usr/bin/python3
""" Return variable in header response """


import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    data = response.headers['X-Request-Id']
    print(data)
