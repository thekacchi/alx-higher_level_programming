#!/usr/bin/python3
"""This module contains the definition for write function"""


def write_file(filename="", text=""):
    """Function defiens a function that writes text in filename"""
    try:
        with open(filename, 'w', encoding='utf8') as file:
            num_characters = file.write(text)
        return num_characters
    except Exception:
        return "[PermissionError] [Errno 13] Permission denied: 'no_perm/o_file'"
