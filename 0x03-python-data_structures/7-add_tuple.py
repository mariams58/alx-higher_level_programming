#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)
    if tuple_a and tuple_b:
        if i == j:
            x = tuple_a[0] + tuple_b[0]
            y = tuple_a[1] + tuple_b[1]
        elif i < j:
            y = tuple_b[1]
        elif j < i:
            y = tuple_a[1]
    if i == 0:
        return(tuple_b)
    if j == 0:
        return(tuple_a)
    tuple_n = (x, y)
    return(tuple_n)


if __name__ == "__add_tuple__":
    add_tuple(tuple_a, tuple_b)
