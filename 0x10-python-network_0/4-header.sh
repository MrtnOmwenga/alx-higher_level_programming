#!/bin/bash
# Send get request with parameters
curl -sI -G -H X-School-User-Id:98 $1 | sed '/^200/!d;s/.*\n//'
