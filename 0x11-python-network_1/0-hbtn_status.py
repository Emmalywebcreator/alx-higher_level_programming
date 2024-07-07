#!/usr/bin/env python3

import urllib.request

""" URL to fetch """
url = 'https://alx-intranet.hbtn.io/status'

""" Fetch the URL and handle the response"""
with urllib.request.urlopen(url) as response:
    """ Read the response content (bytes)"""
    body = response.read()

    """ Display information about the response"""
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))

