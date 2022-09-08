
def Euclid(a:int, b:int):
    assert a >= b >= 0
    j = 0
    r = a % b
    print("j={j}: {r_j} = {r_j_1} * {q_j_1} + {r_j_2}".format(j=j, r_j=a, r_j_1=b, q_j_1=a//b, r_j_2=r))
    while r != 0:
        j += 1
        a = b
        b = r
        r = a % b
        print("j={j}: {r_j} = {r_j_1} * {q_j_1} + {r_j_2}".format(j=j, r_j=a, r_j_1=b, q_j_1=a//b, r_j_2=r))
    return b

def gcd(a:int, b:int):
    assert a >= 0 and b >= 0
    if a < b:
        a, b = b, a # swap(a,b)
    return Euclid(a, b)

def print_gcd(a, b):
    print("gcd({}, {}) = {}".format(a, b, gcd(a, b)))

if __name__ == "__main__":
    print_gcd(252, 198)

