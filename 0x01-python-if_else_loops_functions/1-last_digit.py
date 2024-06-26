#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sta = "Last digit"
end = "and is 0"
y = number
if number < 0:
    y = y * -1
    x = y % 10
    end = "and is less than 6 and not 0"
else:
    x = y % 10
    if y % 10 > 5:
        end = "and is greater than 5"
    elif y % 10 < 6 and y % 10 != 0:
        end = "and is less than 6 and not 0"
print(f"{sta} of {number:d} is {x * -1 if number<0 else x} {end}")
