#!/usr/bin/python3

import urllib.request
import sys


def main():
    """
    Send a POST request with an email parameter to a specified URL and
    display the decoded body of the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = 'email=' + urllib.parse.quote(email)

    try:
        with urllib.request.urlopen(url, data=data.encode('utf-8'))
        as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except Exception as e:
        print(f"Error sending POST request: {e}")


if __name__ == "__main__":
    main()
