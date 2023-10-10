#!/usr/bin/python3
"""
Definies a function that adds integers
"""


def add_integer(a, b=98) -> int:
    """Return the sum of a and b

    Float arguments are typecasted to ints before addition

    Raises: TypeError if either of a or b is a non-integer and non-float
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
