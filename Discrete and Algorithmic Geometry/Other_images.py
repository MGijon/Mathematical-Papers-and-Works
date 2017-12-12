import math as mt
import matplotlib.pyplot as plt


##
## GRAPH THEORICALTHICKNES
## =======================

def GTT(last_value, lines = False, col = 'blue'):
    X = [i for i in range(1, last_value)]
    value = [i for i in range(1, last_value)]

    for i in range(0, len(X)):
        if X[i] <= 4:
            value[i] = 1
        else:
            # X[i] > 4
            if X[i] <= 8:
                value[i] = 2;
            else:
                # X[i] > 9
                if X[i] <= 10:
                    value[i] = 3
                else:
                    # X[i] > 10
                    value[i] = mt.ceil((X[i] + 2) / 6)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(X, value, color = col)
    if lines:
        ax.plot(X, value, color = col)
    plt.title(r'Value of $\theta (K_{n})$ for $n = 1$ to $n =$' + str(last_value))
    ax.set_xlabel(r'$\theta(K_{n})$')
    ax.set_ylabel('Value of n')
    plt.savefig('Geometrical-theorical thickness from 1 to ' + str(last_value) + '.png')
    plt.show()

GTT(last_value = 30)
GTT(last_value = 100, lines = True)
GTT(last_value = 200, col = 'black')

##
## LOWER BOUND FOR GEOMETRIC THICKNESS > 11
## ========================================

import numpy as np
last_value = 100
first_value = 12
X = [i for i in range(first_value, last_value)]
value = [i for i in range(first_value, last_value)]
for i in range(0, len(X)):
    value[i] = mt.ceil((X[i] / 5.646) + 0.342)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(X, value, color = 'red')
ax.set_xlabel(r'Value of $n$')
ax.set_ylabel('Value of the lower bound')
plt.title(r'Lower bound for $K_{n}$ with $n \geq 12$')
plt.savefig('LBK_n.png')
plt.show()

##
## GEOMETRICL THICKNES BIPARTITE GRAPHS
## ====================================

from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
import numpy as np

def GTBG(a, b):
    A = [i for i in range(1, a)]
    B = [i for i in range(1, b)]

    fig = plt.figure(figsize = plt.figaspect(0.5))

    ax = fig.add_subplot(1, 2, 1, projection = '3d')

    ## Lower bound for theorical thickness:
    TT = mt.ceil((A*B)(2*A + 2*B - 4))
    ax.scatter(A, B, TT)
    plt.title(r'Value of $\theta (K_{n})$ for $n = 1$ to $n =$' + str(last_value))
    ax.set_xlabel(r'$\theta(K_{n})$')
    ax.set_ylabel('Value of n')
   # plt.savefig(' ')
    plt.show()