#!/bin/bash
# Acceps a URL, sends a Post Request and shows the response body
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD" $1
