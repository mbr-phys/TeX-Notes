---
title: "Foundations of Physics B"
author: "Dr Douglas Halliday"
date: "Epiphany 2018"
---

# Condensed Matter Physics

## Lecture 2

### describing crystals

* regular periodic array of atoms - highly defined
* x-rays discovered in 1912
    * diffraction of x-rays key to studying crystals
* crystals classified by certain physical properties
* a perfect crystal is assumed to be a regular array of repeating points
    * we can construct a set of theoretical points in 3D (defined by vectors), called a lattice
* lattice described by unit vectors $\vec{a}_1,\vec{a}_2,\vec{a}_3$, called the lattice constants
* lattice given physical reality by placing atoms at lattic points
    * these atoms are called a basis - there can be more than one atom in a basis, e.g. NaCl
* use the relationship, where: $\vec{r},\vec{r}'$ are points on the lattice; $a_i$ are unit vectors; and $n_i$ are scalar multiples -
$$
    \vec{r}' = \vec{r} + n_1\vec{a}_1 + n_2\vec{a}_2 + n_3\vec{a}_3
$$
* it is called a primitive lattice if this equation cannot be reduced
* think of lattices as 3D constructs for filling space
* crystals have a high degree of symmetry

### symmetry operators

1. translation
2. rotation
3. reflection
4. inversion
5. combinations of above

* a lattice should remain invariant under specific symmetry operations
* point operators in 2D lead to 2D lattices, of which you can get different types -  
    1. square
    2. hexagonal
    3. rectangular
    4. centred rectangular
    5. oblique parallelogram
    * cannot get a five-fold symmetry shape

### three-dimensional lattices

* there are seven basic crystal systems
    1. triclinic
    2. monoclinic
    3. orthohombic
    4. tetragonal
    5. rhombohedral (trigonal)
    6. hexagonal
    7. cubic

* use parameters to define these -
    * p - primitive
    * i - interstitial
    * f - face-centred
    * c - base-centred
* by varying the parameters for each basic type (see table in lecture summary), get 14 Bravais lattices in 3D
    * these are the basic building blocks of all crystals

### miller indices

* **key concept for categorising crystals**
* describe a particular crystallographic plane or orthogonal direction in crystal
* effectively describes crystals as families of parallel planes
* method for determining the index:
    1. find the intercepts of plane on crystal axes - the three lattice constants
    2. take the reciprocal of these constants
    3. reduce to 3 integers with the same ratio
    4. this gives the index of the plane, using the notation $(hkl)$, or $(\nu_1 \nu_2 \nu_3)$ in Kittel
    5. if one of the indices is negative, put a bar above the magnitude
* separation between planes:
$$
    d = \frac{1}{\sqrt{\frac{h^2}{a_1^2} + \frac{k^2}{a_2^2} + \frac{l^2}{a_3^2}}}
$$
* For a cubic, this reduces to
$$
    d_{hkl} = \frac{a}{\sqrt{N}}
$$

## Lecture 3

### x-ray diffraction

* crystal is defined by a set of parallel planes separated by distance $d$
* waves incident on crystals will be diffracted - developed by Bragg and lead to the law of x-ray diffraction
* for each wave will experience specular reflection - small reduction in intensity
* path length difference $A \to B \to C = 2d\sin\theta$
* if path length is equal to an integer multiple of the wavelength of wave, get constructive interference
* Bragg Law:
$$
    2d\sin\theta = n\lambda
$$
* typically, $\lambda \approx 0.15\,nm$ for x-rays
* it is observed that each plane of atoms reflects $10^{-3} - 10^{-5}$ of the intensity
* bragg law is a consequence of periodic structure of crystals
* fourier analysis is used

### electron density

* crystal lattice is defined by translation vector,
$$
    \underline{T} = n_1\vec{a}_1 + n_2\vec{a}_2 + n_3\vec{a}_3
$$
* crystal is invariant under $\underline{T}$ translation
* many physical properties related to electron density, $n(\vec{r})$
* crystal symmetry $\implies n(\vec{r}) = n(\vec{r} + \underline{T})$, local electron environment is also invariant under $\underline{T}$
* consider electron density in one dimension:
$$
    n(x) = n_0 + \sum_p \left[c_p\cos\left(\frac{2\pi xp}{a}\right) + s_p\sin\left(\frac{2\pi xp}{a}\right)\right]
$$
* $p \in \mathbb{N}$; $a =$ the lattice constant; and $x =$ distance
* crystal symmetry also $\implies n(x) = n(x + a)$

### reciprocal lattice points

* arguments of $\sin$ and $\cos$ are called reciprocal lattice points
    * there is a factor of $\frac{2\pi}{a}$ - requires functions to have correct periodicity
    * units - $\cos,\sin$ are dimensionless; $\frac{2\pi p}{a}$ is the basis of summation
    * only certain values are allowed by the relationship above
$$
    n(x) = \sum_p n_p e^{\frac{i2\pi px}{a}}
$$
* allowed points in $\sin()$ and $\cos()$ are equivalent to families of planes described by Miller indices $(hkl)$
* in 3D:
$$
    n(\vec{r}) = \sum_G n_G e^{\vec{G}\cdot\vec{r}}, ~ G = \text{reciprocal lattice vectors}
