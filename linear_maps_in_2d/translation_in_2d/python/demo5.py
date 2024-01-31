#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from matrices import *
from utility import *
from dino_vectors import dino_vectors

homo_dino_vectors = [point_to_homogeneous_coordinates(v) for v in dino_vectors]

m = ((1, 0, -1.5),
     (0, 1, -2.5),
     (0, 0,    1))

homo_dino_vectors2 = [multiply_matrix_vector(m, v) for v in homo_dino_vectors]

dino_vectors2 = [point_from_homogeneous_coordinates(v) for v in homo_dino_vectors2]


arrows = [Arrow(tip,tail,color=black) for (tip,tail) in
         zip(dino_vectors2, dino_vectors)]
draw(
    Points(*dino_vectors, color=blue),
    Polygon(*dino_vectors, color=blue),
    Points(*dino_vectors2, color=red),
    Polygon(*dino_vectors2, color=red),
    *arrows
)
