#!/bin/bash
# get request is sent to a given URL and response status code is displayed
curl -so /dev/null --write-out "%{http_code}" "$1"
