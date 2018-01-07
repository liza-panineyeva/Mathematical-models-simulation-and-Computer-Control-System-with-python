import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#using streamplot

def euler(x0,y0,T,h,a,b):
    t=0
    time = []
    x=[]
    y=[]

    while t<=T:
        time.append(t)
        x.append(x0)
        y.append(y0)
        x0 = x0 + h * (y0+x0-x0**3/3+0.4)
        y0 = y0 + h *(-x0+a-b*y0)
        t = t+h
    return x,y,time
def model(a,b,x,y):
    u,v = y+x-x**3/3+0.4, -x+a-b*y
    return u,v


if __name__ == "__main__":

    l = 5.0
    n = 100
    mu=0.5
    x1 = np.linspace(-l,l,n)
    x2 = np.linspace(-l,l,n)
    X1,X2 = np.meshgrid(x1,x2)
    U,V = model(0.8,0.5,X1,X2)
    vels = (U**2+V**2)**0.5
    lw = 4*vels/np.max(vels)
    fig1 = plt.figure()
    ax2 = fig1.add_subplot()
    plt.streamplot(X1, X2, U, V, arrowsize=2,density=2, arrowstyle='->',color = vels, linewidth=lw, cmap = plt.cm.seismic)
    plt.show()