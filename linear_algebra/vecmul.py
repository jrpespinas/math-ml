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
'''Vector Multiplication using Python'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import matrix_methods as mm # My linear algebra library

__version__: '1.3.0'
__author__: 'Jan Rodolf Espinas'

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

    if (A_columns == B_rows) and (A_rows == 1 and B_columns == 1):

        dot_product = []
        
        dot_product.append(sum([A[0][i]*B[i][0] for i in range(A_columns)]))

        return float(dot_product)
        
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
    print(A)
    print(B)
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


def main():
    A = mm.create_matrix() # [[1,2,3]]
    B = mm.create_matrix() #[[1],[2],[3]]
    C = dot_product(A,B)
    print(C)
    
if __name__ == '__main__':
    main()
    
    