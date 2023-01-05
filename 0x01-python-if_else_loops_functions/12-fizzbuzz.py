#!/usr/bin/python3


def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0:
            x = "Fizz"
        elif x % 5 == 0:
            x = "Buzz"
        elif x % 5 == 0 and x % 3 == 0:
            x = "FizzBuzz"
        print({}.format(x), end=' ')
