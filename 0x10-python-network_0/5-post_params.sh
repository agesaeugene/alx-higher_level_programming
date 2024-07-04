#!/bin/bash
# Acceps a URL, sends a Post Request and shows the response body
curl -sX POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" 
