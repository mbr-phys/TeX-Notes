## Foundations A
### Quantum Mechanics
###### Shaun Cole

#### 1. Basics of QM

* Useless so just read notes
* Particles described by wave functions, psi
* $P(x) dx = \psi^2 dx = \psi^* \psi dx$
    * $\int_{-\infty}^{\infty} = 1$


#### 2. Operators and Expectation Values

* Expectation value is average value
    * $\langle x \rangle  = \int_{-\infty}^{\infty} xP(x) dx$
    * Doesn't always mean most expected value, just average
    * page 7
* $\hat{p}$ now means $-i\hbar \frac{\partial}{\partial x}$
    * page 8
* Hamiltonian
    * sum of potential and kinetic energy
    * use $-\frac{\hat{p}^2}{2m} \frac{\partial^2}{\partial x^2} + V$ for the operator version
    * $\hat{H} \psi = E \psi$
        * alternate form of Schrodinger
    * page 8
* Klein-Gordon for relativistic electrons
    * probably won't need it
    * page 9



#### 3. The Origin Of Uncertainty
* Page 10
* Complex conjugate operators of position, momentum, etc operate on the function immediately to the right
* Hermitian -- the complex conjugate of the integral for the expectation value is equivalent
    * Swapping positions of variables and taking cplx conjugate
* Any dynamical quantity can be an operator
* Expectation value only real if it is Hermitian
* Can use Hermitian to show uncertainty principle
    * try finding $\langle xp\rangle$
    * will not got $= \langle xp\rangle*$
* $\hat{x}\hat{p} \neq \hat{p}\hat{x}$
    * they do not commute
* Page 11
* Square bracket notation for commutator
    * $[\hat{a},\hat{b}] = \hat{a}\hat{b} - \hat{b}\hat{a}$
* The x and p operators don't commute so aren't real and can't be measured
    * can be a test for other operators too to find relations for uncertainty
    * the difference between the two double commutators for x and p is ihbar which is where the hbar/2 comes from for uncertainty
* Use a Gaussian function and find EVs for $\langle x \rangle , \langle p \rangle , \langle x^2 \rangle , \langle p^2 \rangle$ to get minimum Heisenberg values
* Ehrenfest's Theorem fulfils Newton's second law with EVs



#### 4. Schrodinger Equation and Eigenfunctions
* page 14
* $ln T = \frac{E}{i\hbar}t + K$
* $T = e^{-it\frac{E}{\hbar}}$
* Can covert from time-dep to time-indep if $V = V(x)$, separable fns
* Kronacker delta fn from Maths
    * for distinct eigenfns and orthogonality
* Bra-ket notation for eigen stuff
    * $\langle$ | for cplx conjugate
    * | $\rangle$  for normal
    * $\langle$ | $\rangle$  = $\int$
* Eigenfns of the Hamiltonian are stationary

#### 5. Eigenfunctions versus Superpositions
* page 17
* $\Psi(x,t) = \Psi_{E}(x,t)e^{-\frac{iE}{\hbar}t}$
* $\Psi(x,t) = C_{1}\Psi_{E_{1}}(x,t)e^{-\frac{iE_{1}}{\hbar}t} + C_{2}\Psi_{E_{2}}(x,t)e^{-\frac{iE_{2}}{\hbar}t}$
* Certain harmonics for standing waves
    * only certain wavelengths and energies for these systems
* Infinite square well example
    * see last year's notes
    * normal SHO
        * sin and cos solns
        * $\cos = 0$
        * $\Psi(x) = A\sin(kx)$
        * $k = \frac{\sqrt{2mE}}{\hbar}$
        * $A = \sqrt{\frac{2}{L}}$
        * all usual maths from last year, find $\Psi$ and integrate for constants
    * can make this into a full energy eigenfn:
    $$
        \Psi_{n}(x,t) = \sqrt{\frac{2}{L}}\sin\Big(\frac{n\pi x}{L}\Big)e^{-\frac{iE_{n}t}{\hbar}}
    $$
* Mixture of states leads to time dep
* For any single eigenfn, probability is not time dep
    * we say these are stationary states
    * expectation values are not time dep
* General solution to time dep Schrodinger eqn is superposition of eigenstates:
$$
    \Psi(x,t) = \sum_{n} c_{n}\Psi_{n}(x,t) = \sum_{n}c_{n}\sqrt{\frac{2}{L}}\sin\Big(\frac{n\pi x}{L}\Big)e^{-\frac{iE_{n}t}{\hbar}}
$$
* $c_{n}$ must be chosen so as to normalise total wavefn
    * must equate to one as usual

##### Orthogonality
* Form an overlap integral of two states n and m:
    * $\langle\Psi_{n}|\Psi_{m}\rangle$
    * use [!wa](www.wolframalpha.com) as usual for indefinite integral
* when $n \neq m$ both sin terms are for integer $\pi$ and so both are zero
* when $n = m$, the denominator on the first term goes to zero and the rest tends to 1 as the inside tends to zero
    * this shows it is orthonormal
    * like dot product
* Span the space known from Fourier analysis for expressed as sum of sin waves

##### Wavefns in Superposition of Eigenstates
* **this is much more thorough in the notes**
* General solution for superpositions:
$$
    \Psi(x) = \sum_{n} c_{n}\Psi_{n}(x) \\
    |\Psi\rangle  = \sum_{n} c_{n}|\Psi_{n}\rangle
$$
* Normalisation condition for two states:
    * $|c_{1}|^{2} + |c_{2}|^{2} = 1$
    * for general,
        * use Kronacker delta fn to simplify integrals to get down to:
        * $\sum_{m}|c_{m}|^{2}$
        * **always adds up to 1**
* For average energy,
    * using Kronacker delta again
