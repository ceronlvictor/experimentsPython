from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return np.sin(x) + 2*np.cos(y)

res = 100

#Ejes
x = np.linspace(-4,4, num = res)
y = np.linspace(-4,4, num = res)
x, y = np.meshgrid(x,y)

#funcion
z = f(x,y)

#grafica
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
suf = ax.plot_surface(x,y,z, cmap=cm.gist_rainbow_r)

#curvas de nivel
fig2, ax2 = plt.subplots()
level_map = np.linspace(np.min(z),np.max(z), num=res)
cp = ax2.contour(x,y,z, levels = level_map, cmap = cm.gist_rainbow_r)
#Relleno completo de las curvas de nivel = cp = ax2.contourf(x,y,z, levels = level_map, cmap = cm.cool)
fig2.colorbar(cp)

fig.colorbar(suf)
plt.show()