#!/usr/bin/python3
"""Sends a request to the passed URL and displays
the body of the response(decoded in utf-8)"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e}")
