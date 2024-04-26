#!/bin/bash
# terminates a JSON POST request to a URL supplied as the first argument and shows the response's body.
curl -sL -X PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: HolbertonSchool"
