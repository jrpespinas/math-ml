from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.2'
__author__: 'Jan Rodolf Espinas'

# import local file containing matrix operations
import matrix_operations

def transpose(matrix):
    """
    Returns `transposed_matrix` from a given matrix 
    by appending its contents to an empty list with
    a switched rows and columns.

    Parameters
    ----------
    matrix : list
        The given matrix.

    Returns
    -------
    transposed_matrix : list
        The transposed matrix
    """
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = []
    
    for col in range(0, columns):
        transposed_matrix.append([
            matrix[i][col] 
            for i in range(rows)
        ])

    return transposed_matrix

if __name__ == '__main__':
    A = matrix_operations.create_matrix()
    transpose(A)
    matrix_operations.display(A)