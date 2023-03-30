#!/usr/bin/env bash
# Takes in a URL, sends a request to that URL
# and displays the size of the body of the response

curl -sI REQUEST $1 | grep -iF content-length
