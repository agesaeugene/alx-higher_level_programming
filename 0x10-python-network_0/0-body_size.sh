#!/bin/bash
#receives a URL, makes a request to that URL, and shows the size of the return body.
curl -s "$1" | wc -c
