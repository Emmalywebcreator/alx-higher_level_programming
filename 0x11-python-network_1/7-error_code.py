#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL 
and displays the body of the response
"""


import sys
import requests


def main():
    """
    Display the body of the response.
    """

    url = sys.argv[1]
    try:
        r = requests.get(url)
        status = r.status_code
        print(r.text)
    except Exception as err:
        if err >= 400:
            print(f"Error code: {err}")


if __name__ == "__main__":
    main()
