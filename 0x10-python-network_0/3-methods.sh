#!/bin/bash
# Show all methods a URL will allow
curl -s -i -L -X OPTIONS $1 | awk '/Allow/ {print $2 $3 $4 $5}'
