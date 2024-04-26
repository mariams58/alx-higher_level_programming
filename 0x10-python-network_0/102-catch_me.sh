#!/bin/bash
# sends a GET request to 0.0.0.0:5000/catch_men and responds with a message
curl -sLXH PUT "Origin: X-School-User-Id" -d "user_id=98" 0.0.0.0:5000/catch_me
