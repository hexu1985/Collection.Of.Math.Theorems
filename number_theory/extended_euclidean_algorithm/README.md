## 扩展欧几里得算法（extended Euclidean algorithm）的证明与实现

首先，我们还是回顾一下欧几里得算法相关的一些基本概念的定义：

**定义（整除）** 如果$a$和$b$为整数且$a \neq 0$，我们说$a$**整除**$b$是指存在整数$c$使得$b = a \cdot c$。如果$a$整除$b$，我们还称$a$**是**$b$**的一个因子**，且称$b$**是**$a$**的倍数**。

如果$a$整除$b$，则将其记为$a \mid b$，如果$a$不能整除$b$，则记其为$a \nmid b$。


**定义（最大公因子）** 不全为零的整数$a$和$b$的最大公因子是指能够同时整除$a$和$b$的最大整数。

$a$和$b$的最大公因子记作$(a, b)$。有时也记作$gcd(a, b)$。

注意当$n$为正整数时，$(0, n) = (n, 0) = n$。

虽然所有的正整数都能够整除$0$，我们还是定义$(0, 0) = 0$。这样可以确保关于最大公因子的相关结论在所有情况下均成立。


**定理（欧几里得算法）** 令整数$r_{0} = a$，$r_{1} = b$满足$a \ge b > 0$，
如果连续做带余除法得到$r_{j} = r_{j+1} \cdot q_{j+1} + r_{j+2}$，
且$0 < r_{j+2}  < r_{j+1}$（$j = 0, 1, 2, \cdots, n-2$），$r_{n+1} = 0$，
那么$(a, b) = r_{n}$，它是最后一个非零余数。

具体的，令$r_{0} = a$，$r_{1} = b$是正整数且满足$a \ge b$，那么通过连续运用带余除法，我们求得

$$
\begin{aligned}
  r_{0} & = r_{1} \cdot q_{1} + r_{2}           & 0 \le r_{2} < r_{1} \\
  r_{1} & = r_{2} \cdot q_{2} + r_{3}           & 0 \le r_{3} < r_{2} \\
        & \vdots                                & \\
  r_{j} & = r_{j+1} \cdot q_{j+1} + r_{j+2}     & 0 \le r_{j+2} < r_{j+1} \\
        & \vdots                                & \\
r_{n-3} & = r_{n-2} \cdot q_{n-2} + r_{n-1}     & 0 \le r_{n-1} < r_{n-2} \\
r_{n-2} & = r_{n-1} \cdot q_{n-1} + r_{n}       & 0 \le r_{n} < r_{n-1} \\
r_{n-1} & = r_{n} \cdot q_{n}
\end{aligned}
$$

最终$(a, b) = r_{n}$，

- - -

然后我们介绍一下，用线性组合的方法来表示最大公因数的理论支持：

**贝祖定理（裴蜀定理）** 如果$a$和$b$为正整数，且$(a, b) = d$，那么对于任意的整数$x$和$y$，
$x \cdot a + y \cdot b$都一定是d的倍数，特别地，一定存在整数$s$和$t$，
使$s \cdot a + t \cdot b = d$成立。

**定义** 如果$a$和$b$为正整数，则使得$(a, b) = s \cdot a + t \cdot b$的整数$s$和$t$，
称为$a$和$b$的贝祖系数。等式$(a, b) = s \cdot a + t \cdot b$称为贝祖恒等式。

根据贝祖定理，我们知道任意两个正整数的最大公约数可以表示为这两个整数的整系数的线性组合。
接下来我们会给出两种方法，用于找出两个正整数的线性组合以使之等于其最大公约数。

- - -

第一种方法要对欧几里得算法的除法步骤做反向处理，所以需要将欧几里得算法的步骤正反向各走一遍。
我们用一个例子来解释这种工作方法的工作原理，并给出python语言的实现。

**例子1** 通过欧几里得算法的反向处理，试把$(252, 198) = 18$表示为$252$和$198$的线性组合。

首先我们先回顾一下用欧几里得算法求$(252, 198)$的步骤：
$$
\begin{aligned}
252 & = 198 \times 1 + 54 \\
198 & = 54 \times 3 +36 \\
 54 & = 36 \times 1 + 18 \\
 36 & = 18 \times 2
\end{aligned}
$$
我们将这些步骤总结在下表中：

| $j$  | $r_{j}$ | $r_{j+1}$ | $q_{j+1}$ | $r_{j+2}$ |
| ---- | ------- | --------- | --------- | --------- |
| 0    | 252     | 198       | 1         | 54        |
| 1    | 198     | 54        | 3         | 36        |
| 2    | 54      | 36        | 1         | 18        |
| 3    | 36      | 18        | 2         | 0         |

最后一个非零除数（在最后一列倒数第二行的那个数）就是252和198的最大公因子。因此$(252, 198) = 18$

