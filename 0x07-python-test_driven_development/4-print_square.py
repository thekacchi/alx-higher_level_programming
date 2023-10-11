#!/usr/bin/python3
"""This module defines a function"""


def print_square(size: int):
    """This function prints # as a square"""

    if type(size) not in [float, int] or type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    size = int(size)
    for x in range(size):
        print('#' * size)
