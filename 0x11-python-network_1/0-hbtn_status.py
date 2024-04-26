#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status
and prints respone body in a given format
"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rep:
        body = rep.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