$$
    \langle E \rangle = \sum_{n}|c_{n}|^{2}E_{n}
$$
* Only works if $|c_{n}|^{2}$ is probability of being in state $\Psi_{n}$ and measuring energy $E_{n}$
* QM predicts only the probability of measuring particular energies
    * non-deterministic

##### Expectation for Energy and Time dep
* Expectation value of energy is probability weighted sum of energies associated with each state
* A superposed states probability of being in any particular state is
$$
    \Psi(x,t) = \sum_{n} c_{n}\Psi_{n}e^{-\frac{iE_{n}t}{\hbar}}
$$
* it oscillates with time
* Looking at the probability for a two state system:
    * last two terms contain $e^{\pm\frac{i(E_{2} - E_{1})t}{\hbar}}$
    * write this as $e^{\pm i\omega t}$
    * $\hbar\omega = E_{2} - E_{1}$
$$
    P(x,t) = |c_{1}|^{2}|\Psi_{1}|^2 + |c_{2}|^{2}|\Psi_{2}|^{2} + c_{1}^{*}c_{2}\Psi_{1}^{*}\Psi_{2}e^{-i\omega t} + c_{1}c_{2}^{*}\Psi_{1}\Psi_{2}^{*}e^{i\omega t}
$$
* This is real as last two terms are cplx conjugate of each other and so, when added together, their imaginary parts cancel.
* Notes that this probability varies with time
* **Superposed states are not stationary states**
* It is still normalised, $\int P(x,t) = 1$, as orthogonality of eigenfns makes last two terms zero when integrated over x



#### 6. Superposition of eigenstates and transitions
* page 21
* All expectation values are constant in time for single eigenfn
    * A general soln which contains multiple is not
* For two terms in the infinite square well, the probability density oscillates with
    * $\omega = \frac{E_2 - E_1}{\hbar}$
* For an electron in ground state of an atom,
    * it can be said it is a single eigenfn so it is not dep on time
    * standing wave
* QM probability distributions solve radiation problem
    * probability density is stationary so the charge is not 'moving' and it doesn't radiate
    * otherwise everything crashes into nucleus
* The mixture of two or more different states, say $n = 1, 2$ then it has a chance of decaying down
    * can't happen at ground state as no lower state to mix with

##### How to find the cm
* Going from particular soln to general assume that energy eigenfns span the entire space
    * complete set of basis fns
    * any arbitrary fn can be expanded as sum of these
* For any functional form $f(x)$, can decompose it into a weighted sum of energy eigenfns $c_n \Psi_n$ by calculating each $c_n = \int \Psi_{n}^{*}f(x)dx*$
    * find the overlap of f with the wavefn
    * $\sum_{n} c_n \delta_{nm} = c_m$



#### 7. Eigenfunctions of various potentials
* page 22

* Consider infinite square well, symmetric about the origin

##### Infinite Square Well
* For $0 < x < L,~ \Psi_{n}(x,t) = \Psi_{n}e^{-i\frac{E_{n}t}{\hbar}}$:
$$
    \Psi_{n}(x) = \sqrt{\frac{2}{L}}\sin(\frac{n\pi x}{L}) ~;~ E_n = \frac{n^{2}\pi^{2}\hbar^2}{2mL^2}
$$
* Can make this symmetric about origin by using a change of variable:
    * $x' = x - \frac{L}{2}$
    * Energy levels are unchanged but solns for odd n will become cos
        * seen by drawing a diagram
    * This gives
$$
    \Psi_{n}(x)' = \sqrt{\frac{2}{L}}\sin(\frac{n\pi x'}{L} + \frac{n\pi}{2}) = \sqrt{\frac{2}{L}}\sin(\frac{n\pi x'}{L})\cos(\frac{n\pi}{2}) + \cos(\frac{n\pi x'}{L}\sin(\frac{n\pi}{2}))
$$
* Depends on n
    * odd n wavefns are even fns
        * $\Psi(x') = \Psi(-x')$
    * even n wavefns are odd fns
        * $\Psi(x') = \Psi(-x')$
    * Note that in either case the probability distribution $P(x) = |\Psi(x)|^2$ is symmetric about $x' = 0$

##### Finite Square Well
* Potential is now V instead of infinity
* Expect bound wavefns to be similar to infinite square well but broader and leak out slightly
* Solve Schrodinger for three regions:
    * $x < -\frac{L}{2}$
    * $-\frac{L}{2} < x < \frac{L}{2}$
    * $x > \frac{L}{2}$
* For central region, $V = 0$:
$$
    -\frac{\hbar^2}{2m} \frac{d^2 \Psi}{dx^2} = E\Psi \\
    \Psi = A\cos{ks} + B\sin(kx) ~;~ k^2 = \frac{2mE}{\hbar^2}
$$
* For $x > \frac{L}{2}$:
$$
    -\frac{\hbar^2}{2m} \frac{d^2 \Psi}{dx^2} + V_0 \Psi = E\Psi \\
    \frac{d^2 \Psi}{dx^2} = \frac{2m}{\hbar^2}(V_0 - E)\Psi = \alpha^2 \Psi ~;~ \alpha^2 = \frac{2m}{\hbar^2}(V_0 - E)
$$
* Here we have used that for bound states $V_0 > E$
    * $-\alpha^2 < 0$
    * General soln is $\Psi(x) = Ce^{\alpha x} + De^{-\alpha x}$
    * For soln to be normaliseable, $C = 0$, or exponent just increases
$$
    \Psi(x) = De^{-\alpha x} ~;~ x > \frac{L}{2}
$$
* Similarly for $x < -\frac{L}{2}$:
$$
    \Psi(x) = Fe^{\alpha x}
