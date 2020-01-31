"""Riemann Sums: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_style('dark')

def delta_x(lower_bound, upper_bound, n):
    return (upper_bound - lower_bound)/n

def f(x):
    return (2*(x**3)) + (x**2) - x + 1

def graph_function(lower_bound, upper_bound, n):
    x = np.linspace(lower_bound, upper_bound, n)
    y = f(x) # temporary function
    
    plt.plot(x, y, label = r'$y = 2x^3+x^2-x+1$')
    plt.title(r'Graph of $f(x)$')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    graph_function(-1,1,6)