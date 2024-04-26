#!/bin/bash
# Displays the http method
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