$$
* Not an infinite discontinuity in V, then $\frac{\partial \Psi}{\partial x}$ as well as $\Psi$ must be continuous at $x = \pm \frac{L}{2}$
    * In principle, this is all wee need for solns
    * solns will either be odd or even - $\Psi(x) = \pm \Psi(-x)$

###### Even Solns
* page 24
* Only need to consider the join at $x = \frac{L}{2}$ as it's the same at $x = -\frac{L}{2}$ by symmetry
* Applying continuity:
    * In $\Psi$: $A\cos{\frac{kL}{2}} = De^{-\frac{\alpha L}{2}}$
    * In $\frac{\partial \Psi}{\partial x}$: $-kA\sin{\frac{kL}{2}} = -\alpha De^{-\frac{\alpha L}{2}}$
* We find that:
$$
    (\frac{kL}{2}\tan{\frac{kL}{2}} = \frac{\alpha L}{2})
$$
* Meanwhile for defns of k and $\alpha$, in terms of energy we also have:
$$
    \Big(\frac{\alpha L}{2}\Big)^2 + \Big(\frac{kL}{2} \Big)^2 = \frac{2mV_0}{\hbar^2}\Big(\frac{L}{2} \Big)^2
$$
* Solving for simultaneous eqns finds allowed values for k, energy levels and wavefns
    * Isn't trivial, but can find informative graphical soln by setting
$$
    X = \frac{kL}{2} ~;~ Y = \frac{\alpha L}{2}
$$
* Two eqns become:
$$
    Y = X\tan X ~;~ X^2 + Y^2 = \frac{2mV_0}{\hbar^2}\Big(\frac{L}{2} \Big)^2
$$
* Plot Y(X) for both eqns and where they intersect are allowed solns

###### Odd Solns
* Follow same method for odd solns, so sin instead of cos
$$
    Y = -X\cot X ~;~ X^2 + Y^2 = \frac{2mV_0}{\hbar^2}\Big(\frac{L}{2} \Big)^2
$$
* Look at plot on page 24:
    1. There is always at least one bound state
        * if $R < \frac{\pi}{2} \to V_0 < \frac{\hbar^{2}\pi^2}{2mL^2}$ then this is the only state
    2. For intermediate circle, there are 4 allowed states corresponding to the four points of intersection
        * Reading X and Y values determines k and $\alpha$
        * Plugging back into eqns above gives D and F (for symmetry) in terms of A
        * To get value for A, use normalisation
            * split into bounds $-\infty \leq x \leq -\frac{L}{2}$, $-\frac{L}{2} \leq x \leq \frac{L}{2}$, $\frac{L}{2} \leq x \leq \infty$
    3. In lim as $V_0 \to \infty$, radius of circle becomes very large and intersections occur at
        * $X(= \frac{kL}{2}) = \frac{n\pi}{2}$
        * energy values are same as in infite square well
            * $E_n = \frac{n^{2}\hbar^{2}k^2}{2m} = \frac{\pi^{2}\hbar^{2}}{2mL^2}$

##### Commutator Algebra
* $[A, B] = AB - BA = -[B, A]$
    * not necessarily zero
    * operators do not have to commute
    * E.g. $[x, p] = i\hbar$
* **See page 25 for commutator identity proofs**
$$
    [A,A] = AA - AA = 0
$$
$$
    (A + B, C) = [A, C] + [B, C]
$$
$$
    (AB, C) = A[B, C] + [A,C]B
$$
$$
    (A,BC) = [A,B]C + B[A,C]
$$

##### Consequences of non-commutation
* All operators which commute share a common set of eigenfns
    * page 26 for proof
* Tells a bit more about uncertainty principle
    * measuring an operator does not disturb wavefn for measurement of next
    * if they don't commute, then in measuring A, we change the wavefn to be one of the eigenfns of A
        * if not eigenfns of B, can still expand f in terms of eigenfns of B
$$
    f_n = \sum_{m} c_{m}g_m ~;~ c_{m} = \int g_{m}^{*}f_{n}\,dx*
$$
* Now if we measure B, don't get a deterministic value of B
    * measure value $b_m$ with probability $|c_{m}|^2$
* Non-commutation means the two associated variables cannot simultaneously have deterministic values
    * this implies the uncertainty principle

##### The linear harmonic oscillator
* Potential, $V(x) = \frac{1}{2}kx^2$
    * oscillates with $\omega = \sqrt{\frac{k}{m}}$
    * $V(x) = \frac{1}{2}m\omega^{2}x^2$
* Wide applications as about equilibrium psn, $x_0$, any arbitrary continuous potential V(x) is harmonic to leading order
$$
    V(x) \approx V(x_{0}) + \Bigg[\frac{dV}{dx}\Big|_{x_{0}} (x - x_{0}) \Bigg]^{= 0} + \frac{1}{2}\frac{d^{2}V}{dx^2}\Big|_{x_{0}} (x - x_{0})^2 + \cdots
$$
* Time Indep Schrodinger eqn is:
$$
    \Big(\frac{\hat{p}^2}{2m} + V\Big)\Psi = E\Psi
$$
$$
    \frac{1}{2m}(\hat{p}^2 + (m\omega x)^2)\Psi = E\Psi
$$

###### Ladder Operators
* Can't do this factorisation:
$$
    (a^2 + b^2) = (-ib + a)(-b + a)
$$
* These are operators and they don't commute, so this doesn't work
* Consider:
$$
    a_{\pm} = \frac{1}{\sqrt{2\hbar m\omega}}(\mp ip + m\omega x)
$$
* The prefactor is chosen to make things neater later on
$$
    a_{+}a_{-} = \Big(\frac{1}{\hbar\omega}H - \frac{1}{2} \Big)
$$
$$
    a_{-}a_{+} = \Big(\frac{1}{\hbar\omega}H + \frac{1}{2} \Big)
