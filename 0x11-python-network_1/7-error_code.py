#!/usr/bin/python3
""" Handling HTTPError """


if __name__ == '__main__':
    import requests
    import sys

    data = requests.get(sys.argv[1])

    if data.status_code == 200:
        print(data.text)
    else:
        print('Error code: {}'.format(data.status_code))
