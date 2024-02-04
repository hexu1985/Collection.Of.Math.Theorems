#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from dino_vectors import dino_vectors

rotation_angle = pi/4

dino_rotated = [rotate2d(rotation_angle, v) for v in dino_vectors]

draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_rotated, color=red)
)
