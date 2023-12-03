#!/usr/bin/python3

# Assigning values to variables a and b
a = 1
b = 2

# Importing the add function from add_0.py
from add_0 import add

# Using string.format to print the result
print("{} + {} = {}".format(a, b, add(a, b)))

