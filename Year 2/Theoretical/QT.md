---
title: "Theoretical Physics"
author: "Dr Robert Potvliege"
date: "Epiphany 2018"
---

# Quantum Theory

## Lecture 1

*Course notes and audiorecordings of the lectures can be found on DUO*

## Lecture 2

### Vector Spaces

#### Examples in Vector Spaces

##### A. Geometric vectors

Summing vectors (*only valid for addition of vectors*):

1. If $\vec{v}_1$ and $\vec{v}_2$ are vectors, then $\vec{v}_1 + \vec{v}_2$ is also a vector
    * The plane bounded by $\vec{v}_1$ and $\vec{v}_2$ is a closed vector space under vector addition.
2. $$(\vec{v}_1 + \vec{v}_2) + \vec{v}_3 = \vec{v}_1 + (\vec{v}_2 + \vec{v}_3)$$
3. There is a zero vector $\vec{0}$ (vector of zero length) such that $\vec{v} + \vec{0} = \vec{v}$.
4. Each vector has an inverse $-\vec{v}$ such that $\vec{v} + (-\vec{v}) = \vec{0}$.
5. $$\vec{v}_1 + \vec{v}_2 = \vec{v}_2 + \vec{v}_1$$
6. $\alpha\vec{v}$ is the vector whose length is $\alpha$ times $|\vec{v}|$ in the same direction as $\vec{v}$ for any real $\alpha$. This is scalar multiplication.
7. $$\begin{aligned}(\alpha_1 + \alpha_2)\vec{v} = \alpha_1 \vec{v} + \alpha_2\vec{v} \\ \alpha(\vec{v}_1 + \vec{v}_2) = \alpha\vec{v}_1 + \alpha\vec{v}_2\end{aligned}$$
8. $$(\alpha\beta)\vec{v} = \alpha(\beta\vec{v})$$
9. $$1\cdot\vec{v} = \vec{v}$$
10. Dot product:
$$\vec{v}_1 \cdot \vec{v}_2 = |\vec{v}_1||\vec{v}_2|\cos\theta_{12}$$
11. $$\vec{v}_1\cdot\vec{v}_2 = (\vec{v}_2\cdot\vec{v}_1)^* $$
12. Linear combinations:
$$(\alpha\vec{v}_1 + \beta\vec{v}_2)\cdot\vec{w} = \alpha^{*}(\vec{v}_1\cdot\vec{w}) + \beta^{*}(\vec{v}_2\cdot\vec{w})$$
13. $$\vec{v}\cdot\vec{v} = |\vec{v}|^2 \geq 0$$

These are the axioms of the inner product.

A vector space with inner product $\equiv$ an inner product space

##### B. 2-component complex column vectors

$$
    V = \begin{pmatrix} a \\ b \end{pmatrix}
$$

where $a$ and $b$ are complex numbers

1. Addition of two vectors:
$$
    \begin{aligned}
    V = \begin{pmatrix} a \\ b \end{pmatrix} ~&;~ W = \begin{pmatrix} a' \\ b' \end{pmatrix} \\
    V + W &= \begin{pmatrix} a + a' \\ b + b' \end{pmatrix}
    \end{aligned}
$$
2. $$(v_1 + v_2) + v_3 = v_1 + (v_2 + v_3)$$
3. $$\begin{pmatrix} a \\ b\end{pmatrix} + \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ b \end{pmatrix}$$
4. $$\begin{pmatrix} a \\ b\end{pmatrix} + \begin{pmatrix} -a \\ -b \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$  
5. $$\alpha\begin{pmatrix} a \\ b\end{pmatrix} = \begin{pmatrix} \alpha a \\ \alpha b \end{pmatrix}$$
6. Inner product of $v$,$w$ is:
$$
    (v,w) = \begin{pmatrix} a^* & b^* \end{pmatrix}\begin{pmatrix} a' \\ b' \end{pmatrix} = a^* a' + b^* b'
$$

##### C. Functions of x

$$
    f(x), \psi(x)
$$

These functions form a vector space.

1. $$(f + g)(x) = f(x) + g(x)$$
2. $$(\alpha f)(x) = \alpha f(x)$$
3. Inner product:
$$
    (f, g) = \int_{-\infty}^{\infty} f^* (x)g(x)\,dx
$$

#### Norm of a vector

The norm of a vector is defined as:

$$
    ||v|| = \sqrt{(v,v)}
$$

* Two vectors are said to be orthogonal if $(v,w) = 0$
    * orthonormal if there are orthogonal and have a unit norm $(||v|| = ||w|| = 1)$

## Lecture 3

### Hilbert Spaces

Wave function of a harmonic oscillator:

$$
    \int_{-\infty}^\infty |\psi(x)|^2dx = 1
$$

Wave function of atomic hydrogen:

$$
    \int_{-\infty}^\infty r^2dr \int_{0}^\pi \sin\theta\,d\theta \int_0^{2\pi} d\phi \; |\psi(r,\theta,\phi)|^2 = 1
$$

* Wave functions must be square-integrable  
* The set of all functions forms a vector space  
    * The set of all square-integrable functions also forms a vector space, a subset of the above space (a subspace)
    * A subspace is a vector space which is a subset of another vector space

* A squre-integrable function refers to using the Leberque integration

Hilbert space: a complete vector space with an inner product, e.g. the vector space of square-integrable functions on $(-\infty, \infty)$

The inner product is:

$$
    (\phi, \psi) = \int_{-\infty}^\infty \phi^* (x)\psi(x)dx
$$

### Bases

1. Span of a set of vectors: the set of all linear combinations of these vectors, e.g. the span of

