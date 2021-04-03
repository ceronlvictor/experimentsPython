from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

def f(x,y):
    return np.sin(x) + np.cos(y)

res = 100

x = np.linspace(-4,4,res)
y = np.linspace(-4, 4, res)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)

#Creamos superficie 
surf = ax.plot_surface(X,Y,Z, cmap=cm.gist_rainbow_r)

#amplitud de colores
fig.colorbar(surf)

plt.show()

#Descenso del gradiente
level_map = np.linspace(np.min(Z), np.max(Z), res)
plt.contourf(X,Y,Z, levels=level_map, cmap=cm.gist_rainbow_r) #cm.cool es un tema diferente
plt.colorbar()
plt.title("Descenso del gradiente")


#Para comenzar la simulación del descenso del gradiente escogemos un punto aleatorio
#Multiplicamos y restamos porque el rango de aleatoriedad es de 0 a 1  y con estas opreaciones conseguimos que el intervalo sea de -4 a 4
p = np.random.rand(2) * 8 - 4
#Grafica del punto aleatorio
plt.plot(p[0],p[1], 'o', c = 'k')

h = 0.01
lr = 0.01

def derivate(cp,p):
    return (f(cp[0], cp[1]) - f(p[0], p[1]))/h

#Pasos para descender al puunto minimo con el gradiente
def gradient(p):
    grad = np.zeros(2)

    #Iteramos atravez de las componentes, funcion enumerate regrewa el indice y nos regresa el valor de la  misma componente
    for idx, val in enumerate(p):
        cp = np.copy(p)
        cp[idx] = cp[idx] + h

        #La derivada se calcula dependiendo la componente
        dp = derivate(cp, p)
        grad[idx] = dp
    return grad

#Iteración del algoritmo 
for i in range(1000):
    p = p - lr*gradient(p)
    if( i % 10 == 0):
       plt.plot(p[0],p[1], 'o', c = 'r')

plt.plot(p[0],p[1], 'o', c = 'w')
print(p)
plt.show()