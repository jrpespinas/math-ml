"""Source:
    Abien Fred Agarap 
    https://github.com/AFAgarap
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__: '1.0.1'
__author__: 'Jan Rodolf Espinas'

import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns  

if __name__ == '__main__':

    x1 = np.linspace(-10, 10, 101)
    x2 = np.linspace(-10, 10, 101)

    sns.set_style('dark')

    y1 = 1/x1
    y2 = 1/x2**2
    
    plt.subplot(2, 1, 1)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(x1, y1)
    plt.title('Limits: Symmetric on origin')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2)
    plt.title('Limits: Symmetric on y-axis')
    plt.grid()
    plt.show()
