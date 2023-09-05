#!/usr/bin/python3
"""This module defines ythe square class"""


class Square:
    """Addition: Solves for area"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        return self._size * self._size

    @property
    def size(self):
        """Getter method for size attribute"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter method for size attribute"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def my_print(self):
        """Method prints new line"""
        if self._size == 0:
            print()
        elif isinstance(self._size, int) is True:
            for i in range(self._size):
                for i in range(self._size):
                    print("#", end="")
                print()
