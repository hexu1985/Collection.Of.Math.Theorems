#!/usr/bin/env python3

from vectors import *
from vector_drawing import *
from matrices import *
from utility import *
from dino_vectors import dino_vectors

homo_dino_vectors = points_to_homogeneous_coordinates(dino_vectors)
homo_dino_vectors2 = translate_in_2d((-1.5, -2.5), homo_dino_vectors)
dino_vectors2 = points_from_homogeneous_coordinates(homo_dino_vectors2)

arrows = [Arrow(tip,tail,color=black) for (tip,tail) in
         zip(dino_vectors2, dino_vectors)]
draw(
    Points(*dino_vectors, color=blue),
    Polygon(*dino_vectors, color=blue),
    Points(*dino_vectors2, color=red),
    Polygon(*dino_vectors2, color=red),
    *arrows
)
