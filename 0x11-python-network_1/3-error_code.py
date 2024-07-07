#!/usr/bin/python3
"""
This script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
from urllib.error import HTTPError
import sys


def main():
    try:
        url = sys.argv[1]
        res = urllib.request.Request(url)
        with urllib.request.urlopen(res) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


if __name__ == '__main__':
    main()
