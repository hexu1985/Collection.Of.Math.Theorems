
def Euclid(a:int, b:int):
    assert a >= b >= 0
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
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
