#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()

    for itm in my_list:
        unique_set.add(itm)

    sum = 0

    for itm in unique_set:

        sum += itm

    return sum
