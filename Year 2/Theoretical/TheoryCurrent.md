## Lecture 4

### Operators I

Examples:
1. energy operator $\to H$
2. angular momentum operator $\to \vec{L} = L_x\hat{x} + L_y\hat{y} + L_z\hat{z}$
3. linear momentum operator $\to \vec{p} = -i\hbar\vec{\nabla},~ p_x = -i\hbar\frac{\partial}{\partial x} = -i\hbar\frac{d}{dx}$
4. position operator $\to x$ (in 1D)

* operators deal with _dynamical variables_
* they transform wavefunctions:

$$
    p_x e^{-\frac{x^2}{a^2}} = -i\hbar\frac{d}{dx}e^{-\frac{x^2}{a^2}} = 2i\hbar\frac{x}{a^2}e^{-\frac{x^2}{a^2}}
$$

* linear operators are ones that act linearly: $A(c_1v_1 + c_2v_2) = c_1Av_1 + c_2Av_2$

* non-linear operators do exist:

$$
    \begin{aligned}
    Av &= v||v|| \\
    Acv &= cv||cv|| = c|c|v||v|| \\
    &= c|c|Av \neq cAv
    \end{aligned}
$$

* many operators are _unbounded_
* identity operator, $I$ such that $Iv = v$

#### Using Linear Operators

1. adding operators:

$$
    (A + B)v = Av + Bv
$$

2. multiplying an operator by a scalar:

$$
    (cA)v = A(cv)
$$

3. product of two operators, i.e. act on v with B first then act on the result with A:

$$
    (AB)v = A(Bv), ~ [AB \neq BA]
$$

4. invertible operator, an operator which has an inverse: $A^{-1}$  
$A^{-1}$ being such that
$$AA^{-1} = A^{-1}A = I$$  
singular operators are defined as non-inertible operators
$$
    \begin{aligned}
    (AB)^{-1} &= B^{-1}A^{-1} \\
    (A^{-1})^{-1} &= A
    \end{aligned}
$$

5. any operator $A$ has a unique adjoint, $A^\dagger$  
$A^\dagger$ is the operator such that for any $v,w$
$$
    \begin{aligned}
    (v,Aw) &= (w,A^\dagger v)^* \\
    (AB)^\dagger &= B^\dagger A^\dagger \\
    (A^\dagger)^\dagger &= A \\
    (A + B)^\dagger &= A^\dagger + B^\dagger \\
    (cA)^\dagger &= c^* A^\dagger
    \end{aligned}
$$

### Representation by a matrix

orthonormal basis: $\{u_1,u_2,\cdots,u_n\}$
$$
    \begin{aligned}
    (u_i,u_j) &= \delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases} \\
    v&= c_1u_1 + c_2u_2 + \cdots + c_nu_n \\
    w &= Av \\
    w &= d_1u_1 + \cdots + d_nu_n \\
    \vec{c} &= \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} ~;~ \vec{d} = \begin{pmatrix} d_1 \\ d_2 \\ \vdots \\ d_n \end{pmatrix} \\
    \vec{d} &= \hat{A}\vec{c} \\
    \hat{A} &= \begin{pmatrix} A_{11} & A_{12} & \cdots & A_{1n} \\ \vdots & & & \\ A_{n1} & A_{n2} & \cdots & A_{nn} \end{pmatrix} \\
    A_{ij} &= (u_i, Au_j)
    \end{aligned}
$$
this matrix represents the operator $A$ in the basis $\{u_1,u_2,\cdots,u_n\}$

Example:  
$$\left\{\frac{1}{\sqrt{2}}, \sqrt{\frac{3}{2}}x\right\}$$
is an orthonormal basis in the space of all functions of the form $f(x) = a_0 + a_1x$

$$
    \begin{aligned}
    (u_i,u_j) &= \delta_{ij} \\
    \int_{-1}^1 u_{i}^{*}(x)u_j(x)\,dx = \delta_{ij}*
    \end{aligned}
$$
