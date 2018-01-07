import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def euler(a,y0,T,h,d):

    t=0
    time = []
    u=[]
    y=[]
    e=[]
    u0 = 0
    sum = 0
    div = 0
    i=0

    while t<=T:
        time.append(t)
        y.append(y0)
        e0 = d - y0
        e.append(e0)
        sum = sum + e0*h
        if i>=2:
            div = (e0 - e[len(e)-2])/h
        u0 = 0.5*e0+2*sum+div*4
        y0 = y0 + (y0 * a + u0) * h
        t = t+h

        u.append(u0)
        i+=1

    return y,u,time,e

if __name__ == "__main__":
    y,u,time,e = euler (-0.5,0,30,0.01,0.5)
    print (u)
    print (e)
    fig1 = plt.figure()
    ax2 = fig1.add_subplot(311)
    #ax2.set_ylim(-1,1)
    #ax2.set_xlim(-1,5.0)
    ax1 = fig1.add_subplot(312)
    #ax3 = fig1.add_subplot(313)
    ax2.set_xlabel('t')
    ax2.set_ylabel('u')
    ax2.plot(time,u,color = 'y')
    ax1.plot(time,e,color = 'r')
    #ax3.set_xlim(-0.1,0.1)
    #ax3.set_ylim(-2,2)
    #ax3.plot(e,u,color = 'pink')
    plt.show()