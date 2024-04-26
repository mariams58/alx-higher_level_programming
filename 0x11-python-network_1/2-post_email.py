#!/usr/bin/python3
""" This script ppst email to https://alx-intranet.hbtn.io
and fetches content
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    val = {'email': email}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as rep:
        body = rep.read()
        print(body.decode("utf-8"))
