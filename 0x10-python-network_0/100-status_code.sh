#!/bin/bash
# Displays the status code for request to the url passsed as 1st arg
curl -s -o /dev/null -w "%{http_code}" "$1"
