from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

import matrix_operations # My linear algebra library

def add(matrix_one, matrix_two):
    if (len(matrix_one[0]) == len(matrix_two[0])) \
    and (len(matrix_one) == len(matrix_two)):

        rows = len(matrix_one)
        columns = len(matrix_one[0])

        sum = []
        for row in range(rows):
            sum.append([matrix_one[row][column] + matrix_two[row][column] \
            for column in range(columns)])

        return sum

    else:
        print("Dimensions are not matched")
        

if __name__ == '__main__':
    a = matrix_operations.create_matrix()
    b = matrix_operations.create_matrix()
    c = add(a,b)
    matrix_operations.display(c)