$$
* $G$ is defined as the family of reciprocal lattice points in 3D - each describing a family of crystal planes
* $b_1,b_2,b_3$ are the reciprocal lattice unit vectors, units of frequency
$$
    b_1 = 2\pi\frac{\vec{a}_2 \times \vec{a}_3}{\vec{a}_1\cdot(\vec{a}_2 \times \vec{a}_3)} ~;~ b_2 = 2\pi\frac{\vec{a}_3 \times \vec{a}_1}{\vec{a}_1\cdot(\vec{a}_2 \times \vec{a}_3)} ~;~ b_3 = 2\pi\frac{\vec{a}_1 \times \vec{a}_2}{\vec{a}_1\cdot(\vec{a}_2 \times \vec{a}_3)}
$$
* $a_i$ are unit vectors of crystal
* $a_i \cdot b_j = 2\pi\delta_{ij}$ - delta function
$$
    \begin{aligned}
    \underline{G} &= \nu_1\vec{b}_1 + \nu_2\vec{b}_2 + \nu_3\vec{b}_3 \\
    n(\vec{r} + \underline{T}) &= \sum_G n_G e^{i\underline{G}\cdot\vec{r}}\underbrace{e^{i\underline{G}\cdot\underline{T}}}_{2\pi \times p}
    \end{aligned}
$$

## Lecture 4

### x-ray diffraction

* incident electromagnetic wave on crystal - $\exp[9(\vec{k}\cdot \vec{r})]$
    * $\vec{k}$ is the wavevector of the x-ray
* elastic process - conservation of energy
* assume interaction between electric field of wave and elctrons in atom
* electron density - $n(\vec{r})$
* scattered wave is described by