$$
* *full derivation on page 27*
$$
    H = \hbar\omega (a_{+}a_{-} + \tfrac{1}{2})
$$
$$
    H = \hbar\omega (a_{-}a_{+} - \tfrac{1}{2})
$$
* Hamiltonian does not quite factor properly and we have
$$
    \hbar\omega (a_{\pm}a_{\mp} \pm \tfrac{1}{2})\Psi = E\Psi
$$
* Suppose could find soln $\Psi_n$, with associated energy, $E_n$
    * operate on this with $a_+$ for $a_{+}\Psi_n$ which is also a soln
$$
    H(a_{+}\Psi_n) = \hbar\omega (a_{+}a_{-} + \tfrac{1}{2})a_{+}\Psi_n
$$
$$
    H(a_{+}\Psi_{n}) = (E_n + \hbar\omega)a_{+}\Psi_n
$$
* If $\Psi_n$ satisfies Schrodinger with energy, $E_n$, then $a_{+}\Psi_n$ satisfies it with energy, $E_n + \hbar \omega$
    * This works similary with $a_{-}$
* Need one energy to get started and find the rest of them with this method
    * must be a bottom rung
$$
    a_{-}\Psi_{0} = 0 \\
    \frac{1}{\sqrt{2\hbar m\omega}}(\hbar\frac{d}{dx} + m\omega x)\Psi_0 = 0
$$
$$
    \frac{d\Psi_0}{dx} = -\frac{m\omega}{\hbar}x\Psi_0
$$
$$
    \Psi_0 = Ne^{-\tfrac{m\omega x^2}{2\hbar}}
$$
$$
    \Psi_{0}(x) = \Big(\frac{m\omega}{\pi\hbar} \Big)^{\tfrac{1}{4}} e^{-\tfrac{m\omega x^2}{2\hbar}}
$$
* This solution is the Gaussin wavefn used in the first few sections
    * $a = \frac{m\omega}{\hbar}$
    * associated energy is easy to find from $H\Psi = \hbar\omega(a_{+}a_{-} + \tfrac{1}{2})\Psi = E\Psi$
$$
    a_{-}\Psi_{0} = 0
$$
$$
    \frac{1}{2}\hbar\omega\Psi_0 = E_{0}\Psi_{0}
$$
$$
    \therefore E_0 = \frac{\hbar\omega}{2}
$$
* Call this state $n = 0$, then all other states follow:
$$
    \Psi_n = A_{n}a_{+}^{n}\Psi_{0}
$$
$$
    E_n = (n + \tfrac{1}{2})\hbar\omega
$$
* $n = 0$ is the ground state for SHO

###### Brute Force Solution
* lots of maths - see page 28
* Can be solved using the Frobenius/Power series technique
* Polynomial solns known as Hermite polynomials $H_{n}(\zeta)$
    * n denotes order of polynomial
    * will get lots of other terms involved
$$
    H_{n + 2}(\zeta) - 2\zeta H_{n + 1}(\zeta) + 2(n + 1)H_{n}(\zeta) = 0
$$
* Above eqn fixes this
* Swap between even and odd fns as you go up in n

##### Properties of Harmonic Potential
* Wavefns for ISW, FSW, and SHO have similar properties
$$
    E_n = (n + \tfrac{1}{2})\hbar\omega
$$
* Runs from n = 0
* System has zero point energy which is non-zero
    * due to Heisenberg uncertainty
    * can't sit motionless at the bottom of well as then psn and momentum are both known
    * ground state of system must satisfy Heisenberg
    * implies energy is greater than the minimum of the pot well


#### 8. The 3-D Schrodinger Equation
* page 30

$$
    i\hbar\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\Big(\frac{\partial^2 \Psi}{\partial x^2} + \frac{\partial^2 \Psi}{\partial y^2} + \frac{\partial^2 \Psi}{\partial z^2} \Big) + V(x, y, z, t)\Psi
$$
$$
    i\hbar\frac{\partial \Psi}{\partial t} -\frac{\hbar^2}{2m}\nabla^{2}\Psi(\vec{r}, t) + V(\vec{r}, t)\Psi(\vec{r}, t)
$$
$$
    -\frac{\hbar^2}{2m}\nabla^{2}\Psi_{n}(\vec{r}) + V\Psi_{n}(\vec{r}) = E_{n}\Psi_{n}(\vec{r})
$$

* This is separable over space
$$
    \Psi_n(x, y,  z) = X(x)Y(y)Z(z) \text{ if } V(x,y,z) = V_{x}(x) + V_{y}(y) + V_{z}(z)
$$
* Can separate into three equations for dimensions
$$
    -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V_{x}X(x) = E_{x}X(x)
$$
$$
    -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial y^2} + V_{y}Y(y) = E_{y}Y(y)
$$
$$
    -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial z^2} + V_{z}Z(z) = E_{z}Z(z)
$$
$$
    E_x + E_y + E_z = E
$$
* Not many useful potentials can be split up like this
    * Harmonic Osciallator can be though

##### ISW Potential
* Inside the well, we have explicit eqns as above
* Soln is just the same as 1D case in each direction
* Full wavefn and energy level:
$$
    \Psi(x,y,z) = X(x)Y(y)Z(z) = \sqrt{\frac{8}{L_{x}L_{y}L_{z}}}\sin(\frac{n_x \pi x}{L_x})\sin(\frac{n_y \pi y}{L_y})\sin(\frac{n_z \pi z}{L_z})
$$
$$
    E = E_x + E_y + E_z + \frac{\pi^2 \hbar^2}{2m} \Big(\frac{n_{x}^2}{L_{x}^2} + \frac{n_{y}^2}{L_{y}^2} + \frac{n_{z}^2}{L_{z}^2} \Big)
