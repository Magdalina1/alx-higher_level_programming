#!/usr/bin/python3
"""Defines a Base class for other classes in the project."""


import json
import os
import csv


class base:
    """Private class attribute: __nb_objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a Base instance."""

        if type(id) != int and id is not None:
            raise TypeError("id most be integer")

        if id not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
