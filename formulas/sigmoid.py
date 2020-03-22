from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.0'
__author__: 'Jan Rodolf Espinas'

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(x))

def main():
    print(sigmoid(0))

if __name__ == '__main__':
    main()