"""Riemann Sums: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.5.0'
__author__: 'Jan Rodolf Espinas'

import numpy as np
import matplotlib.pyplot as plt 
import error_analysis as ea
import argparse

def get_delta_x(lower_bound, upper_bound, n):
    return (upper_bound-lower_bound) / n

def f1(x):
    return (2*(x**3)) + (x**2) - x + 1

def f2(x):
    return (2*(x**2)) - x + 1

def f3(x):
    return np.sin(x)

def f4(x):
    return x**2

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
    y = function(x) 
    
    plt.plot(x, y, label = f'Riemann Sum: {riemann_sum}')
    plt.title(fr'Graph of $y = f(x)$')
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
    return sum(function(x)*delta_x)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Riemann Integrals")
    parser.add_argument(
        '-lb', 
        '--LOWER_BOUND', 
        type=int,
        help='Lower Bound'
    )
    parser.add_argument(
        '-ub', 
        '--UPPER_BOUND', 
        type=int,
        help='Upper Bound'
    )
    parser.add_argument(
        '-sub', 
        '--SUBINTERVALS',
        nargs='+', 
        type=int,
        help='Subintervals'
    )
    args = vars(parser.parse_args())

    LOWER_BOUND = args['LOWER_BOUND']
    UPPER_BOUND = args['UPPER_BOUND']
    SUBINTERVALS = args['SUBINTERVALS']

    for N in SUBINTERVALS:
        x = np.linspace(LOWER_BOUND,UPPER_BOUND,N,endpoint=False)
        delta_x  = get_delta_x(LOWER_BOUND,UPPER_BOUND,N)
        riemann_sum = graph_function(f4,x,delta_x)
        print(f'Interval [{LOWER_BOUND},{UPPER_BOUND}], Subintervals = {N}, Riemann Sum: {riemann_sum}')
    plt.show()