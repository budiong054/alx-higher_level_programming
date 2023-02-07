#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL -w "%{http_code}" $1 -o /dev/null | grep -q "200" && curl -sL $1
