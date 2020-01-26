from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

import matrix_methods as mm # My linear algebra library

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
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if (A_columns == B_columns) and (A_rows == B_rows):

        sum = []

        [sum.append([A[i][j] + B[i][j] for j in range(A_columns)])
        for i in range(A_rows)]

        return sum
        

if __name__ == '__main__':
    a = mm.create_matrix()
    b = mm.create_matrix()
    c = add(a,b)
    mm.display(c)