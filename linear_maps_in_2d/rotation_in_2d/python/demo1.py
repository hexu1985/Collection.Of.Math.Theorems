#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from dino_vectors import dino_vectors

draw(
    Points(*dino_vectors),
    Polygon(*dino_vectors)
)


