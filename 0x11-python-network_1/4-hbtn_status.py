#!/usr/bin/python3
"""This a script that fetches https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""


import requests


def main():
    """
    Fetches the url and print the response body
    """

    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    body = resp.text()
    print("body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    main()
