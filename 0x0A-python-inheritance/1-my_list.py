#!/usr/bin/python3
"""This is the main module of this project"""


class MyList(list):
    """Class MyList inherits from list"""

    def print_sorted(self):
        """Prints the list, in ascending sort."""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
