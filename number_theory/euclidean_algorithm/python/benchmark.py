import math

def print_gcd(a, b):
    print("gcd({}, {}) = {}".format(a, b, math.gcd(a, b)))

if __name__ == "__main__":
    print_gcd(252, 198)
    print_gcd(414, 662)
