#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    i = 0
    for blk in matrix:
        for item in blk:
            i += 1
            print("{:d}".format(item), end='')
            if i < 3:
                print(" ",end='')
        print()


if __name__ == "__print_matrix_integer__":
    print_matrix_integer(matrix)
