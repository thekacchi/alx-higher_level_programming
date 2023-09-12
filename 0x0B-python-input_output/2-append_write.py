#!/usr/bin/python3
"""This module contains the definition for append_rite function"""


def append_write(filename="", text=""):
    """Function defines a function that appends text in filename"""
    try:
        with open(filename, 'a', encoding='utf8') as file:
            num_characters_added = file.write(text)
        return num_characters_added
    except Exception:
        return 0
