from math import sin, cos


def point2d_to_homogeneous(point):
    assert len(point) == 2
    return (point[0], point[1], 1)

def point2d_from_homogeneous(point):
    assert len(point) == 3 and point[2] == 1
    return (point[0], point[1])

def point2d_list_to_homogeneous(points):
    return [point2d_to_homogeneous(point) for point in points]

def point2d_list_from_homogeneous(points):
    return [point2d_from_homogeneous(point) for point in points]

def create_translate2d_matrix(translation):
    assert len(translation) == 2
    m13 = translation[0]
    m23 = translation[1]
    return ((1, 0, m13),
            (0, 1, m23),
            (0, 0,   1))

def create_rotate2d_matrix(rotate_angle):
    m11 = cos(rotate_angle)
    m21 = sin(rotate_angle)
    m12 = -m21  # -sin(rotate_angle)
    m22 = m11   #  cos(rotate_angle)
    return ((m11, m12, 0),
            (m21, m22, 0),
            (  0,   0, 1))

def create_scale2d_matrix(scaling_vector):
    assert len(scaling_vector) == 2
    m11 = scaling_vector[0]
    m22 = scaling_vector[1]
    return ((m11,   0, 0),
            (  0, m22, 0),
            (  0,   0, 1))

def create_shear2d_matrix(shear_vector):
    assert len(shear_vector) == 2
    m12 = shear_vector[0]
    m21 = shear_vector[1]
    return ((  1, m12, 0),
            (m21,   1, 0),
            (  0,   0, 1))
