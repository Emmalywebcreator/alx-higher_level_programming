#!/usr/bin/python3
"""This a script that fetches https://alx-intranet.hbtn.io/status"""

import requests


def main():
    url = 'https://alx-intranet.hbtn.io/status'
    body = requests.get(url)
    print("body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))


if __name__ == '__main__':
    main()
