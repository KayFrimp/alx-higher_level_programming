#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.h\
btn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"     - body: {type(body)}")
        print(f"     - content: {body}")
        print(f"     - utf8 content: {body.decode('utf-8')}")
