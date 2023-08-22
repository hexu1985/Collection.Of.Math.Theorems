import numpy as np
import matplotlib.pyplot as plt

def calculate_line_points(A, B, C, x1, x2, y1, y2):
    assert A != 0 or B != 0
    if A == 0:
        return [x1, x2], [-C/B, -C/B]
    elif B == 0:
        return [-A/C, -A/C], [y1, y2]
    else:
        return [x1, x2], [-(A*x1+C)/B, -(A*x2+C)/B]

def calculate_perpendicular_root(A, B, C, x0, y0):
    t = -(A*x0+B*y0+C)/(A**2+B**2)
    return (A*t+x0), (B*t+y0)

xmin=-10
xmax=10
ymin=-10
ymax=10
plt.axis([xmin, xmax, ymin, ymax])
plt.axis('on')
plt.axis("equal")

plt.grid(True)

# draw line Ax+By+C=0
A=3
B=4
C=5
x, y = calculate_line_points(A,B,C, xmin, xmax, ymin, ymax)
plt.plot(x, y)

# draw point (x0, y0)
x0 = 4
y0 = 5
plt.scatter([x0], [y0])

# calculate foot of a perpendicular (x1, y1)
x1, y1 = calculate_perpendicular_root(A, B, C, x0, y0)

# draw point (x1, y1)
plt.scatter([x1], [y1])

# draw line segment from (x0, y0) to (x1, y1)
plt.plot([x0, x1], [y0, y1])

plt.show()
