#!/usr/bin/python3
"""
This module prints the square using #
"""


class Square:
    """
    This module always runs
    """
    def __init__(self, size=0):
        self.__size = size
    def area(self):
        """
        Return the area
        """
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
    def my_print(self):
        """
        Prints the Value using # to print a square
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
