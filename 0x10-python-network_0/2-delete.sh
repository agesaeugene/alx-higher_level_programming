#!/bin/bash
# A Bash script that shows the body of the response after sending a DELETE request to the URL supplied as the first parameter
curl -sX DELETE "$1"
