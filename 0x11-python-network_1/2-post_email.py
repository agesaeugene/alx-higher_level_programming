#!/usr/bin/python3
"""
receives a URL, makes a request to the URL, and shows the value of the X-Request-Id variable that can be found in the response header.
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as r:
        print(r.read().decode("utf-8"))
