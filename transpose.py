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
    
    

if __name__ == '__main__':
    main()