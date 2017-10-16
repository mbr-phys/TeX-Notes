#### Foundations A
##### Quantum Mechanics
###### Shaun Cole
---
##### 1. Basics of QM

Useless so just read notes
* Particles described by wave functions, psi
* $P(x) dx = \psi^2 dx = \psi^* \psi \, dx$
    * $ \int_{-\infty}^{\infty} = 1 $
---

##### 2. Operators and Expectation Values

* Expectation value is average value
    * $< x > = \int_{-\infty}^{\infty} xP(x) dx$
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

---

##### 3. The Origin Of Uncertainty
* Page 10
* Complex conjugate operators of position, momemtum, etc operate on the function immediately to the right
* Hermitian -- the complex conjugate of the integral for the expectation value is equivalent
    * Swapping positions of variables and taking cplx conjugate
* Any dynamical quantity can be an operator
* Expectation value only real if it is Hermitian
* Can use Hermitian to show uncertainty principle
    * try finding $<xp>$
    * will not got $= <xp>* $
* $\hat{x}\hat{p} \neq \hat{p}\hat{x}$
    * they do not commute
* Page 11
* Square bracket notation for commutator
    * $[\hat{a},\hat{b}] = \hat{a}\hat{b} - \hat{b}\hat{a}$
* The x and p operators don't commute so aren't real and can't be measured
    * can be a test for other operators too to find relations for uncertainty
    * the difference between the two double commutators for x and p is ihbar which is where the hbar/2 comes from for uncertainty
* Use a Gaussian function and find EVs for < x >, < p >, < $x^2$ >, < $p^2$ > to get minimum Heisenberg values
* Ehrenfest's Theorem fulfils Newton's second law with EVs

##### 4. Schrodinger Equation and Eigenfunctions
* page 14
* $ln T = \frac{E}{i\hbar}t + K$
* $T = e^{-it\frac{E}{\hbar}}$
* Can covert from time-dep to time-indep if $V = V(x)$, separable fns
* Kronacker delta fn from Maths
    * for distinct eigenfns and orthogonality
* Bra-ket notation for eigen stuff
    * < | for cplx conjugate
    * | > for normal
    * < | > = int
* Eigenfns of the Hamiltonian are stationary
