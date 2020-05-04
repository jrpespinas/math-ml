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
'''Transposing a matrix using Python'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import matrix_methods as mm

__version__: '1.1.3'
__author__: 'Jan Rodolf Espinas'

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
    
    [transposed_matrix.append([matrix[i][j] for i in range(rows)])
    for j in range(columns)]

    return transposed_matrix


def main():
    A = mm.create_matrix()
    mm.display(A)
    print('\n')
    A = transpose(A)
    mm.display(A)
    
if __name__ == '__main__':
    main()