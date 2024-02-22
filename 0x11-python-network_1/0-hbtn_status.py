#!/usr/bin/python3
"""Fetch web response of url"""

import urllib.request

if __name__ == "__main__":
    """documentstion here"""
    with urllib.request.urlopen(
        'https://alx-intranet.hbtn.io/status'
    )
    as response:
        content = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
    print('\t- utf8 content: {}'.format(str(content)[2:-1]))
