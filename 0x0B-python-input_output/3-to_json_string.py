#!/usr/bin/python3
"""This module returns JSON representation of a string"""
import json


def to_json_string(my_obj):
    """function returns JSON rep of string"""
    return json.dumps(my_obj)
