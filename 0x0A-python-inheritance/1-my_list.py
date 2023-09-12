#!/usr/bin/python3
"""This moduloe defines a class tht inherits from built-in list"""


class MyList(list):
    """
    Class inherits attributes, methods and properties from list class
    """

    def print_sorted(self):
        """
        Method for printing sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
