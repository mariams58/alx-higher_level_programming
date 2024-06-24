#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status
and prints respone body in a given format
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
