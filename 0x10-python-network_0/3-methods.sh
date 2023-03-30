#!/bin/bash
# Show all methods a URL will allow
curl -s -i -L -X OPTIONS $1 | awk '/Allow/ {$1=""; print $0}'
