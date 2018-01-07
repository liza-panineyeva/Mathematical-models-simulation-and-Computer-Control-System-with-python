import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def get_chart(x0, y0, time, h, d):
    all_x = []
    all_y = []
    x_prior = x0
    y_prior = y0
    for i in range(0, len(time)):
        x = x_prior + h * (0.04 * x_prior ** 2 + 5 * x_prior + 140 - y_prior + 30)
        y = y_prior + h * (0.02 * (0.2 * x - y_prior))
        if (x >= 30):
            x = c
            y = y + d
        all_x.append(x_prior)
        all_y.append(y_prior)
        x_prior = x
        y_prior = y
    return all_x, all_y


T, t0 = 100, 0
c = -65
d = 8
x0, y0 = c, 0
h = 0.01

time = np.arange(t0, T, h).tolist()
line1, line2 = get_chart(x0, y0, time, h, 8)

fig = plt.figure()
ax2 = fig.add_subplot(211)
ax3 = fig.add_subplot(212)

ax2.plot(time, line1, color='g')
ax2.set_xlabel("czas")
ax2.plot(time, line2, color='b')

ax3.plot(line1, line2, color='m')
ax3.set_xlabel("V")
ax3.set_ylabel("X")

ax2.grid()
ax3.grid()

plt.show()