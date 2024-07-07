#!/usr/bin/python3
"""Retrieve and display the X-Request-Id header value from a URL"""

import urllib.request
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python get_request_id.py <URL>")
        return
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.getheader('X-Request-Id')
            if request_id:
                print(f"{request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except Exception as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    main()
