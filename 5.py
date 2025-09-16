import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    y = np.sinh(x)
    return y

def f2(x):
    y = np.tanh(x)
    return y

def f3(x):
    y = np.cosh(x)
    return y

x = np.linspace(-3,10,1000)
plt.plot(x, f1(x), x, f2(x), x, f3(x))
plt.ylabel('funcion')
plt.xticks((-3, 0, 3, 6, 10))

plt.legend()
plt.show()