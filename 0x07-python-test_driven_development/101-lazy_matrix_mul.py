#!/usr/bin/python3
import numpy

def lazy_matrix_mul(m_a, m_b):
    """
    This function multiply two matrices m_a and m_b.

    Parameters
    ----------
    m_a : numpy.ndarray
        A 2D matrix.
    m_b : numpy.ndarray
        A 2D matrix.

    Returns
    -------
    m_c : numpy.ndarray
        A 2D matrix.
    """
     m_c = numpy.zeros((m_a.shape[0], m_b.shape[1]))
     for i in range(m_a.shape[0]):
         for j in range(m_b.shape[1]):
             for k in range(m_a.shape[1]):
                 m_c[i, j] += m_a[i, k] * m_b[k, j]
    return m_c
