#!/usr/bin/python3


def no_c(my_string):
    n_str = ''
    size = len(my_string)
    for x in range(size):
        if my_string[x] != 'c' and my_string[x] != 'C':
            n_str = n_str + my_string[x]
    return n_str


if __name__ == "__no_c__":
    no_c(my_string)
