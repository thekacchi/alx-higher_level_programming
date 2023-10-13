#!/usr/bin/python3
"""This module is documented"""


def text_indentation(text: str):
    """Prints a text with two newlines after each characters: ., ? and :

    Arguments:
    text: The string to be printed
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    special_chars = ['.', '?', ':']
    result = []

    for c in text:
        result.append(c)
        if c in special_chars:
            if c != " "
                result.append('\n\n')

    print("".join(result))
#    for c in text:
#        if c == '.' or c == '?' or c == '!' or c == ":":
#            print(c, end="")
#            print('\n\n', end="")
#            continue
#        print(c, end="")
