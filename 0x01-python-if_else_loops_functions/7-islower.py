#!/usr/bin/python3


def islower(c):
    test = ord(c)
    if test > 122 or test < 97:
        return(False)
    else:
        return(True)
