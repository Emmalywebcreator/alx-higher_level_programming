#!/usr/bin/python3
"""
This module validates the size instance attribute
"""


class Square:
    """
    The init is an instance of the Square class
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
