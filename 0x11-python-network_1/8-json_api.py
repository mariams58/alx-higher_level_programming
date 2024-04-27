#!/usr/bin/python3
""" This script fetches http://0.0.0.0:5000/search_user
and prints respone body in json format
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        val = {'q':sys.argv[1]}
    else:
        val = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data= val)
    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
    except ValueError:
        print("Not a valid JSON")
