---
title: "Theoretical Physics"
author: "Dr Eke"
date: "Michaelmas 2017"
---

# Classical Mechanics

## Lecture 1
* DoF
* Constraints

## Lecture 2
* Differential Formulation of Lagrangian Mechanics

### Generalised Coordinates
* Page 6
* Only need as many coordinates $q_k$ as there are DoFs ($N = 3M - j$)
* Generalised velocities are $\frac{d q_k}{dt}$
* Regard $q_k$ and $\dot{q}_k$ as independent variables
    * $\frac{\partial q_k}{\partial \dot{q}_k} = \frac{\partial \dot{q}_k}{\partial q_k} = 0$

### Lagrangian
* Page 7
* Assume:
    1. Holonomic constraints
    2. Constraining forces do no work
    3. Applied forces are conservative, such that a scalar potential energy function exists
        * Potential function may change with time
* Generalised Coordinates don't necessarily have to be in metres - Force is not in Newtons, it is $\frac{\partial W}{\partial q_k}$


## Lecture 3
* Ignorable coords
    * if it doesn't appear in the Lagrangian, it can be ignored
    * Canonically conjugate momentum to the coord
        * $p_k = \frac{\partial L}{\partial \dot{q}_k}$
    * simplifies eqn of motion
    * example:
        * $L = \frac{1}{2}m\dot{x}^2 \implies p = \frac{\partial L}{\partial \dot{q}_k} = m\dot{x}~$ is constant
* E.g. Ladder sliding down a wall
    * A ladder of length 2a and uniform mass/length = $\lambda$ leans against a wall. It is initially stationaryy before sliding down the wall without friction. Find $\ddot{\theta}$ where $\theta$ is the ladder's angle to the horizontal, while it remains in contact with the wall.
    * We need to define the Lagrangian in terms of the one generalised coord, $\theta$
    * Define s as the distance along the ladder from the end in contact with the floor. Then $dm(s) = \lambda\,ds$. Also, we can write $\underline{r}(s) = -2a\cos{\theta} + s\cos{\theta} = [(s - 2a)\cos{\theta}, \sin{\theta}]$
    * Differentiating wrt time: $\underline{\dot{r}}(s) = [-(s-2a)\dot{\theta}\sin{\theta},s\dot{\theta}\cos{\theta}]$
    * $\therefore \underline{\dot{r}}^{2}(s) = \dot{\theta}^2 [s^2 + (4a^2 - 4as)\sin^{2}{\theta}]$
    * Combining this into T gives:


$$
    T = \int_{0}^{2a} \frac{1}{2}\underline{\dot{r}}^{2}(s)\,dm(s)
$$
$$
    T = \int_{0}^{2a} \frac{\lambda \dot{\theta}^2}{2}[s^2 + (4a^2 - 4as)\sin^{2}{\theta}] \, ds
$$
$$
    T = \frac{\lambda \dot{\theta}^2}{2} [\frac{s^3}{3} + \sin^{2}{\theta} (4a^{2}s - 2as^2)]_{0}^{2a_{}}
$$
$$
    T = \frac{4\lambda\dot{\theta}^{2}a_{1}^{3}}{3}
$$
$$
    V = (\lambda 2a)g(a\sin{\theta}) \implies
$$
$$
    L =  \frac{4\lambda\dot{\theta}^{2}a^{3}}{3} - \lambda 2a^{2}g\sin{\theta} = 2\lambda a^{2}(\frac{2a\dot{\theta}^2}{3} - g\sin{\theta})
$$
    E-L:
$$
    \frac{d}{dt}(\frac{\partial L}{\partial \dot{\theta}}) - \frac{\partial L}{\partial \theta} = 0
$$
$$
    \frac{d}{dt} (\frac{4a\dot{\theta}}{3}) + g\cos\theta = 0
$$
$$
    \therefore \ddot{\theta} = -\frac{3g}{4a}\cos\theta
$$

#### An example of an integral principle: Fermat's Principle
* _A light ray takes the quickest available path between two points_
* Consider a boundary between two materials
    * Refractive indices of n1 and n2
    * Going from A in n1 to B in n2
    * Travelling x1 in A and x2 in B
    * Distance l between A and B in y dirn
    * travels distnce y in A, so $l - y$ in B
    * paths of s1 and s2 in A and B
    * $\theta_1$ and $\theta_2$ are angles from sn to xn

$$
    T = \int_{A}^{B} dt = \int_{A}^{B} \underline{ds} $$ $$
    T = \frac{1}{c} \int_{A}^{B} n\,ds $$ $$
    cT = n_1 s_1 + n_2 s_2 $$ $$
    s_1 = \sqrt{x_{1}^{2} + y^2} $$ $$
    s_2 = \sqrt{x_{2}^{2} + (l - y)^2} $$ $$
    cT = n_{1}\sqrt{x_{1}^{2} + y^2} + n_{2}\sqrt{x_{2}^{2} + (l - y)^2} $$ $$
    \frac{dT}{dy} = 0 \implies $$ $$
    \frac{n_1 y}{\sqrt{x_{1}^{2} + y^2}} - \frac{n_2 (l - y)}{\sqrt{x_{2}^{2} + (l - y)^2}} = 0 $$ $$
    n_{1}\sin\theta_1 - n_{2}\sin\theta_2 = 0 ~~~\text{i.e. Snell's Law}
$$

### Variational Calculus
* $I[y] = \int_{x_1}^{x_2} f(y,y',x)\,dx$
    * I is a functional
    * for a whole path
    * solution will be in form of E-L
* For any perturbation we make to the path, the value of the functional wil not change
    * like how looking for dy/dx = 0
    * essentially same but extra dimension
* $\epsilon$ is small number, constant, and independent of x
    * how far away from x
* $\eta$ tells us above or below x
    * $\eta(x_1) = \eta(x_2) = 0$
* $(\frac{dI}{d\epsilon})_{\epsilon = 0_{}}$
* For $\frac{\partial f}{\partial x} = 0$:

$$
    \frac{df}{dx} = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial y}\frac{dy}{dx} + \frac{\partial f}{\partial y'}\frac{dy'}{dx} $$ $$
    \frac{d}{dx}(f - y'\frac{\partial f}{\partial y'}) = 0
$$

* **Alternate form of E-L which can be useful**


## Lecture 4

### Hamilton's Principle

$$
    S[\underline{q}(t)] = \int_{t_1}^{t_2} L(\underline{q}(t), \dot{q}(t), t)\,dt $$ $$
    \frac{\delta L}{\delta q} \equiv \frac{\partial L}{\partial q} - \frac{d}{dt}(\frac{\partial L}{\partial \dot{q}})
$$

### Brachistochrome

* What is the quickest route for mass m to fall under gravity from A to B?
    * assuming no friction
* Conservation of energy to start with for speed:

$$
    \frac{1}{2}mv^2 + mgy = 0 $$ $$
    \implies v = \sqrt{-2gy} $$ $$  
$$

* Total time taken:

