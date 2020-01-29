"""Error Analysis: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

def absolute_value(value):
    if value <= 0:
        return value * -1
    return value

def absolute_error(true_fx, approximate_fx):
    return absolute_value(true_fx - approximate_fx)

def relative_error(true_fx, approximate_fx):
    return absolute_error(true_fx, approximate_fx)/absolute_value(true_fx)

if __name__ == '__main__':
    print(relative_error(10,9))