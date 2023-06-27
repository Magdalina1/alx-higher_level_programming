#!/usr/bin/python3
"""this module defines a class square"""


def is_palindrome(string):
    """
    Determine if a string is a palindrome.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return string == string[::-1]
