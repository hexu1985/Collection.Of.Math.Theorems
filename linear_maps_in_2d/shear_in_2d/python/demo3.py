#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from homogeneous_coordinates_2d import *
from matrices import *
from dino_vectors import dino_vectors

shear_vector = (0.25, 0)
homo_dino_vectors = point2d_list_to_homogeneous(dino_vectors)
m = create_shear2d_matrix(shear_vector)
homo_dino_sheared = [multiply_matrix_vector(m, v) for v in homo_dino_vectors]
dino_sheared = point2d_list_from_homogeneous(homo_dino_sheared)

draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_sheared, color=red)
)


