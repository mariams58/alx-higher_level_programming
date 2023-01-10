#!/usr/bin/python


def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for item in list:
            print("{:d}".format(item), end=' ')
        print()


if __name__ == "__print_matrix_integer__":
    print_matrix_integer(matrix)
