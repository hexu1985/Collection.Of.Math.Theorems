
def extended_Euclid(a:int, b:int, j:int):
    ''' 
    return s, t, d
    s * a + t * b = d
    '''
    assert a >= b >= 0
    if b == 0:
        # s * a + t * b = d
        # d = a and s = 1 and t = 0
        return (1, 0, a)
    s, t, d = extended_Euclid(b, a%b, j+1)
    # a = r_{j}, b = r_{j+1}, a%b = r_{j+2}, a//b = q_{j+1}
    # d = t * r_{j} + (s - t * q_{j+1}) * r_{j+1}
    # return t, (s - t * (a//b)), d
    return (t, (s-t*(a//b)), d)

def extended_gcd(a:int, b:int):
    assert a >= 0 and b >= 0
    if a < b:
        a, b = b, a # swap(a,b)
    return extended_Euclid(a, b, 0)

def print_extended_gcd(a, b):
    s, t, d = extended_gcd(a, b)
    print("gcd({}, {}) = {}".format(a, b, d))
    print(f"({s}) * {a} + ({t}) * {b} = {d}")

if __name__ == "__main__":
    print_extended_gcd(252, 198)
