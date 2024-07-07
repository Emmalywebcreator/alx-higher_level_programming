#!/usr/bin/python3
"""This a script that fetches https://alx-intranet.hbtn.io/status"""


import requests


def main():
    url = 'https://alx-intranet.hbtn.io/staus'
    body = requests.get(url)
    print("body response:")
    print("\t- type:",  type(body))
    print("\t- content:", body)


if __name__ == '__main__':
    main()
