#!/usr/bin/python3
""" POST an email """


if __name__ == '__main__':
    import requests
    import sys

    email_dict = {'email': sys.argv[2]}
    data = requests.post(sys.argv[1], json=email_dict)
    print(data.text)
