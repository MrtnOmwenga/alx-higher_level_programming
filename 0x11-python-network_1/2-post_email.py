#!/usr/bin/python3
""" POST request """


if __name__ == '__main__':
    from urllib import request, parse
    import sys

    email_dict = {'email': sys.argv[2]}
    data = parse.urlencode(email_dict).encode()
    req = request.Request(sys.argv[1], data=data)

    with request.urlopen(req) as response:
        print(response.read())
