#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = str[i]
        if ord(x) > 96:
            x = ord(x) - 32
        print("{}".format(chr(x)), end='')
