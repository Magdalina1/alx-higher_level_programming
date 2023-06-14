#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result = {}

    for key, value in a_dictionary.itm():
        result[key] = value * 2

    return result
