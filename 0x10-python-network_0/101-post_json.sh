#!/bin/bash
# a Bash script that only shows the response's status code after sending a request to a URL supplied as an input.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
