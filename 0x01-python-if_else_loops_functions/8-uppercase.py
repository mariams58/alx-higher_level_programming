#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = str[i]
        x = ord(x) - 0
        if x > 96:
            x = x - 32
        print("{}".format(chr(x)), end='')
    print()
