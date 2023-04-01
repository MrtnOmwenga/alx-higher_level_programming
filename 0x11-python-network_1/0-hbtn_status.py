#!/usr/bin/python3
""" Fetch URL """


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print('Body response:')
    print('\t- type: ' + str(type(response)))
    print('\t- content: ' + str(response.read()))
    print('\t- utf8 content: ' + str(response.read().decode('utf-8')))
