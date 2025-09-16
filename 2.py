import numpy as np

l = []
m = 6
for i in range(1,m):
    l.append(i / m)

vect = np.array(l)

print(vect, end='\n\n')

vect2 = np.linspace(0, 1, 15)

print(vect2)