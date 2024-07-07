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

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(f"{x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except Exception as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    main()