观察用欧几里得算法求$(252, 198)$的倒数第二步，
$$
18 = 54 - 36 \times 1 
$$
它的前面一步是
$$
36 = 198 - 54 \times 3
$$
这意味着
$$
18 = 54 - (198 - 54 \times 3) \times 1 = 54 \times 4 - 198 \times 1
$$
同样，由第一步，我们得
$$
54 = 252 - 198 \times 1 
$$
因此
$$
18 = (252 - 198 \times 1) \times 4 - 198 \times 1 = 252 \times 4 - 198 \times 5 = 4 \times 252 - 5 \times 198
$$
最后一个等式将$18 = (252, 198)$写成了$252$, $198$的线性组合的形式。$\blacktriangleleft$

一般地，为了知晓如何使用$a$, $b$的线性组合来表示它们的最大公因数$d = (a, b)$，需要涉及欧几里得算法中产生的一系列等式。
由倒数第二个等式有
$$
r_{n} = (a, b) = r_{n-2} - r_{n-1} \cdot q_{n-1}
$$
这就是用$r_{n-2}$和$r_{n-1}$线性组合表示了$(a, b)$。倒数第三步可以将$r_{n-1}$用$r_{n-3}$和$r_{n-2}$来表示，即
$$
r_{n-1} = r_{n-3} - r_{n-2} \cdot q_{n-2}
$$
用这个等式消去上面的表达式中的$r_{n-1}$，则有
$$
\begin{aligned}
(a, b) & = r_{n-2} - (r_{n-3} - r_{n-2} \cdot q_{n-2}) \cdot q_{n-1} \\
       & = r_{n-3} \cdot (-q_{n-1}) + r_{n-2} \cdot (1 + q_{n-2} \cdot q_{n-1})
\end{aligned}
$$
这就将$(a, b)$表示成了$r_{n-3}$和$r_{n-2}$的线性组合。我们继续沿着欧几里得算法相反的步骤将$(a, b)$
表示成接下来的余数的线性组合，直到将$(a, b)$表示成$r_{0} = a$, $r_{1} = b$的线性组合。对于特定的$j$，
如果已经求得
$$
(a, b) = s \cdot r_{j+1} + t \cdot r_{j+2}
$$
那么，因为
$$
    r_{j+2} = r_{j} - r_{j+1} \cdot q_{j+1}
$$
我们有
$$
\begin{aligned}
(a, b) & = s \cdot r_{j+1} + t \cdot (r_{j} - r_{j+1} \cdot q_{j+1}) \\
       & = t \cdot r_{j} + (s - t \cdot q_{j+1}) \cdot r_{j+1}
\end{aligned}
$$
这显示了如何沿着欧几里得算法产生的等式递进，最终使得$a$和$b$的最大公因数$(a, b)$可以表示成它们的线性组合，即
如果已经求得
$$
(a, b) = s' \cdot r_{1} + t' \cdot r_{2}
$$
那么，因为
$$
    r_{2} = r_{0} - r_{1} \cdot q_{1}
$$
我们有
$$
\begin{aligned}
(a, b) & = s' \cdot r_{1} + t' \cdot (r_{0} - r_{1} \cdot q_{1}) \\
       & = t' \cdot r_{0} + (s' - t' \cdot q_{1}) \cdot r_{1}
\end{aligned}
$$
其中$a = r_{0}$，$b = r_{1}$，$q_{1} = \lfloor a / b \rfloor $ 算法就此结束。

下面给出该算法的python语言实现：

```python
def extended_Euclid(a:int, b:int):
    ''' 
    return s, t, d
    s * a + t * b = d
    '''
    assert a >= b >= 0
    if b == 0:
        # s * a + t * b = d
        # d = a and s = 1 and t = 0
        return (1, 0, a)
    s, t, d = extended_Euclid(b, a%b)
    # a = r_{j}, b = r_{j+1}, a%b = r_{j+2}, a//b = q_{j+1}
    # d = t * r_{j} + (s - t * q_{j+1}) * r_{j+1}
    # return t, (s - t * (a//b)), d
    return (t, (s-t*(a//b)), d)

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
```

这里简单注解一下extended_Euclid的实现：

- 结束条件，`b为0`时，`return (1, 0, a)`，

    因为这时$b = 0$，$d = (a, b) = a$，于是乎$d = 1 \cdot a + 0 \cdot b$

- 递归调用， `b不为0`时，`return (t, (s-t*(a//b)), d)`

    假设当前帧`a` = $r_{j}$，`b` = $r_{j+1}$，那么由`s, t, d = extended_Euclid(b, a%b)`这条语句可知，
    `a%b` = $r_{j+2}$，`a//b` = $q_{j+1}$，套用之前的公式
    $$
    \begin{aligned}
    d = (a, b) & = s \cdot r_{j+1} + t \cdot r_{j+2} \\
               & = s \cdot r_{j+1} + t \cdot (r_{j} - r_{j+1} \cdot q_{j+1}) \\
               & = t \cdot r_{j} + (s - t \cdot q_{j+1}) \cdot r_{j+1}
    \end{aligned}
    $$
    并且把`a` = $r_{j}$，`b` = $r_{j+1}$，`a//b` = $q_{j+1}$代回上式，就得到return语句中的三元组了。


- - -

