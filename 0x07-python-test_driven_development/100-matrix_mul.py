#!/usr/bin/python3
"""This module contains a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (list of lists): the first matrix
        m_b (list of lists): the second matrix

    Returns:
        list of lists: the product of m_a and m_b

    Raises:
        TypeError: if m_a or m_b is not a list,
        a list of lists, or contains non-numbers
        ValueError: if m_a or m_b is empty or if their shapes are incompatible
    """
    # Validate the inputs
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the product matrix with zeros
    m_p = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform the multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_p[i][j] += m_a[i][k] * m_b[k][j]

    return m_p
