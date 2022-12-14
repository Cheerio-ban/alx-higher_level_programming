#!/usr/bin/python3

"""Defines a Square class"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """
        Initializes a square class
        and validates the argument

        Args:
            size (int): The size of a square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
