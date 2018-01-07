import numpy as np
import scipy
import matplotlib.pyplot as plt
import math


def xfrange(start, stop, step):
    i = 0
    while start + i * step <= stop:
        yield start + i * step
        i += 1
x = [x for x in xfrange(0,13.0,0.2)]
x1 = [x for x in xfrange(0,13.0,0.08)]
def euler(x0,T,h):
    x=[]
    t=0
    while t<T:
        x.append(x0)
        x0 = x0+h*-1*x0
        t=t+h
    return x

y1 = euler(0,13,0.2)
y2 = [math.exp(-1*t) for t in x1 ]


plt.figure(figsize=(10, 5))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.xlim(0, 13)
plt.ylim(0, 1)

plt.plot(x, y1, color="red", label="numerical")
plt.plot(x1, y2, color="blue", label="analytical")
plt.legend()

plt.show()
