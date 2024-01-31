from matrices import *

def point_to_homogeneous_coordinates(v):
    return (*v, 1)

def point_from_homogeneous_coordinates(v):
    return tuple(v[:-1])

def points_to_homogeneous_coordinates(vlist):
    return [point_to_homogeneous_coordinates(v) for v in vlist]

def points_from_homogeneous_coordinates(vlist):
    return [point_from_homogeneous_coordinates(v) for v in vlist]

def multiply_matrix_vector_list(m, vlist):
    return [multiply_matrix_vector(m, v) for v in vlist]

def translate_in_2d(v, vlist): 
    m = ((1, 0, v[0]),
         (0, 1, v[1]),
         (0, 0,    1))
    return multiply_matrix_vector_list(m, vlist)
