#!/usr/bin/python3
"""This module is documented"""


def text_indentation(text: str):
    """Prints a text with two newlines after each characters: ., ? and :

    Arguments:
    text: The string to be printed
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    for c in text:
        if c == '.' or c == '?' or c == '!' or c == ":":
            print(c, end="")
            print('\n\n', end="")
        else
            print(c, end="")
