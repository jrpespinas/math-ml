"""Riemann Sums: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.5.0'
__author__: 'Jan Rodolf Espinas'

import numpy as np
import matplotlib.pyplot as plt 
import error_analysis as ea

def get_delta_x(lower_bound, upper_bound, n):
    return (upper_bound-lower_bound) / n

def f1(x):
    return (2*(x**3)) + (x**2) - x + 1, "2x^3+x^2-x+1"

def f2(x):
    return (2*(x**2)) - x + 1, "2x^2-x+1"

def f3(x):
    return np.sin(x), "sin(x)"

def f4(x):
    return x**2, "x^2"

def graph_function(function,x,n):
    """
    Shows the plot of the riemann sum given a `function` and 
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
    float
       The integral sum
    """
    riemann_sum = get_riemann_sum(function,x,n)
    y, fx = function(x) 
    
    plt.plot(x, y, label = f'Riemann Sum: {riemann_sum}')
    plt.title(fr'Graph of $y = {fx}$')
    plt.legend()
    plt.grid()

    return riemann_sum

def get_riemann_sum(function, x, delta_x):
    """
    Returns the riemann `sum` given a `function` and 
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
    float
       The integral sum
    """
    fx, string = function(x)
    return sum(fx*delta_x)
    
if __name__ == '__main__':
    LOWER_BOUND = [0, 0]
    UPPER_BOUND = [3, 5]
    SUBINTERVALS = [9, 15, 20, 50, 100, 200]
    FUNCTIONS = [f4,f4]

    for i in range(len(FUNCTIONS)):
        print(f'Function {i+1}:')
        for N in SUBINTERVALS:
            x = np.linspace(LOWER_BOUND[i],UPPER_BOUND[i],N,endpoint=False)
            delta_x  = get_delta_x(LOWER_BOUND[i],UPPER_BOUND[i],N)
            riemann_sum = graph_function(FUNCTIONS[i],x,delta_x)
            print(f'Interval [{LOWER_BOUND[i]},{UPPER_BOUND[i]}], Subintervals = {N}, Riemann Sum: {riemann_sum}')
        plt.show()
    