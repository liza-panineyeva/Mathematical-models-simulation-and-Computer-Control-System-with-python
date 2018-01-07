import numpy as np
import scipy
import matplotlib.pyplot as plt
import math


def xfrange(start, stop, step):
    i = 0
    while start + i * step <= stop:
        yield start + i * step
        i += 1
x = [x for x in xfrange(0,10.0,0.02)]

def euler(x0,y0,T,a,b,h):
    x=[]
    y = []
    t=0
    while t<T:
        x.append(x0)
        y.append(y0)
        x1= x0
        x0 = x0 + y0 * h
        y0 = y0 + (-b * x0 - a * y0) * h
        t=t+h
    return x,y

y1 = euler(1,0,10,1,1,0.02)[0]
y2 = euler(1,0,10,1,1,0.02)[1]


"""plt.figure(figsize=(10, 5))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.xlim(0, 13)
plt.ylim(-1, 1)"""

"""plt.plot(x, y1, color="red", label="x")
plt.plot(x, y2, color="blue", label="y")
plt.legend()"""
plt.plot(y1,y2)

plt.show()