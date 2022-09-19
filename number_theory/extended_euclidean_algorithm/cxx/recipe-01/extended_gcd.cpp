#include <cassert>
#include <utility>
#include <tuple>
#include <iostream>

std::tuple<long, long, long> extended_Euclid(long a, long b) {
    /* 
    return s, t, d
    s * a + t * b = d
    */
    assert(a >= b && b >= 0);
    if (b == 0) {
        // s * a + t * b = d
        // d = a and s = 1 and t = 0
        return std::make_tuple(1, 0, a);
    }
    auto [s, t, d] = extended_Euclid(b, a%b);
    // a = r_{j}, b = r_{j+1}, a%b = r_{j+2}, a//b = q_{j+1}
    // d = t * r_{j} + (s - t * q_{j+1}) * r_{j+1}
    // return t, (s - t * (a//b)), d
    return std::make_tuple(t, (s-t*(a/b)), d);
}

std::tuple<long, long, long> extended_gcd(long a, long b) {
    assert(a >= 0 && b >= 0);
    if (a < b) {
        std::swap(a, b);
    }
    return extended_Euclid(a, b);
}

void print_extended_gcd(long a, long b) {
    auto [s, t, d] = extended_gcd(a, b);
    std::cout << "gcd(" << a << ", " << b << ") = " << d << std::endl;
    std::cout << "(" << s << ") * " << a << " + (" << t << ") * " << b << " = " << d << std::endl;
}

int main() {
    print_extended_gcd(252, 198);
}
