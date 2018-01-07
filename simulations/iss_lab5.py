import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#regulator dwupołożeniowy dla ruchu z przyspieszeniem (opóźnieniem)


def euler(a,y0,T,h,d):
    delay = 0.5 #czas opóźnienia
    wstecz =(int)(delay/h) #ile iteracji wstecz musimy wrócić(w liście błędów), gdy wyliczamy u(t)
    t=0
    time = []
    u=[]
    y=[]
    e = [] #błedy
    e_o = [] #opóźnione błędy
    u0 = 0
    i = 0 #licznik iteracji
    e_op = 0 #jest zerem dla pierwszych kilku iteracji
    while t<=T:
        e0 = d - y0
        e.append(e0)
        if (wstecz<=i):
            e_op = e[i-wstecz]
        e_o.append(e_op)
        if (e_op>0):
            u0=1
        if (e_op<=-0.1):
            u0=0
        time.append(t)
        y.append(y0)
        u.append(u0)
        y0 = y0+(y0*a+u0)*h
        t = t+h
        i+=1
    return y,u,time,e,e_o

if __name__ == "__main__":


    y,u,time,e,e_op = euler (-0.5,0.0,5,0.01,0.7)
    print(e)
    print(e_op)
    fig1 = plt.figure()
    ax2 = fig1.add_subplot(212)
    ax1 = fig1.add_subplot(211)
    ax2.plot(time,u,color = 'y')
    ax1.plot(time,e_op,color = 'r')
    ax1.set_title('e(t)')
    ax2.set_title('u(t)')
    plt.show()