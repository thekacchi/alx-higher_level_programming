#!/usr/bin/python3
"""This module is well documented"""


def text_indentation(text: str):
    """Prints a text with two newlines after each characters: ., ? and :

    Arguments:
    text: The string to be printed
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    skip_space = True

    for c in text:
        if c == '.' or c == '?' or c == '!' or c == ":":
            print(c, end="")
            print('\n\n', end="")
            skip_space = True
        elif c == ' ' and skip_space:
            continue
        else:
            print(c, end="")
            skip_space = False
