#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        row_new = []

        for itm in row:
            row_new.append(itm ** 2)

        new_matrix.append(row_new)

    return new_matrix
