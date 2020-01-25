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

    [input_matrix.append([float(input(f'M[{i+1},{j+1}] = ')) \
    for j in range(columns)])
    for i in range(0,rows)]

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
    
    [transposed_matrix.append([matrix[j][i] 
    for j in range(rows)])
    for i in range(columns)]

    return transposed_matrix

def add(A, B):
    """
    Returns `sum` from a pair of matrix
    with matching dimensions.

    Parameters
    ----------
    A : list
        The given left-hand side matrix.
    B : list
        The given right-hand side matrix.

    Returns
    -------
    sum : list
        The sum of two given matrix.

    """
    if (len(A[0]) == len(B[0])) \
    and (len(A) == len(B)):

        rows = len(A)
        columns = len(A[0])

        sum = []

        [sum.append([A[i][j] + B[i][j]
        for j in range(columns)])
        for i in range(rows)]

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
        
        for i in range(product_rows):
            product.append([
                (i,j)
                for j in range(product_columns)
            ])

        return product

    else:
        print('The matrix can not be multiplied.\n \
         Be sure to input the right dimensions of both matrix.')

def dot_product(A, B):
    """
    Returns `dot_product` from a pair of matrix wherein `A` is transposed
    into a row vector and `B` is a column vector.

    Parameters
    ----------
    A : list
        The given left-hand side transposed matrix.
    B : list
        The given right-hand side matrix.

    Returns
    -------
    dot_product : float
        dot product of two vectors.

    """
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if (A_columns == B_rows)\
    and (A_rows == 1 and B_columns == 1):

        dot_product = []

        # multi-line list comprehension for dot product
        [dot_product.append(sum(A[i][j]*B[j][i] 
        for j in range(A_columns))) 
        for i in range(A_rows)]

        return float(dot_product[0])
        
    else:
        print("dimensions of vector do not match.")

def outer_product(A, B):
    """
    Returns `outer_product` from a pair of vectors wherein 
    `B` is transposed into a row vector and `A` is a column vector.

    Parameters
    ----------
    A : list
        The given left-hand side matrix.
    B : list
        The given right-hand side transposed matrix.

    Returns
    -------
    outer_product : list
        Returns a matrix.
    """    
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])
    
    if A_columns == 1 and B_rows == 1:
    
        outer_product = []

        # multi-line list comprehension for outer product
        [outer_product.append([A[i][0] * B[0][j] for j in range(B_columns)]) 
        for i in range(A_rows)]

        return outer_product

    else:
        print("dimensions of vector do not match.")


def element_wise_product(A, B):
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
    if (len(A[0]) == len(B[0])) \
    and (len(A) == len(B)):

        rows = len(A)
        columns = len(A[0])

        hadamard_product = []
        
        [hadamard_product.append([A[i][j] * B[i][j]
        for j in range(columns)])
        for i in range(rows)]

        return hadamard_product

    else:
        print("Dimensions are not matched")

def display(matrix):
    """Prints a `matrix` in a presentable manner."""
    print('\n')
    [print(row) for row in matrix]

if __name__ == '__main__':
    A = create_matrix()
    c = transpose(A)
    display(c)