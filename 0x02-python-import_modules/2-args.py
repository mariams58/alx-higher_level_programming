#!/usr/bin/python3
if __name__ == "__main__":
    """Prints args and um of args passed"""
    import sys
    num = len(sys.argv)
    if num <= 1:
        print("0 arguments")
    else:
        if num > 2:
            print("{} arguments:".format(num - 1))
            for i in range(1, num):
                print("{}: {}".format(i, sys.argv[i]))
        else:
            print("{} argument:".format(num - 1))
            print("{}:{}".format(num - 1, sys.argv[1]))
