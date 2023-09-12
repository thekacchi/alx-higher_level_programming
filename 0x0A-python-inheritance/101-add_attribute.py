#!/usr/bin/python3
"""this module defines a function"""


def add_attribute(obj, attribute_name, attribute_value):
    """adds new attribute to object if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute_name, attribute_value)
    else:
        raise TypeError("can't add new attribute")
