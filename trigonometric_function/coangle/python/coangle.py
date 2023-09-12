#!/usr/bin/env python3

# Usage: coangle.py [theta]
# 根据输入角度theta的值，
# 在坐标系上绘制theta角的射线，-theta角的射线，以及pi/2-theta角的射线

import numpy as np
import matplotlib.pyplot as plt
import math
import sys

xmin=-100
xmax=100
ymin=-100
ymax=100
plt.axis([xmin, xmax, ymin, ymax])
plt.axis('on')
plt.axis("equal")

plt.plot([xmin, xmax], [0, 0], color='k')
plt.plot([0, 0], [ymin, ymax], color='k')

r=100

# degree
theta=math.radians(120)
if len(sys.argv) == 2:
    theta=math.radians(float(sys.argv[1]))

x1 = r*math.cos(theta)
y1 = r*math.sin(theta)

x2 = r*math.cos(math.pi/2-theta)
y2 = r*math.sin(math.pi/2-theta)

x3 = r*math.cos(-theta)
y3 = r*math.sin(-theta)

plt.plot([0, x1], [0, y1], label=r"$\theta$")
plt.plot([0, x2], [0, y2], label=r"$\frac{\pi}{2} - \theta$")
plt.plot([0, x3], [0, y3], label=r"$-\theta$")

plt.legend()

plt.grid(True)

plt.show()
