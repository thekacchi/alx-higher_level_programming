#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    """A Calculator for operating on 10 and 5."""
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
