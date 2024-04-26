#!/usr/bin/python3
"""
value of the variable X-Request-Id is displayed
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-id'))
