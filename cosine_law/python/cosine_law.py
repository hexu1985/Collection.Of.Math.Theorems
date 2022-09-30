# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1=-10
x2=10
y1=-5
y2=10
plt.axis([x1,x2,y1,y2])

plt.title("cosine law")
plt.axis('on')
plt.grid(True)

xa = -4; ya = 6;
xb = 5; yb = 0
xc = 0; yc = 0;

# 绘制边
plt.plot([xa, xb], [ya, yb], linewidth=2, color='k')
plt.plot([xa, xc], [ya, yc], linewidth=2, color='k')
plt.plot([xb, xc], [yb, yc], linewidth=2, color='k')

# 绘制辅助线
plt.plot([xa, 0], [ya, ya], color='gray', linestyle=':')
plt.plot([xa, xa], [ya, 0], color='gray', linestyle=':')

# 绘制点
plt.scatter([xa, xb, xc], [ya, yb, yc])
plt.scatter([xa, 0], [0, ya])

# 绘制点的名称
plt.text(xa-0.3, ya+0.3, "A")
plt.text(xb, yb-0.8, "B")
plt.text(xc, yc-0.8, "C")

plt.show()

