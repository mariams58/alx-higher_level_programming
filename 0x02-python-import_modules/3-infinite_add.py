#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the sum of number as args passed"""
    import sys
    size = len(sys.argv)
    add = 0
    i = 1
    while size > i:
        add += int(sys.argv[i])
        i += 1
    print("{:d}".format(add))
