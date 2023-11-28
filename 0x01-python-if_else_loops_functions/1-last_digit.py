#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
L = abs(number) % 10
if number < 0:
    L = -(L)
str = "Last digit of {} is {}".format(number, L)
if L > 5:
    print(f"{str} and is greater than 5")
if L == 0:
    print(f"{str} and is 0")
elif L < 6:
    print(f"{str} and is less than 6 and not 0")
