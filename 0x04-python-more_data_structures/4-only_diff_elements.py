#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = set()

    for itm in set_1:
        if itm not in set_2:
            result.add(itm)

    for itm in set_2:
        if itm not in set_1:
            result.add(itm)

    return result
