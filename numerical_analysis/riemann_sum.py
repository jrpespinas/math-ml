"""Riemann Sums: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns  

def delta_x(lower_bound, upper_bound, n):
    return (lower_bound - upper_bound)/n

def f(x):
    return (2*(x**3)) + (x**2) - x + 1

if __name__ == '__main__':
    