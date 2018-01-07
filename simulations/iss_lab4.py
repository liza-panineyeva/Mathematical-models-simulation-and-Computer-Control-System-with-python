import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

if __name__ == "__main__":
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(211)
    y1,y2,time = euler(1,-4,30,0.01,0.8,0.5)
    y3, y4, time1 = euler(0, -5, 30, 0.01, 0.8, 0.5)
    ax1.plot(time,y1,color="blue")
    ax1.plot(time,y2,color="red")
    # = -1 - 1 ** 2 +y2
    #V = 1 + y1 +y2 ** 2
    ax1.set_xlabel("t")
    ax2.plot(y1,y2)
    ax2.plot(y3, y4)

    ax2.scatter(y1[0],y2[0], marker='o', color='r',label = 'start')
    ax2.scatter(y1[len(y1)-1], y2[len(y2)-2], marker='x', color='y', label = 'end')
    ax2.legend(loc = 'best')
    plt.show()