$$
* Things simplify a bit for a cube, see notes page 31
* Only one way to get ground state, (1, 1, 1), so it is non-degenerate
    * next energy level can be (1, 1, 2), (1, 2, 1), (2, 1, 1), so it is three-fold degenerate
    * get degeneracies because of symmetries of the potential

##### Schrodinger in Spherical Polars
* page 32
$$
    x = r\sin\theta\cos\phi
$$
$$
    y = r\sin\theta\sin\phi
$$
$$
    z = r\cos\theta
$$
* Usual shit for integration in sphericals
* Usual conversion for everything else too
$$
    \nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\Big(r^2 \frac{\partial}{\partial r} \Big) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial \theta} \Big(\sin\theta \frac{\partial}{\partial\theta} \Big) + \frac{1}{r^2 \sin^2\theta} \frac{\partial^2}{\partial \phi^2}
$$
* Solutions are called Spherical Harmonials, $Y(\theta, \phi)$
* Related to angular momentum


#### 9. Angular Momentum
* $\underline{L} = \underline{r} \times \underline{p}$
* The angular momentum operators:
$$
    \hat{L}_x = -i\hbar \Big(y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y} \Big)
$$
$$
    \hat{L}_y = -i\hbar \Big(z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z} \Big)
$$
$$
    \hat{L}_z = -i\hbar \Big(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} \Big)
$$
* Angular momentum operators are Hermitian
* Heisenberg doesn't apply across these operators, if measuring in different directions

###### Combinations
* $L_x, L_y, L_z$ do not commute
$$
    [L_x, L_y] = i\hbar L_z
$$
* Same cycle for other permutations
* Non-commutation means can't measure all components at once
* Can't know a pair of the angular momentums
* Uncertainty for this:
$$
    \sigma_{L_x}\sigma_{L_y} \geq \frac{1}{2}\Bigg| \Big\langle[L_x, L_y]\Big\rangle\Bigg| = \frac{\hbar}{2}\Bigg|\Big\langle L_z \Big \rangle \Bigg|
$$

###### Total Angular momentums
* $L^2 = L_{x}^2 + L_{y}^2 + L_{z}^2$
* $L^2$ commutes with each of the components, i.e. $[L^2, L_{i}] = 0, ~i = x,y,z$
* So can measure a single component of angular momentum alongside total magnitude of angular momentum
    * Use $L_z$ as t is the simplest
    * $L_z$ and $L^2$ commute, so they share a common set of enfns

##### Spatial Symmetry and L
* page 35
* Angular momentum is zero for any spherically symmetric wavefn
* L about the z-axis is related to angular dependence
    * oscillations between real and imaginary in x-y plane
    * $x + iy = re^{i\theta}$

#### 10. Angular Momentum and Spherical Harmonics

##### Angular momentum Operators in Spherical Polars

* Use angular momentum operators in polar form:
$$
    L_z = -i\hbar \frac{\partial}{\partial\phi}
$$
$$
    L^2 = -\hbar^2 \Big(\frac{1}{\sin\theta}\frac{\partial}{\partial \theta} \big(\sin\theta \frac{\partial}{\partial \theta} \big) + \frac{1}{\sin^2 \theta}\frac{\partial^2}{\partial \phi^2} \Big)
$$

* All of these can be obtained using the chain rule
* $L^2$ is essentially the angular part of the Laplacian
    * use this to rewrite Schrodinger
* Angular dependence of wavefn is related to angular momentum

##### Eigenfunctions of $L_z$

* Want to solve

$$
    L_z \Phi_m = m\hbar\Phi_m
$$

* for eigenvalues m and eigenfunctions $\Phi_m$

$$
    \Phi_m = \frac{1}{\sqrt{2\pi}}e^{im\phi}
$$

* The equation is satisfied for any value of m but the soln requires periodicity of $2\pi$
    * results that m must be a integer
* Eigenvalues of $L_z$ are $0, \pm n\hbar,~ n \in \mathbb{R}$
    * z-axis could be chosen in any arbitray direction then the orbital angular momentum about any axis is quantised
    * m is the magnetic quantum number in atoms
        * response to magnetic fields
* These eigenfunctions are orthonormal

$$
    \int_{0}^{2\pi} \Phi_{n}^{*} \Phi_{m} d\phi = \delta_{nm}*
$$

* Can expand any angular function:

$$
    f(\phi) = \sum c_m \Phi_m
$$

##### Eigenfunctions of $L^2$

* There is a common set of eigenfunctions for $L_z$ and $L^2$
    * Call these $Y_{lm}(\theta, \phi)$
$$
    L_z Y_{lm}(\theta, \phi) = m\hbar Y_{lm}(\theta, \phi)
$$
$$
    L^2 Y_{lm}(\theta, \phi) = l(l + 1)\hbar^2 Y_{lm}(\theta, \phi)
$$
* Set the constant to $l(l + 1)$
    * will be explained later
* $Y_{lm}$ is separable, otherwise it wouldn't share eigenfunctions with $L_z$
    $Y_{lm}(\theta, \phi) = \Theta_{lm}(\theta)\Phi_{m}(\theta)$
* derivation on page 38
    * will solve this in maths lectures

* When $m = 0$, solutions are called **Legendre polynomials**, $P_{l}(\cos\theta)$
    * l is the order of the polynomial

* For $m \neq 0$, the solutions are **associated Legendre polynomials**
    * related to the $|m|^{th}$ derivative of the $P_l$
    * page 39

* Since $P_l$ is a polynomial of degree l, then its $l + 1$ derivative vanishes
    * for a fixed value of l, we require $|m| \leq l$
    * $2l + 1$ values of m for every l
* Normalise all of this to get $\Theta_{lm}(\theta)$

