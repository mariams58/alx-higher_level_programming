#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io
and displays the value of X-Request-Id
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as rep:
        body = rep.read()
        print(rep.headers['X-Request-Id'])
