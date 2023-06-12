#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for m in my_string:
        if m != 'c' and m != 'C':
            new_str += m
            return new_str
