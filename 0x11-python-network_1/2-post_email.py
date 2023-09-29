#!/usr/bin/python3
"""Make a POST to passed url with email as parameter
and display the body of the response(decoded in utf-8"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
