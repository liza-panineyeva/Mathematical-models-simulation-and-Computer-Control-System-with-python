import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 #neurons simulation
def euler(x0,y0,T,h,c,d):
    t=0
    time = []
    x=[]
    y=[]

    while t<=T:
        time.append(t)
        x.append(x0)
        y.append(y0)
        x0 = x0 + h * (0.04 * x0 ** 2 + 5 * x0 + 140 - y0+ 30)
        y0 = y0 + h * (0.02 * (0.2 * x0 - y0))
        if (x0>=30):
            x0=c
            y0=y0+d
        t = t+h
    return x,y,time

if __name__ == "__main__":
    y1,y2,time = euler(-65,1,100,0.01,-65,8)
    plt.plot(time,y1,color="blue")
    plt.plot(time,y2,color="red")
    #plt.plot(y1,y2)
    #plt.scatter(y1[0],y2[0], marker='o', color='r')
    #plt.scatter(y1[len(y1)-1], y2[len(y2)-2], marker='x', color='y', label = 'end')
    #plt.legend(loc = 'best')
    plt.show()
