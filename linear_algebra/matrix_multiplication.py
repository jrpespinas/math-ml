from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.2'
__author__: 'Jan Rodolf Espinas'

# import local file containing matrix operations
import matrix_operations

def matrix_mul(matrix_one, matrix_two):
    if len(matrix_one[0]) == len(matrix_two):
        product_matrix = []
        product_matrix_rows = len(matrix_one)
        product_matrix_columns = len(matrix_two[0])
        
        matrix_two = matrix_operations.transpose(matrix_two)
        
        # prints indices
        for row in range(product_matrix_rows):
            product_matrix.append([(row,column) for column in range(product_matrix_columns)])

    else:
        print('The matrix can not be multiplied.\n \
         Be sure to input the right dimensions of both matrix.')

    return product_matrix

if __name__ == '__main__':
    A = matrix_operations.create_matrix()
    B = matrix_operations.create_matrix()
    C = matrix_mul(A,B)
    matrix_operations.display(C)

