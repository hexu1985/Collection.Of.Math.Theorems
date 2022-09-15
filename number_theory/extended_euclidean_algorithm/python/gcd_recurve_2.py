
def Euclid(a:int, b:int, j:int):
    ''' 
    return s, t, d
    s * a + t * b = d
    '''
    assert a >= b >= 0
    if b == 0:
        # (s * a + t * b) 
        print("j={j}: ({s}) * {a} + ({t}) * {b} = {d}".format(j=j, s=1, a=a, t=0, b=b, d=a))
        return (1, 0, a)
    print("j={j}: {r_j} = {r_j_1} * {q_j_1} + {r_j_2}".format(j=j, r_j=a, r_j_1=b, q_j_1=a//b, r_j_2=a%b))
    x, y, d = Euclid(b, a%b, j+1)
    # x * b + y * (a%b) = d
    # a%b == a - (a//b)*b
    # x * b + y * (a - (a//b) * b) = d
    # y * a + (x - y * (a//b)) * b = d
    print("j={j}: ({s}) * {a} + ({t}) * {b} = {d}".format(j=j, s=y, a=a, t=(x-y*(a//b)), b=b, d=d))
    return (y, (x-y*(a//b)), d)

def gcd(a:int, b:int):
    assert a >= 0 and b >= 0
    if a < b:
        a, b = b, a # swap(a,b)
    return Euclid(a, b, 0)

def print_gcd(a, b):
    s, t, d = gcd(a, b)
    print("gcd({}, {}) = {}".format(a, b, d))
    print(f"({s}) * {a} + ({t}) * {b} = {d}")

if __name__ == "__main__":
    print_gcd(252, 198)
