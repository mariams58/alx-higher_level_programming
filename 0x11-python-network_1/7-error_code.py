#!/usr/bin/python3
""" This script fetchesurl given drom the cli
and prints error code in a given format
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error Code: {}".format(r.status_code))
    else:
        print(r.text)
