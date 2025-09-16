import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 3, 10000)
funcion = np.piecewise(x, [x<-1, (x>=-1) & (x<2), x>=2], [lambda x: -x**3 + np.sin(np.pi*x), lambda x: x**2 - 3, lambda x: np.exp(x-1) - 10])


plt.plot(x, funcion, marker='^')
plt.show()