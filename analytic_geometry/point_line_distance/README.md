## 平面上点到直线的距离公式证明

**点到直线的距离公式** 设直线的方程是
$$
l: Ax+By+C = 0
$$
那么点$P_0(x_0,y_0)$到直线$l$的距离是
$$
d = \cfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}
$$

**证明** 我们这里利用向量工具来证明：

我们假设直线$l: Ax+By+C=0$的法向量为$\mathbf{n}$（方向朝上或朝下无所谓），点M, N为直线$l$上的任意两点（不重合），点Q为点P到直线$l$的垂线段的垂足，如图：

![点到直线的距离](draw.io/point_line_distance.png)

设$M(x_1,y_1)$和$N(x_2,y_2)$，我们可以求得向量$\overrightarrow{MN} = (x_2-x_1, y_2-y_1)$，又由于点M和N在直线$l$上，所以有方程组
$$
\begin{cases}
Ax_1+By_1+C=0 \\
Ax_2+By_2+C=0
\end{cases}
$$
成立，我们将两个方程相减，得$A(x_2-x_1)+B(y_2-y_1)=0$，即
$$
(A,B) \cdot (x_2-x_1,y_2-y_1) = 0
$$
这里的$\cdot$代表向量内积。所以向量$(A,B)$与向量$\overrightarrow{MN}$垂直（即与直线$l$垂直），
所以法向量为$\mathbf{n}$与$(A,B)$平行，$\mathbf{n} \mathop{//} (A,B)$。
由于PQ垂直于直线$l$，所以向量$\overrightarrow{PQ}$平行于$\mathbf{n}$（同向或反向无所谓），所以$\overrightarrow{PQ} = t(A,B)$，这里$t$为实数，我们设Q的坐标为$(x,y)$，所以$(x-x_0, y-y_0) = t(A,B)$，即
$$
\begin{cases}
x - x_0 = tA \\
y - y_0 = tB
\end{cases}
\Rightarrow
\begin{cases}
x = x_0+tA \\
y = y_0+tB
\end{cases}
$$
又由点Q在直线$l$上（点Q为点P到直线$l$的垂线段的垂足），所以有
$$
Ax+By+C=0
$$
把方程组代入直线方程有：
$$
A(x_0+At)+B(y_0+Bt)+C=0
$$
解出t：
$$
t = -\cfrac{Ax_0+By_0+C}{A^2+B^2}
$$
在根据两点间距离公式，有
$$
\begin{align}
\left| \overrightarrow{PQ} \right| & = \sqrt{(x-x_0)^2+(y-y_0)^2} \\
                      & = \sqrt{(At)^2+(Bt)^2} \\
                      & = |t|\sqrt{A^2+B^2} \\
                      & = \cfrac{|Ax_0+By_0+C|}{A^2+B^2} \sqrt{A^2+B^2} \\
                      & = \cfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}
\end{align}
$$
最后的式子就是需要证明的点到直线的距离公式。
