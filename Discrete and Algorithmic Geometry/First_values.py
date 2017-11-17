import matplotlib.pyplot as plt

x = [i for i in range(1, 101)]

lower_bound = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
				6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11,
			 	11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15,
			 	15, 15, 16, 16, 16, 16, 16, 16,17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19]

upper_bound = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8,
 				8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13 , 13, 13, 14, 14, 14,
 				14, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20,
 				20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25]

print(len(upper_bound))

known_values = [lower_bound[i] for i in range(0, len(lower_bound)) if lower_bound[i] == upper_bound[i]]

## Draw the grafics

##
## Comparation between lower and upper bound
## =========================================


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, lower_bound, color = 'blue', label = 'Lower Bounds')
ax.plot(x, upper_bound, color = 'red', label = 'Upper Bounds')
plt.title(r'Comparation between lowe and upper bounds for $K_{n}$')
ax.set_xlabel(r'Value of $n$')
ax.set_ylabel('Bounds')
plt.legend()
plt.show()



##
## Comparation between lower and upper bound
## Enfasis on known values
## =========================================


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x[:20], lower_bound[:20], color = 'lightblue', label = 'Lower Bounds')
ax.scatter(x[:20], upper_bound[:20], color = 'pink', label = 'Upper Bounds')

ax.scatter([i for i in range(1, len(known_values) + 1)], known_values, marker = '^', color = 'red', label = 'Known values')
plt.title(r'Comparation between lowe and upper bounds for $K_{n}$')
ax.set_xlabel(r'Value of $n$')
ax.set_ylabel('Bounds')
plt.legend()
plt.show()


