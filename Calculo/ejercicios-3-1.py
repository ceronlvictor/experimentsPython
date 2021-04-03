import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**4 -3*x**3 - 6*x**2 + 7*x + 30

res = 1000


x = np.linspace(-50.0, 50.0, num = res )
y = f(x)
fig, ax = plt. subplots()

ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()