$$
    t = \int_{A}^{B} \frac{ds}{v} ~;~ (ds)^2 = (dx)^2 + (dy)^2 $$ $$
    ds = \sqrt{1 + (\frac{dy}{dx})^2} \cdot dx $$ $$
    \implies t = \int_{x_{A}}^{x_{B}} \frac{\sqrt{1 + y'^{2}} \cdot dx}{\sqrt{-2gy}}
$$

* Calculus of Variations problem
    * $f = \sqrt{\frac{1 + y'^2}{-2gy}}$
    * no explicit dependence on x
        * from eq. 9 on notes, we get
        $f - y'\frac{\partial f}{\partial y'} = c$

$$
    \sqrt{\frac{1 + y'^2}{-2gy}} - \frac{y' \cdot y'}{\sqrt{-2gy(1 + y'^2)}} = c $$ $$
    \frac{1}{\sqrt{-2gy(1 + y'^2)}} = c $$ $$
    y(1 + y'^2) = A $$ $$
    \frac{dy}{dx} = \sqrt{\frac{A - y}{y}} $$ $$
    \int \sqrt{\frac{y}{A - y}} \cdot dy = \int dx = x
$$

* Try substitution:
    * $y = \frac{A}{2}(1 - \cos\theta) = A\sin^{2}(\frac{\theta}{2})$
    * from $1 - \cos\theta = 2\sin^{2}(\frac{\theta}{2})$

$$
    dy = A\sin\frac{\theta}{2}\cos\frac{\theta}{2} $$ $$
    x = \int \sqrt{\frac{A\sin^{2}\frac{\theta}{2}}{A\cos^{2}\frac{\theta}{2}}} \cdot A\sin\frac{\theta}{2}\cos\frac{\theta}{2}\,d\theta $$ $$
    x = A\int \frac{1}{2}(1 - \cos\theta)\,d\theta = \frac{A}{2}(\theta - \sin\theta) + B $$ $$
    x_A = y_A = 0 ~;~ \theta = 0 ~;~ \theta = 0 \therefore $$ $$
    x = \frac{A}{2}(\theta - \sin\theta) $$ $$
    y = \frac{A}{2}(1 - \cos\theta)
$$

* x and y final solns give a cycloid
* see on DUO for python code for showing particle motion

### Lagrange Multiplier

* If you have a constraint, and want to eliminate number of variables to solve, use Lagrange Multipliers
* Consider a pendulum of length, l
    * The natural coordinate to choose is $\theta$
    * If you want to use x and y then,

$$
    \delta S = \int \Bigg[\frac{\delta L}{\delta x}\cdot \delta x + \frac{\delta L}{\delta y}\cdot \delta y \Bigg]dt
$$

* Hamilton's principle says $\delta S = 0$ but non-independence of x and y means can't say each variational deriv is zero
* Use $\lambda$ as an arbitrary Lagrange multiplier

$$
    \delta S = \int \Bigg[\Big(\frac{\delta L}{\delta x} - \lambda\frac{\partial G}{\partial x} \Big)\delta x + \Big(\frac{\delta L}{\delta y} - \lambda\frac{\partial G}{\partial y} \Big)\delta y \Bigg]dt $$ $$
    \delta(F - \lambda G) = 0
$$

### Linear Oscillators

* Mech system is at equilibrium at rest
* This occurs at points in space where all forces, $F_k$ vanish
* For conservative systems, this is when the potential energy is stationary
    * its first derivs wrt to $q_k$ vanish
* Near Static Equilibrium
    * define equilibrium psn and velocity as zero
    * $\frac{\delta V}{\delta q} = 0$ at equilibrium point
    * expand out and only go up to quadratic terms as near equilibrium
    * Sub into E-L eqn:

$$
    L = \frac{m}{2}\Big(\dot{q}^2 + \frac{D}{F}q^2 \Big)
$$

* Normal EoM for particle
* SHO:
    * equilibrium psn is minimum of pot energy
    * close to equilibrium, we have SHM
    * $\omega = \sqrt{-\frac{D}{F}}$
    * if $\frac{D}{F} > 0$, it is unstable
    * $\ddot{q} + \omega^2 q = 0$ is linear, homegeneous diff eqn

$$
    q(t) = q(0)\cos(\omega t) + \frac{\dot{q}(0)}{\omega}\sin(\omega t)
$$

* Damping force
    * frictional force to suppress motion
    * opposes motion and vanishes when motion ceases
    * $F_d = -\gamma\dot{q} = -(\frac{m\omega}{Q})\dot{q}$
    * Q is dimensionless quality factor
    * higher quality system leads to small Q and motion lasts longer

### Damped Oscillators

* For Damped SHO, E-L:

$$
    \frac{d}{dt}\Big(\frac{\partial L}{\partial \dot{q}}\Big) - \frac{\partial L}{\partial q} = F_d $$ $$
    \ddot{q} + \frac{\omega}{Q}\dot{q} + \omega^2 q = 0 $$ $$
    q = e^{\lambda t} \implies \lambda^2 + \frac{\omega}{Q}\lambda + \omega^2 = 0 $$ $$
    \lambda = -\frac{\omega}{2Q} \pm \sqrt{(\frac{\omega}{2Q})^2 - \omega^2} $$ $$
    \lambda = -\frac{\omega}{2Q} + \underbrace{\frac{\omega}{2Q}\sqrt{1 - 4Q^2}}_{\omega '}
$$

* The sqrt becomes positive, zero, or negative depending on Q
* Overdamped: $Q < \frac{1}{2} \implies \sqrt{} \in \mathbb{R}$
    * Increasing Q but keeping it under $\frac{1}{2}$ makes it tend to equilibrium faster

$$
    q(t) = e^{-\frac{\omega t}{2Q}}(A\cosh(\omega 't) + B\sinh(\omega 't)) $$ $$
    \dot{q}(t) = e^{-\frac{\omega t}{2Q}}(A\omega '\cosh(\omega 't) + B\omega '\sinh(\omega 't))\cdot -\frac{\omega}{2Q}q $$ $$
    \dot{q}(0) = B\omega ' - \frac{\omega}{2Q}q(0) $$ $$
    B = \frac{1}{\omega '}(\dot{q}(0) + \frac{\omega}{2Q}q(0)) $$ $$
    q(0) = A
$$


## Lecture 5

### Damped Oscillators Ctd

* Critically Damped: $Q = \frac{1}{2} \implies$ 2 equal roots for $\lambda = -\frac{omega}{2Q}$
    * Fastest return to equilibrium without overshooting

$$
    q(t) = e^{-\frac{\omega t}{2Q}}(\underbrace{A}_{q(0)} + \underbrace{B}_{\dot{q}(0) + \frac{\omega}{2Q}q(0)}t) $$ $$
$$

* Underdamped: $Q > \frac{1}{2} \implies \lambda = -\frac{\omega}{2Q} \pm i\omega ' ~;~ \omega = \frac{\omega}{2Q}\sqrt{4Q^2 - 1}$
    * Solution is like overdamped case but with cosh replaced by cos and sinh replaced by sin
    * Sin/cos oscillation with exponential decay envelope
    * Larger quality factor, Q, implies slower decay, and more oscillations

### Driven Oscillators

#### Oscillators Driven by an External Force

* Consider an undamped oscillator, driven by time dep external force, F(t)
* Driving force is not part of the system
    * do not consider force back on driver by system

$$
    L = \underbrace{\frac{m\dot{q}^2}{2}}_{T} - \underbrace{\Bigg[\frac{m\omega^{2}q^2}{2} - F(t)q \Bigg]}_{V}
$$
$$
    \ddot{q} + \omega^2 q = \frac{F(t)}{m}
$$

* Yield a second order linear, inhomogeneous differential eqn
* Split into infinite number of impulsive forces and sum up displacements caused by each
* Method is analagous to Poisson's eqn in electrostatics
    * $\nabla^{2}\Phi(x) = -\frac{\rho(r)}{\epsilon}$

### Dirac delta-fn

* Zero-width limit of a function/distribution of t, sharply peaked at $t = t'$
* If t has dimension of time, $\delta$ has dimension of inverse time, i.e. frequency

$$
    f(t') = \int_{-\infty}^{\infty} \delta(t - t')f(t)\,dt
$$

* Use this to find impulsive force at time t' as $F(t) = K\delta(t - t')$

#### Response of oscillator to an indep impulsive force

$$
    \int_{t' - \epsilon}^{t + \epsilon} (\ddot{q} + \omega^{2}q)dt $$ $$
    \implies \dot{q}(t' + \epsilon) - \dot{q}(t' - \epsilon) + \underbrace{\omega^{2} \int_{t' - \epsilon}^{t + \epsilon} q(t)dt}_{\to 0 \text{ as } \epsilon \to 0, \text{ unless } q(t') \to \infty} = \frac{K}{m}
$$

* Instantaneous change in velocity of $\frac{K}{m}$ from this force but no change in psn as no change in time

#### Evolution of SHO

1. $t < t'$ - normal SHO motion
2. $t = t'$ - Instantaneous jump in velocity as above
3. $t > t'$ - no more driving force, back to SHO

$$
    q(t) = q(t')\cos(\omega[t - t']) + \frac{\dot{q}(t') + \tfrac{K}{m}}{\omega}\sin(\omega[t - t'])
$$

### Green's Function

* Solution to differential equation:

$$
    \ddot{G}(t - t') + \omega^{2}G(t - t') = \delta(t - t') $$ $$
    G(t - t') = \frac{1}{\omega}\sin(\omega[t - t']),~ t \geq t'
$$

* Using defn of $\delta$-fn, the eqn of motion for driven oscillator can be written as

$$
    \ddot{q} + \omega^{2}q = \frac{1}{m}\int_{-\infty}^{\infty} dt'\,F(t')\delta(t - t')
$$

* Just splitting up driving force into infinite number of impulsive forces
* eliminate $\delta$-fn by using Green's fn

$$
    \ddot{q} + \omega^{2}q = \frac{1}{m}\int_{-\infty}^{\infty} dt'\,F(t')[\ddot{G}(t - t') + \omega^{2}G(t - t')] $$ $$
    q(t) = \frac{1}{m\omega} \int_{-\infty}^{t} F(t')G(t - t')dt' = \frac{1}{m\omega} \int_{-\infty}^{t} F(t')\sin(\omega[t - t'])dt'
$$

#### Example

* Consider driving force of the form
    * $F(t) = F_{0}\sin(\omega_{0}t)$ for $t > 0$
    * $F(t) = 0$ for $t \leq 0$

$$
    q(t) = \frac{F_0}{m\omega}\int_{0}^{t} dt' \sin(\omega_{0}t')\sin(\omega(t - t'))
$$

* Use $\sin A \sin B = \frac{1}{2} [\cos(A - B) - \cos(A + B)]$

$$
    q(t) = \frac{F_0}{m\omega}\int_{0}^{t} \frac{1}{2}\Big[\cos[t'(\omega_{0} + \omega) - \omega t] - \cos[t'(\omega_{0} - \omega) + \omega t] \Big]dt
$$

* For $\omega_{0} \neq \omega$, one observes oscillating behaviour with

$$
    q(t) = \frac{F_0}{m\omega}\Big[\frac{\sin(\omega_{0}t) + \sin(\omega t)}{2(\omega_{0} + \omega)} - \frac{\sin(\omega_{0}t) - \sin(\omega t)}{2(\omega_{0} - \omega)} \Big]
$$

* In resonance, (when $\omega_{0} = \omega$), q(t) grows without limit

$$
    q(t) = \frac{F_0}{m\omega}\Big[\underbrace{\frac{\sin(\omega t)}{2\omega}}_{\text{oscillates}} - \underbrace{\frac{t\cos(\omega t)}{2}}_{\text{grows}} \Big]
$$

* If we consider an underdamped SHO subject to the same driving force as above, then EoM can be solved to give

$$
    q(t) = q_{s}(t) + q_{t}(t)
$$

* Solution is split into the steady-state solution, $q_{s}$, and the transient solution, $q_{t}$.
    * In this case, the Green's function for the damped oscillator is

$$
    G(t - t') = \frac{e^{-\hat{\omega}(t - t')}}{\omega'}\sin[\omega'(t - t')], ~~ t \geq t' $$ $$
    w' = \hat{\omega}\sqrt{4Q^2 - 1} ~;~ \hat{\omega} = \frac{\omega}{2Q}
$$


## Lecture 6

#### Recap

* Green's function
    * response of an oscillator to an impulsive force
* Split force up into lots of tiny impulsive forces

$$
    q(t) = \frac{1}{m\omega} \int_{-\infty}^{t} F(t')G(t - t')dt'
$$

### Underdamped Driven Oscillator Ctd

* Displacement at time, t:

$$
    q(t) = \frac{1}{m} \int_{-\infty}^{t} F_0 \sin(\omega_{0}t')\frac{e^{-\hat{\omega}(t - t')}}{\omega'}\sin[\omega'(t - t')]dt'
$$

* To solve this, just write sins as $\sin x = \frac{1}{2i}(e^{ix} - e^{-ix})$ and integrate

* The steady-state soln is:

$$
    q_{s}(t) = \frac{F_0}{2m\omega'} \Bigg\{\Big[\frac{\hat{\omega}}{\hat{\omega}^2 + (\omega_{0} + \omega')^2} - \frac{\hat{\omega}}{\hat{\omega}^2 + (\omega_{0} - \omega')^2} \Big]\cos(\omega_{0}t)
$$

$$  
    + \Big[\frac{\omega_{0} + \omega'}{\hat{\omega}^2 + (\omega_{0} +   \omega')^2} - \frac{\omega_{0} - \omega'}{\hat{\omega}^2 + (\omega_{0} - \omega')^2} \Big]\sin(\omega_{0}t) \Bigg\}
$$

* The transient state is:

$$
    q_{t}(t) = \frac{F_0 e^{-\hat{\omega}t}}{2m\omega'} \Bigg\{ \Big[\frac{\omega_{0} + \omega'}{\hat{\omega}^2 + (\omega_{0} + \omega')^2} + \frac{\omega_{0} + \omega'}{\hat{\omega}^2 - (\omega_{0} - \omega')^2} \Big]\sin(\omega't)
$$
$$
    - \Big[\frac{\hat{\omega}}{\hat{\omega}^2 + (\omega_{0} + \omega')^2} - \frac{\hat{\omega}}{\hat{\omega}^2 + (\omega_{0} - \omega')^2} \Big]\cos(\omega't) \Bigg\} $$ $$
    q(t) = q_{s}(t) + q_{t}(t)
$$

* The transient soln oscillates with the intrinsic oscillator frequency, $\omega'$, but dies away with time
* The steady-state soln oscillates with driving frequency, and remains at large t
* After the transient has died away, the dynamical behaviour is like that of SHO, but at the driving frequency
* Note that there is no singularity at resonance
    * The effect of resonance has been softened by the presence of damping

### Coupled Small Oscillations

* look at page 20 of notes
* Consider system with two pendulums of length, l, connected half way down with a spring
* Use $\theta$s as generalised coords
* Use Taylor expansion of cos up to deg 2 to get potential expression

$$
    T = \frac{ml^2}{2}(\dot{\theta}_{1}^{2} + \dot{\theta}_{2}^{2}) $$ $$
    V = \frac{mgl}{2}(\theta_{1}^2 + \theta_{2}^2) $$ $$
    V_{coupling} = \frac{k}{2}\Big(\frac{l}{2}\Big)^2 (\theta_2 - \theta_1)^2 $$ $$
    L = \frac{ml^2}{2}(\dot{\theta}_{1}^{2} + \dot{\theta}_{2}^{2}) - \frac{1}{2}\Bigg(mgl(\theta_{1}^2 + \theta_{2}^2) + k\Big(\frac{l}{2}\Big)^2 (\theta_2 - \theta_1)^2 \Bigg)
$$

* $\theta_1 \theta_2$ makes things awkward, so transform to centre of mass, $\theta_c = \frac{\theta_1 + \theta_2}{2}$ and relative, $\theta_r = \theta_2 - \theta_1$
* Also define $\omega_0 = \sqrt{\frac{g}{l}}$ and constant, $\eta = \frac{kl}{4mg}$

$$
    L = ml^2 \Bigg[(\dot{\theta}_{c}^2 - \omega_{0}^2\theta_{c}^2) + \frac{1}{4}(\dot{\theta}_{r}^2 - \omega_{0}^2 \Big(1 + 2\eta)\theta_{r}^2\Big) \Bigg] $$ $$
    \ddot{\theta}_{c} + \omega_{c}^2 \theta_{c} = 0 $$ $$
    \ddot{\theta}_{r} + \omega_{0}^2 (1 + 2\eta)\theta_r = 0
$$

* $\eta$ is essentially the relative strengths of the spring force to gravity
* Total motion is linear combination of two EoMs above

### General Method

* N coupled oscillators gives N generalised coords, yiedling N homegeneous eqns
* If undergoing SHM, *normal coordinates*

1. Find equilibrium config, values of generalised coords where generalised forces are 0
2. Taylor expand Lagrangain to second order in generalised coords, around values for the generalised coords given by equilibrium config
3. For N DoF, the Taylor expansion must in principal be in 2N variables
    * In practice, fewer variables may be adequate

* Use Matrices
    * page 21
    * generalised coordinates are column vectors

$$
    L = \underbrace{\underline{\dot{q}}^T \hat{\tau} \underline{\dot{q}}}_{T} - \underbrace{\underline{q}^T \hat{\upsilon}\underline{q}}_V + c
$$

* Elements of these matrices:

$$
    \tau_{jk} = \frac{1}{2} \frac{\partial^2 T}{\partial \dot{q}_j \partial \dot{q}_k}\Bigg|_{\dot{q}_{j},\dot{q}_k = 0} ~;~ \upsilon_{jk} = \frac{1}{2} \frac{\partial^2 V}{\partial \dot{q}_j \partial \dot{q}_k}\Bigg|_{q_{j},q_k = 0}
$$


## Lecture 7

#### Recap from Last time

$$
    T = \underline{\dot{x}} \hat{\tau} \underline{\dot{x}}
$$
$$
    V = \underline{x}^T \hat{\upsilon} \underline{x}
$$
$$
    L = T - V = \frac{1}{2}m(\dot{x}_{1}^2 + \dot{x}_{2}^2) - \frac{1}{2}k(x_{1}^2 + x_{2}^2 - 2x_{1}x_{2})
$$

* E-L: ($x_1$)

$$
    m\ddot{x}_{1} - k(x_{1} - x_2) = 0
$$

* E-L: ($x_2$)

$$
    m\ddot{x}_2 + k(x_2 - x_1) = 0
$$

* Other coordinates in each E-L is the coupling
* Equivalent to

$$
    \begin{pmatrix} m & 0 \\ 0 & m \end{pmatrix}
    \begin{pmatrix}\ddot{x}_1 \\ \ddot{x}_2 \end{pmatrix} +
    \begin{pmatrix} k & -k \\ -k & k \end{pmatrix}
    \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \underline{0}
$$
$$
    2(\hat{\tau}\underline{\ddot{x}} + \hat{\upsilon}\underline{x})
$$

* Equation for coupled oscillators:

$$
    \hat{\tau}\underline{\ddot{q}} + \hat{\upsilon}\underline{q} = 0
$$

### Normal Modes

* Usual thing to do is guess a solution
    * try $\underline{q} = \underline{b}e^{i\omega t}$

* This yields

$$
    (\hat{\upsilon} - \omega^{2}\hat{\tau})\underline{b}
$$

* Eigenvalue problem
    * det must be zero
    * $\hat{\tau}$ must be a multiple of the identity matrix

* In the pendulum example, $T = \frac{mgl}{2\omega_{0}^2}(\dot{\theta}_{1}^2 + \dot{\theta}_{2}^2)$

$$
    \tau_{ij} = \frac{1}{2} \frac{\partial^2 T}{\partial \dot{\theta}_{i} \partial \dot{\theta}_{j}}
$$
$$
    \tau_{11} = \frac{1}{2} \frac{\partial^2 T}{\partial \dot{\theta}_{1}^{2}} = \frac{mgl}{2\omega_{0}^2} ~;~ \tau_{12} = \frac{1}{2}\frac{\partial^2 T}{\partial \dot{\theta}_{1} \partial \dot{\theta}_{2}} = 0 = \tau_{21}
$$
$$
    \tau_{22} = \tau_{11}
$$
$$
    \hat{\tau} = \frac{mgl}{2\omega_{0}^2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$
$$
    \omega^2 \hat{\tau} = \frac{mgl}{2}\begin{pmatrix} \lambda & 0 \\ 0 & \lambda \end{pmatrix} ~;~ \lambda = \Big(\frac{\omega}{\omega_{0}} \Big)^2
$$

* page 21
* find eigenvalues from det of matrix above
* Gives

$$
    \frac{b_{(j)2}}{b_{(j)1}} = \frac{1 + \eta - \lambda_{j}}{\eta}
$$

### Normal Coordinates

$$
    r_j = \sum_{k = 1}^{N} b_{(j)k}q_{k}
$$

* Note that for coupled pendulum example $r_1 \propto (\theta_1 + \theta_2)$ and $r_2 \propto (\theta_2 - \theta_1)$
* Any general motion is a superposition of the normal modes
    * similar to eigenfunctions in Quantum

### Mode Orthogonality

$$
    \underline{b}_{i}^{T} \hat{\tau} \underline{b}_j = 0 ~;~ i \neq j
$$

1. If $\omega_{i}$s are all different, then $b_i$s are unique
2. If some $\omega_i$s are the same then there is a choice of $b_i$s but can always find orthogonal ones

#### Example - Free Vibrations of a linear triatomic molecule

* Central atom of mass, M and outer atoms have masses, m
    * constrained to move on an axis
    * connected together via springs of constant, k and natural length, l
    * point masses
    * Consider $x_1, x_2, x_3$

$$
    T = \frac{m}{2}(\dot{x}_{1}^2 + \dot{x}_{3}^2) + \frac{M}{2}\dot{x}_{2}^2
$$
$$
    \hat{\tau} = \frac{1}{2}\begin{pmatrix}m & 0 & 0 \\ 0 & M & 0 \\ 0 & 0 & m \end{pmatrix} $$ $$
    V = \frac{k}{2}\Big[(x_2 - x_1 - l)^2 + (x_3 - x_2 - l)^2 \Big] $$ $$
    \hat{\upsilon} = \frac{1}{2} \frac{\partial^2 V}{\partial x_i \partial x_j} = \frac{k}{2} \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix} $$ $$
    \hat{\tau}\underline{\ddot{q}} + \hat{\upsilon}\underline{q} = \underline{0}
$$

* Trial solution: $\underline{q} = \underline{b}e^{i\omega t}$

$$
    (\hat{\upsilon} - \omega^2 \hat{\tau})\underline{b} = 0 $$ $$
    \begin{pmatrix} k - \omega^2 m & -k & 0 \\ -k & 2k - \omega^2 M & -k \\ 0 & -k & k - \omega^2 m \end{pmatrix} \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = 0
$$

* The normal modes woll oscillate with frequencies satisfying

$$
    \begin{vmatrix} k - \omega^2 m & -k & 0 \\ -k & 2k - \omega^2 M & -k \\ 0 & -k & k - \omega^2 m \end{vmatrix} = 0
$$

* Do some algebra and you get

$$
    \omega^2 (k - \omega^2 m)[k(M + 2m) - \omega^2 Mm] = 0
$$

* Therefore, the nornal modes oscillate with frequencies
    * $\omega_{(1)} = 0$
    * $\omega_{(2)} = \sqrt{\frac{k}{m}}$
    * $\omega_{(3)} = \sqrt{\frac{k}{m}\big(1 + \frac{2m}{M}\big)}$
* The corresponding, unnormalised mode vectors are found by substituting these eigenvalues into the matrix above
* Doing this, you find that they are:

$$
    b_{(1)} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} ~;~ b_{(2)} = \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} ~;~ b_{(3)} = \begin{pmatrix} 1 \\ -\frac{2m}{M} \\ 1 \end{pmatrix}
$$

* Three different states:
    1. Just a translation
        * could have constrained the centre of mass to remain at origin and solve in 2 DoFs
    2. The two outer atoms are oscillating in anti-phase with big M static
    3. The m atoms are in phase with one another, and anti-phase with M atom, which has a relative amplitude of $\frac{2m}{M}$ so as to keep the centre of mass fixed

## Lecture 8

### Central Forces

#### Two Interacting Bodies

* Consider two point masses with positions $\underline{r}_1$ and $\underline{r}_2$
* Connected via central force between them
    * Interaction potential
    * Potential depends on distance between bodies in straight line
    * $V_12 = V_{12}(\underline{r}_1,\underline{r}_2) = V_{12}(|\underline{r}_1 - \underline{r}_2|) = V(r)$

$$
    L = \frac{1}{2}(m_1 \dot{\underline{r}}_{1}^2 + m_2 \dot{\underline{r}}_{2}^2) - \underbrace{V_1(\underline{r}_1) - V_2(\underline{r}_2)}_{\text{external potentials}} - \underbrace{V_{12}(|\underline{r}_1 - \underline{r}_2|)}_{\text{interaction potential}}
$$

* Consider an infinitesimal translation $\epsilon\underline{a}$ and Taylor expand Lagrangian to first order in $\epsilon$
    * page 25 for the maths
    * canonically conjugate momentum is first expression of E-L equation
        * in this case, the linear momentum
    * this comes from the translational invariance of the Lagrangian

#### Ignorable CoM

* Conservation of total momentum implies that CoM ($\underline{R} = \frac{m_1 \underline{r}_1 + m_2 \underline{r}_2}{(m_1 + m_2)}$) moves like a free particle
    * rewrite Lagrangian in terms of $\underline{R}$ and the relative coordinate, $\underline{r} = \underline{r}_1 - \underline{r}_2$

$$
    L = \frac{1}{2}M\dot{\underline{R}}^2 + \frac{1}{2}\mu \underline{\dot{r}}^2 - V_{12}(r) $$ $$
    \mu = \frac{m_1 m_2}{m_1 + m_2} $$ $$
    M = m_1 + m_2
$$

* Check that

$$
    \frac{1}{2}M\dot{\underline{R}}^2 + \frac{1}{2}\mu \underline{\dot{r}}^2 = \frac{1}{2}(m_1 \dot{\underline{r}}_{1}^2 + m_2 \dot{\underline{r}}_{2}^2) $$ $$
    LHS = \frac{1}{2} \Bigg[(m_1 + m_2)\Big(\frac{m_1 \underline{\dot{r}}_1 + m_2 \underline{\dot{r}}_2}{m_1 + m_2}\Big)^2 + \frac{m_1 m_2}{m_1 + m_2}(\underline{\dot{r}}_1 = \underline{\dot{r}}_2)^2 \Bigg] $$ $$
    LHS = \frac{1}{2(m_1 + m_2)} \Bigg[m_{1}^2 \underline{\dot{r}}_{1}^2 + m_{2}^2 \underline{\dot{r}}_{2}^2 + 2m_1 m_2 \underline{\dot{r}}_1 \underline{\dot{r}}_2 + m_1 m_2 (\underline{\dot{r}}_{1}^2 + \underline{\dot{r}}_{2}^2 - 2\underline{\dot{r}}_1 \underline{\dot{r}}_2) \Bigg] $$ $$
    LHS = \frac{1}{2(m_1 + m_2)} \Bigg[m_1 \underline{\dot{r}}_{1}^2 (m_1 + m_2) + m_2 \underline{\dot{r}}_{2}^2 (m_1 + m_2) \Bigg] $$ $$
    LHS = \frac{1}{2}(m_1 \dot{\underline{r}}_{1}^2 + m_2 \dot{\underline{r}}_{2}^2) = RHS
$$

### Rotational Invariance

* Transform to the centre of mass frame and remove first expression from Lagrangian
    * potential on depends on distance so we get rotational invariance

$$
    \underline{\dot{r}}^2 = \dot{x}^2 + \dot{y}^2 + \dot{z}^2 $$ $$
    \underline{\dot{r}}^2 = \dot{r}^2 + r^2\dot{\theta}^2 + (r\sin\theta)^2\dot{\phi}^2
$$ $$
    L = \frac{1}{2}\mu \underline{\dot{r}}^2 - V_{12}(r) $$ $$
    L = \frac{1}{2}\mu [\dot{r}^2 + r^2 \dot{\theta}^2 + r^2 \dot{\phi}^2\sin^2\theta] - V_{12}(r)
$$

* $\phi$ is ignorable, as it does not appear in L, therefore:

$$
    p_{\phi} \equiv \frac{\partial L}{\partial \dot{\phi}} = \mu r^2\dot{\phi}\sin^2\theta = \text{constant} \equiv \underbrace{J_z}_{\text{z component of } \underline{J} = \underline{r} \times \mu\dot{\underline{r}}}
$$

* Can choose coordinate system such that total angular momentum, $\underline{J}$, lies along the z-axis
    * Therefore, $\underline{J}$ is always constant

$$
    \underline{J} = \underline{r} \times \mu\underline{\dot{r}} ~;~ \underline{r} = \begin{pmatrix} r\cos\phi\sin\theta \\ r\sin\phi\sin\theta \\ r\cos\theta \end{pmatrix} $$ $$
    \underline{\dot{r}} = \begin{pmatrix} \dot{r}\cos\phi\sin\theta - r\dot{\phi}\sin\phi\sin\theta + r\dot{\theta}\cos\phi\cos\theta \\ \dot{r}\sin\phi\sin\theta + r\dot{\phi}\cos\phi\sin\theta + r\dot{\theta}\sin\phi\cos{\theta} \\ \dot{r}\cos\theta - r\dot{\theta}\sin\theta \end{pmatrix} $$ $$
    \underline{J} = \mu \begin{vmatrix} \underline{i} & \underline{j} & \underline{k} \\ r_i & r_j & r_k \\ \dot{r}_i & \dot{r}_j & \dot{r}_k \end{vmatrix} = \mu \begin{pmatrix} r_j \dot{r}_k - r_k\dot{r}_j \\ r_k\dot{r}_i - r_i\dot{r}_k \\ r_i\dot{r}_j - r_j\dot{r}_i \end{pmatrix}
$$

* Plug in $\underline{\dot{r}}$:

$$
    J_z = \mu r\sin\theta [r\dot{\phi}\sin\theta] = \mu r^2 \dot{\phi} \sin^2\theta
$$

* $\underline{J} = \underline{r} \times \mu\underline{\dot{r}}$, so $\underline{p}$ and $\underline{r}$ must be perpendicular to $\underline{J}$
* Hence, these must be in a plane perpendicular to $\underline{J}$, and remain in that plain as $\underline{J}$ is constant
* Choose $\underline{J}$ to lie along z direction, so that angle of elevation,

$$
    \theta = \frac{\pi}{2} $$ $$
    \dot{\theta} = 0 $$ $$
    J = |\underline{J}| = J_z = \mu r^2 \dot{\phi}
$$

### Lecture 9

##### Kepler's Second Law

$$
    \frac{dA}{dt} = \frac{1}{2}r^2 \dot{\phi} = \frac{J}{2\mu}
$$

* J is conserved, so the rate at which area is swept out is constant
* Kepler's second law comes from this
    * nothing to do much with gravity specifically

##### Equivalent 1D Problem

* In this case, remove $\theta$ and $\phi$ from Lagrangian

$$
    E = T + V = \frac{1}{2}\mu[\dot{r}^2 + r^2\dot{\theta}^2 + r^2\dot{\phi}^2\sin^2\theta] + V_{12}(r) $$ $$
    \dot{\theta} = 0 ~;~ \theta = \frac{\pi}{2} ~;~ \dot{\phi} = \frac{J}{\mu r^2} $$ $$
    E = \frac{1}{2}\mu \dot{r}^2 + \underbrace{\frac{J^2}{2\mu r^2} + V_{12}(r)}_{V_{eff}(r)}
$$

* Effective potential combines interaction potential with angular momentum barrier
* total energy E is the same as that corresponding to an effective Lagrangian
    * $L_{eff} = \frac{1}{2}\mu \dot{r}^2 - V_{eff}$
    * yields:

$$  
    \mu \ddot{r} = \frac{J^2}{\mu r^3} - \frac{\partial V_{12}}{\partial r}
$$

##### Example on Central Forces

* Find the orbit shape for the following potential:

$$
    V(r) = \begin{cases} -V_0 & r \leq R \\ 0 & r > R \end{cases} \implies V_{eff}(r) = \begin{cases} \frac{J^2}{2\mu r^2} - V_0 & r \leq R \\ \frac{J}{2\mu r^2} & r > R \end{cases}
$$

* If $\frac{J^2}{2\mu R^2} - V_0 < E < \frac{J^2}{2\mu R^2}$, then we have a bound orbit
    * $r_t$ there for E
    * $r_t \leq r \leq R$

$$
    r_{t}^2 = \frac{J^2}{2\mu (E + V_0)}
$$

* Set the azimuthal angle, $\phi = 0$, and $r = r_t$ at $t = 0$, and find the shape of the orbit:

$$
    E = \frac{1}{2}\mu\dot{r}^2 + \frac{J^2}{2\mu r^2} - V_0,~ r \leq R ~~ (1)
$$

* Define $\mu = \frac{1}{r}$, then $\frac{dr}{dt} = -\frac{1}{u^2}\frac{du}{dt}$

$$
    \dot{\phi} = \frac{d\phi}{dt} = \frac{J}{\mu r^2} = \frac{Ju^2}{\mu} $$ $$
    \frac{dr}{dt} = -\frac{1}{u^2}\frac{Ju^2}{\mu}\frac{du}{d\phi} $$ $$
    \to (1): \implies $$ $$
    E + V_0 - \frac{J^2 u^2}{2\mu} = \frac{\mu}{2}\frac{J^2}{\mu^2}\Big(\frac{du}{d\phi}\Big)^2 $$ $$
    \frac{du}{d\phi} = \pm \sqrt{\underbrace{\frac{2\mu}{J^2}(E + V_0)}_{\frac{1}{r_{t}^2} = u_{t}^2} - u^2} $$ $$
    \int_{U_0}^{U} -\frac{du}{\sqrt{u_{t}^2 - u^2}} = \int_{\phi_0}^{\phi} d\phi = \phi
$$

* Use substitution: $u = u_t \cos\alpha, du = -u_t\sin\alpha \,d\alpha$

$$
    \phi = \alpha + \alpha_0, ~~ t = 0 \implies \alpha_0 = \cos^{-1}\Big(\frac{u_t}{u_t}\Big) = 0 $$ $$
    \phi = +\cos^{-1}\Big(\frac{r_t}{r}\Big)
$$

* Sign is set by sign of angular momentum, J

$$
    \cos\phi = \frac{r_t}{r} \implies r = r_t\sec\phi,~ \phi < \Phi,~ R = r_t \sec\Phi
$$

#### Gravitational Attraction

* For gravity, we have the differential to be solved as:

$$
    \mu \ddot{r} = \frac{J^2}{\mu r^3} - \frac{k}{r^2},~ k = Gm_{1}m_{2}
$$

* solving this to determine orbits of bodies

##### The $u = \frac{1}{r}$ transformation

* See last example for this transformation or page 28

$$
    \frac{d^2 u}{d\phi^2} + u = \frac{\mu k}{J^2} $$ $$
    \implies \frac{1}{r} \equiv u = \frac{\mu k}{J^2} + B\cos\phi
$$

##### Elliptical Orbits

* Define $p \equiv \frac{J^2}{\mu k}$ and $\epsilon \equiv pB \implies$

$$
    E = \frac{\mu k^2}{2J^2}(\epsilon^2 - 1) = \frac{k}{2p}(\epsilon^2 - 1)
$$

* For $0 \leq \epsilon < 1$, bound elliptical orbit
* page 29
* $\epsilon$ is the eccentricity of the elliptical orbit:   
    * $\epsilon = 0 \implies$ circular orbit
    * $\epsilon = 1 \implies$ parabolic trajectory
    * $\epsilon > 1 \implies$ hyberbola

* elliptical orbits come from defining the $\frac{1}{r^2}$ potential

##### Third Law

$$
    T = 2\pi \sqrt{\frac{1}{G(m_1 + m_2)}a^{3/2}} \implies T^2 \propto a^2
$$

* Same proportionality constant for all planets
    * This is approximately true as the mass of the sun largely cancels out the mass of the planet

##### See page 29 and 30 for Bertrand's Theorem and Quadrature

##### Example: Kepler's Equation

* Given a set of observations of positions of a solar system body, how would one infer the orbit of that body?
* From the equation for an ellipse in the notes (Eq. 22), we can use the identity $\cos^2\psi +\sin^2\psi = 1$ to introduce the parameterisation:

$$
    x + \frac{\epsilon p}{1 - \epsilon^2} = a\cos\psi \implies x = a(\cos\psi - \epsilon) $$ $$
    y = b\sin\psi \implies y = a\sqrt{1 - \epsilon^2}\sin\psi
$$

* It follows that:

$$
    r = \sqrt{x^2 + y^2} = a(1 - \epsilon\cos\psi)
$$

## Lecture 10

#### Kepler's Equation Continued

* **INCLUDE IMAGE OF ELLIPSE**
* Relationship of the eccentric anomaly, $\psi$, to the true anomaly, $\phi$, for an effective particle placed a distance r and aximuthal angle $\phi$ from the centre of mass  
    * The elliptical orbit, with semi-major axis a, has been placed inside an imaginary circle of radius a
* We can solve the effective 1D problem by quadrature   
    * Eq 17 in notes, page 27, implies:

$$
    \int dt' = \sqrt{\frac{\mu}{2}} \int \frac{dr'}{\sqrt{E + \tfrac{k}{r'} - \tfrac{J^2}{2\mu r'^2}}}
$$

* For elliptical orbits, $E = -\frac{k}{2a}$
    * Also use $\frac{J^2}{\mu k} \equiv p$
    * $p = a(1 - \epsilon^2)$

$$
    \int dt' = \sqrt{\frac{\mu}{2k}} \int \frac{r'\,dr'}{\sqrt{-\tfrac{r'^2}{2a} + r' - \tfrac{a}{2}(1 - \epsilon^2)}}
$$

* Finally, use $r = a(1 - \epsilon\cos\psi)$
    * $dr = a\epsilon\sin\psi\,d\psi$

$$
    \int dt' = \sqrt{\frac{\mu}{2k}} \int \frac{a^2\epsilon\sin\psi'(1 - \epsilon\cos\psi')\,d\psi'}{-\tfrac{a}{2}(1 - \epsilon\cos\psi')^2 + a(1 - \epsilon\cos\psi') - \tfrac{a}{2}(1 - \epsilon^2)} $$ $$
    \int dt' = \sqrt{\frac{\mu}{2k}} \int \frac{a^2\epsilon\sin\psi' (1 - \epsilon\cos\psi')\,d\psi'}{\sqrt{\tfrac{a}{2}}(\epsilon\sin\psi')} $$ $$
    \int dt' = \sqrt{\frac{\mu a^3}{k}} \int (1 - \epsilon\cos\psi')\,d\psi'
$$

* This integral measures the time elapsed between initial and final value of this eccentric anomaly, $\psi'$
    * Customary to choose $t' = 0$ for when $\psi' = \phi' = 0$
        * when the orbiting body is at its perihelion
        * i.e. closest to the sun
* Hence, if $t(\psi)$ is the time elapsed from perihelion to when the eccentric anomaly takes the values $\psi$, then we have Kepler's equation

$$
    t(\psi) = \sqrt{\frac{\mu a^3}{k}} (\psi - \epsilon\sin\psi)
$$

* If we measure elapsed times and radii since perihelion, then Kepler's equation and the definition of an ellipse ($r = a(1 - \epsilon\cos\psi)$) can be solved to give the semi-major axis, a, and the eccentricity, $\epsilon$

### Hamiltonian Mechanics

#### Example in Swinging Atwood Machine

* Atwood machine with slight difference
    * One mass moves like a normal pulley, other like a pendulum
    * $DoFs = 2$

#### Noether's Theorem and Invariance of L

_"If the Lagrangian is invariant under a continuous symmetry transformation, then there are conserved quantities associated with that symmetry, one for each parameter of the transformation. These can be found by differentiating each coordinate wrt to the parameters of the transformation in the immediate neighbourhood of the identity transformation, multiplying by the conjugate momentum, and summing over the degreers of theorem."_

* page 31 for maths

* point mass moving in free space

$$
    L = \frac{1}{2}m\dot{q}^2 $$ $$
    Q = q + s $$ $$
    \frac{dQ}{ds}\Bigg|_{s_{} = 0} = 1 \implies I(q) = m\dot{q}
$$

* Consider phase space approach of 6D instead of just normal space
    * normal dimensions plus the canonically conjugate momenta

##### Legendre Transformations

* $A(x,y)$, intro third variable z
    * $B(x,y,z) \equiv yz - A(x,y)$
    * use chain rule
    * page 32
    * y can be written in terms of x and z
    * $B = B(x,y(x,z),z) = B(x,z) = yz - A(x,y)$

$$
    \frac{\partial B}{\partial z}\Bigg|_x = y_{} ~;~ \frac{\partial B}{\partial x}\Bigg|_z = -\frac{\partial A}{\partial x}\Bigg|_{y}
$$

* Similar to thermodynamics:
    * Enthalpy, X, such that
    * Use for isentropic and isobaric processes

$$
    dX = T\,dS + V\,dP
$$

* However for isothermal and isobaric processes, better to use the Gibbs energy:

$$
    \underbrace{G = X - TS}_{\text{Legendre transformation}} \to dG = S\,dT + V\,dp
$$

#### The Hamiltonian

$$
    H(q, p) \equiv p\dot{q} - L(q,\dot{q}) ~;~ p \equiv \frac{\partial L}{\partial \dot{q}}\Bigg|_{constant\, q_{}} $$ $$
    \frac{\partial H}{\partial p}\Bigg|_{q} = \dot{q} ~;~ \frac{\partial H}{\partial q}\Bigg|_{p} = -\frac{\partial L}{\partial q}\Bigg|_{\dot{q}} = -\frac{d}{dt}\frac{\partial L}{\partial \dot{q}}\Bigg|_{q} = -\dot{p}
$$

## Lecture 11

#### Hamilton's Principle Continued

* $S = \int L\,dt \implies \delta S = S[q + \delta q]$
    * $S[q] = \int \delta L\,dt$
* page 33 for maths from the following:

$$
    \delta L = \dot{q}\delta p + p\delta\dot{q} - \underbrace{\Big(\frac{\partial H}{\partial q}\delta q + \frac{\partial H}{\partial q}\delta p\Big)}_{\delta H}
$$

* $\int \delta L\,dt = 0$
* independent infinitesimal variations in $\delta q, \delta p$ from physical space in coordinate-momentum space (phase space) do not change the action, S

#### Hamilton's Equations of Motion

* For N DoF, Hamiltonian is dfined using the Legendre transformation:

$$
    H \equiv \Bigg(\sum_{k = 1}^{N} p_{k}\dot{q}_k \Bigg) - L
$$

* L may now be explicitly time-dependent
* Include a time differential to give

$$
    dH = \sum_{k = 1}^{N} \Big(\dot{q}_k dp_k - \dot{p}_kdq_k\Big) - \frac{\partial L}{\partial t}dt
$$

* page 33 for more

$$
    \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t} $$ $$
    \dot{q}_k = \frac{\partial H}{\partial p_k} ~;~ \dot{q}_k = -\frac{\partial H}{\partial q_k} ~;~ \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}
$$

#### Examples in Hamiltonians

##### Example 1

* particle of mass, m, moving vertically in a uniform gravitational field

$$
    T = \frac{1}{2}m\dot{z}^2 ~;~ V = mgz $$ $$
    L = T - V = \frac{1}{2}m\dot{z}^2 - mgz
$$

* The canonically conjugate momentum to coordinate z,

$$
    p_z = \frac{\partial L}{\partial \dot{z}} = m\dot{z}
$$

* Legendre transformation of $L(z,\dot{z})$ to give $H(z, p_z)$:

$$
    H(z, p_z) = p_z\dot{z} - L(z,\dot{z}) $$ $$
    H(z, p_z) = p_z \cdot \frac{p_z}{m} - \frac{m}{2} \Big(\frac{p_z}{m}\Big)^2 + mgz $$ $$
    H(z, p_z) =  \frac{p_{z}^2}{2m} + mgz = T + V = E_T s
$$

* EoM:

$$
    \dot{z} = \frac{\partial H}{\partial p_z} = \frac{p_z}{m} ~;~ \dot{p}_z = -\frac{\partial H}{\partial z} = -mg
$$

* Integrate $\dot{p}_z$ first to find $p_z$ as a function of time and then integrate $\dot{z}$ using this to find z as a function of time

##### Example 2

* particle of mass m moves in gravitational field, along the spiral of the form, $z = k\theta$ and $r = cst$, where k is a constant and z is the vertical direction
* Find the Hamiltonian, $H(z, p)$, and the equation of motion
* Show in the limit $r \to 0$, that $\ddot{z} \to -g$

$$
    T = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) ~;~ x = r\cos\theta,~ y = r\sin\theta,~ z = k\theta $$ $$
    \dot{x} = -r\dot{\theta}\sin\theta ~;~ \dot{y} = r\dot{\theta}\cos\theta ~;~ \dot{z} = k\dot{\theta} $$ $$
    T = \frac{1}{2}m (r^2\dot{\theta}^2 + \dot{z}^2) = \frac{1}{2}m\dot{z}^2 \Big(1 + \frac{r^2}{k^2}\Big) ~;~ V = mgz $$ $$
    L = \frac{1}{2}m\dot{z}^2 \Big(1 + \frac{r^2}{k^2}\Big) - mgz
$$

* Canonically conjugate momentum to z:

$$
    p = \frac{\partial L}{\partial \dot{z}} = m\dot{z}\Big(1 + \frac{r^2}{k^2}\Big) \implies \dot{z} = \frac{p}{m\big(1 + \tfrac{r^2}{k^2}\big)} $$ $$
    H = p\dot{z} - L = \frac{p^2}{m\big(1 + \tfrac{r^2}{k^2}\big)} - \frac{p^2}{2m\big(1 + \tfrac{r^2}{k^2}\big)} + mgz $$ $$
    H(z, p) = \frac{p^2}{2m\big(1 + \tfrac{r^2}{k^2}\big)} + mgz = T + V = E_T
$$

* EoM:

$$
    \dot{z} = \frac{\partial H}{\partial p} = \frac{p}{m\big(1 + \tfrac{r^2}{k^2}\big)} ~;~ \dot{p} = -\frac{\partial H}{\partial z} = -mg
$$

* Integrating:

$$
    p(t) = p(0) - mgt
$$

* Put this into the other equation:

$$
    z = \int_{0}^{t} \frac{p(0) - mgt'}{m\big(1 + \tfrac{r^2}{k^2}\big)} dt' = z(0) + \frac{p(0)t}{m\big(1 + \tfrac{r^2}{k^2}\big)} - \frac{gt^2}{2\big(1 + \tfrac{r^2}{k^2}\big)}
$$

* Find expression for $\ddot{z}$:

$$
    \ddot{z} = \frac{\dot{p}}{m\big(1 + \tfrac{r^2}{k^2}\big)} = \frac{-g}{\big(1 + \tfrac{r^2}{k^2}\big)}
$$

* As $r \to 0$, $\ddot{z} \to -g$ as denominator tends to 1

##### Example 3

* Stretched Spring attached to a uniformly moving cart
* passes $x = 0$ at $t = 0$
* cart moving at speed, $v_0$
* unstretched length of the spring is negligible

$$
    L(x, \dot{x}, t) = T - V = \frac{m\dot{x}^2}{2} - \frac{k}{2}(x - v_0t)^2 $$ $$
    E-L \implies m\ddot{x} = -k(x - v_0t),~[x' = x - v_0t] $$ $$
    \ddot{x}' = \ddot{x} ~;~ m\ddot{x}' = -kx'
$$

* SHM in the cart's frame of reference

$$
    p_x = \frac{\partial L}{\partial \dot{x}} = m\dot{x} $$ $$
    H(x, p_x) = p_x\dot{x} - \frac{m\dot{x}^2}{2} + \frac{k}{2}(x - v_0t)^2 = \frac{p_{x}^2}{2m} + \frac{k}{2}(x - v_0t)^2 = T + V = E_T
$$

* H explicitly depends on t, therefore it is not conserved
* To keep the cart moving uniformly despite the oscillating mass, energy flows in and out of the system
* However, in terms of $x' = x - v_0t$, $\dot{x}' = \dot{x} = v_0$:

$$
    L(x', \dot{x}') = \frac{m\dot{x}'^2}{2} + m\dot{x}'v_0 + \frac{mv_{0}^2}{2} - \frac{kx'^2}{2} $$ $$
    p_{x'} = \frac{\partial L}{\partial \dot{x}'} = m\dot{x}' + mv_0 $$ $$
    H'(x', p_{x'}) = p_{x'}\dot{x}' - L(x', \dot{x}') $$ $$
    H'(x', p_{x'}) = m\dot{x}'^2 + m\dot{x}'v_0 - \frac{m\dot{x}'^2}{2} - m\dot{x}'v_0 - \frac{mv_{0}^2}{2} + \frac{kx'^2}{2} $$ $$
    H'(x', p_{x'}) = \frac{m\dot{x}'^2}{2} + \frac{kx'^2}{2} - \frac{mv_{0}^2}{2} $$ $$
    H'(x', p_{x'}) = \frac{(p_{x'} - mv_0)^2}{2m} + \frac{kx'^2}{2} - \frac{mv_{0}^2}{2} \neq E_T
$$

* $H'(x', p_{x'})$ has no explicit time dependence so it is conserved but it is no longer the total energy
