# Optics

## Lecture 1

### Intro

* _Always assume $\mathcal{E}$ is vector in these notes_

* Cover Optics f2f:
    * Early chapters are mainly covered
    * 5, 6, 7 cover limited or not at all
    * first halves of 8 and 9  

#### Timeline

* Pre-1700 - Huygens supported waves
* 1705 - Newton supported particles
* 1800s - Young and Fresnel experiments showed waves
* Maxwell's equations supported this
* 1900s: deBroglie showed duality
* 1972: Photons exist

### Wave Optics

* waves of photons carry momentum:

$$
    \underbrace{p}_{particle} = \underbrace{\frac{h}{\lambda}}_{wave}
$$


### Maxwell's Wave Equations

$$
    \nabla \times \mathcal{E} = -\frac{\partial \mathcal{B}}{\partial t} $$ $$
    \nabla \times \mathcal{B} = \mu_0 \epsilon_0 \frac{\partial \mathcal{E}}{\partial t} $$ $$
    \nabla \cdot \mathcal{E} = 0 $$ $$
    \nabla \cdot \mathcal{B} = 0
$$

* Leads to

$$
    \nabla^2 \mathcal{E} = \frac{1}{c^2}\frac{\partial^2 \mathcal{E}}{\partial t^2} = 0 $$ $$
    \nabla^2 \mathcal{B} = \frac{1}{c^2}\frac{\partial^2 \mathcal{B}}{\partial t^2} = 0
$$

### Harmonic Wave Solution

* In a vacuum (or air),

$$
    |\underline{\mathcal{E}}| \approx \frac{|\underline{\mathcal{B}}|}{c}
$$

* Harmonic wave solution from this, giving monochromatic light

$$
    \mathcal{E} = \mathcal{E}_0 \cos(\underline{k}\cdot\underline{r} - \omega t)
$$

1. $\mathcal{E}$ is a vector, to do with polarisation
2. $\underline{k}$ is the wave vector, it sets the direction of propagation

* Choose $\underline{k}$ along the z-axis (the optical axis)
* Consider Figure 1.3 in _f2f_
    * optical waves are too fast to detect
    * instead we measure time-average intensity

##### Spatial Frequency

$$
    \text{Frequency} = \text{number of waves per unit time},~ s^{-1} (Hz) $$ $$
    \text{Spatial Frequency} = u = \text{number of waves per unit distance},~ m^{-1} $$ $$
    u = \frac{1}{\lambda}
$$

* u is also called the wave number for harmonic waves, i.e. only moving on z-axis
* Consider a wave propagating at an angle $\theta$ relative to the z-axis, in the x-z plane
    * Figure 1.5
