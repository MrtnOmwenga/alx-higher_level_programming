#!/bin/bash
# Display body of a response
curl -sI $1 | awk '/Body/ {print $2}'
