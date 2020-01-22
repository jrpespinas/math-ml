from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.2'
__author__: 'Jan Rodolf Espinas'

def create_matrix():
    rows = int(input('Number of rows: '))
    columns = int(input('Number of columns: '))

    input_matrix = []

    for row in range(0,rows):
        input_matrix.append([int(input(f'M[{row+1},{col+1}] = ')) \
        for col in range(columns)])  

    return input_matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = []
    
    for col in range(0, columns):
        transposed_matrix.append([matrix[i][col] for i in range(rows)])

    return transposed_matrix

def display_matrix(matrix):
    print('\n')
    [print(row) for row in matrix]

def matrix_multiplication(matrix_one, matrix_two):
    if len(matrix_one[0]) == len(matrix_two):
        product_matrix = []
        product_matrix_rows = len(matrix_one)
        product_matrix_columns = len(matrix_two[0])
        
        matrix_two = transpose_matrix(matrix_two)
        
        for row in range(0, product_matrix_rows):
            for column in range(0, product_matrix_columns):
                print(row,column)

    else:
        print('The matrix can not be multiplied.\n Be sure to input the right dimensions of both matrix.')

    return product_matrix
if __name__ == '__main__':
    A = create_matrix()
    B = create_matrix()
    matrix_multiplication(A,B)