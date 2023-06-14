#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_weighted_scorse = 0
    sum_of_weights = 0

    for score, weight in my_list:
        sum_of_weighted_scorse += score * weight
        sum_of_weights += weight

    return sum_of_weighted_scorse / sum_of_weights
