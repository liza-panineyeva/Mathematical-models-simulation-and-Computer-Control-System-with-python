import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as ax3d
import random
import matplotlib.animation as animation
from matplotlib import cm

#układ lorentza 2d i 3d

def euler(x0,y0,z0,T,h):
    t=0
    time = []
    x=[]
    y=[]
    z = []
    while t<=T:
        time.append(t)
        x.append(x0)
        y.append(y0)
        z.append(z0)
        x0 = x0+10*(y0-x0)*h
        y0 = y0+(28*x0-y0-x0*z0)*h
        z0 = z0 + ((-8/3)*z0+x0*y0)*h
        t = t+h
    return x,y,z,time
def model(x,y,z):
    x0 = 10*(y-x)
    y0 = (28*x-y-x*z)
    z0 = ((-8/3)*z+x*y)
    return x0,y0
if __name__ == "__main__":
    y1,y2,y3,time = euler(1,1,1,30,0.01)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax1.plot(time,y1,color="blue")
    ax1.plot(time,y2,color="red")
    ax1.plot(time, y3, color="yellow")
    ax2.plot(y1,y2)
    ax2.scatter(y1[0], y2[0], marker='o', color='r', label='start')
    ax2.scatter(y1[len(y1)-1], y2[len(y2)-2], marker='x', color='y', label='end')
    plt.legend(loc = 'best')

    fig3 = plt.figure()
    a = ax3d.Axes3D(fig3)
    a.plot(y1,y2,y3, color = 'pink')

    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111, projection= '3d')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('z')

    for i in range (0,20):
        y1, y2, y3, time = euler(random.randint(0, 20) , random.randint(0, 20) , random.randint(0, 20) , 30, 0.01)
        ax4.plot(y1,y2,y3)
        ax4.scatter(y1[0], y2[0],y3[0], marker='o', color='r', label='start')
        ax4.scatter(y1[len(y1) - 1], y2[len(y2) - 2],y3[len(y3) - 3], marker='x', color='b', label='end')
    #plt.streamplot(X1, X2, U, V, arrowsize=2, density=2, arrowstyle='->', color=vels, linewidth=lw, cmap=plt.cm.seismic)
    plt.show()
    #ax3.plot(y1,y2,y3,color="pink")

    '''plt.scatter(y1[0],y2[0], marker='o', color='r')
    plt.scatter(y1[len(y1)-1], y2[len(y2)-2], marker='x', color='y', label = 'end')
    plt.legend(loc = 'best')'''
