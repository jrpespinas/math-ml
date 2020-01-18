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
    for i in range(0,rows):
        matrix.append(list(map(int, input(f"Row {i+1}: Columns 1-{cols}: ").split())))   
    print(matrix)

if __name__ == '__main__':
    main()