$$
    \Theta_{lm} = (-1)^m \Big(\frac{2l + 1}{2} \frac{(l - m)!}{(l + m)!} \Big)^{1/2} P_{l}^{m}(\cos\theta)
$$

##### Spherical Harmonics of $Y_{lm}$

* Eigenfunctions common to $L_z$ and $L^2$ are given by:
    * with $l \geq 0$ and $-l \leq m \leq l$

$$
    Y_{lm}(\theta, \phi) = \Theta_{lm}\Phi_m = (-1)^m \Big(\frac{2l + 1}{2} \frac{(l - m)!}{(l + m)!} \Big)^{1/2} P_{l}^{m}(\cos\theta)e^{im\phi}
$$

* Convention of:

$$
    Y_{lm}^{*}(\theta, \phi )* = (-1)^m Y_{l,-m}(\theta, \phi)
$$

* page 39 for proof of values of m
* Start with this:

$$
    \langle L^2 \rangle = \langle L_{x}^2 + L_{y}^2 + L_{z}^2 \rangle = \langle L_{x}^2\rangle + \langle L_{y}^2 \rangle + \langle L_{z}^2 \rangle
$$

* Operators are all Hermitian and real and non-negative

$$
    \langle L^2 \rangle \geq \langle L_{z}^2 \rangle
$$

* Continue from there to get

$$
    l(l + 1) \geq m^2
$$

* This implies the physical limit of $|m| \leq l$
* Specifying $L_z$ means that $L_x$ and $L_y$ can't have deifned values
    * measuring them will get a quantised level, $\pm n\hbar,~~ 0 \leq n \leq l$
    * probability varies
* Can explicitly evaluate expectation values of $\langle L_x \rangle$ and $\langle L_y \rangle$
    * both turn out to be zero  
    * the probability of $\pm \hbar$ etc are equal

* page 40
* A semi-classical vector model helps understand this behaviour
    * set magnitude to $\sqrt{l(l + 1)}\hbar$
    * spherical harmonics as well
    * can deduce m from the length etc
    * dipole patterns of 'heat'

* page 41 for probability distributions
    * more interesting than the wavefunctions

$$
    P(\theta, \phi) \sin\theta d\theta d\phi = Y_{lm}^* Y_{lm} \sin\theta d\theta d\phi
$$
$$
    P(\theta, \phi) d\Omega = Y_{lm}^* Y_{lm} d\Omega
$$

* $d\Omega$ is the element of solid angle
    * $\sin\theta d\theta d\phi$
* Easier to visualise as exponents in $Y_{lm}$ cancel out
* To get $\theta$ dependence, integrate over $\phi$

$$
    P(\theta) d\theta = \int_{\phi = 0}^{2\pi} |Y_{lm}(\theta, \phi)|^2 d\phi \sin\theta d\theta
$$

#### 11. Finding the Hydrogen Wavefunction

##### Radial Equation for Spherical Potential

$$
    \frac{1}{R}\frac{\partial}{\partial r} \Big(r^2 \frac{\partial R}{\partial r} \Big) - \frac{2mr^2}{\hbar^2}(V(r) - E) = \frac{L^2 Y}{\hbar^2 Y} $$ $$
    L^2 Y = l(l + 1)\hbar^2 Y $$ $$
    \frac{1}{R}\frac{\partial}{\partial r} \Big(r^2 \frac{\partial R}{\partial r} \Big) - \frac{2mr^2}{\hbar^2}(V(r) - E) - l(l + 1) = 0
$$

* This is equation for the eigenfunctions, $R(r)$
    * depends on l but not m
    * for each l, different eigenfunctions
        * can label with index n
    * denote $R_{nl}(r)$
* page 42
    * lots of simplifications to equation
    * $rR(r) = U_{nl}$
* Radial equation:

$$
    -\frac{\hbar^2}{2m}\frac{d^2 U_{nl}}{dr^2} + \Bigg[V(r) + \frac{\hbar^2}{2m}\frac{l(l + 1)}{r^2} \Bigg]U_{nl} = EU_{nl}
$$

* Identical to 1D Schrodinger
    * normal potential replaced with effection potential in square brackets
    * extra term behaves like potential:
        * Centripetal force: $F = \frac{mv^2}{r}$
        * $F = \frac{L^2}{mr^3} ~;~ L = mvr$
        * integrate from this to get the term

##### The Hydrogen Atom

* Hydrogen atom
    * electron and proton instead of just one particle
    * replace electron mass with the reduced mass:
    * $\mu = \frac{M_p m_e}{(M_p + m_e)}$
* Use Coulomb potential

$$
    -\frac{\hbar^2}{2\mu}\frac{d^2 U_{nl}}{dr^2} + \frac{l(l + 1)\hbar^2}{2\mu r^2}U_{nl} - \frac{Ze^2}{4\pi\epsilon_{0} r}U_{nl} = EU_{nl}
$$

* Solve this for the eigenfunctions
* Multiply by spherical harmonics for total

$$
    R_{nl} \propto \rho^{l} e^{-\rho} L_{n - l - 1}^{2l + 1}(2\rho) $$ $$
    \rho = kr $$ $$
    \Psi_{nlm}(r,\theta,\phi) = R_{nl}(r)Y_{lm}(\theta,\phi) $$ $$
    E = -13.6\frac{Z^2}{n^2}\frac{\mu}{\mu_{H}}\,eV
$$

* This only depends on n
* Properties of Laguerre polynomials require $n \geq l + 1$ so $l \leq n - 1$
    * only features for $1/r$ potential
    * all have energies dep on m

* Degeneracy
    * For given n, n values of l which have same energy so the level is n degenerate
    * for each l, $2l + 1$ values of m, so in fact each level is
    * $\sum_{l = 0}^{n} (2l + 1)$ degenerate
    * $2n^2$ degenerate later on once spin is added

