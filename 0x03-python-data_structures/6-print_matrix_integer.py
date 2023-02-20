#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for blk in matrix:
        for item in blk:
            print("{:d}".format(item), sep = ' ')
        print()


if __name__ == "__print_matrix_integer__":
    print_matrix_integer(matrix)
