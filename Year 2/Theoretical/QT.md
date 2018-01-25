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
