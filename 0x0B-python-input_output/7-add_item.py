#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


try:
    my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
