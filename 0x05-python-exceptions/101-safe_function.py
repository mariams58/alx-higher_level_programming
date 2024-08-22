#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as error:
        res = None
        print("Exception: {}".format(error), file=sys.stderr)
    finally:
        return res
