#!/usr/bin/python3


def multiple_returns(sentence):
    i = len(sentence)
    if sentence and i > 0:
        b = sentence[0]
    else:
        b = "None"
    x = i, b
    return x
