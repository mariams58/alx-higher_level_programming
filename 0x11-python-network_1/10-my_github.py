#!/usr/bin/python3
""" This script that takes your github credentials and displays your
github id using the GITAPI
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=auth)
    print(r.json().get['id'])
