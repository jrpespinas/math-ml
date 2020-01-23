from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.1.3'
__author__: 'Jan Rodolf Espinas'

def create_matrix():
    """
    Returns `input_matrix` by appending `float` inputs
    to an empty array provided `rows` and `columns` as the 
    dimensions.

    Returns
    -------
    `input_matrix` : list
        The input matrix

    Notes
    -----
    a `vector` is just a `matrix` with n rows and 1 column or
    1 row and n columns.
    """
    rows = int(input('Number of rows: '))
    columns = int(input('Number of columns: '))

    input_matrix = []

    for row in range(0,rows):
        input_matrix.append([float(input(f'M[{row+1},{col+1}] = ')) \
        for col in range(columns)])  

    return input_matrix

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
    
    for col in range(0, columns):
        transposed_matrix.append([
            matrix[row][col] 
            for row in range(rows)
        ])

    return transposed_matrix

def add(matrix_one, matrix_two):
    """
    Returns `sum` from a pair of matrix
    with matching dimensions.

    Parameters
    ----------
    matrix_one : list
        The given left-hand side matrix.
    matrix_two : list
        The given right-hand side matrix.

    Returns
    -------
    sum : list
        The sum of two given matrix.

    """
    if (len(matrix_one[0]) == len(matrix_two[0])) \
    and (len(matrix_one) == len(matrix_two)):

        rows = len(matrix_one)
        columns = len(matrix_one[0])

        sum = []
        for row in range(rows):
            sum.append([
                matrix_one[row][col] + matrix_two[row][col]
                for col in range(columns)
            ])

        return sum

    else:
        print("Dimensions are not matched")

def matrix_mul(matrix_one, matrix_two):
    """
    Returns `product` from a pair of matrix with 
    a matching number of columns from the first matrix 
    and rows from the second matrix.

    Parameters
    ----------
    matrix_one : list
        The given left-hand side matrix.
    matrix_two : list
        The given right-hand side matrix.

    Returns
    -------
    product : list
        The product of two given matrix.

    """
    if len(matrix_one[0]) == len(matrix_two):
        product = []
        product_rows = len(matrix_one)
        product_columns = len(matrix_two[0])
        
        matrix_two = transpose_matrix(matrix_two)
        
        for row in range(product_rows):
            product.append([
                (row,col)
                for col in range(product_columns)
            ])

        return product

    else:
        print('The matrix can not be multiplied.\n \
         Be sure to input the right dimensions of both matrix.')

def element_wise_product(matrix_one, matrix_two):
    """
    Returns `hadamard_product` from a pair of matrix
    with matching dimensions.

    Parameters
    ----------
    matrix_one : list
        The given left-hand side matrix.
    matrix_two : list
        The given right-hand side matrix.

    Returns
    -------
    hadamard_product : list
        The element wise product of two given matrix.

    """
    if (len(matrix_one[0]) == len(matrix_two[0])) \
    and (len(matrix_one) == len(matrix_two)):

        rows = len(matrix_one)
        columns = len(matrix_one[0])

        hadamard_product = []
        for row in range(rows):
            hadamard_product.append([
                matrix_one[row][col] * matrix_two[row][col]
                for col in range(columns)
            ])

        return hadamard_product

    else:
        print("Dimensions are not matched")

def display(matrix):
    """Prints a `matrix` in a presentable manner."""
    print('\n')
    [print(row) for row in matrix]

if __name__ == '__main__':
    A = create_matrix()
    B = create_matrix()
    c = element_wise_product(A,B)
    display(c)