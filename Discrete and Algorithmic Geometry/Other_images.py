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
    plt.savefig('Geometrical-tgeorical thickness from 1 to ' + str(last_value) + '.png')
    plt.show()

GTT(last_value = 30)
GTT(last_value = 100, lines = True)
GTT(last_value = 200, col = 'black')


##
## GEOMETRICLTHICKNES (1000 first values)
## ===========================================
