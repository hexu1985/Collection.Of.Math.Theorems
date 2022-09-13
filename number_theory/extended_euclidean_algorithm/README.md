## 扩展欧几里得算法（extended Euclidean algorithm）的证明与实现

**贝祖定理** 如果$a$和$b$为正整数，且$\gcd(a,b) = d$，那么对于任意的整数$x$和$y$，
$x \cdot a + y \cdot b$都一定是d的倍数，特别地，一定存在整数$s$和$t$，
使$s \cdot a + t \cdot b = d$成立。

**定义** 如果$a$和$b$为正整数，则使得$\gcd(a,b) = s \cdot a + t \cdot b$的整数$s$和$t$，
称为$a$和$b$的贝祖系数。等式$\gcd(a,b) = s \cdot a + t \cdot b$称为贝祖恒等式。