$$
    \rho = kr = \frac{\mu Ze^2}{2\pi\epsilon_{0}\hbar^2\rho_{0}}r = \frac{\mu Ze^2}{4\pi\epsilon_{0}\hbar^2 n}r $$ $$
    a = \frac{4\pi\epsilon_{0}\hbar^2}{\mu Ze^2}
$$

* a is the Bohr radius for hydrogen of $5.29 \times 10^{-11} \,m^{-1}$

$$
    \Psi_{nlm} \propto \Big(\frac{r}{2a} \Big)^{l}e^{-\frac{r}{an}}L_{n - l - 1}^{2l + 1} \Big(\frac{2r}{an} \Big) Y_{lm}(\theta, \phi)
$$

* Get the normalisation constant by

$$
    \int_{r = 0}^{\infty} \int_{\phi = 0}^{2\pi} \int_{\theta = 0}^{\pi} \psi^* (r,\theta,\phi)\psi(r,\theta,\phi)r^2 \sin\theta \,d\theta\, d\phi\, dr = 1 $$ $$
    E = -\frac{\mu}{2\hbar^2}\Big(\frac{Ze^2}{4\pi\epsilon_0}\Big)^2 \frac{1}{n^2}
$$

##### Transitions Between Energy Levels

* If Hydrogen is some stationary state, $\psi_{nlm}$, it should be stable, but perturbations can cause the electron to transition to another stationary state
    * collision with atom/photon/electron
    * either by absorbing energy or emitting it
    * perturbations are always present so transitions - quantum jumps - are constantly occurring
    * transitions are between discrete energy levels of n difference

$$
    E_{\gamma} = E_{i} - E_f = 13.6 \Big(\frac{1}{n_{f}^2} - \frac{1}{n_{i}^2} \Big)eV
$$

* Transitions to ground state give rise to Lyman series of emissions lines with wavelengths given by

$$
    E = \frac{hc}{\lambda} = 13.6\Big(1 - \frac{1}{n^2} \Big) eV ~;~ n \geq 2
$$

* page 45 for table of Lyman series
    * tend to a limit for shortest wavelength possible

### 12. Generalising Angular Momentum

#### Preview of Spin Concept

* Spin is the spinning of particles around own axis
    * electron doesn't have internal structure though
    * spin is _intrinsic_ angular momentum

#### Review of Angular Momentum

* Two components of $\underline{L}$ cannot be measured simultaneously
    * one component can be measured with $L^2$ however
    * Share a common set of eigenstates

#### Angular Momentum Ladder Operators

* page 47

$$
    L_{\pm} = L_x \pm iL_y $$ $$
    [L^2, L_+] = 0
$$

* same principle as other ladder operators

$$
    \hbar L_+ f_{\lambda, \mu} \implies L_z (L_+ f_{\lambda, \mu}) = (\mu + 1)\hbar L_+ f_{\lambda, \mu}
$$

##### Properties

* Must be a top and bottom rung
    * max and min values for $\mu$
    * $L_+ f_{\lambda, \mu_{max}} = 0$

* $\lambda = \mu_{max} (\mu_{max} + 1)$
    * Legendre polynomial approach
    * $\mu_{min} = -\mu_{max}$
    * this leads to the range of values for $m$

* $\mu$ can take half-integer values
    * comes from addition of intrinsic and extrinsic

#### Overview of general angular momentum, $\underline{J}$

* $\underline{J}$ is angular momentum if its operator components, $J_x, J_y, J_z$ satisfy

$$
    [J_x, J_y] = i\hbar J_z ~;~ [J_z, J_x] = i\hbar J_y $$ $$
    J^2 = J_{x}^2 + J_{y}^2 + J_{z}^2 $$ $$
    [J^2, J_x] = 0
$$

* Common eigenfunctions of $J^2$ and $J_z$
    * eigenvalues of $j(j + 1)\hbar^2$ and $m_j \hbar$ respectively

* Ladder operators
    * $J_zJ_{+}f_{j,m_j} = (m_j + 1)\hbar J_+ f_{j,m_j}$

* Can't go on forever so top and bottom values for $m$
    * $m_{max} - m_{min} \in \mathbb{N}$
    * $j = \frac{\mathbb{N}}{2}$

* page 49

$$
    \underline{J} = \underline{L} + \underline{S}
$$

### 13. Spin

* $\underline{S}$ as angular momentum spin operator
    * $S^2$ eigenvalues, $s(s + 1)\hbar^2$
    * do not have spherical harmonic eigenfunctions
    * eigenstates not functions of spatial coordinates

* intrinsic property of particle

#### Electron Orbiting Magnetic Field

$$
    \mu_l = IA = -\frac{evr}{2} = -\frac{e}{2m_e}m_e vr = -\frac{e}{2m_e}L $$ $$
    \underline{\mu}_l = -\frac{e}{2m_e}\underline{L} = -\frac{\mu_B}{\hbar}\underline{L} $$ $$
    \mu_B = \frac{e\hbar}{2m_e}
$$

* $\mu_B$ is the Bohr magneton, natural unit of microscopic magnetic moment
    * $= 9.27 \times 10^{-24} J\,T^{-1}$
    * $= 5.79 \times 10^{-5} eV \, T^{-1}$

* $-\frac{\mu_B}{\hbar}\underline{L}$ is quantum mechanical magnetic moment
    * $(\mu_l)_{z} = -\frac{\mu_{B}}{\hbar}\underline{L}_z$
* For a hydrogen atom,
    * $(\mu_l)_{z} = -m_{l}\mu_B,~ -l \leq m_l \leq +l, \in \mathbb{N}$

#### Dirac Notation

