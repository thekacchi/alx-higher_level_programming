#!/usr/bin/python3
"""This module defines ythe square class"""


class Square:
    """Addition: Solves for area"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
        self._position = position

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

    @property
    def position(self):
        """Getter method"""
        return self._position

    @position.setter
    def position(self, position):
        """Setter method"""
        if type(position) is not tuple or (position[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(position[0], int) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(position[1], int) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = position

    def my_print(self):
        """Method prints new line"""
        if type(self._position) is not tuple or (self._position[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(self._position) != 2 or (self._position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(self._position[0], int) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(self._position[1], int) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        if self._size == 0:
            print()
        elif isinstance(self._size, int) is True:
            if self._size == 0:
                print()
                return

            print(end='\n' * self._position[1])
            for i in range(self._size):
                print(f"{' ' * self._position[0]}{'#' * self._size}")
