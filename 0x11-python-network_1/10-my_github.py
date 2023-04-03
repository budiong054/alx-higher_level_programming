#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = f"https://api.github.com/user"

    response = requests.get(url, auth=(user, passwd))
    json = response.json()
    print(json.get('id'))
