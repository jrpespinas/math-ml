"""Riemann Sums: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.5.0'
__author__: 'Jan Rodolf Espinas'

import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import error_analysis as ea

sns.set_style('dark')

def get_delta_x(lower_bound, upper_bound, n):
    return (upper_bound-lower_bound) / n

def f(x):
    return (2*(x**3)) + (x**2) - x + 1

def graph_function(x,n):
    y = f(x) # temporary function
    
    plt.plot(x, y, label = f'{n} intervals')
    plt.title(r'Graph of $y = 2x^3+x^2-x+1$')
    plt.legend()
    plt.grid()

def get_riemann_sum(x, delta_x):
    return sum(f(x)*delta_x)
    
if __name__ == '__main__':
    LOWER_BOUND = -1
    UPPER_BOUND = 1
    SUBINTERVALS = [4,6,10]

    for N in SUBINTERVALS:
        x = np.linspace(LOWER_BOUND,UPPER_BOUND,N,endpoint=False)
        riemann_sum = get_riemann_sum(x,get_delta_x(LOWER_BOUND,UPPER_BOUND,N))
        print(f'Interval [{LOWER_BOUND},{UPPER_BOUND}], Subintervals = {N}, Riemann Sum: {riemann_sum}')
        graph_function(x,N)

    plt.show()