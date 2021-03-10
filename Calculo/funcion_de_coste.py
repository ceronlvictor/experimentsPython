import numpy as np
import matplotlib.pyplot as plt

a = np.array([0, 100])
b = np.array([20, 150])
c = np.array([30, 200])
d = np.array([40, 180])
e = np.array([50, 250])
g = np.array([60, 230])
xy = a[0]*a[1] + b[0]*b[1] + c[0]*c[1] + d[0]*d[1] + e[0]*e[1] + g[0]*g[1] #Aqui aplico las ecuaciones clasicas para calcular la regresion lineal
sumx = a[0] + b[0] + c[0] + d[0] + e[0] + g[0]
sumy = a[1] + b[1] + c[1] + d[1] + e[1] + g[1]
sumx2 = a[0]**2 + b[0]**2 + c[0]**2 + d[0]**2 + e[0]**2 + g[0]**2
n = 6
A1 = (n*xy - sumx*sumy) / (n*sumx2 - sumx**2)
A0 = sumy/n - (A1*sumx/n)

def f(x):
  return A0 + A1*x
N=1000
x = np.linspace(0,(60), num=N)

y = f(x)
print("y =",A0,"+",A1,"x")
ECM = ((f(0)-a[1])**2 + (f(20)-b[1])**2 + (f(30)-c[1])**2 + (f(40)-d[1])**2 + (f(50)-e[1])**2 +(f(60)-g[1])**2)/n # Aqui aplico la formula del error cuadratico medio que nos explica Enrique donde y gorrito viene dada por la funcion f(x) evaluada en cada uno de los puntos x del conjunto de datos que nos dio Enrique
                                                                                                  
                                                                                                  
print("El error cuadratico medio, ECM = ", ECM)

fig, ax = plt.subplots()
ax.plot(x,y,label='y = 106.43 + 2.36 X')
ax.scatter(a[0], a[1], c='red')
ax.scatter(b[0], b[1], c='red')
ax.scatter(c[0], c[1], c='red')
ax.scatter(d[0], d[1], c='red')
ax.scatter(e[0], e[1], c='red')
ax.scatter(g[0], g[1], c='red')
ax.set_xlabel('Gasto en publicidad')
ax.set_ylabel('Ventas')
ax.legend()
ax.grid()
plt.show()