#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Hecho por: Katzrin Nikhole Myrie Berger 
#Carné: B64980
#PASO1:
#Antes de iniciar se cargó el archivo por analizar llamado ¨xy ¨ y "xyp"
import csv
import seaborn as sns
import scipy as sp
from scipy import stats
from scipy.stats import norm
from scipy.stats import rayleigh
from scipy.optimize import curve_fit
from scipy.stats import kurtosis
from scipy.stats import skew
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import pandas as pd
import numpy as np
L = pd.read_csv('xy (1).csv')
P= pd.read_csv('xyp.csv')
X= np.linspace(5,15,10)
Y= np.linspace(5,25,21)
fX=np.sum(L, axis=1)
fY=np.sum(L, axis=0)

fun1= (fX,X)
fun2=(fY, Y)

def gaussiana(x, mu, sigma):
    return 1/(np.sqrt (2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))
   
print("Los parámetros de ajuste para f(x)= ")
param,_=(curve_fit(gaussiana,X,fX))
print (param)

plt.plot (X, fX)
plt.show()
print("____________________________________________________________________________________________________________________")
plt.plot (Y, fY)
plt.show()




print("Los parámetros de ajuste para f(Y)= ")

param2,_=(curve_fit(gaussiana,Y,fY))
print (param2)



# In[5]:


#(25 %) Asumir independencia de X y Y. 
#Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?
import numpy as np
"""
recuerde de las función de densidad conjunta se define como la multiplicación de que sucedan los intervalos uno primero que el otro 
la función acumulativa sería entonces como la ultiplicación d las densidades marginales de x y de y
pot lo tanto 
            F(x,y)= F(x)*F(y)

"""
X= np.linspace(5,15,10)
Y= np.linspace(5,25,21)
x = X
y = Y
#fDC=  1/(np.sqrt (2*np.pi*3.25802246**2))*np.exp(-(x-9.53068453)**2/(2*3.25802246**2))* 1/(np.sqrt (2*np.pi* 6.32588545**2))*np.exp(-(y-15.1527004)**2/(2* 6.32588545**2))

#print (fDC)




# In[28]:



'''
3. (25 %) Hallar los valores de correlación, 
covarianza y coeficiente de correlación (Pearson) 
para los datos y explicar su significado.
'''
##correlación 
P['correl'] = (P['x']*P['y'])*P['p']
#Hacer la suma 
correlacion=np.sum(P['correl'] , axis=0)
print("La correlación es : ")

print(correlacion)
print("____________________________________________________________________________________________________________________")

### covarianza

YM=np.mean(Y)
XM=np.mean(X)


P['cova'] =(P['x']-XM )*(P['y']-YM)*P['p']
#Hacer la suma 
covarianza=np.sum(P['cova'] , axis=0)
print("La covarianza  es : ")
print(covarianza)

print("____________________________________________________________________________________________________________________")


####coeficiente de pearson 


P['pearson'] =(P['cova']/(3.25802246*6.32588545))
coefp=np.sum(P['pearson'] , axis=0)
print("La constante de pearson :")     
print(coefp)
print("____________________________________________________________________________________________________________________")


# In[10]:


"""
(25 %) Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D)

"""
from matplotlib.pyplot import *
from pylab import *
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import style


x1 = X
plt.plot (X, fX)
G1=1/(np.sqrt (2*np.pi*3.25802246**2))*np.exp(-(x1-9.53068453)**2/(2*3.25802246**2))
plt.plot ( x1, G1, color='#AA1111')
plt.show()

y1=Y
plt.plot (Y, fY)
G2=1/(np.sqrt (2*np.pi* 6.32588545**2))*np.exp(-(y1-15.1527004)**2/(2* 6.32588545**2))
plt.plot ( y1, G2, color='#AA1111')

plt.show()


# Creamos la figura
fig = plt.figure(figsize=(8,7))
# Datos en array bi-dimensional
x = X
y = Y
x,y=np.meshgrid(x,y)
z = 1/(np.sqrt (2*np.pi*3.25802246**2))*np.exp(-(x-9.53068453)**2/(2*3.25802246**2))* 1/(np.sqrt (2*np.pi* 6.32588545**2))*np.exp(-(y-15.1527004)**2/(2* 6.32588545**2))
# Agrrgamos un plano 3D
ax1 = fig.add_subplot(1,1,1,projection='3d')
# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
ax1.plot_wireframe(x, y, z)

# Mostramos el gráfico
show()


# In[ ]:




