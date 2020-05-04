# Copyright 2020 Jan Rodolf Espinas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''Compilation of Matrix Methods'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.2.4'
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

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(float(input(f'[{i+1},{j+1}]:')))
        input_matrix.append(row)

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
    transposed_matrix : list (matrix)
        The transposed matrix
    """
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = []
    
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix[j][i])
        transposed_matrix.append(row)
    
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
    sum : list (matrix)
        The sum of two given matrix.

    """
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if (A_columns == B_columns) and (A_rows == B_rows):

        matrix = []

        for i in range(A_rows):
            row = []
            for j in range(A_columns):
                row.append(sum(A[i][j],B[i][j]))
            matrix.append(row)

        return matrix

    else:
        print("Dimensions are not matched")

def matmul(A, B):
    """
    Returns `product` from a pair of matrix with 
    a matching number of columns from the first matrix 
    and rows from the second matrix.

    Parameters
    ----------
    A : list
        The given left-hand side matrix.
    B : list
        The given right-hand side matrix.

    Returns
    -------
    product : list (matrix)
        The product of two given matrix.

    """
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if A_columns == B_rows:
        product = []
        product_rows = A_rows
        product_columns = B_columns      
        
        for i in range(product_rows):
            row = []
            for j in range(product_columns):
                inner_product = []
                for k in range(A_columns):
                    inner_product.append(A[i][k]*B[k][j])
                row.append(sum(inner_product))
            product.append(row)
            
        return product

    else:
        print('The matrix can not be multiplied.\n \
         Be sure to input the right dimensions of both matrix.')

    return product

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
    dot_product : float (scalar)
        dot product of two vectors.

    """
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if (A_columns == B_rows) and (A_rows == 1 and B_columns == 1):

        dot_product = []
        
        for i in range(A_columns):
            dot_product.append(A[0][i]*B[i][0])

        return sum(dot_product)
        
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
    outer_product : list (matrix)
        Returns a matrix.
    """    
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])
    
    if A_columns == 1 and B_rows == 1:
    
        outer_product = []
        
        for i in range(A_rows):
            row = []
            for j in range(B_columns):
                row.append(A[i][0] * B[0][j])
            outer_product.append(row)

        return outer_product

    else:
        print("dimensions of vector do not match.")


def element_wise_product(A, B):
    """
    Returns `hadamard_product` from a pair of matrix
    with matching dimensions.

    Parameters
    ----------
    A : list
        The given left-hand side matrix.
    B : list
        The given right-hand side matrix.

    Returns
    -------
    hadamard_product : list (matrix)
        The element wise product of two given matrix.

    """
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if (A_rows == B_rows) and (A_columns == B_columns):

        hadamard_product = []
        
        for i in range(A_rows):
            row = []
            for j in range(A_columns):
                row.append(A[i][j] * B[i][j])
            hadamard_product.append(row)

        return hadamard_product

    else:
        print("Dimensions are not matched")

def display(matrix):
    """
    Prints a matrix in a presentable manner.

    Parameters
    ----------
    matrix : list
        a 2-dimensional matrix
    """
    [print(row) for row in matrix]


def main():
    # MATRIX-MATRIX MULTIPLICATION demo
    A = [[3,1,1],[8,2,7],[6,1,8]]
    B = [[5,3,0],[3,7,0],[7,4,4]]
    C = matrix_mul(A, B)
    print("""---------------------
    \nMatrix-Matrix Multiplication
    A = [3,1,1],
        [8,2,7],
        [6,1,8]

    B = [5,3,0],
        [3,7,0],
        [7,4,4]
    """)
    print("A * B")
    display(C)

    # MATRIX-VECTOR_MULTIPLICATION demo
    A = [[1,2,3],[4,5,6],[7,8,9]]
    b = [[1],[2],[3]]
    C = matrix_mul(A, b)
    print("""---------------------
    \nMatrix-Vector Multiplication
    A = [1,2,3],
        [4,5,6],
        [7,8,9]

    b = [1],
        [2],
        [3]
    """)
    print("A * b")
    display(C)

    #VECTOR-VECTOR (INNER PRODUCT) MULTIPLICATION demo
    a = [[1],[2],[3]]
    b = [[1],[2],[3]]
    a = transpose(a)
    c = dot_product(a,b)
    print("""---------------------
    \nDot Product Multiplication
    a.T = [1,2,3]

    b   =   [1],
            [2],
            [3]
    """)
    print(f'a.T * b\n{c}')

    #VECTOR-VECTOR (OUTER_PRODUCT) MULTIPLICATION demo
    a = [[1],[2],[3]]
    b = [[1],[2],[3]]
    b = transpose(b)
    c = outer_product(a,b)
    print("""---------------------
    \nOuter Product Multiplication
    a   =   [1],
            [2],
            [3]

    b.T   = [1,2,3]
    """)
    print("a * b.T")
    display(c)

    # ELEMENT-WISE MATRIX MULTIPLICATION demo
    A = [[3,1,1],[8,2,7],[6,1,8]]
    B = [[5,3,0],[3,7,0],[7,4,4]]
    C = element_wise_product(A, B)
    print("""---------------------
    \nElement-wise Matrix Multiplication
    A = [3,1,1],
        [8,2,7],
        [6,1,8]

    B = [5,3,0],
        [3,7,0],
        [7,4,4]
    """)
    print("A * B")
    display(C)

    # MATRIX-MATRIX ADDITION demo
    A = [[3,1,1],[8,2,7],[6,1,8]]
    B = [[5,3,0],[3,7,0],[7,4,4]]
    C = add(A, B)
    print("""---------------------
    \nMatrix-Matrix Adition
    A = [3,1,1],
        [8,2,7],
        [6,1,8]

    B = [5,3,0],
        [3,7,0],
        [7,4,4]
    """)
    print("A + B")
    display(C)

    # VECTOR-VECTOR ADDITION demo
    a = [[3,1,1]]
    b = [[5,3,0]]
    c = add(a, b)
    print("""---------------------
    \nVector-Vector Adition
    a.T = [3,1,1],

    b.T = [5,3,0],
    """)
    print("a.T + b.T")
    display(c)
    
if __name__ == '__main__':
    main()