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
    
    [transposed_matrix.append([matrix[i][j] for i in range(rows)])
    for j in range(columns)]

    return transposed_matrix


def main():
    A = mm.create_matrix()
    mm.display(A)
    print('\n')
    A = transpose(A)
    mm.display(A)
    
if __name__ == '__main__':
    main()