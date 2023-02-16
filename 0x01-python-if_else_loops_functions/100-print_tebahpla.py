#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 == 0:
        i = i + 32
    x = chr(i)
    print("{}".format(x), end='')
