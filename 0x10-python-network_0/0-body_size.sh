#!/usr/bin/env bash
# Takes url, sends request and returns content size
curl -sI REQUEST $1 | grep -iF content-length
