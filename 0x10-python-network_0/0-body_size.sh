#!/bin/bash
#receives a URL, makes a request to that URL, and shows the size of the return body.
curl -sI "$1" | grep Content-Length | cut -d " " -f 2-

