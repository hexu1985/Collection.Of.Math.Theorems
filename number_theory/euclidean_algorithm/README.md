## 欧几里得算法（Euclidean algorithm）的证明与实现

欧几里得算法也称为辗转相除法, 用于计算两个正整数的最大公因数, 一般用(a,b)来表示a和b的最大公因数, 计算机领域一般表示成gcd(a,b).

### 欧几里得算法（Euclidean algorithm）的证明

欧几里得算法的定理描述如下:

**定理（欧几里得算法）** 令整数$r_0 = a$，$r_1 = b$满足$a \ge b > 0$，如果连续做带余除法得到$r_j = r_{j+1} q_{j+1} + r_{j+2}$，
且$0 < r_{j+2}  < r_{j+1}$（$j = 0, 1, 2, \cdots, n-2$），$r_{n+1} = 0$，那么$(a, b) = r_n$，它是最后一个非零余数。

从定理中我们看到通过连续应用带余除法，在每一步中被除数和除数被更小的数代替（这些更小的数实际上是每一步中的除数和余数），运算直到余数为零时终止。
这一系列运算产生了一系列的等式，而最大公因子就是最后一个非零的余数。

接下来我们看看欧几里得算法的定理证明:

**证明** 令$r_0 = a$，$r_1 = b$是正整数且满足$a \ge b$，那么通过连续运用带余除法，我们求得

$$
\begin{aligned}
    r_0 & = r_1 \cdot q_1 + r_2             & 0 \le r_2 < r_1 \\
    r_1 & = r_2 \cdot q_2 + r_3             & 0 \le r_3 < r_2 \\
        & \vdots                            & \\
    r_j & = r_{j+1} \cdot q_{j+1} + r_{j+2} & 0 \le r_{j+2} < r_{j+1} \\
        & \vdots                            & \\
r_{n-2} & = r_{n-1} \cdot q_{n-1} + r_n     & 0 \le r_n < r_{n-1} \\
r_{n-1} & = r_n \cdot q_n
\end{aligned}
$$

可以假设最终一定会有一个余数为零，这是因为余数组成的序列$a = r_0 \ge r_1 > r_2 > \cdots \ge 0$所包含的项的个数不会大于$a$（因为每个余数都是整数）。
由引理1，我们得到$(a, b) = (r_0, r_1) = (r_1, r_2) = (r_2, r_3) = \cdots = (r_{n-2}, r_{n-1}) = (r_{n-1}, r_n) = (r_n, 0) = r_n$。因此$(a, b) = r_n$，
这是最后一个非零余数。$\blacksquare$

**引理1** 如果$e$和$d$是整数且$e = d \cdot q + r$，其中$q$，$r$是整数，那么$(e, d) = (d, r)$。

**证明** 在定理1中，取$a = r$，$b = d$，$c = q$，（即$(r + q \cdot d, d) = (r, d)$），那么由定理1可以直接得到引理。$\blacksquare$

**定理1** 令$a$，$b$，$c$是整数，那么$(a + c \cdot b, b) = (a, b)$。

**证明** 令$a$，$b$，$c$是整数。我们将证明$a$，$b$的公因子与$a + c \cdot b$，$b$的公因子相同，即证明$(a + c \cdot b, b) = (a, b)$。
令$e$是$a$，$b$的公因子。由定理2可知$e  \mid  (a + c \cdot b)$，所以$e$是$a + c \cdot b$和$b$的公因子。
如果$f$是$a + c \cdot b$和$b$的公因子，那么由定理2可知$f$整除$(a + c \cdot b) - c \cdot b = a$，所以$f$是$a$，$b$的公因子。
因此$(a + c \cdot b, b) = (a, b)$。$\blacksquare$

**定理2** 如果$a$，$b$，$m$和$n$为整数，且$c \mid a$，$c \mid b$，则$c \mid (m \cdot a + n \cdot b)$。

**证明** 因为$c \mid a$且$c \mid b$，故存在整数$e$和$f$，使得$a = c \cdot e$，$b = c \cdot f$。
因此$m \cdot a + n \cdot b = m \cdot c \cdot e + n \cdot c \cdot f = c (m \cdot e + n \cdot f)$。从而，$c \mid (m \cdot a + n \cdot b)$。$\blacksquare$

我们举下面的例子来说明欧几里得算法的具体步骤。

**例子** 用欧几里得算法求$(252, 198)$的步骤如下：
$$
\begin{aligned}
252 & = 198 \times 1 + 54 \\
198 & = 54 \times 3 +36 \\
 54 & = 36 \times 1 + 18 \\
 36 & = 18 \times 2
\end{aligned}
$$
我们将这些步骤总结在下表中：

| $j$  | $r_j$ | $r_{j+1}$ | $q_{j+1}$ | $r_{j+2}$ |
| ---- | ----- | --------- | --------- | --------- |
| 0    | 252   | 198       | 1         | 54        |
| 1    | 198   | 54        | 3         | 36        |
| 2    | 54    | 36        | 1         | 18        |
| 3    | 36    | 18        | 2         | 0         |

最后一个非零除数（在最后一列倒数第二行的那个数）就是252和198的最大公因子。因此$(252, 198) = 18$

- - -

### 欧几里得算法（Euclidean algorithm）的实现

接下来，我们给出欧几里得算法的python语言实现：

- 递归版本

```python
def Euclid(a:int, b:int):
    assert a >= b >= 0
    if b == 0:
        return a
    return Euclid(b, a%b)

def gcd(a:int, b:int):
    assert a >= 0 and b >= 0
    if a < b:
        a, b = b, a # swap(a,b)
    return Euclid(a, b)

def print_gcd(a, b):
    print("gcd({}, {}) = {}".format(a, b, gcd(a, b)))

if __name__ == "__main__":
    print_gcd(252, 198)
    print_gcd(414, 662)
```

- 迭代版本

```python
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
    print_gcd(414, 662)
```

另外，python标准库的math模块内置了gcd的实现，可以作为基准版本：

```python
import math

def print_gcd(a, b):
    print("gcd({}, {}) = {}".format(a, b, math.gcd(a, b)))

if __name__ == "__main__":
    print_gcd(252, 198)
    print_gcd(414, 662)
```
