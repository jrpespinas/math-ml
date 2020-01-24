from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.2.0'
__author__: 'Jan Rodolf Espinas'

import matrix_operations # My linear algebra library

def vector_multiplication(matrix_one, matrix_two):
    matrix_one_rows = len(matrix_one)
    matrix_one_columns = len(matrix_one[0])

    matrix_two_rows = len(matrix_two)
    matrix_two_columns = len(matrix_two[0])

    # inner product
    if (matrix_one_columns == matrix_two_rows)\
    and (matrix_one_rows == 1 and matrix_two_columns == 1):

        dot_product = []

        for row in range(matrix_one_rows):
            dot_product.append(
                sum([
                    matrix_one[row][col]*matrix_two[col][row]
                    for col in range(matrix_one_columns)
                ])
            )
 
        return dot_product

    # outer product
    elif matrix_one_columns == 1 and matrix_two_rows == 1:
    
        outer_product = []

        for row in range(matrix_one_rows):
            outer_product.append([
                matrix_one[row][0] * matrix_two[0][col]
                for col in range(matrix_two_columns)
            ])

        return outer_product
    
    else:
        print("dimensions of vector do not match.")

if __name__ == '__main__':
    a = matrix_operations.create_matrix()
    b = matrix_operations.create_matrix()
    b = matrix_operations.transpose(b)
    c = vector_multiplication(a,b)
    matrix_operations.display(c)
    
    