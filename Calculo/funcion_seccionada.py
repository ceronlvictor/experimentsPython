import matplotlib.pyplot as plt
import numpy as np

def H(x):
    y = np.zeros(len(x))
    for idx, x in enumerate(x):
        if x >= 0:
            y[idx] = 1.0
    return y

res = 1000

x = np.linspace(-10.0, 10.0, num = res )
y = H(x)
fig, ax = plt. subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()
