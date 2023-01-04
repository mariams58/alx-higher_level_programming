#!/usr/bin/python3

def uppercase(str):
    for i in str:
        x = ord(i)
        print("{}".format(chr(x - 32)), end='')
    print("{}".format(chr(10)), end='')
