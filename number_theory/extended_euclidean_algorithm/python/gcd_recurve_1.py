
def Euclid(a:int, b:int, j:int):
    assert a >= b >= 0
    if b == 0:
        return a
    print("j={j}: {r_j} = {r_j_1} * {q_j_1} + {r_j_2}".format(j=j, r_j=a, r_j_1=b, q_j_1=a//b, r_j_2=a%b))
    return Euclid(b, a%b, j+1)

def gcd(a:int, b:int):
    assert a >= 0 and b >= 0
    if a < b:
        a, b = b, a # swap(a,b)
    return Euclid(a, b, 0)

def print_gcd(a, b):
    print("gcd({}, {}) = {}".format(a, b, gcd(a, b)))

if __name__ == "__main__":
    print_gcd(252, 198)
