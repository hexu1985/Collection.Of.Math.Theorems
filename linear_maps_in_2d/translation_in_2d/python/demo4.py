#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from dino_vectors import dino_vectors

dino_vectors2 = [add((-1.5,-2.5), v) for v in dino_vectors]

arrows = [Arrow(tip,tail,color=black) for (tip,tail) in
         zip(dino_vectors2, dino_vectors)]
draw(
    Points(*dino_vectors, color=blue),
    Polygon(*dino_vectors, color=blue),
    Points(*dino_vectors2, color=red),
    Polygon(*dino_vectors2, color=red),
    *arrows
)


