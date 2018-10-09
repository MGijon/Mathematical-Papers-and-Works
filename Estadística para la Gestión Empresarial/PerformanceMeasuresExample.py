import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## ============= ##
## PREPROCESSING ##
## ============= ##

# import the data.set
datos = pd.read_csv('Data/vgsales.csv')

print(datos.describe())
# erase the data with unsense data
datos = datos[datos.Year < 2017]
print(datos.describe())

print(datos[datos.Global_Sales == max(datos.Global_Sales)])
datos = datos[datos.Global_Sales != max(datos.Global_Sales)]

print(datos[datos.Global_Sales == max(datos.Global_Sales)])

## ================== ##
## FIRST EXPLORATIONS ##
## ================== ##

# International sales by year
plt.scatter(datos.Year, datos.Global_Sales, color = 'b', label = '')



plt.legend()


plt.show()
