#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from homogeneous_coordinates_2d import *
from matrices import *
from dino_vectors import dino_vectors

scaling_vector = (1, -1)
homo_dino_vectors = point2d_list_to_homogeneous(dino_vectors)
m = create_scale2d_matrix(scaling_vector)
homo_dino_scaled = [multiply_matrix_vector(m, v) for v in homo_dino_vectors]
dino_scaled = point2d_list_from_homogeneous(homo_dino_scaled)

draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_scaled, color=red)
)


