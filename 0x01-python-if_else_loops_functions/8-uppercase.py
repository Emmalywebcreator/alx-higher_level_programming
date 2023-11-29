#!/usr/bin/python3
def uppercase(s):
    for i in s:
        temp = i
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(i) - 32)
        print("{}".format(temp), end='')
    print()
