

def calucate_line_equation_by_two_points(x1, y1, x2, y2):
    a = y2-y1
    b = x2-x1
    A = a
    B = -b
    C = b*y1-a*x1
    return A, B, C

if __name__ == "__main__":
    x1 = 3
    y1 = 5
    x2 = -2
    y2 = -2
    print("P1({},{}) - P2({},{})".format(x1, y1, x2, y2))
    A, B, C = calucate_line_equation_by_two_points(x1, y1, x2, y2)
    print("Ax+By+C=0: A={}, B={}, C={}".format(A, B, C))
    print("Ax1+By1+C={}".format(A*x1+B*y1+C))
    print("Ax2+By2+C={}".format(A*x2+B*y2+C))

