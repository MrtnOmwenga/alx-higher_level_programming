#!/bin/bash
# Takes url, sends request and returns content size
curl -sI REQUEST $1 | awk '/Content-Length/ {print $2}'
