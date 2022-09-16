#include <cassert>
#include <utility>
#include <iostream>

long Euclid(long a, long b) {
    assert(a >= b && b >= 0);
    auto r = a % b;
    while (r != 0) {
        a = b;
        b = r;
        r = a % b;
    }
    return b;
}

long gcd(long a, long b) {
    assert(a >= 0 && b >= 0);
    if (a < b) {
        std::swap(a, b);
    }
    return Euclid(a, b);
}

void print_gcd(long a, long b) {
    std::cout << "gcd(" << a << ", " << b << ") = " << gcd(a, b) << std::endl;
}

int main() {
    print_gcd(252, 198);
}
