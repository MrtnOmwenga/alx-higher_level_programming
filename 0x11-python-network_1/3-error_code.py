#!/usr/bin/python3
""" Handling Error codes """


if __name__ == '__main__':
    import urllib.request, urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            #response.getcode() == 200
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as error:
        print('Error code: {}'.format(error.code))
