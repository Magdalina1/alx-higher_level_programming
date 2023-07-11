#!/usr/bin/python3
"""Reads from a file and prints."""


def read_file(filename=""):
    """Reads from filename and prints its contents to stdout."""
    with open(filename) as file:
        read_text = f.read()
        print(read_text, end="")
