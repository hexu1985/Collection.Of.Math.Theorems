#include <cassert>
#include <utility>
#include <map>
#include <tuple>
#include <iostream>

class Memo {
public:
    Memo() {
        s[0] = 1; t[0] = 0;
        s[1] = 0; t[1] = 1;
    }

    void update_q(int j, long q_j) {
        assert(j >= 1);
        q[j] = q_j;
        calculate_s_t(j);
    }

    std::tuple<long, long> get_s_t(int j) {
        assert(j >= 0);
        return std::make_tuple(s[j], t[j]);
    }
    

private:
    void calculate_s_t(int j) {
        if (j < 2)
            return;
        s[j] = s[j-2] - q[j-1]*s[j-1];
        t[j] = t[j-2] - q[j-1]*t[j-1];
    }

private:
    std::map<int, long> q;
    std::map<int, long> s;
    std::map<int, long> t;
};

std::tuple<long, long, long> extended_Euclid(long a, long b) {
    assert(a >= b && b >= 0);
    Memo memo;
    auto r = a % b;
    auto q = a / b;
    int j = 1;  // a = r_{0}, b = r_{1}, q = q_{1}, r = r_{2}
    memo.update_q(j, q);
    while (r != 0) {
        a = b;
        b = r;
        r = a % b;
        q = a / b;
        j += 1; // a = r_{j-1}, b = r_{j}, q = q_{j}, r = r_{j+1}
        memo.update_q(j, q);
    }
    auto [s, t] = memo.get_s_t(j);
    return std::make_tuple(s, t, b);
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
