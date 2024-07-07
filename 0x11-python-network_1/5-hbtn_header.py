#!/usr/bin/python3
"""
 script that takes in a URL, sends a request to the URL and displays
 the value of the variable X-Request-Id in the response header
"""


import requests
import sys


def main():
    """
    sends a request to the URL and displays the value of the
    variable X-Request-Id in the response header
    """

    url = sys.argv[1]
    resp = requests.get(url)
    x_request_id = resp.headers.get("X-Request-Id")
    print(x_request_id)


if __name__ == "__main__":
    main()
