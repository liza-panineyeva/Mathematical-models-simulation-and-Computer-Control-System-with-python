import matplotlib.pyplot as plt
import math

def xfrange(start,stop,step):
    i =0
    while start+step*i<stop:
        yield start+step*i
        i=i+1

def euler(x0,h,T):
    t=0
    x = []
    stan = 0
    while t<T:
        x.append(x0)
        if (x0>=0.8):
            stan = 1
        if (x0<0.1):
            stan = 0
        if (stan==0):
            x0 = x0 + h * (1-x0)
        if(stan == 1):
           x0 = x0+h*(-x0)

        t = t+h
    return x

x = [x for x in xfrange(0,20,0.05)]
y = euler(0.1,0.05,20)
plt.figure(figsize=(10,5))
plt.ylabel("f(t)")
plt.xlabel("t")
plt.grid(True)
plt.plot(x,y,color = "red", label = "euler")
plt.show()
