#!/usr/bin/python3
"""
script tp accept an email address and and a URL
"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)
