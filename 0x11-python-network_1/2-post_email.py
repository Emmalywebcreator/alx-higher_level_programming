#!/usr/bin/python3

import urllib.request
import sys

"""takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter
"""


def main():
    """
    Send a POST request with an email parameter to a specified URL and
    display the decoded body of the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('ascii')
    try:
        with urllib.request.urlopen(url, data=encoded_data) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except Exception as e:
        print(f"Error sending POST request: {e}")


if __name__ == "__main__":
    main()
