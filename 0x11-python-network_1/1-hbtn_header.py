#!/usr/bin/python3
"""
Retrieve and display the X-Request-Id header value from a URL.

This script takes a URL as input, sends a request to the URL using urllib,
and prints the value of the X-Request-Id header found in the response.
"""


import urllib.request
import sys


def main():
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = dict(response.headers).get('X-Request-Id')
        print(f"{x_request_id}")


if __name__ == "__main__":
    main()