$$
    \begin{aligned}
    F &= \int n(\vec{r})\exp\left[i((\vec{k}-\vec{k}')\cdot\vec{r})\right]\,dV \\
    &= \int n(\vec{r})\exp\left[i(\vec{\Delta k}\cdot \vec{r})\right]\,dV
    \end{aligned}
$$

* $\vec{\Delta k} = \vec{k} - \vec{k}'$
* elastic scattering - $|\vec{k}| = |\vec{k}'|$
* $\vec{\Delta k}$ - scattering vector
    * for Bragg condition - $\vec{\Delta k} = \vec{G}$

$$
    F = \sum_G \int n_G \exp\left[i(\vec{G} - \vec{\Delta k})\cdot\vec{r}\right]
$$

* alternative formulation of Bragg condition -

$$
    \begin{aligned}
    \vec{k} + \vec{G} &= \vec{k}' \\
    \implies (\vec{k} + \vec{G})^2 &= |\vec{k}|^2 \\
    2\vec{k}\cdot\vec{G} + |\vec{G}|^2 &= 0 \\
    \implies 2\vec{k}\cdot\vec{G} &= |\vec{G}|^2
    \end{aligned}
$$

* n.b. $\vec{\Delta k}$ has equivalent positive and negative values

### brillouin zones

* analogy to unit cells in reciprocal space
* first brillouin zone is wigner-seitz primitive cell in reciprocal lattice
    * used to describe a wide range of physical properties
* construct brillouin zone:
    1. select origin in reciprocal space
    2. draw reciprocal lattice vector to all nearest neighbours
    3. perpendicular bisectors enclose first brillouin zone

#### examples of reciprocal lattices

* simple cubic lattice:

$$
    \begin{aligned}
    \vec{a}_1 &= a\hat{x} & \vec{a}_2 &= a\hat{y}, & \vec{a}_3 &= a\hat{z} \\
    \vec{b}_{1} &= \frac{2\pi}{a} \hat{x} & \vec{b}_2 &= \frac{2\pi}{a}\hat{y} & \vec{b}_3 &= \hat{z}
    \end{aligned}
$$

* reciprocal lattice is a simple cube with lattice constant $\frac{2\pi}{a}$

* body centred cubic lattice:

$$
    \begin{aligned}
    \vec{a}_1 &= \frac{1}{2}a(-\hat{x} + \hat{y} + \hat{z}) & \vec{a}_2 &= \frac{1}{2}a(\hat{x}-\hat{y}+\hat{z}) & \vec{a}_3 &= \frac{1}{2}a(\hat{x}+\hat{y}-\hat{z}) \\
    \vec{b}_1 &= \frac{2\pi}{a}(\hat{y} + \hat{z}) & \vec{b}_2 &= \frac{2\pi}{a}(\hat{x}+\hat{z}) & \vec{b}_3 &= \frac{2\pi}{a}(\hat{x}+\hat{y})
    \end{aligned}
$$

* these are primitive lattice vectors of fcc (face centre cubic) lattice
* similarly, reciprocal of fcc lattice is bcc lattice

### structure factor

* structure factor describes intensity of Bragg peaks
    * arises because Bragg law considers parallel planes but can also get interference within unit cell
* integral over unit cell describes total scattered intensity

$$
    \begin{aligned}
    F_G &= N \int_{cell} n(\vec{r}) \exp\left[-i\vec{G}\cdot\vec{r}\right] = NS_G
    \end{aligned}
$$

* $N$ is the total number of cells; $S_G$ is the structure factor for a single cell
* define origin at $\vec{r} = 0$
* consider $n(\vec{r})$ as sum over all unique atoms in unit cell

$$
    \begin{aligned}
    n(\vec{r}) &= \sum_{j=1}^S n_j(\vec{r}-\vec{r}_j) \\
    S_G &= \sum_j \exp\left[-i\vec{G}\cdot\vec{r}\right] \int n_j(\vec{\rho}) \exp\left[-i\vec{G}\cdot\vec{\rho}\right] \\
    &= \sum_j f_j \exp\left[-i\vec{G}\cdot\vec{r}_j\right] \\
    S_G(\nu_1\nu_2\nu_3) &= \sum_j f_j \exp\left[-i2\pi (\nu_1x_j + \nu_2y_j +  \nu_3z_j)\right]
    \end{aligned}
$$

* $\vec{\rho} = \vec{r} - \vec{r_j}, \vec{r}_j$ is position of unique atom in unit cell; $f_j$ is atom form factor scattering of one atom
* $\nu_1\nu_2\nu_3 = hkl$ describing Bragg peak; $(x_j,y_j,z_j)$ is position coordinates within unit cell
* for bcc lattice - have two unique atoms at coordinates $(000),(\frac{1}{2},\frac{1}{2},\frac{1}{2})$
* evaluate $S_G \implies S=0$ when $\nu_1 + \nu_2+\nu_3 =$ odd integer; $S=2f$ when $\nu_1+\nu_2+\nu_3 =$ even integer
* fcc lattice - 4 atoms $(0,0,0),(0,\frac{1}{2},\frac{1}{2}),(\frac{1}{2},0,\frac{1}{2}),(\frac{1}{2},\frac{1}{2},0)$
    * $S = 0$ when integers mixed
    * $S=4f$ when integers all odd or all even

## Lecture 5

### crystal bonding

* bonding is a stable equilibrium between attractive and repulsive force
* repulsive arises from electrons being fermions
    * no two fermions occupy the same quantum state
    * as electrons from adjacent atoms overlap, increases energy to satisfy Pauli exclusion principle
* different types of bonds have different attractive forces:
1. Van Der Waals bonding exists in almost all solid system - very weak force, usually only observed at low temperatures in noble gases
    * attraction is between electric dipoles
        1. permanent
        2. permanent-induced
        3. two induced dipoles
    * spherically symmetrical atom - when brought closer to another atom, electron distribution adjusts because of Coulomb potential
    * can consider movement of charge as electric dipole:
        * amount of charge, $q$, moving distance, $L, \to$ dipole moment $= p = qL$
        * electric dipole consists of charge $+q$ and $-q$ separated by $L$
        * at arbitrary point, electric potential
        $$
        V = \frac{Q}{4\pi \epsilon_0}\left(\frac{1}{r_b} - \frac{1}{r_a}\right)
        $$
        * it can be shown that
        $$
        V(r) = \frac{\vec{p}\cdot\hat{r_1}}{4\pi \epsilon_0 r^2}
        $$
        * where $\vec{p}$ is the electric dipole vector, and $\hat{r}_1$ is the unit vector along $\vec{r}$
        * show potential energy  and force are
        $$
        \begin{aligned}
        U(r) &= \frac{A}{r^6} \\
        F(r) &= -\frac{dU}{dr} = \frac{A}{r^7}
        \end{aligned}
        $$
    * modelling Pauli repulsion - very complex  
        * approximate using empirical function
        * experimental data on solid gases shows that the function is of the form $\frac{B}{r^{12}}$ fits data
        $$
        U(r) = 4\epsilon\left[-\left(\frac{\sigma}{r}\right)^6 + \left(\frac{\sigma}{r}\right)^{12}\right]
        $$
        * this is the Lennard Jones $6-12$ potential - models interatomic potential in Van Der Waals solids
            * $4\epsilon\sigma^6 \equiv A$
            * $4\epsilon\sigma^{12} \equiv B$
2. other examples of bonding
    1. ionic bonding - crystals made of postive and negative energy
        * many salts are under this (NaCl, LiF, MgCl)
        * overall energy of ionic crystal - ionisation energy, electron affinity
        * energy - electrostatic attraction
        $$
        U(r) = -\frac{e^2}{4\pi\epsilon_0 r}
        $$
        * this considers only nearest neighbours
        * in ionic crystals, energy must also consider other ions - not just nearest neighbours
        * interaction of all ions described by $\underline{\text{modelling constant}}$
            * face centred cube crystal has modelling constant of $1.7475$
    2. covalent crystals - sharing of electrons, generally occurs in systems of similar atoms (e.g. silicon semiconductor, diatomic gases)
        * covalent bonding can only be described using QM
        * two electrons, spin $= \frac{1}{2}$
            * $\uparrow \downarrow \to S = 0$ - spin antisymmetric
            * $\uparrow \uparrow \to S = 1$ - spin symmetric
            * when spin is antisymmetric, position (wavefunction) is symmetric or vice versa
            * large electron density between atoms - forms a bond


## Lecture 6

* consider crystals as system of vibrating atoms
* family of excitations in solids, elastic waves - phonons
* range of phenomena suggests atoms vibrate
* describe crystal as series of parallel planes denoted by $s,s\pm1,s\pm2,\cdots$
* describe position of plane using coordinate $u_s,u_{s\pm1},\cdots$, $u_s$ is the displacement from the equilibrium
* longitudinal and transverse waves exist
* physics to describe motion?
    * Hooke's law - elestic wave, restoring force, linear function of $u_S$
* energy of oscillating system:
$$
    E = \frac{1}{2}kA^2
$$

* spring constant - $\omega = \sqrt{\frac{k}{m}}$
* elastic energy is a quadratic function of displacement from mean position
* need to know the force exerted on individual planes
* _assume only nearest neighbour interactions apply_
* forces acring on plane s:
$$
    F_s = c(u_{s+1}-u_s) + c(u_{s-1}-u_s)
$$

* c is a force constant for the nearest neighbour
$$
    M\frac{d^2u_s}{dt^2} = c(u_{s+1}+u_{s-1}-2u_s)
$$

* Assume SHM:

$$
    \frac{d^2u_s}{dt^2} = -\omega^2u_s
$$

* Equation relates motion of planes:

$$
    -M\omega^2 u_s = c(u_{s+1}+u_{s-1}-2u_s)
$$

* by substitution, the general form of equation is:

$$
    u_{s\pm1} = U\exp\left[i(s\pm1)ka\right] = U\exp\left(iska\right)\exp\left(\pm ika\right)
$$

* $U$ is the maximum amplitude, $k$ is the wavevector of the elastic wave, and $a$ is the spacing of adjacent planes

$$
    \begin{aligned}
    -\omega^2Mu\exp\left(iska\right) &= CU\left\{\exp\left[i(s+1)ka\right]+\exp\left[i(s-1)ka\right]-2\exp\left[iska\right]\right\} \\
    \omega^2M &= -C\left[\exp(ika) + \exp(-ika)-2\right] \\
    \omega(k)^2 &= \left(\frac{2c}{M}\right)(1 - \cos(ka)) \\
    \omega(k)^2 &= \frac{4c}{M}\sin^2\left(\frac{1}{2}ka\right) \\
    \implies \omega(k) &= \sqrt{\frac{4c}{M}}\left|\sin\left(\frac{1}{2}ka\right)\right|
    \end{aligned}
$$

* angular frequency depends on the wavevector - phenomena is known as dispersion 
* waves of certain wavelength or wavevector travel at different velocities

### group velocity

* consider displacement of planes as a packet of elastic energy propagating through a crystal (phonons)

$$
    v_g = \frac{\partial \omega}{\partial k}
$$

* velocity is related to the gradient of $\omega(k)$ dispersion curve

$$
    v_g = \sqrt{\frac{Ca^2}{M}}\cos\left(\frac{1}{2}ka\right)
$$

* low wavevector waves have higher velocity, waves at boundary of brillouin zone have zero velocity

### long wavelength limit

* applies to waves $k \approx 0$, defined by $ka \ll 1$
* this corresponds to sound waves in crystal
* when $ka \ll 1 \to \cos(ka) = 1 -\frac{1}{2}(ka)^2$
* dispersion relation (long wavelength):

$$
    \begin{aligned}
    \omega^2 &= \left(\frac{c}{M}\right)k^2a^2 \\
    \omega &= \sqrt{\frac{c}{M}}ka
    \end{aligned}
$$

* $\omega \propto k$ at long wavelengths

## Lecture 7

* consider two atom basis in phonon model - e.g. salts (NaCl), semiconductors (GaAs), etc
* use same equation of motion with $M_1$ and $M_2$ masses and $U_{s,s\pm1\cdots},V_{s,s\pm1\cdots}$

$$
    M_1\frac{d^2U_s}{dt^2} = c(V_s + V_{s-1} - 2U_s) ~;~ M_2\frac{d^2 V_s}{dt^2} = c(U_{s+1} + U_s - 2V_s)
$$

* solutions is SHM - travelling wave, different amplitudes on adjacent planes $u_s,v_s$
* we define $a$ as the distance between identical planes ($M_1$ or $M_2$)

$$
    U_s = U\exp(isKa)\exp(-i\omega t) ~;~ V_s = V\exp(isKa)\exp(-i\omega t)
$$

* substitute travelling wave into equation of motion

$$
    \begin{aligned}
    -\omega^2 M_1U &= cv[1+\exp(-iKa)] - 2cu \\
    -\omega^2 M_2V &= cu[1+\exp(iKa)] - 2cv
    \end{aligned}
$$

* only solution obtained from determinant of matrix equation

$$
    \begin{aligned}
    \begin{vmatrix} 2c - M_1\omega^2 & -c[1+\exp(iKa)] \\ -c[1+\exp(iKa)] & 2c - M_2\omega^2 \end{vmatrix} \\
    M_1M_2\omega^4 -2c(M_1+M_2)\omega^2 + 2c^2(1-\cos(Ka)) = 0 \\
    \omega^2 = \frac{c(M_1+M_2)}{M_!M_2} \pm \frac{C(M_1+M_2)}{M_1M_2}\sqrt{1 - 2\frac{M_1M_2(1-\cos(Ka)}{(M_1+M_2)^2}}
    \end{aligned}
$$

* solution gives two branches in phonon dispersion relation

* consider two limits to illustrate general behaviour
    1. when $Ka \ll 1$ - long wavelength limit
    2. $K = \pm\frac{\pi}{a}$ - boundary of first brillouin zone

* for small $Ka$ (long wavelength limit), $\cos(Ka) \approx 1 - \frac{1}{2}K^2a^2$
* two solutions of dispersion:

$$
    \begin{aligned}
    \omega^2 &\approx 2c\left(\frac{1}{M_1} + \frac{1}{M_2}\right) \\
    \omega^2 &\approx \frac{\frac{1}{2}c}{M_1M_2}K^2a^2
    \end{aligned}
$$

1. $\omega$ is independent of $K$ in the optical branch
    * two atoms out of phase
2. $\omega \propto K$ in the acoustic branch
    * two atoms move in phase

### thermal properties of crystals

* phonon heat capacity: 

$$
    C_V = \left(\frac{dU}{dT}\right)_V
$$

* $C_V$ used because no work done to change volume
* $U$ is the total internal energy of the vibrating lattice

$$
    U_{tot} = \sum_k \sum_p U_{kp} = \sum_k\sum_p \langle n_{kp} \rangle \hbar \omega_{kp}
$$

* where $k$ is the wavevector, and $p$ is the polarisation, and $\langle n_{kp} \rangle$ 
* $\langle n_{kp} \rangle$ described by Planck distribution function:

$$
    n = \frac{1}{\exp\left(\frac{\hbar\omega}{k_BT}\right) - 1}
$$

* number of vibrational nodes is called the density of states - number of vibrations per unit energy

$$
    D(\omega) = \frac{dN}{d\omega} = \left(\frac{vK^2}{2\pi^2}\right)\left(\frac{dK}{d\omega}\right)
$$

* number of phonon nodes in a given frequency or energy range

### debye model

* assumption is that velocity of sound is constant
* Debye model dispersion relation: $\omega = vK$
* density of states goes to

$$
    D(\omega) = \frac{V\omega^2}{2\pi^2v^3} ~;~ D(\omega) \propto \omega^2
$$

* maximum frequency range is Debye frequency:

$$
    \omega_D^3 = 6\pi^2v^3 \frac{N}{V}
$$

* corresponds to Debye wavevector:

$$
    K_D = \frac{\omega_D}{v} = \left(6\pi^2\frac{N}{V}\right)^{1/3}
$$

### einstein model

* assumes all phonons have the same frequency or energy

$$
    U = N\langle n\rangle\hbar\omega = \frac{N\hbar\omega}{\exp\left(\frac{\hbar\omega}{kT}\right) - 1}
$$

* $N$ is the total number of oscillators

## Lecture 8

### electrical properties of crystals from classical physics

* assumptions:
    1. outer valence electrons are detached - free to move through the crystal
    2. electric field due to other electrons and nucleus cancel out
  
* drude model - applied kinetic theory of gases to electrons
1. specific heat capacity of electrons
    * Mean kinetic energy $E = \frac{3}{2}k_BT$
    * specific heat capacity per electron: $C_V = \frac{dE}{dt} = \frac{3}{2}k_B$
2. electrical conductivity
    * begin with Ohm's Law, $V = IR$
    * rewrite in dimensionless form, $E = \rho J$
    * $J = \sigma E$
* drude model assumes electrons collide with something
* describe using a mean time between collision events $\tau$
* equations of motion $\underline{v} = \underline{v}_0 - \frac{|e|t\underline{E}}{m_e}$
* electron velocity $v_0$ is random - no overall contribution
    * considers only drift velocity in response to $\underline{E}$
    * electron drift velocity is average of $-\frac{|e|t\underline{E}}{m_e}$

    $$
        \begin{aligned}
        \bar{\underline{v}} &= -\frac{|e|\bar{t}\underline{E}}{m_e},~ \bar{t} = \tau \\
        \underline{J} &= -n|e|\underline{v} = \frac{n|e|^2\tau}{m_e}\underline{E} \\
        \implies \sigma &= \frac{n|e|^2\tau}{m_e}
        \end{aligned}
    $$

* this is the drude electrical conductivity formula
3. thermal conductivity of electrons
    * temp gradient $\frac{dT}{dz}$
    * assume electron is in thermal equilibrium at point of collision
    * consider thermal energy carried by the electron
    * thermal average is $v_z^2 = \frac{k_BT}{m_e}$

    $$
        \begin{aligned}
        Q &= -nv_z c_V v_z\tau \frac{dT}{dx} \\
        &= -\kappa \frac{dT}{dz} \\
        \kappa = \frac{3}{2}n\frac{k_B^2T}{m_e}\tau
        \end{aligned}
    $$

* comparison with ratio of thermal to electrical conductivity

$$
    \frac{\kappa}{\sigma} = \frac{3}{2}\left(\frac{k}{e}\right)^2T
$$

## Lecture 9

### free electron model

assumptions:
1. outer valence electrons detach - free to move around crystal
2. effects of ions and electrons cancel - electrons move in region of no potential

* free electron model treats metal as empty box (zero potential) of dimensions ($L_x,L_y,L_z$)
    * inside the box, zero potential
    * outside the box, infinite potential

#### periodic boundary conditions

* boundary used in this model - consequence of periodicity of crystals

$$
    \psi(\vec{r}) = \psi(\vec{r}+\vec{L}), \vec{L} = (L_x,L_y,L_z)
$$

* wavefunction is assumed to be periodic with dimensions of sample space, $\vec{L}$ 
* this removes any limitation on the value of $\vec{r}$

$$
    \psi(x,y,z) = \psi(x+L_x,y,z) + \psi(x,y+L_y,z) + \psi(x,y,z+L_z)
$$

#### free electron wavefunction

* potential inside box is zero, so time-independent schrodinger is

$$
    \begin{aligned}
    -\frac{\hbar^2}{2m_e}\nabla^2\psi(\vec{r}) &+ V(\vec{r})\psi(\vec{r}) = E\psi(\vec{r})
    \psi(x,y,z) &= A\exp\left[i(k_xx + k_yy + k_zz)\right], k_i = \frac{2\pi(l/m)}{L_i}
    E &= \frac{\hbar^2}{2m_e}\left(k_x^2 + k_y^2 + k_z^2\right)
    \end{aligned}
$$

* electron energy eigenstates are stationary (independent of time)
* amplitude $A$ is constant, uncertainty in position coordinate, all energy states overlap

#### k-space

* reciprocal space
* can describe electrons using k-coordinate
* each electron has coordinate ($k_x,k_y,k_z$) in k-space, separated by $\frac{2\pi}{l}$ in each dimension
* allowed points form mesh in k-space - each within a volume $\left(\frac{2\pi}{L}\right)^3$
    * "exclusion zone"
    * no other allowed k-states within the volume
* each k-state has 2 electron spin degeneracy - Pauli exclusion principle 
* allowing for spin, we have 

$$
    2\div\left(\frac{2\pi}{L}\right)^3 = \frac{L^3}{4\pi^3}
$$

#### fermi energy and surface

* maximum energy of system
* define fermi energy as highest occupied energy level when system is in ground state (0 Kelvin)

$$
    E = \frac{\hbar^2k^2}{2m_e}
$$

* surface of constant energy is constant, $k^2$
* fermi surface is a sphere of radius $k_F$
* $\frac{L^3}{4\pi^3}$ electron states per unit volume, so volume of sphere is $V = \frac{4}{3}\pi k_F^3$
* total nnumber of electrons:

$$
    \begin{aligned}
    N &= \left(\frac{4}{3}\pi k_F\right)^3\left(\frac{L^3}{4\pi^3}\right)
    k_F &= \left(\frac{3N\pi^2}{L^3}\right)^{1/3} = (3\pi^2n)^{1/3}, n = \text{ electron density}
    E_F &= \frac{\hbar^2}{2m_e}k_F^2 = \frac{\hbar^2}{2m_e}(3\pi^2n)^{2/3}
    \end{aligned}
$$

#### density of states

* number of electron energy states oer unit energy range
* consider volume of k-space between $k$ and $k+\delta k$:
    * volume is surface area $\times \delta k = 4\pi k^2\delta^2$
* number of states between $k$ and $k+\delta k \to$

$$
    n(k)\delta k - \frac{L^3}{4\pi^3}4\pi k^2 \delta k
$$

* express energy:

$$
    n(E)\delta E = \frac{L^3}{\pi^2}k^2\delta k \implies n(E) = \sqrt{2}\frac{L^3}{\pi^2}\frac{n_e^{3/2}}{k^3}\sqrt{E}
$$

## Lecture 10

### fermi-dirac distribution

* fermi energy is energy of highest occupied state at 0 Kelvin (overall ground state)
* fermi function describes occupatoin of energy levels
* at 0 Kelvin, states above $E_F$ are empty $f=0$, states below $E_F$ are occupied $f=1$
* define an occupation number:

$$
    f(E) = \begin{cases} 1 & 0 < E \leq E_F \\ 0 & E > E_F \end{cases}
$$

* can be considered a continuous distribution function

$$
    N = \int_0^{E_F} n(E)dE = \int_0^infty f(E)n(E)dE
$$

* consider how function varies with temperature - energy range covering transition from $f=1$ to $f=0$ is broadened out at finite temperatures
* this is described by the Fermi-Dirac distribution function - derived by consdiering 3 constraints:
    1. Conservation of Energy
    2. Conservation of Particle Number
    3. Subject to Pauli Exclusion principle

$$
    f(E) = \frac{1}{1 + \exp\left[\frac{(E-E_F)}{k_BT}\right]}
$$

* this is a normalised statistical distribution function
* describes the probability of energy state $E$ being occupied by an electron

#### behaviour of fermi-dirac function

* at low temperatures, $k_BT \ll E_F$
1. when $E < E_F \to \frac{E - E_F}{k_BT} \to$ large and negative
2. when $E > E_F \to \frac{E - E_F}{K_BT} \to$ large and positive, $f(E) \approx 0$
3. when $E \approx E_F$, transition from $f(E) = 1 \to f(E) = 0$ occurs over narrow neergy range around $E_F$ - width is about $k_BT$ on each side of $E_F$

* in systems with low densities of electrons, $f(E) \ll 1$
    * approximation, when $E_F \ll k_BT$:

    $$
    f(E) \approx \exp\left[-\left(\frac{E - E_F}{k_BT}\right)\right] \approx \exp\left(-\frac{E}{k_BT}\right)
    $$

    * this behaves like the classical system, very low $E_F$

#### free electron heat capacity

* can determine the electronic specific heat capacity using free electron model
* what happens when temperature is increased?
* only small proportions of electrons will increase their energy - those that are within $k_BT$ of $E_F$
* we require am empty electron state for the excited electron to move to
* electrons within region $k_BT$ of $E_F$ will absorb thermal energy
* assume number of electrons with energy close to $E_F$ is given by $n(E_F)k_BT$
* extra energy acquired by electron is $k_BT$

$$
    U(T) - U(0) = n(E_F)(k_BT)^2 - \text{ only for electrons}
$$

* $n(E_F)$ is the density of states at Fermi energy

$$
    C_V = \frac{dU}{dT} \approx 2n(E_F)k_B^2T
$$

* note that this assumes $n(E_F)$ is constant over energy range

$$
    \begin{aligned}
    n &= \frac{(E_F2m_e)^{3/2}}{3\pi^2\hbar^3} \\
    N &= n(E_F)E_FV \\
    n(E_F) = \frac{3}{2}\frac{N}{E_F} \\
    C_V \approx \frac{3}{2}k_BT\left(\frac{2k_BT}{E_F}\right)
    \end{aligned}
$$

* specific heat capacity is modified from classical value by bracketed factor
* electronic specific heat capacity is proportional to temperature

## Lecture 11

### magnetic properties of free electrons

* Free electron model can predict magnetic properties
* how does metal respond when placed in magnetic field?

#### magnetic susceptibility of metals

* metals develop an induced magnetic moment in magnetic fields
* interactions between B-feild and electron spin
* it is known all materials show a weak paramagnetism which is independent of temperature
    * this is parallel to apllied field
* use free electron model to demonstrate this observed effect 
* electrons have a magnetic moment due to spin:

$$
    \mu_B = \frac{e\hbar}{2m_e} = 9.27\times10^{-24}\,J\,T^{-1}
$$

* energy of electron will change in field by $\pm \mu_B$ depending on spin
* assume equal numbers of $\pm$ spin for electons 
    * parallel
    * anti-parallel
* when B field applied:
    * half of electrons increase energy by:

    $$
        + \frac{e\hbar}{2m_e}B \text{ - antiparallel}
    $$

    * half of electrons reduce energy by:

    $$
        - \frac{e\hbar}{2m_e}B \text{ - parallel}
    $$

* total energy of system can be reduced if some electrons reverse spins
* a proportion of electrons with antiparallel spins can reverse spins to reduce overall energy
* how many electrons reverse spin?
    * need to have the same Fermi energy for spin up and spin down electrons
* density of states function evaluated at $E_F$ multiplied by change in energy gives number of electrons
* number of electrons within $\mu_BB$ of the original Fermi energy: $ne = \frac{1}{2}n(E_F)\mu_BB$
* difference in population: $n(E_F)\mu_BB$ - number of electrons with spin up increased by this amount
* net magnetic moment: $n(E_F)\mu_B^2B$ - produces net magnetic moment per unit volume

$$
    M = \frac{\mu_B^2Bn(E_F)}{V}
$$

* paramagnetic susceptibility, a measure of how easy it is to magnetise system:

$$
    \begin{aligned}
    \chi &= \frac{\partial M}{\partial H}, H = \frac{M}{\mu_0}
    \chi &= \mu_0\mu_B^2\frac{n(E_F)}{V}
    \end{aligned}
$$

* this is called the Pauli Paramagnetism - it is independent of temperature
* at finite temperatures, temperature dependence of Fermi distribution will lead to a small temperature dependence

### hall effect

* observed in 1879
* consider current density, $j$, flowing along bar in $x$ direction:
* apply perpendicular magnetic field, $B$
* electrons experience Lorentz force - $F = e(v\times B + E)$
* electrons are pushed to one side of metal bar by this force
* electric field will compensate for motion due to Lorentz force - $eE_y = -F \implies E_y = -v\times B$
* current density, $j = nev$

$$
    E_y = -\frac{1}{ne}j\times B, \frac{1}{ne} = R_H
$$

* $R_H$ is the Hall coefficient
* the sign of the Hall coefficient shows the charge on the carriers
    * some metals, however, have positive Hall coefficient

## Lecture 12

### nearly free electron model

* free electron model - ignored some interactions:
    1. electron-atoms - free electron approximation
    2. electron-electron - independent electron approximation
* nearly free electron model includes electron-atom interactions
* failures of free electron model:
    * temperature dependence of conductivity
    * some metals have a positive Hall coefficient
* interaction between electrons and crystal lattices?
    * lattice $\underline{R} = n_1\underline{a}_1 + n_2\underline{a}_2 + n_3\underline{a}_3$, where $\underline{a}_1,\underline{a}_2,\underline{a}_3$ are lattice vectors

### bloch theorem

* this is a consequence of periodic properties of crystals 
    * provides insights into behaviour of electrons in periodic potnetial Bloch states
    * describes electrons moving in periodic potential
* consider a 10 crystal (line of atoms). $\psi(x)$ is solution satisfying time-independent Schrodinger equation
    * Schrodinger equation has periodic potential $V(x)$ representing atoms
    * energy eigenvalues, $\sigma$
* schrodinger equation evaluated at $(x+R)$ must give same solution as as $(x)$
    * local electronic environment at $x$ and $x+R$ are identical
    * have second solution $\phi(x)$ which also satisfies the Schrodinger equation with energy $E$
    * Assume $\psi$ and $\phi$ are unique solutions, can write $\phi(x) = \psi(x+R)$
    * $R$ is lattice vector $=na$
    * $\psi(x+R) = c(R)\psi(x)$ where $c(R)$ is a constant equal to $1$
* using series of lattice translations, $c(R_1+R_2) = c(R_1)c(R_2)$
    * therefore $c(nR) = [c(R)]^n,~ n \in \mathbb{N}$
* wavefunction must satisfy boundary conditions (periodic over M lattice translation where $Ma = l$, the length of 10 crystals)
* bloch theorem brings together two requirements to satisfy both periodic bonding conditions and lattice translation by $n_1a_1$ where $n_1$ is an integer
* from this we have $\psi(x+Ma) = \psi(x) \implies [c(a)]^M = 1$
    * a functions that satisfies replacement for $c(a) = \exp[ika]$, where $ka = \frac{2\pi l}{M}$ ($l \in \mathbb{Z}$)
* for any lattice translation, $\underline{R} = m\underline{a}$ ($m \in \mathbb{Z},\underline{a}$ is lattice constant)
    * $c(R) = [c(a)]^M \equiv \exp[iMka] = \exp[ikR], R = \frac{2\pi l}{L}$ - $l \in \mathbb{Z}$, $L$ is the total dimensino of sample
* these statments set oit bloch's theorem - they explain the difference between free electron and nearly free electron models
* free electron model $\psi(x) = C\exp[ikx]$ - plane wave with constant energy $E$, $k$ is the electron wavevector
* nearly free electron model $\psi(x+R) = C\exp[ik(x+R)] = C\exp[ikR]\psi(x) = Cu_k(R)\psi(x),~ u_k(R)$ is the bloch function
* the bloch theorem tellls us that nearly free electron wavefunctions (weak periodic potential) are composed of two parts:
    1. plane wave free electron behaviour, $C\exp[ikx]$
    2. modulated in intensity by bloch function, $u_k(R)$, has periodicity of lattice
    * fundamental nature of $\psi$ is still free electron behaviour, but with a modification

#### consequences of bloch theorem

* adding multiples of $\frac{2\pi}{a}$ to bloch wavevectors does not alter solution $\psi$
    * only $k$ values in $\frac{2\pi}{a}$ range are physically distinct
    * all other values can be mapped into unique range 
* convention is to define this as $-\frac{\pi}{a} \to \frac{\pi}{a}$
    * this corresponds to the first brillouin zone

#### energy band diagrams

* shows electron behaviour in terms of energy and wavevector - free electron model $E = \frac{\hbar^2k^2}{2m_e}$
* branches of $E(k)$ curve are moved into first brillouin zone

## Lecture 13

### nearly free electron energy bands

* physical origin of energy gaps and energy bands:
    1. bragg reflection - electronw aves can scatter from planes of atoms. Weak periodic potentiation Schrodinger equation. Gives corresponding values for energy gaps at $k = \frac{n\pi}{a}$
    2. interference at certain wavelengths, get interference between electron waves and atoms

#### energy bands

* describe relationship between eenrgy and wavevector
* electrons of different '$k$' propagate at different velocities - dispersion
* travelling wave group velocity:

$$
    v_g = \frac{d\omega}{dk}
$$

* For electron:

    $$
    v_g = \frac{1}{\hbar}\frac{dE(k)}{dk}
    $$

* velocity of Block electrons (know $E = \frac{\hbar^2k^2}{2m_e}$). This gives:

$$
    v_g = \frac{1}{\hbar}\frac{d}{dk}\left(\frac{\hbar^2k^2}{2m_e}\right) = \frac{\hbar k}{m_e} = \frac{p}{m} = vk
$$

_$\hbar k$ is the crystal momentum_

* crystal momentum is the momentum an electron has as a result of interacting with periodic potential   
  exhibits different physical parameters

#### current carried by energy bands

* we know that the current density is $j = ne\langle v\rangle$, where $n \equiv$ electron density, $\langle v\rangle \equiv$ average velocity

$$
    \langle v\rangle = \frac{1}{\hbar}\int_{k=-\frac{\pi}{a}}^{k=\frac{\pi}{a}} \frac{dE}{dk}dk\,\frac{a}{2\pi}
$$

* consider $k = \frac{\pi}{a}$ nd $k = -\frac{\pi}{a}$  
  these are physically equivalent states (from Block theorem)  
    * tells us that $E\left(\frac{\pi}{a}\right) = 0 = E\left(-\frac{\pi}{a}\right)$

$$
    \langle v\rangle = \frac{a}{2\pi\hbar}\left[E\left(\frac{\pi}{a}\right) - E\left(-\frac{\pi}{a}\right)\right] = 0
$$

* above implies average velocity of fulled energy band is zero, as is current density
* completely filled energy band carries no electrical current (insulators)
* current carried by partially filled bands (metals or semiconductors)

### equation of motoin for block electrons

* consider force $F$ applied to electron - $Fv_g =$ rate of work being done

$$
    \begin{aligned}
    Fv_g &= \frac{dE}{dt} = \frac{dE}{dk}  \times \frac{dk}{dt} \\
    v_g &= \frac{1}{\hbar}\frac{dE}{dk} \\
    \implies F &= \hbar\frac{dk}{dt}
    \end{aligned}
$$

* can predict how electron will respond in electric field

### effective mass

* electrons in bloch states move as though the mass of electron is different form free electron masses
* consider $E(k)$ relationship near band edge at $k = k_0$ where $\frac{dE}{dk} = 0$ (i.e. zero group velocity)
* general form given by $E = E(k_0) + \frac{1}{2}A(k - k_0)^2$  
  group velocity: $v_g(k) = \frac{A(k-k_0)}{\hbar}$ - compare with free electrons, where we have $v_{free} = \frac{p}{m_e} = \frac{\hbar k}{m_e}$
* electrons behave as though they have an effective mass of $m_{eff} = \frac{\hbar^2}{A_{}}$
* from taylor's theorem, we can show that $A = \frac{d^2E}{dk^2}\Big|_{k=k_0}$

$$
    m_{eff} = \hbar^2\left[\frac{d^2E}{dk^2}\right]^{-1}_{k=k_0}
$$

* second derivative is curvature - when $E \propto k^2$ then $m_{eff_{}}$ is constant  
  some regions of $m_{eff_{}}$ are positive, some regions are negative  
  negative mass $\implies$ electrons slow down in electric field, force is in opposite direction

### electrons and holes

* an energy band which is nearly filled has some vacant energy states near top of energy band   
  consider vacant states of holes - charge of $+e$   
  equivalent to negative effective mass   
  hole wavevector $k_h = -k_e$, energy $E(k_h) = - E(k_e), v_h = v_e$

1. if energy band is full there is no current
2. if energy band is partially full then electrons with $m_{eff_{}} describe electrical response
3. if energy band is almsot completely filled, then holes with negative $m_{eff_{}}$, positive charge
