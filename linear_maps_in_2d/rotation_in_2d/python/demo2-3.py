#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from dino_vectors import dino_vectors

rotation_angle = pi/4

dino_polar = [to_polar(v) for v in dino_vectors]
dino_rotated_polar = [(l,angle + rotation_angle) for l,angle in dino_polar]
dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]

arrows = [Arrow(tip,tail,color=black) for (tip,tail) in
         zip(dino_rotated, dino_vectors)]
draw(
    Points(*dino_vectors, color=blue),
    Polygon(*dino_vectors, color=blue),
    Points(*dino_rotated, color=red),
    Polygon(*dino_rotated, color=red),
    *arrows
)


