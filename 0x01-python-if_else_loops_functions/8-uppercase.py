#!/usr/bin/python3


def uppercase(str):
    for i in str:
        x = ord(i)
        if x > 96 and x < 123:
            i = chr(x - 32)
        print("{}".format(i), end='')
    print()
