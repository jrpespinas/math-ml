from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.2'
__author__: 'Jan Rodolf Espinas'

# import local file containing matrix operations
import matrix_methods as mm

def matrix_mul(A, B):
    """
    Returns `product` from a pair of matrix with 
    a matching number of columns from the first matrix 
    and rows from the second matrix.

    Parameters
    ----------
    A : list
        The given left-hand side matrix.
    B : list
        The given right-hand side matrix.

    Returns
    -------
    product : list
        The product of two given matrix.

    """
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if A_columns == B_rows:
        product = []
        product_rows = A_rows
        product_columns = B_columns      

        [product.append([sum([A[i][k]*B[k][j] for k in range(A_columns)]) 
        for j in range(product_columns)]) 
        for i in range(product_rows)]

        return product

    else:
        print('The matrix can not be multiplied.\n \
         Be sure to input the right dimensions of both matrix.')

    return product

if __name__ == '__main__':
    A = [[3,1,1],[8,2,7],[6,1,8]]
    B = [[5,3,0],[3,7,0],[7,4,4]]
    C = matrix_mul(A,B)
    mm.display(C)