另外一种计算方法，叫做扩展的欧几里得算法，和第一种的区别主要在于不需要反向计算步骤，在计算最大公因数的同时，
就将线性组合的系数计算出来了。具体定理如下：

**定理（扩展欧几里得算法）** 令$a$, $b$是正整数，那么
$$
(a, b) = s_{n} \cdot a + t_{n} \cdot b
$$
其中$s_{n}$, $t_{n}$是下面定义的递归序列的第$n$项：
$$
\begin{aligned}
s_{0} = 1, & & t_{0} = 0, \\
s_{1} = 0, & & t_{1} = 1,
\end{aligned}
$$
且
$$
s_{j} = s_{j-2} - q_{j-1} \cdot s_{j-1}, \quad t_{j} = t_{j-2} - q_{j-1} \cdot t_{j-1}
$$
其中$j = 2, 3, \cdots, n$，而$q_{j}$是欧几里得算法求$(a, b)$时每一步的商。

**证明** 我们将证明
$$
r_{j} = s_{j} \cdot a + t_{j} \cdot b   \quad   (1)
$$
因为$(a, b) = r_{n}$，一旦等式(1)成立，我们就有
$$
(a, b) = s_{n} \cdot a + t_{n} \cdot b
$$
我们用数学归纳法来证明(1)。对于$j=0$，有$a = r_{0} = 1 \cdot a + 0 \cdot b = s_{0} \cdot a + t_{0} \cdot b$。
因此对于$j = 0$成立。类似地，$b = r_{1} = 0 \cdot a + 1 \cdot b = s_{1} \cdot a + t_{1} \cdot b$，所以(1)对于$j=1$成立。

现在假设
$$
r_{j} = s_{j} \cdot a + t_{j} \cdot b   \quad   (1)
$$
对于$j = 1, 2, \cdots, k-1$成立。那么，由欧几里得算法的第$k$步，我们有
$$
r_{k} = r_{k-2} - r_{k-1} \cdot q_{k-1}
$$
由归纳假设，得到
$$
\begin{aligned}
r_{k} & = (s_{k-2} \cdot a + t_{k-2} \cdot b) - (s_{k-1} \cdot a + t_{k-1} \cdot b) \cdot q_{k-1} \\
      & = (s_{k-2} - s_{k-1} \cdot q_{k-1}) \cdot a + (t_{k-2} - t_{k-1} \cdot q_{k-1}) \cdot b   \\
      & = s_{k} \cdot a + t_{k} \cdot b
\end{aligned}
$$
这就完成了证明。$\blacksquare$

下面我们还是用一个例子说明扩展的欧几里得算法如何将$(a, b)$表示成$a$, $b$的线性组合。
**例子2** 我们在下面的表中总结了用扩展欧几里得算法将$(252, 198) = 18$表示为$252$和$198$的线性组合的步骤。

| $j$  | $r_{j}$ | $r_{j+1}$ | $q_{j+1}$ | $r_{j+2}$ | $s_{j}$ | $t_{j}$ |
| ---- | ------- | --------- | --------- | --------- | ------- | ------- |
| 0    | 252     | 198       | 1         | 54        |  1      |  0      |
| 1    | 198     | 54        | 3         | 36        |  0      |  1      |
| 2    | 54      | 36        | 1         | 18        |  1      | -1      |
| 3    | 36      | 18        | 2         | 0         | -3      |  4      |
| 4    | 18      | -         | -         | -         |  4      | -5      |

$s_{j}$和$t_{j}$ $(j = 0, 1, 2, 3, 4)$的值计算如下：
$$
\begin{aligned}
s_{0} & = 1, & t_{0} & = 0, \\
s_{1} & = 0, & t_{1} & = 1, \\
s_{2} & = s_{0} - q_{1} \cdot s_{1} = 1 - 1 \times 0 = 1,    & t_{2} & = t_{0} - q_{1} \cdot t_{1} = 0 - 1 \times 1 = -1, \\
s_{3} & = s_{1} - q_{2} \cdot s_{2} = 0 - 3 \times 1 = -3,   & t_{3} & = t_{1} - q_{2} \cdot t_{2} = 1 - 3 \times (-1) = 4, \\
s_{4} & = s_{2} - q_{3} \cdot s_{3} = 1 - 1 \times (-3) = 4, & t_{4} & = t_{2} - q_{3} \cdot t_{3} = -1 - 1 \times (4) = -5, \\
\end{aligned}
$$
因为$r_{4} = 18 = (252, 198)$且$r_{4} = s_{4} \cdot a + t_{4} \cdot b$，故
$$
18 = (252, 198) = 4 \times 252 - 5 \times 198
$$
最后一个等式将$18 = (252, 198)$写成了$252$, $198$的线性组合的形式。$\blacktriangleleft$

最后我们给出扩展欧几里得算法的python语言实现：

```python
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
```

- - -

参考文献：
- 初等数论及其应用（原书第6版）: ISBN 978-7-111-48697-8
- 离散数学及其应用（原书第8版）: ISBN 978-7-111-63687-8
- 算法概论: ISBN 978-7-302-17939-9
