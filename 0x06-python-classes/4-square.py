#!/usr/bin/python3
"""
This is module uses setters, property operators
and getters
"""


class Square:
    """
    This method runs each time a new instance
    of a class is created
    """
    def __init__(self, size=0):
        self.__size = size
    """
    This method return the area when called
    """
    def area(self):
        return(self.__size*self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
