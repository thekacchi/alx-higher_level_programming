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
