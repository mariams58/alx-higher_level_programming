#!/bin/bash
# sends a GET request to 0.0.0.0:5000/catch_men and responds with a message
curl -sX PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
