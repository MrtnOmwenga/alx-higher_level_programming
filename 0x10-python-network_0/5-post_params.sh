#!/bin/bash
# Curl DELETE request
curl -s -d 'email=test@gmail.com&subject=I will always be here for PLD' -X POST $1
