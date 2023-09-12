#!/usr/bin/python3
"""This modeyle defines my int"""


class MyInt(int):
    """definition of class My_int"""
    def __eq__(self, other):
        """method inverts the == sign"""
        return super().__ne__(other)

    def __ne__(self, other):
        """method inverts the != sign"""
        return super().__eq__(other)
