#!/usr/bin/python3
""" a get request to a given URL package is requested"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)

