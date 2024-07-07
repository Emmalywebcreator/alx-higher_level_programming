#!/usr/bin/python3

import urllib.request
import sys
import urllib.parse

"""takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter
"""


def main():
    """
    Send a POST request with an email parameter to a specified URL and
    display the decoded body of the response.
    """
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    response_body = urllib.request.Request(url, data)
    with urllib.request.urlopen(response_body) as res:
        print(res.read().decode('utf8'))


if __name__ == "__main__":
    main()
