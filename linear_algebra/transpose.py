from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

def main():
    print("Matrix")
    rows = int(input('Number of rows: '))
    columns = int(input('Number of columns: '))

    input_matrix = []
    transposed_matrix = []

    # input values of the matrix per element
    for row in range(0,rows):
        input_matrix.append([int(input(f'M[{row+1},{col+1}] = ')) \
        for col in range(columns)])  

    print('\nInput Matrix')
    [print(row) for row in input_matrix]

    # transpose matrix
    for col in range(0, columns):
        transposed_matrix.append([input_matrix[i][col] for i in range(rows)])

    print('\nTransposed')
    [print(row) for row in transposed_matrix]

if __name__ == '__main__':
    main()