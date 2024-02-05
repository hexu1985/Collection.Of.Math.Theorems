#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from dino_vectors import dino_vectors

shear_vector = (0.25, 0)
dino_scaled = [(v[0]+shear_vector[0]*v[1], v[0]*shear_vector[1]+v[1]) for v in dino_vectors]

draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_scaled, color=red)
)


