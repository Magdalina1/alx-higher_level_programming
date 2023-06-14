#!/usr/bin/python3
def common_elements(set_1, set_2):

    result = set()

    for itm in set_1:
        if itm in set_2:
            result.add(itm)

    return result
