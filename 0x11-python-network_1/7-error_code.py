#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body of the response.

If the HTTP status code is greater than or equal to 400,
prints: Error code: followed by the value of the HTTP status code.
"""

import sys
import requests


def main():
    """
    Display the body of the response.
    """

    url = sys.argv[1]
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code >= 400:
            print(f"Error code: {status_code}")
        else:
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