$$
    \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}
$$

is the set of linear combinations,

$$
    a\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + b\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + c\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} a \\ b \\ c \end{pmatrix}
$$

The span of those three vectors is the set of all 3-component column vectors, were $a, b, c \in \mathbb{C}$

2. A set of N vectors is said to be linearly independent if it is not possible to write a vector from that set as a linear combination of the other vectors.

$$
    \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}
$$

is a linearly independent set since it is not possible to find $\alpha$ and $\beta$ such that

$$
    \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \alpha\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + \beta\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
$$

Orthogonal vectors are always linearly independent.  
The dimension of a finite-dimensional vector space is the max number of vectors forming a linearly-independent set.  
An infinite-dimensional vector space is one in which there is no upper bound on the size of the linearly-independent sets.

#### Example

Functions of the form $e^{inx}, n \in \mathbb{N}$  
These functions form a linearly-independent set since any two such functions are orthogonal.

$$
    \int_0^{2\pi} \left(e^{inx}\right)^* e^{imx} dx = 0, n \neq m
$$

3. A basis is a set of linearly-independent vectors spanning the whole vector space.  
An orthonormal basis is a basis whose vectors are orthonormal.

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
    \int_{-1}^1 u_{i}^{*}(x)u_j(x)&\,dx = \delta_{ij}*
    \end{aligned}
$$

## Lecture 5

* **Note:** _order of presenting the basis matters, flipping the order of a 2 base basis transverses the matrix_
* For a function, $f = a + bx = c_1u_1(x) + c_2u_2(x)$, calculate the constants using the inner product
* One says that the vector space spanned by $u_1(x)$ and $u_2(x)$ is isomorphic to the vector space of 2-component column vectors

### Dirac Notation

$$
    \begin{aligned}
    u_1(x) &= \begin{pmatrix} 1 \\ 0 \end{pmatrix} = |1\rangle \\
    u_2(x) &= \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |2\rangle \\
    f &= a + bx = \begin{pmatrix} a\sqrt{2} \\ b\sqrt{\frac{2}{3}} \end{pmatrix} = |f\rangle
    \end{aligned}
$$

* denote inner product of g and f as $(g,f) = \langle g | f \rangle$

$$
    \begin{aligned}
    \frac{d}{dx}f &= Df = \hat{D}|f\rangle \\
    \left(g,\frac{df}{dx}\right) &= \langle g | \hat{D} | f \rangle
    \end{aligned}
$$

* The inner product of $c|g\rangle$ and $|f\rangle$ is $c^* \langle g|f\rangle$
* Ket vectors are vectors in their own right, forming a Hilbert space

### Dual Space

* Each state of a quantum system can be described by a vector belonging to a Hilbert space

## Lecture 6

### Degenerate Eigenvalues of an Operator

$$
    \begin{aligned}
    \hat{A}|\psi\rangle &= \lambda|\psi\rangle \\
    c|\psi\rangle &= |c\psi\rangle \\
    \hat{A}|c\psi\rangle &= \hat{A}c|\psi\rangle \\
    &= c\hat{A}|\psi\rangle \\
    &= c\lambda|\psi\rangle \\
    &= \lambda c|\psi\rangle = \lambda|c\psi\rangle
    \end{aligned}
$$

* $\lambda$ always corresponds to infinitely many different eigenvectors
* It happens that:

$$
    \begin{aligned}
    \hat{A}|\psi_1\rangle &= \lambda_1|\psi_1\rangle \\
    \hat{A}|\psi_2\rangle &= \lambda_1|\psi_2\rangle \\
    |\psi_2\rangle &\neq |\psi_1\rangle
    \end{aligned}
$$

* i.e., $|\psi_1\rangle$ and $|\psi_2\rangle$ are linearly independent, but correspond to the same eigenvalues
    * If so, $\lambda$ is said to be degenerate
    * e.g. for hydrogen, the $2s$, $2p_{m=0}$, and $2p_{m=\pm1}$ states all have the same energy, $E_2$
* These states are orthogonal, and hence, linearly independent:

