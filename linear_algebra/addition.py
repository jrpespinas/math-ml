from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

import matrix_operations # My linear algebra library

def add(A, B):
    """
    Returns `sum` from a pair of matrix
    with matching dimensions.

    Parameters
    ----------
    A : list
        The given left-hand side matrix.
    B : list
        The given right-hand side matrix.

    Returns
    -------
    sum : list
        The sum of two given matrix.

    """
    if (len(A[0]) == len(B[0])) \
    and (len(A) == len(B)):

        rows = len(A)
        columns = len(A[0])

        sum = []

        [sum.append([A[i][j] + B[i][j]
        for j in range(columns)])
        for i in range(rows)]

        return sum

    else:
        print("Dimensions are not matched")
        

if __name__ == '__main__':
    a = matrix_operations.create_matrix()
    b = matrix_operations.create_matrix()
    c = add(a,b)
    matrix_operations.display(c)