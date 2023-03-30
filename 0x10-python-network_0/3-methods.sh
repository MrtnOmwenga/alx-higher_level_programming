#!/bin/bash
# Show all methods a URL will allow
curl -s -I -X OPTIONS $1 | awk -vOFS= '/Allow/ {$1=""; print $0}'
