from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.0'
__author__: 'Jan Rodolf Espinas'

def main():
    print("Matrix")
    rows = int(input('Number of rows: '))
    cols = int(input('Number of columns: '))

    matrix = []
    zeros = []

    # input values of the matrix per element
    for row in range(0,rows):
        matrix.append([int(input(f'M[{row+1},{col+1}] = ')) for col in range(cols)])  
        zeros.append([int(0) for i in range(cols)])
    
    print('\nMatrix A')
    [print(f'{row}') for row in matrix]
    
    # swap the rows and columns
    for i,rows in enumerate(zeros):
        for j,cols in enumerate(zeros):
            zeros[i][j] = matrix[j][i]
    
    print('\nTransposed')
    [print(f'{row}') for row in zeros]

if __name__ == '__main__':
    main()