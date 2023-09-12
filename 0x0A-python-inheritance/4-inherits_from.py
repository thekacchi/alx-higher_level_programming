#!/usr/bin/python3
"""This module defines a function"""

def inherits_from(obj, a_class):
    """
    This function checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    """
    obj_class = obj.__class__

    if issubclass(obj_class, a_class):
        return True

    for base_class in obj_class.__bases__:
        if inherits_from(base_class, a_class):
            return True

    return False
