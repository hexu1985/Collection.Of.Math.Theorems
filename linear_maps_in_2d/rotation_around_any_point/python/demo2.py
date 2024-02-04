#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from homogeneous_coordinates_2d import *
from matrices import *

rotate_center_point = (-2, 3)
rotation_angle = pi/6

src_point = (1, 2)
homo_src_point = point2d_to_homogeneous(src_point)
m1 = create_translate2d_matrix(scale(-1, rotate_center_point))
m2 = create_rotate2d_matrix(rotation_angle)
m3 = create_translate2d_matrix(rotate_center_point)
m = matrix_multiply(m3, matrix_multiply(m2, m1))
homo_dst_point = multiply_matrix_vector(m, homo_src_point)
dst_point = point2d_from_homogeneous(homo_dst_point)

draw(
    Points(rotate_center_point),
    Points(src_point, color=gray),
    Points(dst_point, color=red),
    Segment(rotate_center_point,src_point,color=black),
    Segment(rotate_center_point,dst_point,color=black)
)

