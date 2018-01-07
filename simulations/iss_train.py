import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def xfrange(start,stop,step):
    i = 0
    while start+step*i<=stop:
        yield start+step*i
        i = i+1
x = [x for x in xfrange(0,10,0.01)]
def euler(x0,y0,z0,a,b,c,T,h):
    x = []
    y = []
    z = []
    t=0
    while t<T:
        x.append(x0)
        y.append(y0)
        z.append(z0)
        x0 = x0+h*y0
        y0 = y0+h*z0
        z0 = z0 +(- a*z0-b*y0-c*x0)*h
        t = t+h
    return x,y,z

y1,y2,y3 = euler(1,0,-1,1,1,1,10,0.01)


fig1 = plt.figure()
ax1 = fig1.add_subplot(111,projection = '3d')
'''plt.plot(x,y1,color ="blue")
plt.plot(x,y2,color="red")
plt.plot(x,y3,color="yellow")'''
ax1.plot(y1,y2,y3)
plt.show()