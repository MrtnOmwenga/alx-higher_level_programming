#!/bin/bash
# POST using a file
curl -s -H 'Content-Type: application/json' -d "$(cat "$2")" -X POST "$1"
