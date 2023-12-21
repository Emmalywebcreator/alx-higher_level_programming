#!/usr/bin/python3
"""
This module returns the area of the square after
validating the size instance attribute
"""


class Square:
    """
    This method runs each time a new instance of a class is created
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
    """
    This method returns the area when called
    """
    def area(self):
        return(self.__size*self.__size)
