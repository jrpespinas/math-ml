from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.0'
__author__: 'Jan Rodolf Espinas'

class MatrixMethods:

    def __init__(self):
        print('Matrix')
        self.rows = int(input('Number of rows: '))
        self.cols = int(input('Number of columns: '))

    def create_matrix(self):
        print(f'M[{self.rows}x{self.cols}]')
        matrix = []
        for i in range(0,self.rows):
            matrix.append([int(input(f'M[{i+1},{j+1}] = ')) for j in range(3)])  
        
        self.matrix = matrix
    
    def print_matrix(self):
        print('\nMatrix A')
        for rows in self.matrix:
            print(f'\t{rows}')


def main():
    A = MatrixMethods()
    A.create_matrix()
    A.print_matrix()

if __name__ == '__main__':
    main()