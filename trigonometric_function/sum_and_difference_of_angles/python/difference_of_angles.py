# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1=-8
x2=8
y1=-8
y2=8
plt.axis([x1,x2,y1,y2])

plt.title("difference of angles")
plt.axis('off')
plt.grid(False)

# 绘制坐标轴
plt.arrow(x1+1, 0, x2-x1-2, 0, head_length=0.4, head_width=0.3, color='k')
plt.text(x2-1, 0.5, 'x')
plt.arrow(0, y1+1, 0, y2-y1-2, head_length=0.4, head_width=0.3, color='k')
plt.text(0.5, y2-1, 'y')

# 隐藏刻度值
ax = plt.gca()

ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])

# 设置等比例
ax.set_aspect(1)

# 绘制原点
plt.text(-0.8, -0.8, r"$O$")

# 绘制单位圆
xc=0
yc=0
r=5

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1,p2+dp,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],color='k')
    xlast=x
    ylast=y

# 绘制点
alpha = 130*np.pi/180
xp = xc+r*np.cos(alpha)
yp = xc+r*np.sin(alpha)
plt.scatter(xp, yp, color='k')
plt.text(xp-4, yp+0.2, r"$P(\cos \alpha, \sin \alpha)$")

beta = 30*np.pi/180
xq = xc+r*np.cos(beta)
yq = xc+r*np.sin(beta)
plt.scatter(xq, yq, color='k')
plt.text(xq, yq+0.3, r"$Q(\cos \beta, \sin \beta)$")

plt.scatter(r, 0, color='k')
plt.text(r+0.2, -0.8, r"$A(1, 0)$")

# 绘制线

plt.plot([xc, xp], [yc, yp], color='k') # OP
plt.plot([xc, xq], [yc, yq], color='k') # OQ
plt.plot([xp, xq], [yp, yq], color='k') # PQ

# 绘制角的弧线和名称
p1=0
p2=alpha
r=0.8
dp=(p2-p1)/50
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1+dp,p2,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],linewidth=1,color='r')
    xlast=x
    ylast=y

plt.text(xc+(r+0.2)*np.cos(p2/2), yc+(r+0.2)*np.sin(p2/2), r"$\alpha$")

p1=0
p2=beta
r=1.5
dp=(p2-p1)/50
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1+dp,p2,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],linewidth=1,color='b')
    xlast=x
    ylast=y

plt.text(xc+(r+0.2)*np.cos(p2/2), yc+(r+0.2)*np.sin(p2/2), r"$\beta$")

p1=beta
p2=alpha
r=2
dp=(p2-p1)/50
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
for p in np.arange(p1+dp,p2,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],linewidth=1,color='g')
    xlast=x
    ylast=y

plt.text(xc+(r+0.2)*np.cos(p2/2), yc+(r+0.2)*np.sin(p2/2), r"$\alpha - \beta$")

plt.show()