$$
    |\chi_+ \rangle \to \begin{pmatrix} 1 \\ 0 \end{pmatrix} ~;~ |\chi_- \rangle \to \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$ $$
    \langle \chi_+ | \to \begin{pmatrix} 1 & 0 \end{pmatrix} ~;~ \langle \chi_- | \to \begin{pmatrix} 0 & 1 \end{pmatrix}
$$

* kets are equivalent ti column vectors
* bras to row vectors
* operators to square matrices

* taking complex conjugate of inner product can be seen as taking Hermitian conjugate of three matrices:
    * $(ABC)^{\dagger} = C^\dagger B^\dagger A^\dagger$
    * $\langle \psi_n | A | \psi_m \rangle* = \langle \psi_m | A^\dagger | \psi_n \rangle$
    * $\langle \psi_n | A | \psi_m \rangle* = \langle \psi_m | A | \psi_n \rangle$, if A is Hermitian

* Bra-Ket inner products were introduced earlier as shorthand for integrals
    * more general than this for when there are no spatial coordinates to integrate over
        * i.e. spin

### 14. Time-dependent Perturbation Theory

#### Small Modification to Hamiltonian

* Solved time-dependent Schrodinger for some Hamiltonian, $H^0$
    * Get eigenfunctions, $\psi_{n}^0$ for each energy level
    * $H^0 \psi_{n}^0 = E_{n}^0 \psi_{n}^0$
    * orthonormal

* Perturb the system slightly
    * a small bump in the square well
    * want to find eigenfunctions and eigenvalues for new Hamiltonian
    * can't solve this exactly but can use _perturbation theory_ for approx solution
        * build on known solutions of unperturbed system

* Write new Hamiltonian as
    * $H = H^0 + \lambda H'$
        * H' is the perturbation

#### Power expansion

* Want to write $E_n$ and $\psi_n$ as power series in $\lambda$

$$
    E_n = E_{n}^0 + \lambda E_{n}^1 + \lambda^2 E_{n}^2 + \cdots $$ $$
    \psi_n = \psi_{n}^0 + \lambda \psi_{n}^1 + \lambda^2 \psi_{n}^2 + \cdots
$$  

* $E_{n}^1$ and $\psi_{n}^1$ refer to the first order corrections for the nth eigenfunctions
    * superscript 2 is second order correction etc

$$
    H\psi_n = E_{n}\psi_n $$ $$
    (H = H^0 + \lambda H')(\psi_{0} + \lambda \psi_{n}^1 + \lambda^2 \psi_{n}^2 + \cdots) = ( E_{n}^0 + \lambda E_{n}^1 + \lambda^2 E_{n}^2 + \cdots)(\psi_0 + \lambda \psi_{n}^1 + \lambda^2 \psi_{n}^2 + \cdots)
$$

* collect powers of lamba together

$$
    H^0\psi_0 + \lambda(H^0\psi_{n}^1 + H'\psi_{n}^0) + \lambda^2 (H^0 \psi_{n}^2 + H'\psi_{n}^1) + \cdots = E_{n}^0\psi_{n}^0 + \lambda(E_{n}^0\psi_{n}^1 + E_{n}^1\psi_{n}^0) + \lambda^2(E_{n}^0\psi_{n}^2 + E_{n}^1\psi_{n}^1 + E_{n}^2\psi_{n}^0) + \cdots
$$

#### First Order correction

* Zeroth order expansion is just no perturbation

* Look at first order in $\lambda$:

$$
    H^0\psi_{n}^1 + H'\psi_{n}^0 = E_{n}^0\psi_{n}^1 + E_{n}^1\psi_{n}^0
$$

* Take an inner product with $\psi_{n}^0$  
    * use Dirac notation for maximum generality
    * some terms from this will cancel so:

$$
    E_{n}^1 = \langle \psi_{n}^1 | H' | \psi_{n}^0 \rangle
$$

* Expressing this with integrals instead yields the same result:

$$
    E_{n}^1 = \int (\psi_{n}^0)^* H' \psi_{n}^0 \,dx
$$

* Either way, the first order correction to an energy eigenvalues is the **expectation value** of the perturbation using the unperturbed eigenfunctions

#### 1D Square Well with Delta Function

* With Kronacker delta, $\delta_{nm} = 1$ if $n = m$, or 0 otherwise
    * The **Dirac Delta** is the contiuum version:

$$
    \int f(x)\delta(x - x_0) \,dx = f(x_0)
$$

* collapses any integral to the point marked out by the function   
    * $\int \delta(x - x_0)\,dx = 1$
* So if we have $H' = \lambda\delta(x - \frac{a}{2})$ then

$$
    E_{n}^1 = \int \int (\psi_{n}^0)^* H' \psi_{n}^0 \,dx $$ $$
    E_{n}^1 = \frac{2}{a}\int_{0}^{a} \sin\Big(\frac{n\pi x}{a}\Big)\lambda\delta(x - \frac{a}{2})\sin\Big(\frac{n\pi x}{a}\Big)\,dx = \frac{2\lambda}{a}\sin^2 \Big(\frac{n\pi}{2}\Big)
$$

* This is 0 if n is even
    * no correction to even $E_{n}^0$
    * but $E_{n}^1 = \frac{2\lambda}{a}$ for odd n
    * perturbation has no effect for even n
    * odd n gets a peak and energies are shifted

#### First Order Correction to Wavefunction

* Calc by writing $\psi_{n}^1 = \sum_{n \neq 1} c_{nl}\psi_{l}^0$
    * substitute this into the first order correction
    * take inner product with $\psi_{l}^0$

$$
    c_{nl} = -\frac{\langle \psi_{l}^0 | H' | \psi_{n}^0 \rangle}{(E_{n}^0 - E_{l}^0)}
$$

* To first order, $\psi_n \approx \psi_{n}^0 + \lambda\psi_{n}^1$
