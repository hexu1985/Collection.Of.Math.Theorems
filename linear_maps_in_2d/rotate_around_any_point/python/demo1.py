#!/usr/bin/env python3

from vectors import *
from vector_drawing import *

rotate_center_point = (-2, 3)
rotation_angle = pi/6
src_point = (1, 2)
dst_point = add(scale(-1, rotate_center_point), src_point)
dst_point = rotate2d(rotation_angle, dst_point)
dst_point = add(rotate_center_point, dst_point)

draw(
    Points(rotate_center_point),
    Points(src_point, color=gray),
    Points(dst_point, color=red),
    Segment(rotate_center_point,src_point,color=black),
    Segment(rotate_center_point,dst_point,color=black)
)

