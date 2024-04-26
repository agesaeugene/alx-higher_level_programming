#!/usr/bin/python3
"""
accepts a URL, makes a request to the URL, and shows the value of the X-Request-Id variable that can be found in the response's header.
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as r:
        print(r.headers.get('X-Request-id'))
