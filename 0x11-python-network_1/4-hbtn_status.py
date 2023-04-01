#!/usr/bin/python3
"""Fetch "https://alx-intranet.hbtn.io/status"
"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    body = requests.get(url).text
    print(f"Body response:\n\t- type: {type(body)}"
          f"\n\t- content: {body}")
