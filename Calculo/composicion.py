import numpy as np 
import matplotlib.pyplot as plt

def g(x):
    return x**2

def f(x):
    return np.sin(x)

x = np.linspace(-10.0, 10.0, num = 1000)

f_o_g = f(g(x))

plt.plot(x,f_o_g)
plt.grid()
plt.show()
