#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if isinstance(key, str) and key != "":
        if a_dictionary is not None:
            a_dictionary[key] = value

