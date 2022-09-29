# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1=-10
x2=10
y1=-10
y2=10
plt.axis([x1,x2,y1,y2])

plt.axis('on')
plt.grid(True)

xa = -2; ya = 6;
xb = 5; yb = 0
xc = 0; yc = 0;

plt.plot([xa, xb], [ya, yb])
plt.plot([xa, xc], [ya, yc])
plt.plot([xb, xc], [yb, yc])

plt.show()

