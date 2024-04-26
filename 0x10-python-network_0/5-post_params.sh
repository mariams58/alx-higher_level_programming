#!/bin/bash
# sends a post request with email
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
