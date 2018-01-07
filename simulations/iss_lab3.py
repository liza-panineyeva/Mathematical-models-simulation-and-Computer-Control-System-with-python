import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler(x0,y0,T,h):
    t=0
    time = []
    x=[]
    y=[]
    while t<=T:
        time.append(t)
        x.append(x0)
        y.append(y0)
        x0 = x0 +(-x0*x0*x0+6*x0-y0)*h
        y0 = y0+(x0-0.07)*h
        t = t+h
    return x,y,time

if __name__ == "__main__":
    y1,y2,time = euler(1,1,30,0.01)
     #plt.plot(time,y1,color="blue")
    #plt.plot(time,y2,color="red")
    plt.plot(y1,y2)
    plt.scatter(y1[0],y2[0], marker='o', color='r')
    plt.scatter(y1[len(y1)-1], y2[len(y2)-2], marker='x', color='y', label = 'end')
    plt.legend(loc = 'best')
    plt.show()
