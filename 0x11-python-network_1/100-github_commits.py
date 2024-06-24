#!/usr/bin/python3
""" This script takes 2 argument ang fetches 10 commits from the github api url
and prints respone body in a given format
"""
import requests
import sys

if __name__ == "__main__":
    a = sys.argv[2]
    b = sys.argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(a, b)
    r = requests.get(url)
    rp = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                rp[i]["sha"],
                rp[i].get('commit').get('author').get('name')))
    except ValueError:
        pass
