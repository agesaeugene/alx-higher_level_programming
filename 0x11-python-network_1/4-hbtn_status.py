#!/usr/bin/python3
# a get request to a given URL package is requested
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)
