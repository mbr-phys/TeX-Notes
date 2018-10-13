---
title: "Quantum Mechanics 3"
author: "Dr Gidopoulos"
date: "Michaelmas 2018"
---

# Lecture 1

1. Hilbert spaces
2. von Neumanns axioms
3. Hermitian ops
4. T.D. Schrodinger Eq -> T.I. Schrodinger Eq
5. 1 particle in 3D
6. Ang momentum ops, commutators, spin angular momentumo

## von Neumanns axioms

1. In QM, every observable is represented by a Hermitian operator. 
2. The state of the system is represented by a wavefunction.
    - Scalar multiple of the wavefunction still represents system, convenient to choose to be normalised though.  
3. Usual bra-ket stuff
$$
    \begin{align}
    \langle\psi|Q\psi\rangle &= \int dx \psi^{*}(x)\left(Q\psi(x)\right) \\
    \langle\psi|Q\psi\rangle^{*} = \langle Q\psi|\psi\rangle &= \int dx \left(Q\psi(x)\right)^{*}\psi(x) \\
    \langle Q\rangle &= \langle\psi|Q\psi\rangle = \langle Q\psi|\psi\rangle = \langle\psi|Q|\psi\rangle
    \end{align}
$$
4. Usual orthonormal eigen stuff

### Example

See Pauli spin operators and stuff
Find result of $\omega = \gamma B$, the angular momentum around a magnetic field

# Lecture 2

nothing

# Lecture 3

1. Study motion of charged particle in magnetic fields
2. Study means to solve S.E. - we need H for B, E, $H = \frac{1}{2m}\left(-i\hbar\nabla - qA\right)^2 + q\phi$
3. It turns out H contains $\phi, A$, not E, B, $E = -\nabla\phi$, $B = \nabla\times A$
4. But different As may gave same B
5. Solve examples
    1. 2D motion of q in uniform mag field (cyclotron freq)
    2. Explore A vs B - 1D example where $B = 0, A \neq 0$

## Guage freedom
\begin{align}
    \vec{A} &= \frac{B}{2}(-y\hat{x} + x\hat{y} \implies \vec{\nabla} \times\vec{A} = B\hat{z} \\
    \vec{A}' &= -By\hat{x} \implies \vec{\nabla}\times\vec{A}' = B\hat{z} \\
    \vec{A} - \vec{A}' &= \frac{By}{2}\hat{x} + \frac{Bx}{2}\hat{y} = \vec{\nabla}\left(-\frac{Bxy}{2}\right) \implies \vec{A} = \vec{A}' + \vec{\nabla}\times(x,y,z) \\
    \vec{\nabla} \times \vec{A} &= \vec{\nabla} \times \vec{A} + \cancel{\vec{\nabla} \times \vec{\nabla}\times(\vec{r}) 
\end{align}

### Time deriv of fn
\begin{align}
    \phi' &= \phi + \frac{\partial}{\partial t}\times(r,t) \\
    \vec{A}' &= \vec{A} + \vec{\nabla}\times(r,t) \\
    (\phi',\vec{A}'),& (\phi,\vec{A}) \to \vec{E},\vec{B}
\end{align}
Convenient to choose $\vec{A}$ s.t. $\vec{\nabla}\cdot\vec{A} = 0$.

## 2D motion (x,y) of q in mag field, B along z

\begin{align}
    H &= \frac{1}{2m}\left(-i\hbar\vec{\nabla} - q\vec{A}\right)^2 \\
    &= \frac{1}{2m}\left(-i\hbar\frac{\partial}{\partial x}\hat{x} - i\hbar\frac{\partial}{\partial y}\hat{y} + qBy\hat{x}\right)^2 \\
    &= \frac{1}{2m}\left(-i\hbar\frac{\partial}{\partial y}\hat{y} + \left(-i\hbar\frac{\partial}{\partial x} + qBy\right)\hat{x}\right)^2 \\
    E\psi(x,y) &= \frac{1}{2m}\left(-\hbar^2\frac{\partial}{\partial x^2} - 2i\hbar qBy\frac{\partial}{\partial x} + q^2B^2y^2 - \hbar^2\frac{\partial^2}{\partial y^2}\right)\psi(x,y) \\
    \psi(x,y) &= e^{-ikx}\phi(y) \\
    \implies &\frac{1}{2m}\left(\hbar^2k^2 - 2\hbar kqBy + q^2B^2y^2 - \hbar^2\frac{\partial^2}{\partial y^2}\right)\cancel{e^{-ikx}}\phi(y) = E\cancel{e^{-ikx}}\phi(y)  \\
    \implies &\frac{1}{2m}(qBy - \hbar k)^2\phi(y) = E\phi(y), y_0 = \frac{\hbar k}{qB} \\
    \implies &\left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial y^2} + \frac{m}{2}\frac{q^2B^2}{m^2}(y - y_0)^2\right]\psi(y) = E\psi(y)
\end{align}
This is Simple harmonic motion with $\frac{qB}{m} = \omega$, and energy $E = \left(n + \frac{1}{2}\right)\hbar\omega$.
These are the Landau levels.

### Periodic boundary conditions

\begin{align}
    e^{-ik(x + L)} = e^{-ikx} \\
    e^{-ikL} = 1 \\
    kL = 2\pi j \\
    k_j = \frac{2\pi}{L}j, j \in Z \\
    0 < y_0 < L \\
    0 < \frac{\hbar k_j}{qB} < L \\
    0 < \frac{\hbar 2\pi j}{qBL} < L \\
    0 < j < \frac{qBL^2}{h} \\
    0 < j < \frac{\Phi}{h/q} \\
    j_{max} = \frac{\Phi}{h/q}
\end{align}

## A vs B, Aharanov-Bohm

\begin{align}
    H = \frac{L_z^2}{2I} &= -\frac{\hbar^2}{2mb^2}\frac{\partial^2}{\partial \phi^2} \\
    -frac{\hbar^2}{2mb^2}\frac{\partial^2}{\partial \phi^2}\psi(\phi) &= E\psi(\phi) \\
    E &= \frac{\hbar^2 k^2}{2mb^2}
\end{align}

Single valued: $e^{ik\phi$ soln, $e^{ik(\phi + 2\pi)} = e^{ik\phi}$. k is integer. 












