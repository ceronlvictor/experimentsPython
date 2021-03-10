import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**9 -x**4 + 3*x**2+4

res = 100


x = np.linspace(-10.0, 10.0, num = res )
y = f(x)
fig, ax = plt. subplots()
plt.xlim(-2, 2)
plt.ylim(-10, 10)
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()
