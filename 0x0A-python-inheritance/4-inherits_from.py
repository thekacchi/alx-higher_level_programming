#!/usr/bin/python3
"""This module defines a function"""


def inherits_from(obj, a_class):
    """
    This function checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    """
    obj_classes = [obj.__class__]

    while obj_classes:
        curr_class = obj_classes.pop()

        if issubclass(curr_class, a_class) and curr_class is not a_class:
            return True

        obj_classes.extend(base_class for base_class in curr_class.__bases__)

    return False
