#!/usr/bin/python3
""" This scrip[t post an email to the given hostname from the cli args
and prints respone body in a given format
"""
import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    r = requests.post(sys.argv[1], data={'email': email})
    print(r.text)
