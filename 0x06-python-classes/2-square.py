#!/usr/bin/python3
"""This module raises errors when the value passed to size is 
nt a positive integer"""


class Square:
    """The class Square"""
    def __init__(self, size=0):
        self.__size = size

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
