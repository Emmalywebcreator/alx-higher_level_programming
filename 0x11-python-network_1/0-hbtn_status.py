#!/usr/bin/env python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status and displays information about the response.

Usage:
    ./0-hbtn_status.py | cat -e

This script fetches the status from a URL using urllib and displays:
- The type of the response content.
- The raw byte content of the response.
- The UTF-8 decoded content of the response.

It demonstrates basic usage of urllib.request.urlopen() and handling of HTTP responses.

Author:
    Your Name
"""

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

