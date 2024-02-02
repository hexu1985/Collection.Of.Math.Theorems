
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