#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for item in names:
        if item[0] != '_':
            print("{}".format(item))


if __name__ == "__main__":
    main()
