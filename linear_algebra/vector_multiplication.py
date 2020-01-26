from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.3.0'
__author__: 'Jan Rodolf Espinas'

import matrix_methods as mm # My linear algebra library

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

    if (A_columns == B_rows) and (A_rows == 1 and B_columns == 1):

        dot_product = []
        
        dot_product.append(sum([A[0][i]*B[i][0] for i in range(A_columns)]))

        return float(dot_product)
        
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
    print(A)
    print(B)
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
    A = mm.create_matrix() # [[1,2,3]]
    B = mm.create_matrix() #[[1],[2],[3]]
    C = dot_product(A,B)
    print(C)
    
    