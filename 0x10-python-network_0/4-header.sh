#!/bin/bash
# accepts an argument as a url, sends a get request to the url and displays the body of the response

curl -sH "X-School-User-Id: 98" "$1"
