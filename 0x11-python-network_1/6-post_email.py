#!/usr/bin/python3
"""Make a POST to passed url with email as parameter
and display the body of the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.post(url, data={'email': sys.argv[2]})
    print(res.text)
