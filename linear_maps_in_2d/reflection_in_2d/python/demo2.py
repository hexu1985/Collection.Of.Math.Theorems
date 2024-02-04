#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from dino_vectors import dino_vectors

scaling_vector = (-1, 1)
dino_scaled = [(scaling_vector[0]*v[0], scaling_vector[1]*v[1]) for v in dino_vectors]

draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_scaled, color=red)
)


