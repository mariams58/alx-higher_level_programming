#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status
and prints respone body in a given format
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get['X-Request-Id'])
