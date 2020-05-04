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
'''Addition in Linear Alebra using Python''' 

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import matrix_methods as mm # My linear algebra library

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

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
    A_rows = len(A)
    A_columns = len(A[0])

    B_rows = len(B)
    B_columns = len(B[0])

    if (A_columns == B_columns) and (A_rows == B_rows):

        sum = []

        [sum.append([A[i][j] + B[i][j] for j in range(A_columns)])
        for i in range(A_rows)]

        return sum
        
def main():
    a = mm.create_matrix()
    b = mm.create_matrix()
    c = add(a,b)
    mm.display(c)

if __name__ == '__main__':
    main()