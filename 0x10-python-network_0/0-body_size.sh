#!/bin/bash
# gets the size of an hhtp response in bytes
curl -s "$1" | wc -c
