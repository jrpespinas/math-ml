from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.2.0'
__author__: 'Jan Rodolf Espinas'

import matrix_operations # My linear algebra library

def dot_product(A, B):
    """
    Returns `dot_product` from a pair of matrix wherein `A` is transposed
    into a row vector and `B` is a column vector.

    Parameters
    ----------
    A : list
        The given left-hand side transposed matrix.
    B : list
        The given right-hand side matrix.

    Returns
    -------
    dot_product : float
        dot product of two vectors.

    """
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if (A_columns == B_rows)\
    and (A_rows == 1 and B_columns == 1):

        dot_product = []

        # multi-line list comprehension for dot product
        [dot_product.append(sum(A[i][j]*B[j][i] 
        for j in range(A_columns))) 
        for i in range(A_rows)]

        return float(dot_product[0])
        
    else:
        print("dimensions of vector do not match.")

def outer_product(A, B):
    """
    Returns `outer_product` from a pair of vectors wherein 
    `B` is transposed into a row vector and `A` is a column vector.

    Parameters
    ----------
    A : list
        The given left-hand side matrix.
    B : list
        The given right-hand side transposed matrix.

    Returns
    -------
    outer_product : list
        Returns a matrix.
    """    
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])
    
    if A_columns == 1 and B_rows == 1:
    
        outer_product = []

        # multi-line list comprehension for outer product
        [outer_product.append([A[i][0] * B[0][j] for j in range(B_columns)]) 
        for i in range(A_rows)]

        return outer_product

    else:
        print("dimensions of vector do not match.")

if __name__ == '__main__':
    a = matrix_operations.create_matrix()
    b = matrix_operations.create_matrix()
    a = matrix_operations.transpose(a)
    c = dot_product(a,b)
    print(c)
    
    