#!/bin/bash
# accepts an argument as a url, sends a get request to the url and displays the body of the response

curl -sX "GET" -H 'X-School-User-Id: 98' "$1"