$$
    \begin{aligned}
    \int \psi_{nlm}^* (r,\phi,\theta)\,\psi_{n'l'm'}(r,\phi,\theta)\,d'r = 0
    \end{aligned}
$$

_unless $n = n'$, $l = l'$, and $m = m'$_  

* The $E_2$ eigenvalues of hydrogen are degenerate
* The span of all the eigenvectors belonging to a degenerate eigenvalue is a vector space.
* The degree of degeneracy of that eigenvalue is the dimension of that space.
    * e.g. the degree of degeneracy of $E_2$ is 4 - "$E_2$ is 4-fold degenerate"
* If an operator $\hat{A}$ is represented by a matrix, $\underline{\underline{A}}$, then the eigenvalues of $\hat{A}$ are the same as those of $\underline{\underline{A}}$
    * The eigenvectors of $\hat{A}$ are $\iff$ in correspondence with those of the matrix
* Spectrum of an operator: The set of all its eigenvalues (physicist's definition)
    * $\hat{A} - \lambda\hat{I}$
    * $\hat{A}|\psi\rangle = \lambda|\psi\rangle$
* Momentum operator: $p = -i\hbar\frac{d}{dx}$

$$
    \begin{aligned}
    p\psi(x) &= \lambda\psi(x) \\
    -i\hbar\frac{d\psi}{dx} &= \lambda\psi(x) \\
    \psi(x) &= Ce^{i\frac{\lambda}{\hbar}x} \\
    \lambda = a + ib \implies e^{i\frac{\lambda}{\hbar}x} &= e^{\frac{1}{\hbar}(ai - b)x}
    \end{aligned}
$$

_for any constant C_

$$
    \begin{aligned}
    e^{-bx} \to \begin{cases} 0 & fn \to \infty \\ \infty & fn \to -\infty \end{cases}
    \end{aligned}
$$

_for positive b_

* $\psi(x)$ is not square integrable if $b \neq 0$
* If $b = 0$, then $e^{i\frac{a}{\hbar}x}$ remains of modulus 1, but

$$
    \int_{-\infty}^{\infty} |\psi(x)|^2dx = \int^{-\infty}_{\infty} |C|^2dx
$$

_this diverges_

* None of these eigenfunctions are square-integrable
* $p$ has no eigenfunctions in the Hilbert space of square-integrable functions
* In physics, functions like $e^{\pm ikx}$, where k is real, are also "eigenfunctions" (i.e., pseudo-eigenfunctions or generalised eigenfunctions)

### Dynamical Variables and Operators

* Each state of a quantum system can be represented by a vector belonging to a Hilbert space, $\mathcal{H}$
* With every dynamical variable is associated a linear operator acting in $\mathcal{H}$
    * e.g. position, momentum, angular momentum, spin, energy
    * i.e. physical quantities that may vary in time
* quantities that are constant in time are not dynamical variables
    * e.g. the charge of the electron, etc
    * therefore, they do not correspond to an operator in quantum mechanics
* The only values a dynamical variable can be found to have in a measurement are the eigenvalues of the operator associated with that variable

Suppose that $|\psi\rangle$ represents a state of a quantum system, and $\hat{A}$ represents a dynamical variable:

$$
    \hat{A}|\psi_n\rangle = \lambda_n|\psi_n\rangle
$$

then the probability to find the result $\lambda_n$ in an experiemt  is

$$
    P(\lambda_n) = \frac{|\langle\psi_n|\psi|\rangle|^2}{\langle\psi_n|\psi_n\rangle\langle\psi|\psi\rangle}
$$

Usually one takes

$$
    \begin{aligned}
    \langle{\psi|\psi\rangle} &= 1 \\
    \& \; \langle\psi_n|\psi_n\rangle &= 1 \\
    \implies P(\lambda_n) &= |\langle\psi_n|\psi\rangle|^2
    \end{aligned}
$$

## Lecture 7

1. Experiment
    * System is prepared in a certain state
    * measurement
    * results
2. Theory
    * state of system is represented by a state vector, $|\psi\rangle$
    * theoretical description in which what is measured is described in terms of operators associated to dynamical variables
    * probabilistic "prediction"

### Consequences of the Probability Rule

* All the predictions of the theory are based on the state vector, $|\psi\rangle$, representing the system
* All one can say about the state of a quantum system is what can be deduced from the state vector
* the state vector constains all the information that can be known about the system
* $|\phi_n\rangle$ is an eigenvector $\to \langle \phi_n|\phi_n\rangle \neq 0$
* the zero vector never represents a quantum state $\to \langle\psi|\psi\rangle \neq 0$
* if the probability of a result, $\lambda$, is zero, then finding this result is impossible (within the theoretical model used)
    * if the probability is one, then the result will be obtained with certainty

### The Principle of Superposition

* if $|\psi_1\rangle$ and $|\psi_2\rangle$ represents a possible state of a system, then any linear combination of $|\psi_1\rangle$ and $|\psi_2\rangle$ also represents a possible state of the system
$$
    \begin{aligned}
    \Psi_{100}(\vec{r},t) &= \psi_{100}(\vec{r}\exp\left[-i\left(\frac{E_1t}{\hbar}\right)\right] \\
    \Psi_{200}(\vec{r},t) &= \psi_{200}(\vec{r}\exp\left[-i\left(\frac{E_2t}{\hbar}\right)\right] \\
    \Psi(\vec{r},t) &= c_1\Psi_{100} + c_2\Psi_{200} \text{ is also a possible state}
    \end{aligned}
$$

If $\langle\phi_n|\phi_n\rangle = 1$, then
$$
    P(\lambda_n) = \frac{|\langle|\phi_n|\psi\rangle|^2}{\langle\psi|\psi\rangle}
$$

* multiplying the state vector by a non-zero complex number gives the same probability
* the ket vectors $c|\psi\rangle, c \in \mathbb{C}$ all represent the same state, regardless of the value of $c$
* however, a linear combination of state vectors will be different dependent on the value of $c$ for each state vector

### Hermitian Operators

Definition: an operator, $\hat{A}$, is Hermitian if
$$
    \langle\phi|\hat{A}|\psi\rangle = \langle\psi|\hat{A}|\phi\rangle^*
$$
for any $|\psi\rangle$, $|\phi\rangle$

* the eigenvalues of Hermitian operators are always real
* the eigenvectors of Hermitian operators corresponding to different eigenvalues are always orthogonal
* matrices representing Hermitian operators are always Hermitian, i.e. equal to their conjugate transpose

## Lecture 8

* An operator $\hat{A}$ is said to be Hermitian if $\langle\phi|\hat{A}|\psi\rangle = \langle\psi|\hat{A}|\phi\rangle^{*}$ for any $|\psi\rangle$, $|\phi\rangle$ on which $\hat{A}$ may act.

### Proof of the Orthogonality of Eigenvectors

* $\hat{A}$: Hermitian such that
    * $\hat{A}|\psi_1\rangle = \lambda_1|\psi_1\rangle$
    * $\hat{A}|\psi_2\rangle = \lambda_2|\psi_2\rangle$
    * $\lambda_1 \neq \lambda_2$
    * both $\lambda_1$ and $\lambda_2$ are real since $\hat{A}$ is Hermitian

$$
    \begin{aligned}
    \langle\psi_1|\hat{A}|\psi_2\rangle &= \lambda_2\langle\psi_1|\psi_2\rangle \\
    \langle\psi_2|\hat{A}|\psi_1\rangle * &= \lambda_2^* \langle\psi_2|\psi_1\rangle * \\
    \langle\psi_2|\hat{A}|\psi_1\rangle &= \lambda_2\langle\psi_2|\psi_1\rangle \\
    \langle\psi_2|\hat{A}|\psi_1\rangle &= \lambda_1\langle\psi_2|\psi_1\rangle \\
    0 &= \underbrace{(\lambda_1 - \lambda_2)}_{\neq 0}\underbrace{\langle\psi_2|\psi_1\rangle}_{=0}
    \end{aligned}
$$

* If $\hat{A}$ is a Hermitian operator acting in a finite-dimensional Hilbert space, then it is always possible to form an orthonormal basis of eigenvectors of $\hat{A}$ and this basis is complete.
* A complete set of vectors is a set of vectors spanning the whole space.
    * A basis is always a complete set, by definition.

#### Example (1st Workshop)

$$
    \begin{aligned}
    \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \\
    \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}
    \end{aligned}
$$

* The first matrix above is Hermitian, and the eigenvectors from a complete set.
* The second matrix above is not Hermitian, and the eigenvectors do not form a complete set.

For infinite-dimensional spaces, there are different possibilities:
1. Infinite square well:
$$
    H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
$$
This acts on $[-a,a]$ such that $\psi(x=\pm a) = 0$
    * There are infinitely many eigenvalues (eigenenergies) for this
2. Free particle: Same operator as above on $(-\infty, +\infty)$, acting on a square-integrable function in that bound
$$
    -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}\psi = E\psi
$$

* This has no solution that is square-integrable

3. SHM
$$
    \begin{aligned}
    H &= -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + \frac{1}{2}m\omega^2x^2,~ (-\infty,+\infty) \\
    H\psi_n &= E\psi_n \\
    E_n &= \hbar\omega\left(n + \frac{1}{2}\right) \\
    \psi(x) &= \sum_n c_n\psi_n(x)
    \end{aligned}
$$

### Probability of Obtaining an eigenvalue

$$
    \begin{aligned}
    P_i &= |\langle\phi_i|\psi\rangle|^2 \iff \\
    \langle\phi_i|\phi_1\rangle &= 1 = \langle\psi|\psi\rangle \& \\
    \hat{A}|\phi_i\rangle &= \lambda_i|\phi_i\rangle
    \end{aligned}
$$

If $\lambda_i$ is degenerate:

$$
    \begin{aligned}
    \hat{A}|\psi_n\rangle &= \underbrace{\lambda}_{\forall n}|\psi_n\rangle \\
    \langle\phi_i|\phi_j\rangle &= \delta_{ij}
    \end{aligned}
$$

Probability of finding $\lambda$ is:

$$
    P(\lambda) = \sum_n |\langle\phi_n|\psi\rangle|^2
$$

* This is the sum over all the eigenvectors corresponding to $\lambda$

* "Observable" - a Hermitian operator with a complete set of eigenvectors

$$
    \begin{aligned}
    P_i(|\psi\rangle) &= |\langle\phi_i|\psi\rangle|^2 \\
    P_i(|\phi_j\rangle) &= |\langle\phi_i|\phi_j\rangle|^2 = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}
    \end{aligned}
$$

* Finding $\lambda_i$ or $\lambda_j$ is mutually exclusive:

$$
    \begin{aligned}
    \sum_i P_i(|\psi\rangle) &= 1 \\
    \sum_i |\langle\phi_i|\psi\rangle|^2 &= 1 \\
    \sum_i \langle\phi_i|\psi\rangle * \langle\phi_i|\psi\rangle &= 1 \\
    \sum_i \langle\psi|\phi_i\rangle \langle\phi_i|\psi\rangle &= 1
    \end{aligned}
$$

* One must have this, or any $|\psi\rangle$

$$
    \sum_i |\phi_i\rangle\langle\phi_i| = \hat{I}
$$

* The is the completeness relation

### Variance of the distribution of probability

$$
    (\Delta A)^2 = \langle\psi|\hat{A}^2|\psi\rangle - \langle\psi|\hat{A}|\psi\rangle^2
$$

## Lecture 9

$$
    (\Delta A)^2(\Delta B)^2 \geq -\frac{1}{4}(\langle\psi|[\hat{A},\hat{B}]|\psi\rangle)^2
$$

* system is represented by $|\psi\rangle, \langle\psi|\psi\rangle = 1$

* two dynamical variables, $A$ and $B$, represented by two observables, $\hat{A}$ and $\hat{B}$
    * these are Hermitian operators with a complete set of eigenvalues

$$
    [\hat{A},\hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}
$$

* the commutator of $\hat{A}$ and $\hat{B}$

if

$$
    [\hat{A},\hat{B}] = 0
$$

one would say that $\hat{A}$ and $\hat{B}$ commute, i.e. for any $|\psi\rangle \to [\hat{A},\hat{B}]|\psi\rangle = 0$

$$
    [\hat{Q},\hat{P}] = i\hbar\hat{I}
$$

* $\hat{I}$ is the identity vector and is usually not indicated for simplicity
    * $[\hat{A},\hat{I}] = 0$
* $[\hat{A},\hat{A}] = 0$
* $[\hat{A},\hat{B}] = -[\hat{B},\hat{A}]$
* $[\hat{A},f(\hat{A})] = 0$, where $f(\hat{A})$ can be any function of $\hat{A}$

* if $[\hat{A},\hat{B}] = 0$ and $|\phi_n\rangle$ is an eigenvector of $\hat{A}$, then $\hat{B}|\phi_n\rangle$ is also an eigenvector of $\hat{A}$ corresponding to the same eigenvalue.
* Proof:

$$
    \begin{aligned}
    \hat{A}|\phi_n\rangle &= \lambda_n|\phi_n\rangle \\
    \hat{A}\hat{B}|\phi_n\rangle &= \hat{B}\hat{A}|\phi_n\rangle = \lambda_n\hat{B}|\phi_n\rangle
    \end{aligned}
$$

* If $\lambda_n$ is not a degenerate eigenvalue of $\hat{A}$, then $\hat{B}|\phi_n\rangle = \mu_n|\phi_n\rangle$
    * $|\phi_n\rangle$ is also an eigenvector of $\hat{B}$
* Proof:
    * If $\lambda_n$ were degenerate, then (and only then) could one have several linearly independent eigenvectors of $\hat{A}$ all corresponding to $\lambda_n$
    * Since we assume that $\lambda_n$ is not degenerate, $\hat{B}|\phi_n\rangle$ and $|\phi_n\rangle$ cannot be linearly independent, therefore $\hat{B}|\phi_n\rangle = \mu_n|\phi_n\rangle$ for some non-zero value of $\mu_n$
    * If $[\hat{A},\hat{B}] = 0$, then one can find a basis of the Hilbert space constructed from eigenvectors common to $\hat{A}$ and $\hat{B}$, and reciprocally

#### Example

For atomic hydrogen,
* $H$ - Hamiltonian
* $\vec{L}^2$ and $L_z$ - angular momentum operators

$$
    [H,\vec{L}^2] = [H,L_z] = [\vec{L}^2,L_z] = 0
$$

One can find functions that are eigenfunctions of all these three operators:

$$
    \begin{aligned}
    \psi_{nlm}(r,\theta,\phi) \\
    H\psi_{nlm} &= E_n\psi_{nlm} \\
    \vec{L}^2\psi_{nlm} &= \hbar^2l(l+1)\psi_{nlm} \\
    L_z\psi_{nlm} &= \hbar m\psi_{nlm}
    \end{aligned}
$$

* $H,\vec{L}^2,L_z$ from a "complete set of commuting observables" in the sense that specifying their eigenvalues (e.g. by specifying the corresponding quantum numbers) define their common eigenvectors unambiguously

$$
    (\Delta A)^2(\Delta B)^2 \geq -\frac{1}{4}(\langle\psi|[\hat{A},\hat{B}]|\psi\rangle)^2
$$

* if $\hat{A},\hat{B}$ are Hermitian, $[\hat{A},\hat{B}] = i\hat{C}$ where $\hat{C}$ is Hermitian

$$
    \langle\psi|\hat{C}|\psi\rangle = \langle\psi|\hat{C}|\psi\rangle^{ * }
$$

* the right hand-side is greater than zero
* $(\Delta A)^2$ is the variance of the probability distribution formed by the $P(\lambda_n)$

$$
    \begin{aligned}
    \hat{A}|\phi_n\rangle &= \lambda_n|\phi_n\rangle \\
    \langle\phi_n|\phi_n\rangle &= 1
    \end{aligned}
$$

Probability of finding $\lambda_n$ in the measurement is

$$
    P(\lambda_n) = |\langle\phi_n|\psi\rangle|^2
$$

* inside is the probability amplitude for finding $\lambda_n$
* See last lecture for generalisation to degenerate eigenvalues

$$
    \langle\psi|\hat{A}|\psi\rangle = \langle A\rangle
$$

This is the expectation value of $\hat{A}$

$$
    \sum_n \lambda_n P(\lambda_n)
$$

* If $|\psi\rangle$ is such that $\hat{A}|\psi\rangle = \lambda|\psi\rangle$, then $\langle\psi|\hat{A}|\psi\rangle = \lambda$

$$
    \begin{aligned}
    (\Delta A)^2 &= \langle\psi|(\hat{A} - \langle A\rangle\hat{I})^2|\psi\rangle \\
    &= \langle\psi|\hat{A}^2|\psi\rangle - \langle\psi|\hat{A}|\psi\rangle^2
    \end{aligned}
$$

$\Delta A$ is the uncertainty on $A$

* If we perform a measurement and get $\lambda^{(1)}$ then again and get $\lambda^{(2)}$ etc, after preparing the system to be back in the unmeasured state

$$
    \begin{aligned}
    \bar{\lambda} &= \frac{1}{n} \sum_j \lambda^{(j)} \\
    (\Delta A)^2 &= \langle A^2\rangle - \langle A\rangle^2 \\
    (\Delta A)^2 &\implies \sigma^2 = \frac{1}{n-1} \sum_j (\lambda^{(j)} - \bar{\lambda})^2
    \end{aligned}
$$

## Lecture 10

* If $\Delta A = 0$, there is no dispersion
* $\Delta A = 0$ if $|\psi\rangle$ is an eigenvector of $\hat{A}$
* $\hat{A}|\psi\rangle = \lambda|\psi\rangle$

$$
    \begin{aligned}
    \hat{A}^2|\psi\rangle &= \lambda^2|\psi\rangle = \hat{A}(\hat{A}|\psi\rangle) \\
    &= \hat{A}(\lambda|\psi\rangle) - \lambda\hat{A}|\psi\rangle = \lambda^2|\psi\rangle \\
    \langle\psi|\hat{A}^2|\psi\rangle - \langle\psi|\hat{A}|\psi\rangle^2 &= \lambda^2\langle\psi|\psi\rangle - (\lambda\langle\psi|\psi\rangle)^2 \\
    &= \lambda^2 = \bar{\lambda}^2 = 0
    \end{aligned}
$$

* For finite dimensional spaces, if $|\psi\rangle$ is an eigenvector of $\hat{A}$, then $\rangle\psi|[\hat{A},\hat{B}]|\psi\rangle = 0$ too

$$
    \begin{aligned}
    \langle\psi|\hat{A}\hat{B} - \hat{B}\hat{A}|\psi\rangle &= \lambda^* \langle\psi|\hat{B}|\psi\rangle - \lambda\langle\psi|\hat{B}|\psi\rangle \\
    &= (\lambda - \lambda)\langle\psi|\hat{B}|\psi\rangle = 0
    \end{aligned}
$$

_complex conjugate goes away since $\hat{A}$ is Hermitian_

* If $[\hat{A},\hat{B}] = 0$, then it is possible for $(\Delta A)^2(\Delta B)^2 = 0$
* For $\hat{P}$ as the momentum operator,

$$
    \begin{aligned}
    \hat{P}|\phi\rangle &= p|\phi\rangle \\
    -i\hbar \frac{d}{dx} \phi(x) &= p\phi(x) \\
    \phi_p(x) &= Ce^{i\frac{px}{\hbar}}
    \end{aligned}
$$

_not square summable, therefore not an element of the Hilbert space_

* For $\hat{Q}$ as the position operator,

$$
    Q\phi(x) = x\phi(x) = a\phi(x)
$$

_impossible unless $\phi(x) = 0$, which does not qualify as an eigenfunction_

* Take $\phi_p(x)$ as generalised eigenfunction of the momentum operator

### Measurement of P

* What is the probability of finding a certain value, $p$?
* $p$ is distributed continuously, not quantised
* Better to ask for the probability of finding $p$ between $p_1$ and $p_2$?

$$
    P[(p_1,p_2)] = \int_{p_1}^{p_2} P(p)\,dp
$$

* $P(p)$ is the density of probability, $P(p)\,dp$ is the probabilty to find a momentum between $p$ and $p+dp$
* $P(p)$ has no physical dimensions
    * those of the inverse of a momentum, so that $P[(p_1,p_2)]$ is a pure number

$$
    P(p) = \Bigg|\int_{-\infty}^{\infty} \phi_p^{* }(x) \phi(x)\,dx\Bigg|^2 = \Bigg|C\int_{-\infty}^{\infty} e^{-i\frac{px}{\hbar}}\psi(x)\,dx\Bigg|^2
$$

* This is the Fourier transform of $\psi(x)$

$$
    \begin{aligned}
    \phi(k) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{i\frac{px}{\hbar}}\psi(x)\,dx \\
    \psi(x) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{ikx}\phi(k)\,dk \\
    &= \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx}dk \int_{-\infty}^{\infty} e^{-ikx'}\psi(x')\,dx' \\
    &= \frac{1}{2\pi}\int_{-\infty}^{\infty} \psi(x)\,dx  \int_{-\infty}^{\infty} e^{ik(x-x')} dx
    \end{aligned}
$$

## Lecture 11

* Momentum operator: $p = -i\hbar\frac{d}{dx}$
* Position operator: $Q = x$

$$
    \begin{aligned}
    P\phi_k(x) &= P\left[Ce^{ikx}\right] = \hbar k\phi_k(x) \\
    \phi(k) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \psi(x)e^{-ikx}dx \\
    \psi(x) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \\
    \delta(x-x') &= \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{ik(x-x')}dk
    f(x') &= \int_{-\infty}^{\infty} \delta(x-x')f(x)\,dx
    \end{aligned}
$$

* This is true for any function $f(x)$ that is continuous at $x=x'$

$$
    \begin{aligned}
    \delta(x-x') &= \delta(x'-x) \\
    \int_{-\infty}^{\infty} P(k)\,dk &= 1 \implies \int_{-\infty}^{\infty} |\psi(x)|^2dx = 1 \\
    P(k) &= |\phi(k)|^2|C|^2 \\
    \phi_k(x) &= Ce^{ikx} \\
    |C|^2\int_{-\infty}^{\infty} dk&\left[\int_{-\infty}^{\infty} \psi(x)e^{-ikx}dx\right]^{ * } \cdot \left[\int_{-\infty}^{\infty}\psi(x')e^{-ikx'}dx'\right] = 1 \\
    |C|^2\int_{-\infty}^{\infty} dx&\int_{-\infty}^{\infty} \psi^* (x)\psi(x') dx' \cdot \int_{-\infty}^{\infty} e^{ik(x-x')}dk = 1 \\
    2\pi|C|^2 \int_{-\infty}^{\infty} dx& \int_{-\infty}^{\infty} \psi^* (x)\psi(x')\delta(x-x')\,dx' = 1 \\
    2\pi|C|^2 \int_{-\infty}^{\infty} dx& \psi^* (x)\psi(x) = 1 \\
    \implies 2\pi|C|^2 &= 1 \to C = \frac{1}{\sqrt{2\pi}}
    \end{aligned}
$$

The normalised eigenfunctions of $P$ are:

$$
    \begin{aligned}
    \phi_k(x) &= \frac{1}{\sqrt{2\pi}}e^{ikx} \\
    \phi_p(x) &= \frac{1}{\sqrt{2\pi\hbar}}e^{ip\frac{x}{\hbar}}
    \end{aligned}
$$

* Orthonormality condition here is

$$
    \begin{aligned}
    \int_{-\infty}^{\infty} \phi_k^* (x)\phi_{k'}(x)\,dx &= \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{i(k-k')x}dx = \delta(k'-k) \\
    \int_{-\infty}^{\infty} \phi_n(x)\phi_{n'}(x)\,dx &= \delta_{nn'}
    \end{aligned}
$$

### Eigenfunctions of the position operator

$$
    Q\psi(x) = x\psi(x)
$$

An eigenfunction of $Q$ would be such that

$$
    Q\phi_q(x) \equiv q\phi_k(x) \equiv x\phi_k(x)
$$

Finally, one can take:

$$
    \begin{aligned}
    \phi_k(x) &= \delta(x-q) \\
    P[(q_1,q_2)] &= \int_{q_1}^{q_2} P(q)\,dq \\
    P(q) &= \Bigg|\int_{-\infty}^{\infty} \phi_q^* (x)\psi(x)\,dx\Bigg|^2 \\
    &= \Bigg|\int_{-\infty}^{\infty} \delta(q-x)\psi(x)\,dx\Bigg|^2 \\
    &= |\psi(q)|^2
    \end{aligned}
$$

This is the Born Rule

* Normalisation:

$$
    \int_{-\infty}^{\infty} \delta^* (x-q)\delta(x-q')\,dx = \delta(q-q')
$$

Discrete case: $|\psi\rangle = \sum_n c_n|\phi_n\rangle$ if $\{|\phi_n\rangle\}$ is an orthonormal basis

$$
    \begin{aligned}
    c_n &= \langle\phi_n|\psi\rangle \\
    \psi(x) &= \int_{-\infty}^{\infty} \phi(p)\phi_p(x)\,dp,~ \phi(p) = \langle p|\psi\rangle \\
    \hat{Q}|x\rangle &= x|x\rangle \\
    \hat{p}|p\rangle &= p|p\rangle \\
    \psi(x) &= \langle x|\psi\rangle
    \end{aligned}
$$

* $\psi(x) = \langle x|\psi\rangle$ - wave function in position representation in position space
* $\phi(p) = \langle p|\psi\rangle$ - wave function in the momentum representation in momentum space

The last two statements are equivalent

$$
    \begin{aligned}
    |\psi\rangle &\leftrightarrow \psi(x) \\
    |x\rangle &\leftrightarrow \begin{pmatrix} a \\ b \end{pmatrix} \\
    |\psi\rangle &\leftrightarrow \phi(p) \\
    \langle x|p\rangle &= \frac{1}{\sqrt{2\pi\hbar}}e^{ip\frac{x}{\hbar}} \\
    \langle p|x\rangle &= \frac{1}{\sqrt{2\pi\hbar}}e^{-ix\frac{p}{\hbar}} \\
    \hat{Q} &\leftrightarrow x \\
    \hat{p} &\leftrightarrow -i\hbar\frac{d}{dx} \\
    \hat{p} &\leftrightarrow p \\
    \hat{Q} &\leftrightarrow -i\hbar\frac{d}{dp}
    \end{aligned}
$$

In 3D position representation:

$$
    \begin{aligned}
    P_x &= -i\hbar\frac{\partial}{\partial x} \\
    P_y &= -i\hbar\frac{\partial}{\partial y} \\
    P_z &= -i\hbar\frac{\partial}{\partial z} \\
    [x,P_x] &= [y,P_y] = [z,P_z] = i\hbar \\
    [x,y] &= [x,z] = [y,z] = 0 \\
    [x,P_y] &= [x,P_z] = \cdots = 0 \\
    [P_x,P_y] &= [P_x,P_y] = 0 \\
    [x,P_y]\psi(x,y,z) &= -i\hbar\left[x\frac{\partial}{\partial y}\psi - \frac{\partial}{\partial y}x\psi\right] = 0 \\
    \vec{P} &= P_x\hat{x} + P_y\hat{y} + P_z\hat{z} \\
    \vec{P}\phi_{\vec{p}}(\vec{r}) &= \vec{P}\phi_{\vec{p}}(\vec{r}) \\
    \vec{p} &= \hbar\vec{k} \\
    \phi_{\vec{p}}(\vec{r}) &= \frac{1}{\sqrt{2\pi\hbar}}e^{i\vec{p}\cdot\frac{\vec{r}}{\hbar}} \\
    \phi_{\vec{k}}(\vec{r}) &= \frac{1}{\sqrt{2\pi}}e^{i\hbar\vec{r}} \\
    \int \phi_k^* (\vec{r})\phi_{k'}(\vec{r})\,d^3r &= \delta^3(\vec{k} - \vec{k}') = \delta(k_x - k_{x}')\delta(k_y - k_y')\delta(k_z - k_z')
    \end{aligned}
$$

## Lecture 13

### Unitary Operators

* If $\hat{A}^\dagger = \hat{U}^{-1}$, then $\hat{U}$ is a unitary operator
    * $\hat{U}^\dagger\hat{U} = \hat{I} = \hat{U}\hat{U}^\dagger$
    * $\hat{U}^{-1}\hat{U} = \hat{I} = \hat{U}\hat{U}^{-1}$
* $\hat{U}$ is the same for all vectors of the Hilbert space

$$
    \begin{aligned}
    |\psi'\rangle &= \hat{U}|\psi\rangle \\
    |\psi\rangle &= \hat{U}^{-1}|\psi'\rangle = \hat{U}^\dagger|\psi'\rangle \\
    |\phi'\rangle &= \hat{U}|\phi\rangle \\
    |\eta\rangle &= \hat{A}|\psi\rangle \\
    |\eta'\rangle &= \hat{U}|eta\rangle = \hat{U}\hat{A}|\psi\rangle = \hat{U}\hat{A}\hat{U}^\dagger|\psi'\rangle \\
    |\eta'\rangle &= \hat{A}'|\psi'\rangle,~ \hat{A}' = \hat{U}\hat{A}\hat{U}^\dagger
    \end{aligned}
$$

* Line four and seven are of the same form - but latter is written in terms of the transformed vectors and operators.
* $\hat{U}$ transforms:
    * vectors $|\psi\rangle$ into $\hat{U}|\psi\rangle$
    * operators $\hat{A}$ into $\hat{U}\hat{A}\hat{U}^\dagger$
* $\hat{A}' = \hat{U}\hat{A}\hat{U}^\dagger$ has all the same properties of untransformed operator $\hat{A}$
* If $\hat{A}$ is Hermitian, then $\hat{A}'$ is also Hermitian
* If $\hat{A} = \alpha\hat{B} + \beta\hat{C}\hat{D}$, then $\hat{A}' = \alpha\hat{B}' + \beta\hat{C}'\hat{D}'$
* Proof:

$$
    \begin{aligned}
    \hat{A} &= \alpha\hat{B} + \beta\hat{C}\hat{D} \\
    \hat{U}\hat{A}\hat{U}^\dagger &= \alpha\hat{U}\hat{B}\hat{U}^\dagger + \beta\hat{U}\hat{C}\hat{I}\hat{D}\hat{U}^\dagger \\
    \hat{A}' &= \alpha\hat{B}' + \beta\hat{C}'\hat{D}'
    \end{aligned}
$$

* $[\hat{A},\hat{B}] = [\hat{A}', \hat{B}']$
* $\hat{A}$ and $\hat{A}'$ have the same eigenvalues
* $\langle\phi|\hat{A}|\psi\rangle = \langle\phi'|\hat{A}'|\psi'\rangle$ for any $|\psi\rangle,|\phi\rangle$
* In particular, $\langle\phi|\psi\rangle = \langle\phi'|\psi'\rangle$
    * inner products are not changed by unitary transformations
* Proof:

$$
    \begin{aligned}
    |\psi'\rangle &= \hat{U}|\psi\rangle \\
    |\phi'\rangle &= \hat{U}|\phi\rangle \\
    \implies \langle\phi'| &= \langle\phi|\hat{U}^\dagger \\
    \implies \langle\phi'|\psi'\rangle &= \langle\phi|\hat{U}^\dagger\hat{U}|\psi\rangle \\
    &= \langle\phi|\psi\rangle
    \end{aligned}
$$

* In particular, unitary transformations do not change the norm of the vector: $\langle\psi|\psi\rangle = \langle\psi'|\psi'\rangle$

### Time evolution of quantum systems

* Time-dependent Schrodinger equation:

$$
    \begin{aligned}
    i\hbar\frac{d}{dt}|\Psi(t)\rangle &= \hat{H}|\Psi(t)\rangle \\
    |\Psi(t)\rangle &= \hat{U}(t,t_0)|\Psi(t_0)\rangle \\
    \hat{U}(t,t_0) &= \hat{U}(t,t_1)\hat{U}(t_1,t_0) \\
    \hat{U}^\dagger(t,t_0) &= \hat{U}^{-1}(t,t_0) = \hat{U}(t_0,t) \\
    \hat{U}(t_0,t_0) &= \hat{I} = \hat{U}(t_0,t)\hat{U}(t,t_0) \\
    \implies i\hbar\frac{d}{dt}\hat{U}(t,t_0) &= \hat{H}\hat{U}(t,t_0)
    \end{aligned}
$$

* $\hat{U}(t,t_0)$ is the time-evolution operator
    * it is unitary
* If $\hat{H}$ is time-independent, then

$$
    \begin{aligned}
    \hat{U}(t,t_0) &= \exp\left[\frac{-i\hat{H}(t-t_0)}{\hbar}\right] \\
    e^{\hat{A}} &= \hat{I} + \hat{A} + \frac{1}{2!}\hat{A}^2 + \frac{1}{3!}\hat{A}^3 + \cdots
    \end{aligned}
$$

* The exponential of an operator is the Taylor expansion of that operator

### Expectation values of observables

$$
    \begin{aligned}
    \langle\hat{A}(t)\rangle &= \langle\Psi(t)|\hat{A}|\Psi(t)\rangle \\
    &= \langle\Psi(t_0)|\underbrace{\hat{U}^\dagger(t,t_0)\hat{A}\hat{U}(t,t_0)}_{\hat{A}_H(t)}|\Psi(t_0)\rangle \\
    \hat{A}_H(t) &= \hat{U}^\dagger(t,t_0)\hat{A}\hat{U}(t,t_0) \\
    &= \hat{U}(t_0,t)\hat{A}\hat{U}^\dagger(t_0,t) \\
    \langle\hat{A}(t)\rangle &= \langle\Psi(t_0)|\hat{A}_H(t)|\Psi(t_0)\rangle
    \end{aligned}
$$

1. State vector changes in time, $\hat{A}$ doesn't - Schrodinger picture
2. State vectors do not change in time, $\hat{A}_H(t_{})$ does - Heisenberg picture
* These two formulations are completely equivalent
* Heisenberg equation of motion:

$$
    i\hbar\frac{d\hat{A}_H(t)}{dt} = [\hat{A}_H,\hat{H}] = [\hat{A},\hat{H}]
$$

if $\hat{A}$ is time-independent.
