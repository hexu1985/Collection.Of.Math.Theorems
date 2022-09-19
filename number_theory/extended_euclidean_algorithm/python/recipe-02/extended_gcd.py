
class Memo:
    def __init__(self):
        self.q = dict()
        self.s = dict()
        self.t = dict()
        self.s[0] = 1; self.t[0] = 0
        self.s[1] = 0; self.t[1] = 1

    def update_q(self, j:int, q_j:int): 
        assert j >= 1
        self.q[j] = q_j
        self.calculate_s_t(j)

    def calculate_s_t(self, j:int):
        if j < 2:
            return
        self.s[j] = self.s[j-2] - self.q[j-1]*self.s[j-1]
        self.t[j] = self.t[j-2] - self.q[j-1]*self.t[j-1]

    def get_s_t(self, j:int):
        assert j >= 0
        return (self.s[j], self.t[j])


def extended_Euclid(a:int, b:int):
    assert a >= b >= 0
    memo = Memo()
    r = a % b 
    q = a // b
    j = 1   # a = r_{0}, b = r_{1}, q = q_{1}, r = r_{2}
    memo.update_q(j, q)
    while r != 0:
        a = b
        b = r
        r = a % b
        q = a // b
        j += 1  # a = r_{j-1}, b = r_{j}, q = q_{j}, r = r_{j+1}
        memo.update_q(j, q)

    s, t = memo.get_s_t(j)
    return s, t, b

def extended_gcd(a:int, b:int):
    assert a >= 0 and b >= 0
    if a < b:
        a, b = b, a # swap(a,b)
    return extended_Euclid(a, b)

def print_extended_gcd(a, b):
    s, t, d = extended_gcd(a, b)
    print("gcd({}, {}) = {}".format(a, b, d))
    print(f"({s}) * {a} + ({t}) * {b} = {d}")

if __name__ == "__main__":
    print_extended_gcd(252, 198)

