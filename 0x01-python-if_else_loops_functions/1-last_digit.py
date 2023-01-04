#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    if number > 0:
        digit = abs(number) % 10
    else:
        digit = -1 * (abs(number) % 10)
    return(digit)


ld = last_digit(number)
if ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, ld))
elif ld == 0:
    print("Last digit of {} is {} and is 0".format(number, ld))
elif ld < 6 and ld != 0:
    print("Last digit of %d is %d and is less than 6 and not 0" % (number, ld))
