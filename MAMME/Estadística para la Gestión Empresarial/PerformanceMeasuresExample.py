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

# Sales by year
plt.figure(figsize=(15, 7))
plt.scatter(datos.Year, datos.Global_Sales, color = 'b', label = 'Global', alpha=0.2)
plt.scatter(datos.Year, datos.JP_Sales, color = 'r', label = 'Japan', alpha=0.2)
plt.scatter(datos.Year, datos.EU_Sales, color = 'G', label = 'Europe', alpha=0.2)
plt.title('"Hits" money by year and area')
plt.xlabel('year')
plt.ylabel('Units')
plt.legend()
plt.show()

# Set of all money raised by year
min_year = int(min(datos.Year))
max_year = int(max(datos.Year))
valores_anuales_Global = []
for i in range(min_year, max_year):
    aux_global = 0
    print(i)
    for j in datos[datos.Year == i]:
        print(j)
            #aux_global += datos.Global_Sales
    valores_anuales_Global.append((i, aux_global))
# necesito recorrer los elementos e ir guardando las ventas totales por año



# introduction
# computacionalgenomics.blog.bristol.ac.uk


bal bla bla bla bla bla bla bal
