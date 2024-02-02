#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from homogeneous_coordinates_2d import *
from matrices import *
from dino_vectors import dino_vectors

homo_dino_vector = point2d_list_to_homogeneous(dino_vectors)
m = create_translate2d_matrix((-1.5, -2.5))
homo_dino_vector2 = [multiply_matrix_vector(m, v) for v in homo_dino_vector]
dino_vectors2 = point2d_list_from_homogeneous(homo_dino_vector2)

draw(
    Points(*dino_vectors, color=blue),
    Polygon(*dino_vectors, color=blue),
    Points(*dino_vectors2, color=red),
    Polygon(*dino_vectors2, color=red)
)

