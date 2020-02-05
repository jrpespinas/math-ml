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

def f1(x):
    return (2*(x**3)) + (x**2) - x + 1

def f2(x):
    return (2*(x**2)) - x + 1

def f3(x):
    return np.sin(x)

def graph_function(function,x,n):
    riemann_sum = get_riemann_sum(function,x,n)
    y = function(x) 
    
    plt.plot(x, y, label = f'Riemann Sum: {riemann_sum}')
    plt.title(r'Graph of $y = 2x^3+x^2-x+1$')
    plt.legend()
    plt.grid()

    return riemann_sum

def get_riemann_sum(function, x, delta_x):
    """
    Returns the integral `sum` given a `function` and 
    the input `x` and `delta_x`

    Parameters
    ----------
    function : equation
        The equation defined above f1, f2, or f3
    x : list
        List of numbers returned by `np.linspace` given a lower
        and upper bound, and the number of intervals
    delta_x : 
        The interval
        
    Returns
    -------
    sum : float
       The integral sum
    """
    return sum(function(x)*delta_x)
    
if __name__ == '__main__':
    LOWER_BOUND = [-1,0,0]
    UPPER_BOUND = [1,2,3]
    SUBINTERVALS = [4,6,10,16]
    FUNCTIONS = [f1,f2,f3]

    for i in range(len(FUNCTIONS)):
        print(f'Function {i+1}:')
        for N in SUBINTERVALS:
            x = np.linspace(LOWER_BOUND[i],UPPER_BOUND[i],N,endpoint=False)
            delta_x  = get_delta_x(LOWER_BOUND[i],UPPER_BOUND[i],N)
            riemann_sum = graph_function(FUNCTIONS[i],x,delta_x)
            print(f'Interval [{LOWER_BOUND[i]},{UPPER_BOUND[i]}], Subintervals = {N}, Riemann Sum: {riemann_sum}')
        plt.show()
    