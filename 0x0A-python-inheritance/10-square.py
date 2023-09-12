#!/usr/bin/python3
"""This module defines class (child) Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inherits Square"""

    def __init__(self, size):
        """Initializes class Square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """string rep"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
