#!/bin/bash
# sends a POST request to the URL with a json
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "{$1}"
