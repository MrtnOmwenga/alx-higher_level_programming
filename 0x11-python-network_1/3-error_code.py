#!/usr/bin/python3
""" Handling Error codes """


if __name__ == '__main__':
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.URLError as err:
        print('Error code: {}'.format(err.code))
