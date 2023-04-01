#!/usr/bin/python3
"""  Fetch requests """


import requests


data = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(data.text)))
print('\t- content: {}'.format(data.text))
