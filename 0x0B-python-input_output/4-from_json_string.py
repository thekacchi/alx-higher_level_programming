#!/usr/bin/python3
"""This module returns object represented byJSON sring"""
import json


def from_json_string(my_obj):
    """function returns object of JSON string"""
    return json.loads(my_obj)
