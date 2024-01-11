## 柯西--施瓦茨不等式

柯西--施瓦茨不等式有很多表示方式，我们只介绍实数域表示和向量表示，并给出基于向量的证明。

**实数域表示**

设$a_i, b_i \in \boldsymbol{R} (i=1,2,\cdots,n)$，则

$$
(\sum\limits_{i=1}^{n}a_{i}b_{i})^{2} \leq (\sum\limits_{i=1}^{n}a_{i}^2) (\sum\limits_{i=1}^{n}b_{i}^2)    \tag{1}
$$

也有将不等式两边取平方根的表示方式：

$$
\left| \sum\limits_{i=1}^{n}a_{i}b_{i} \right| \leq (\sum\limits_{i=1}^{n}a_{i}^2)^{\frac{1}{2}} (\sum\limits_{i=1}^{n}b_{i}^2)^{\frac{1}{2}}       \tag{2}
$$

或者

$$
\left| \sum\limits_{i=1}^{n}a_{i}b_{i} \right| \leq \sqrt{(\sum\limits_{i=1}^{n}a_{i}^2) (\sum\limits_{i=1}^{n}b_{i}^2)}       \tag{3}
$$

式(1)、(2)、(3)是完全等价的。

**向量表示**

在n维欧氏空间中，对任意向量$\mathbf{a} = (a_1, a_2, \cdots, a_n)$和$\mathbf{b} = (b_1, b_2, \cdots, b_n)$，有

$$
(\mathbf{a} \cdot \mathbf{b})^{2} \leq |\mathbf{a}|^{2} |\mathbf{b}|^{2}    \tag{4}
$$

下面我们只给出三维向量空间下的证明：

**证明**

根据向量内积的几何表示定义

$$
\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta)     \tag{5}
$$

其中，$\theta$为两向量的夹角，将(5)式两边平方可得

$$
(\mathbf{a} \cdot \mathbf{b})^{2} = |\mathbf{a}|^{2} |\mathbf{b}|^{2} \cos^{2}(\theta)     \tag{6}
$$

又由$|\cos(\theta)| \leq 1$，所以

$$
(\mathbf{a} \cdot \mathbf{b})^{2} = |\mathbf{a}|^{2} |\mathbf{b}|^{2} \cos^{2}(\theta)  \leq |\mathbf{a}|^{2} |\mathbf{b}|^{2}  \tag{7}
$$

到此，柯西--施瓦茨不等式的向量表示得证。

接下来，我们把向量的代数表示代入(4)式，看看能得到什么结果：

根据向量内积的代数表示，

$$
\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 = \sum\limits_{i=1}^{3}a_{i}b_{i}    \tag{8}
$$

以及，向量的长度公式：

$$
|\mathbf{a}|^{2} = \mathbf{a} \cdot \mathbf{a} = a_1 a_1 + a_2 a_2 + a_3 a_3 = \sum\limits_{i=1}^{3}a_{i}^{2}    \tag{9}
$$

$$
|\mathbf{b}|^{2} = \mathbf{b} \cdot \mathbf{b} = b_1 b_1 + b_2 b_2 + b_3 b_3 = \sum\limits_{i=1}^{3}b_{i}^{2}    \tag{10}
$$

将(8)、(9)、(10)式代入(4)式，可得到

$$
(\sum\limits_{i=1}^{3}a_{i}b_{i})^{2} \leq (\sum\limits_{i=1}^{3}a_{i}^2) (\sum\limits_{i=1}^{3}b_{i}^2)    \tag{11}
$$

这就是(1)式中$n=3$的情况。


#### 参考资料:

- 《实用线性代数 图解版》2.9 不等式
- [知乎：柯西-施瓦茨不等式证明](https://zhuanlan.zhihu.com/p/609498291)

