#!/usr/bin/python3


def def no_c(my_string):
    return my_string.translate({ord(c): None for c in "Cc"})
