#!/usr/bin/python3
"""The say my name module creates a function"""

def say_my_name(first_name, last_name=""):
    """This function prints first_name and last_name

    Args:
        first_name: first name string
        last_name: last name string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('{} {}'.format(first_name, last_name))
