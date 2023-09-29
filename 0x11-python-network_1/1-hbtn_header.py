#!/usr/bin/python3
"""Displays the value of the X-Request-Id found in the header of a response"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        body = response.info()
        print(body.get('X-Request-Id'))
