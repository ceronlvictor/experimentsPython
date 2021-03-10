import matplotlib.pyplot as plt
import numpy as np

"""Esa funcion representra una función cuadratica, utilizamos c como parametro
    para implementar las propiedades de las transformaciones"""
N = 1000
#Función cuadratica desplazamiento 
def f(x):
  return x**2;

c = 10

x = np.linspace(-5,5, num=N)

y = f(x) + c


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()

#funcion seno, alargamiento y contraccion  
N = 1000

def f(x):
  return np.sin(x);

c = 3

x = np.linspace(-15,15, num=N)

y = f((1/1)*x)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()

#reflexion de una función
N = 1000

def f(x):
  return x**3;

x = np.linspace(-10,10, num=N)

y = f(x)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()


