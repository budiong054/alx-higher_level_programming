#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
    "http://0.0.0.0:5000/search_user" with the
    letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    response = requests.post(url, data={'q': q})
    json = res.json()
    if len(json) == 0:
        print("No result")
    else:
        print(f"[{json.get('id')}] {json.get('name')}")
