#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from homogeneous_coordinates_2d import *
from matrices import *
from dino_vectors import dino_vectors

rotation_angle = pi/4

homo_dino_vectors = point2d_list_to_homogeneous(dino_vectors)
m = create_rotate2d_matrix(rotation_angle)
homo_dino_rotated = [multiply_matrix_vector(m, v) for v in homo_dino_vectors]
dino_rotated = point2d_list_from_homogeneous(homo_dino_rotated)

draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_rotated, color=red)
)
