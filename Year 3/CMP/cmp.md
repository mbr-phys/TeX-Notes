---
title: "Condensed Matter Physics"
author: "Tom Lancaster and Others"
date: "Michaelmas 2018 - Epiphany 2019"
---

# Symmetry, Structure, and Excitations

## Lecture 1

__use alongside lecture notes given__

Solid:  
- Can support sheer stress
- Doesn't flow

Liquid:  
- Incompressible
- Can't support sheer stress
- Flows the fill volume, subject to remaining pressure
- Weaker forces ($\approx k_B T$)
- Less dense atoms/molecules

A gas, liquid, or amorphous solid is rotationally invariant   

N particles in a shell, what is $g(r)$?
$$
    g(r) = \frac{N}{4\pi r^2\delta r\langle n\rangle}
$$

For an ideal gas (point particles), $g(r)$ is just 1: 
- $\int_V \langle n \rangle g(r)\,dV = (N' - 1)$
- $\langle n \rangle V g(r) = (N' - 1) \implies g(r) = 1 - \frac{1}{N'}$

- Despite rigidity of ice, it can be seen to flow. 
- For enough stress, it will plastically deform (creep). 
- "Enough" is about 5 orders of magnitude less than expected for a perfect crystal. 
- Ice flows due to the motion of topological defects called dislocations. Electrons can scatter off them too. 
- The pdf does not enable us to easily extinguish between a liquid and amorphous solid. The difference is one of timscale for flow. 
- Therefore an arbitrary definition: "A solid is a material whose shear viscosity exceeds $10^{13.6} N\,s\,m^{-2}$"
    - this corresponds to a relaxation time of about a day

## Lecture 2

### Bonding in Condensed Matter
In general, inter-particle interactions produce a potential with the same type of form, usual potential well plot with repulsive and attractive forces.    
__image here from notes__

#### van der Waals bonding
Fluctuations (instantaneous in time) can lead to instantaneous dipole moments. 
Such dipoles create an electric field:   
$$
    E = \frac{p_1}{4\pi\epsilon_0 r^3},
$$  
where $p_1$ is the fluctuating dipole.
On a neighbouring atom, this field induces a dipole,   
$$
    \begin{align}
    p_2 &= \alpha|E| \\
    p_2 &= \alpha \frac{p_1}{4\pi\epsilon_0 r^3}
$$   
where $\alpha$ is the atomic polarisability.   
We have a dipole-dipole potential:  
$$
    U(r) = \frac{|p_1||p_2|}{4\pi\epsilon_0 r^3} = \frac{\alpha|p_1|^2}{(4\pi\epsilon_0)^2r^6}
$$  
- Note that $|p_1|^2$ does not average to zero even though p does, which implies that $U(r) \neq 0$.

If we have attractive interactions alone, our solid would collapse into a singularity. 
We need repulsion as well. 
Repulsion arises from the Pauli exclusion principle - no electrons (_fermions_) can have the same set of quantum numbers.
Born and Mayer parameterised this repulsion as   
$$
    U_{rep} = B_{ij}\exp{-\frac{r_{ij}}{p_{ij}}}
$$   
where $r_{ij}$ is distance between atom i and j. $p_{ij}$ and $B_{ij_{}}$ are constants.

Buckingham potential - Historically, a potential varying as $r^{-n}$ is easier to deal with and reasonably reproduces $f^n$ form. 

Lennard-Jones potential constants $\epsilon$ and $\sigma$ - parameters which can be found by experiment 

#### Ionic Bonding

When it's energetically favourable to transfer one or more electrons to a neighbour to acheive a closed shell configuration. 

$U_{\text{Madelung}_{}}$ is attractive interaction per mole of formular unit.

- Born-Mayer is very short-ranged

#### Metallic bonding

Metallic bonding resutls from delocalisation of electrons. 
The coulomb energy (attractive) can be found from a lattice sum (with negative charge background) and is $\propto \frac{1}{r}$.
Two results from FoP2B are required to understand the electronic contribution to energy. 
The average energy electron is   
$$
    \begin{align}
    \frac{E}{n} &= \frac{3}{5}E_F = \frac{3\hbar^2 k_{F}^2}{10m_e} \\
    k_F &= \left(3\pi^2\frac{N}{V}\right)^{1/3} \\
    k_F &\propto V^{-1/3} \\
    \implies \frac{E}{n} &\propto r_{0}^{-2} (\because V \propto r_{0}^{3}) \\
    U_{metal} &= U_{coul} + U_{kin} \\
    &= -\frac{a}{r_0} + \frac{b}{r_0^2}
    \end{align}
$$   
Metallic crystal cohesive energy is of order of a few eV per atom. 

## Lecture 3

### Hydrogen bonding

