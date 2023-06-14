#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    for itm in my_list:
        if itm == search:
            new_list.oppend(replace)

        else:
            new_list.oppend(itm)

    return new_list
