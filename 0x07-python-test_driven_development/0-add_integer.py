#!/usr/bin/python3
"""Definies a function that adds integers"""


def add_integer(a, b=98):
    """Return the sum of a and b

    Float arguments are typecasted to ints before addition

    Raises: TypeError if either of a or b is a non-integer and non-float
    """

    if ((not isinstance(a, int) and not isinstance(a, float)))
        raise TypeError("a must be an integer")
    if((not isintance(b, int) and not isinstance(b, float)))
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
