from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.1.3'
__author__: 'Jan Rodolf Espinas'

# import local file containing matrix operations
import matrix_methods as mm

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
    
    [transposed_matrix.append([matrix[j][i] for j in range(rows)])
    for i in range(columns)]

    return transposed_matrix

if __name__ == '__main__':
    A = mm.create_matrix()
    transpose(A)
    mm.display(A)