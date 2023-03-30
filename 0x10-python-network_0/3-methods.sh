#!/bin/bash
# Show all methods a URL will allow
curl -s -I -X OPTIONS $1 | awk '/Allow/ {$1=""; print substr($0,2)}'
