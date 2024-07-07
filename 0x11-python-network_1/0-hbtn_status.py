#!/usr/bin/python3
"""Display information about the response"""

import urllib.request

def main():
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))

if __name__ == "__main__":
    main()

