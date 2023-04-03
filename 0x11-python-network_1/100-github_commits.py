#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of the
    repository "rails" by user "rails"
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    json = response.json()
    i = 0
    for data in json:
        i += 1
        name = data.get('commit').get('author').get('name')
        sha = data.get('sha')
        print(f"{sha}: {name}")
        if i == 10:
            break
