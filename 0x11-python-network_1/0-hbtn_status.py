#!/usr/bin/python3
""" Fetch URL """


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    print('Body response:')
    print('\t- type: ' + str(type(data)))
    print('\t- content: ' + str(data))
    print('\t- utf8 content: ' + str(data.decode('utf-8')))
