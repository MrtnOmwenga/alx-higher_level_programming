#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        first = sentence[1]
        length = len(sentence)
    else:
        first = None
        length = 0
    tup = (length, first)
    return (tup)
