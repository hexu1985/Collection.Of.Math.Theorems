import numpy as np
import matplotlib.pyplot as plt
import math

def calculate_vectorial_angle_cosine(ax, ay, bx, by):
    len_a = math.sqrt(ax**2+ay**2)
    len_b = math.sqrt(bx**2+by**2)
    cos_theta = (ax*bx+ay*by)/(len_a*len_b)
    return cos_theta

xmin=-10
xmax=10
ymin=-10
ymax=10
plt.axis([xmin, xmax, ymin, ymax])
plt.axis('off')
plt.axis("equal")

plt.grid(True)

head_length=0.3
head_width=0.2

# draw vector a (ax, ay)
ax = 3
ay = 5
plt.arrow(0, 0, ax, ay, head_length=head_length, head_width=head_width, color='k')
plt.text(ax+0.3, ay+0.1, r"$\overrightarrow{\mathbf{a}}$")

# draw vector b (bx, by)
bx = 5
by = -1
plt.arrow(0, 0, bx, by, head_length=head_length, head_width=head_width, color='k')
plt.text(bx+0.3, by+0.1, r"$\overrightarrow{\mathbf{b}}$")

# draw vector c (cx, cy)
cx = -3
cy = 0
plt.arrow(0, 0, cx, cy, head_length=head_length, head_width=head_width, color='k')
plt.text(cx-0.4, cy+0.1, r"$\overrightarrow{\mathbf{c}}$")

# set font style
font_style = {"family":"serif","size":12,"style":"italic","weight":"black"}

# calculate angle between a and b
cos_a_b = calculate_vectorial_angle_cosine(ax, ay, bx, by)
angle_a_b = math.acos(cos_a_b)*180/math.pi
print("cos_a_b: {}".format(cos_a_b))
print("angle_a_b: {}".format(angle_a_b))

# calculate angle between a and c
cos_a_c = calculate_vectorial_angle_cosine(ax, ay, cx, cy)
angle_a_c = math.acos(cos_a_c)*180/math.pi
print("cos_a_c: {}".format(cos_a_c))
print("angle_a_c: {}".format(angle_a_c))

# calculate angle between b and c
cos_b_c = calculate_vectorial_angle_cosine(bx, by, cx, cy)
angle_b_c = math.acos(cos_b_c)*180/math.pi
print("cos_b_c: {}".format(cos_b_c))
print("angle_b_c: {}".format(angle_b_c))

plt.text(-5, 5, r"$<\overrightarrow{\mathbf{a}}, \overrightarrow{\mathbf{b}}> = %3.1f ^\circ$" % angle_a_b, **font_style)
plt.text(-5, 4, r"$<\overrightarrow{\mathbf{a}}, \overrightarrow{\mathbf{c}}> = %3.1f ^\circ$" % angle_a_c, **font_style)
plt.text(-5, 3, r"$<\overrightarrow{\mathbf{b}}, \overrightarrow{\mathbf{c}}> = %3.1f ^\circ$" % angle_b_c, **font_style)

plt.show()

