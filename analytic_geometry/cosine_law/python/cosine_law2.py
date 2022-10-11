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

# 隐藏刻度值
ax = plt.gca()

ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])


xa = -4; ya = 6;
xb = 5; yb = 0
xc = 0; yc = 0;

# 绘制边
plt.plot([xa, xb], [ya, yb], linewidth=2, color='k')
plt.plot([xa, xc], [ya, yc], linewidth=2, color='k')
plt.plot([xb, xc], [yb, yc], linewidth=2, color='k')

# 绘制边的名称
plt.text((xa+xb)/2+0.3, (ya+yb)/2, "c")
plt.text((xa+xc)/2-0.8, (ya+yc)/2, "b")
plt.text((xb+xc)/2+0.4, (yb+yc)/2-0.6, "a")

# 绘制辅助线
plt.plot([xa, 0], [ya, ya], color='gray', linestyle=':')
plt.plot([xa, xa], [ya, 0], color='gray', linestyle=':')

# 绘制点
plt.scatter([xa, xb, xc], [ya, yb, yc])
plt.scatter([xa, 0], [0, ya])

# 绘制点的名称
plt.text(xa-0.3, ya+0.3, r"$A (b \cdot \cos \theta, b \cdot \sin \theta)$")
plt.text(xb, yb-0.8, r"$B (a, 0)$")
plt.text(xc, yc-0.8, r"$C (0, 0)$")

# 计算角的度数
theta = np.degrees(np.arctan((ya-yc)/(xa-xc)))
if theta < 0:
    theta += 180
print("theta: {}".format(theta))

# 绘制角的弧线
p1=0
p2=theta*np.pi/180
r=(xb-xc)/7
dp=(p2-p1)/50
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1+dp,p2,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],linewidth=0.5,color='k')
    xlast=x
    ylast=y

# 绘制角的名称
plt.text(xc+0.7, yc+0.7, r"$\theta$")

plt.show()

