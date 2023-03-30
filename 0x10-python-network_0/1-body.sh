#!/bin/bash
# Display body of a response
curl -s -w "%{http_code}" $1 | grep -q 200 && curl -s $1 | cat
