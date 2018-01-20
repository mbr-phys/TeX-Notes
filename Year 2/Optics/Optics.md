---
title: "Foundations of Physics 2B"
author: "Charles Adams"
date: "Michaelmas 2017 - Epiphany 2018"
---

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

## Lecture 2

### Recap
$$
    \underline{k}\cdot\underline{r} = k_xx + k_yy + k_zz $$ $$
    z: \frac{\lambda}{\cos\theta} $$ $$
    x: \frac{\lambda}{\sin\theta}
$$

* Spatial frequency is different depending on direction we are looking at

$$
    x: u = \frac{1}{\tfrac{\lambda}{\sin\theta}}
$$

* Look at magnitude of wave vector

$$
    |\underline{k}| = k = \sqrt{k_x^2 + k_z^2} \implies k_z = \sqrt{k^2 - k_x^2} $$ $$
    k = \frac{2\pi}{\lambda} ~;~ u = \frac{\lambda}{\sin\theta} $$ $$
    \implies k_x = k\sin\theta = \frac{2\pi}{\lambda}\sin\theta = \frac{2\pi}{\tfrac{\lambda}{\sin\theta}} = 2\pi u
$$

* $k_x$ is the rate of phase variation along $x = 2\pi \times$ number of waves per unit length along x

$$
    k_x = 2\pi u
$$

* Frequency in time:
    * $\nu~[Hz]$
    * angular frequency, $\omega = 2\pi\nu ~ [\text{rad } s^{-1}]$
* Spacial Frequency along x:
    * $u ~ [m^{-1}]$
    * angular spacial frequency, $k_x = 2\pi u ~ [\text{rad } m^{-1}]$

### Scalar Approximation

$$
    \begin{aligned}
    \mathcal{E} &= \mathcal{E}_0 \cos(\underline{k} \cdot \underline{r} - \omega t) \\
    \cos\phi &= \frac{1}{2}(e^{i\phi} + e^{-i\phi}) \\
    \implies \mathcal{E} &= \frac{\mathcal{E}_0}{2} \Big[e^{i(\underline{k}\cdot\underline{r} - \omega t)} + e^{-i(\underline{k}\cdot\underline{r} - \omega t)}] \\
    \mathcal{E} &= \mathcal{E}_0 e^{i(\underline{k}\cdot\underline{r} - \omega t)} \text{ - shorthand to write this form}
    \end{aligned}
$$

* Complex notation, but scalar approximation:

$$
    \mathcal{E}_0 = (\mathcal{E}_{0x}, \mathcal{E}_{0y}, \mathcal{E}_{0z})
$$

* Assume linearly polarising light with $\mathcal{E}_0$ along y

$$
    \mathcal{E}_0 = (0, \mathcal{E}_0, 0)
$$

* Scalar approximation:

$$
    \mathcal{E} = \mathcal{E}_0 e^{i(\underline{k}\cdot\underline{r} - \omega t)}
$$

* This is a good approximation exceot for problems involving polarization effects or strong focusing

* $\mathcal{E}_0$ is the amplitude of the wave, leads to two cases of interest:

1. Plane waves - Amplitude is constant, independent of space and time
    * mathematical idealisation, but can be a good approximation of a field in a particular locality.

2. Spherical waves - replace $\mathcal{E_0}$ by $\frac{\mathcal{E}_0}{ikr}$
    * wavefronts are curved

$$
    \mathcal{E} = \frac{\mathcal{E}_0}{ikr} e^{i(\underline{k}\cdot\underline{r} - \omega t)}
$$

* $\underline{k}$ is in the direction of $\underline{r}$:
    * $\underline{k}\cdot\underline{r} = kr$

$$
    \mathcal{E} = \frac{\mathcal{E}_0}{ikr} e^{i(kr - \omega t)}
$$

#### Principle of Superposition

* _If $\mathcal{E}_1$ and $\mathcal{E}_2$ are solutions of the wave equation, then $\mathcal{E}_1 + \mathcal{E}_2$ is also a solution_

* Any light field can be described as a sum of waves with planar or curved wavefronts

### Intensity

* _As the time dependence is too fast, we detect the time-averaged energy flux, or intensity_

#### Complex Plane Wave

$$
    \begin{aligned}
    I &= \frac{1}{2}\epsilon_0 c |\mathcal{E}|^2 \\
    &= \frac{1}{2}\epsilon_0 c \mathcal{E}_0^2 e^{i(\underline{k}\cdot\underline{r} - \omega t)}e^{-i(\underline{k}\cdot\underline{r} - \omega t)} \\
    &= \frac{1}{2}\epsilon_0 c \mathcal{E}_0^2 = I_0
    \end{aligned}
$$

* Recipe: From field, $\mathcal{E}$, to intensity -
    1. take modulus of field
    2. replace constant $\frac{1}{2}\epsilon_0 c \mathcal{E}_0^2$ by $I_0$

#### Spherical Wave

* This is also a mathematical idealisation
    * useful if field is far from the source
    * consider region around z-axis, $x, y \ll z$
        * this is called the paraxial regime

## Lecture 3

* Plane waves - unique $\underline{k}$
* Spherical waves - isotropic $\underline{k} \perp $ to wavefront

### Paraxials

#### Spherical

* Spherical waves are only valid in regions near the z (optical) axis

$$
    r = \sqrt{x^2 + y^2 + z^2} = z\sqrt{1 + \frac{x^2 + y^2}{z^2}} $$ $$
    \fbox{$(1 + \alpha)^n \approx 1 + n\alpha$} $$ $$
    r \approx z\Big(1 + \frac{1}{2}\frac{x^2 + y^2}{z^2}\Big) = z + \frac{x^2 + y^2}{2z}
$$

* Rewrite wave equation

$$
    \mathcal{E} = \frac{\mathcal{E}_0}{ikz}e^{ikz}e^{\frac{ik(x^2 + y^2)}{2z}}
$$

* $\lambda \ll z \implies r \to z$

#### Cylindrical

* Planar in y direction, curved in xz plane, i.e. cylindrical wave

$$
    \mathcal{E} = \frac{\mathcal{E}_0}{\sqrt{ikz}}e^{ikz}e^{\frac{ik(x^2 + y^2)}{2z}}
$$

* Different denominator comes from Intensity proportionality

### Lenses

* Lenses convert planar to curved wavefronts
* Light inside a medium propagates with a wave vector with modified magnitude $nk$, where $n$ is the refractive index.
* page 38

$$
    f = \frac{R}{n - 1} $$ $$
    \mathcal{E}^{(\mathcal{L})} = \mathcal{E}^{(0)}e^{-\frac{ik\rho'^2}{2f}}
$$

* Field above is immediately after the lens
* $\mathcal{E}^{(z)}$ denotes the field in the plane at z
* $\mathcal{E}^{(0)}$ denotes the field in the plane $z = 0$

* Lens imprint a phase that depends quadratically on the transverse displacement

$$
    \rho' = \sqrt{x'^2 + y'^2}
$$

* Introduced dashed variables specifically for the $z = 0$ plane.
    * Resver $x,y,\rho$ for a distance z donwstream.

## Lecture 4

### Lenses Continued

* Lens operator:

$$
    e^{-i\frac{k\rho'^2}{2f}}
$$

* See Fig 2.15 in notes, page 39

$$
    \begin{aligned}
    \mathcal{E}^{(0)} &= \frac{\mathcal{E}_0}{ks_1} e^{i\frac{kx'^2}{2s_1}} \\
    \mathcal{E}^{(\mathcal{L})} &= \frac{\mathcal{E}_0}{ks_1}e^{i\frac{kx'^2}{2s_1}}e^{-i\frac{kx'^2}{2f}} \\
    &= \frac{\mathcal{E}_0}{ks_1}e^{i\frac{k}{2}(\frac{1}{s_1} - \frac{1}{f})x'^2} \\
    \mathcal{E} &= \frac{\mathcal{E}'_{0}}{ks_{2}}e^{-i\frac{kx'^2}{2s_2}} \\
    \implies \frac{1}{s_1} &- \frac{1}{f} = -\frac{1}{s_2}
    \end{aligned}
$$


* Thin lens formula:

$$
    \frac{1}{s_1} + \frac{1}{s_2} = \frac{1}{f} $$ $$
    \frac{1}{u} + \frac{1}{v} = \frac{1}{f}
$$

### Interfering Waves

* pages 46 to 51
* For two slits, assume isotropic in vertical direction

#### Plane Waves

$$
    \begin{aligned}
    \mathcal{E} &= \mathcal{E}_0 e^{i(k_1\cdot r - \omega t)} + \mathcal{E}_0 e^{i(k_2\cdot r - \omega t)} \\
    \mathcal{E} &= \mathcal{E}_0 e^{i(k_1\cdot r - \omega t)} \Big[1 + e^{i(k_2 - k_1)\cdot r} \Big] \\
    \mathcal{I} &= \mathcal{I}_0 \Big[1 + e^{i(k_2 - k_1)\cdot r} \Big]^2 \\
    &= 2\mathcal{I}_0 \{1 + \cos[(k_2 - k_1)\cdot r]\}
    \end{aligned}
$$

* For two plane waves at angles $\pm \frac{\alpha}{2}$ relative to z:

$$
    \begin{aligned}
    \mathcal{E} &= 2\mathcal{E}_0 e^{i[k\cos(\alpha/2)z - \omega t]}\cos[k\sin(\alpha/2)x] \\
    \mathcal{I} &= 4\mathcal{I}_0 \cos^2[k\sin(\alpha/2)x]
    \\ &= 2\mathcal{I}_0 \{1 + \cos[2k\sin(\alpha/2)x]\} \\
    \Lambda &= \frac{\lambda}{2\sin(\alpha/2)}
    \end{aligned}
$$

* $\Lambda$ is the distance between maxima in the interference pattern
    * small angle leads to this being large
        * fringes are more widely spread when close together
    * inverse is spatial frequency

#### Cylindrical Waves (Young's Slits)

* page 50 for the **Fresnel approximation**

## Lecture 11

### Fraunhofer Diffraction

Fresnel Diffraction Integral (field uniform in y direction):

$$
    \begin{aligned}
    \mathcal{E}^{(z)} &= \frac{\mathcal{E}_0}{\sqrt{i\lambda z}} \int_{-\infty}^{\infty} f(x') e^{ikr_p}\,dx' \\
    r &= [(x - x') + z^2]^2 \\
    r_p &= z + \frac{(x - x')^2}{2z} \\
    z &> |x - x'| \\
    r_p &= z + \frac{x^2}{2z} - \frac{xx'}{z} + \frac{x'^2}{2z}
    \end{aligned}
$$

For the Fraunhofer Approximation, there are two cases:

1. Far-field -

$$
    z > |x'| \implies \frac{x'^2}{2z} \approx 0 \implies e^{\frac{ikx'^2}{2z}} \approx 1
$$

2. Focal plane of a lens -

$$
    f(x') \to f(x') e^{-\frac{ikx'^2}{2f}}
$$

So at $z = f$, the $x'^2$ term cancels.

* In case 1, can write the intensity at z as

$$
    \mathcal{I}^{(z)} = \frac{\mathcal{I}_0}{\lambda z} \int_{-\infty}^{\infty} f(x')e^{-\frac{ikxx'}{z}} dx'
$$

* In case 2, the intensity at z = f in the focal plane of a lens is

$$
    \mathcal{I}^{(f)} = \frac{\mathcal{I}_0}{\lambda f} \int_{-\infty}^{\infty} f(x')e^{-\frac{ikxx'}{f}}dx'
$$

#### Example: Slit

For a slit of width $a$,

$$
    \begin{aligned}
    f(x') = \begin{cases} 1 & |x| \leq \frac{a}{2} \\ 0 & x > \frac{a}{2} \end{cases} \\
    f(x') = \text{rect}\Big(\frac{x'}{a}\Big)
    \end{aligned}
$$

#### Fraunhofer diffraction formula

$$
    \begin{aligned}
    \mathcal{I}^{(z)} &= \frac{\mathcal{I}_0}{\lambda z} \Bigg| \int_{-\infty}^{\infty} f(x')e^{-\frac{ikxx'}{z}}dx'\Bigg|^2 \\
    &= \frac{\mathcal{I}_0}{\lambda z} \Bigg|\int_{-\frac{a}{2}}^{\frac{a}{2}} e^{-\frac{ikxx'}{z}}dx'\Bigg|^2 \\
    \int_{-\frac{a}{2}}^{\frac{a}{2}} e^{-\frac{ikxx'}{z}}dx' &= \frac{z}{-ikx}e^{-\frac{ikxx'}{z}} \Bigg|^{\frac{a}{2}}_{-\frac{a}{2}} = \frac{z}{-ikx} (e^{-\frac{ikxa}{2az}}-e^{\frac{ikxa}{2a}}) \\
    &= \frac{\lambda z}{\pi x} \frac{1}{2i}(e^{\frac{ikxa}{2az}}-e^{-\frac{ikxa}{2a}}) \\
    &= \frac{\lambda z}{\pi x} \sin\Big(\frac{kxa}{2z}\Big) \\
    &= a\text{sinc}\Big(\frac{\pi xa}{\lambda z}\Big) ~[\text{sinc}\alpha = \frac{\sin\alpha}{\alpha}] \\
    \mathcal{I}^{(z)} &= \frac{\mathcal{I}_0}{\lambda z} a^2 \text{sinc}^2\bigg(\frac{\pi a x}{\lambda z}\bigg) ~[\lim_{\alpha \to 0}\text{sinc}\alpha = 1] \\
    x &= \pm \bigg(\frac{\lambda}{a}\bigg)z ~~ [\text{1st zero}]
    \end{aligned}
$$

Considering fringe pattern, $\Delta\theta$ from middle of pattern is

$$
    \Delta\theta = \frac{\lambda}{a}
$$

The angular spread of the diffraction pattern ($\Delta\theta$) is inversely proportional to the initial width, $a$.  
Intensity on axis is proportional to $a^2$:  
* One factor of $a$ from more light for wider slit and another factor because it spreads out less

## Lecture 12   

Fraunhofer diffraction is a special case of Fresnel

2 cases:

### 1. Far field

$z \gg x',y'$

$$
    \mathcal{I}^{(z)} = \frac{\mathcal{I}_0}{\lambda z} \Bigg[\int_{-\infty}^{\infty} f(x)e^{-i2\pi xx'/\lambda z}dx'\Bigg]^2
$$
 This is a Fourier transform of $f(x')$ where the Fourier variable is $u = \frac{x}{\lambda z}$

$$
    \int_{-\infty}^{\infty} f(x')e^{-i2\pi ux'}dx = \mathcal{F}[f(x')](u)
$$

Fraunhofer diffraction pattern is proportional to the Fourier transform of the input field all squared.

#### Example

slid of width $a$

$$
    \begin{aligned}
    f(x') &= \begin{cases} 1 & |x'| \leq \frac{a}{2} \\ 0 & |x| > \frac{a}{2} \end{cases} \\
    \mathcal{I}^{(z)} &= \frac{\mathcal{I}_0 a^2}{\lambda z}\text{sinc}^2\bigg(\frac{\pi ax}{\lambda z}\bigg) \\
    \Delta\theta &= \frac{x_{bb?}}{z} = \frac{\frac{\lambda}{a}z}{z} = \frac{\lambda}{a}
    \end{aligned}
$$

These results are valid in the Far-field.  
How is Far-field defined?

The Far-field is when the angular spread due to diffraction dominates over the initial size.  
Cross over between initial size determines width of light distribution and diffraction determines width of light distribution when width due to diffraction, $\Delta\theta z = a$

Rayleigh distance:

$$
    \begin{aligned}
    \Delta\theta &= \frac{\lambda}{a}, ~ z = d_R \\
    \Delta\theta d_R &= a \\
    d_R &= \frac{a^2}{\lambda}
    \end{aligned}
$$

1. $z < d_R$ - near field, use Fresnel diffraction integral
2. $z \gg d_R$ - far-field, Fraunhofer approximation and diffraction formula applies

### Case 2 of Fraunhofer diffraction

Focal plane of a lens

$$
    \mathcal{I}^{(z)} = \frac{\mathcal{I}_0}{\lambda z} a^2 \text{sinc}^2\bigg(\frac{\pi ax}{\lambda f}\bigg)
$$

Applies when $z = f$

Width of diffraction pattern is now smaller than initial size.

### Double slit

$$
    \mathcal{I}^{(z)} = \frac{\mathcal{I}_0}{\lambda z} \Bigg[\int_{-\infty}^{\infty} f(x)e^{-i2\pi xx'/\lambda z}dx'\Bigg]^2
$$

For slit at $x' = \frac{d}{2}$, integral is

$$
    \int_{\frac{d}{2}-\frac{a}{2}}^{\frac{d}{2}+\frac{a}{2}} e^{-i2\pi xx'/\lambda z}dx'
$$

By shifting x' axis by $\frac{d}{2}$, we find

$$
    \begin{aligned}
    &= e^{-i\pi xd/\lambda z}\int_{-\frac{a}{2}}^{\frac{a}{2}} e^{-i2\pi xx'/\lambda z}dx' \\
    \int_{-\infty}^{\infty} f(x')e^{-i2\pi xx'/\lambda z}dx' &= (e^{i\pi xd/\lambda z} + e^{-i\pi xd/\lambda z})a\text{sinc}\bigg(\frac{\pi a x}{\lambda z}\bigg) \\
    \mathcal{I}^{(z)} &= \frac{4\mathcal{I}_0}{\lambda z}a^2\cos^2\bigg(\frac{\pi dx}{\lambda z}\bigg)\text{sinc}^2\bigg(\frac{\pi a x}{\lambda z}\bigg)
    \end{aligned}
$$

Missing order in the interference pattern at $m = \frac{d}{a}$, envelope plot from last year

## Lecture 13

The electric field of a laser beam in the $z = 0$ plane is:

$$
    \mathcal{E}^{(0)} = \mathcal{E}_0 e^{-(x'^2 + y'^2)/w_0^2}
$$

This is called a Gaussian beam  
The radius of the laser is $w_0$  
The intensity of the laser is:

$$
    \mathcal{I}^{(0)} = \mathcal{I}_0 e^{-2(x'^2 + y'^2)/w_0^2}
$$

$w_0$ is the distance at which the intensity falls to $\frac{\mathcal{I}_0}{e^2}$ ($\frac{1}{e^2}$ radius)  
Calculate far-field intensity of a laser beam using Fraunhofer diffraction  
Diffraction in both x and y dimensions (2D Fraunhofer)

$$
    \begin{aligned}
    \mathcal{I}^{(z)} &= \frac{\mathcal{I}_0}{\lambda^2z^2}\left[\int_{-\infty}^{\infty} f(x',y')e^{-i2\pi(xx'+yy')/\lambda z}dx'\,dy' \right]^2
    \end{aligned}
$$

If we can write $f(x',y') = g(x')h(y')$ then the diffraction pattern is _cartesian separable_

$$
    \begin{aligned}
    \mathcal{I}^{(z)} &= \frac{\mathcal{I}_0}{\lambda^2z^2} \left[\int_{-\infty}^{\infty} g(x')e^{-i2\pi xx'/\lambda z}dx'\right]^2 \left[\int_{-\infty}^{\infty}h(y')e^{-i2\pi yy'/\lambda z}dy'\right]^2
    \end{aligned}
$$

For laser:

$$  
    f(x',y') = e^{-(x'^2 + y'^2)/w_0^2} = e^{-\frac{x'^2}{w_0^2}}e^{-\frac{y'^2}{w_0^2}} = g(x')h(y')
$$

x' integral:

$$
    \begin{aligned}
    \int_{-\infty}^{\infty} g(x')e^{-i2\pi xx'/\lambda z}dx' &= \int_{-\infty}^{\infty} e^{-\frac{x'^2}{w_0^2}}e^{-i2\pi xx'/\lambda z}dx' \\
    q &= \frac{x'}{w_0} + \frac{i\pi w_0x}{\lambda z} \\
    q^2 &= \frac{x'^2}{w_0^2} + \frac{-2\pi xx'}{\lambda z} - \frac{\pi^2 w_0^2 x^2}{\lambda^2z^2} \\
    w_0e^{-\frac{\pi^2w_0^2x^2}{\lambda^2z^2}}\int_{-\infty}^{\infty} e^{-q^2} dq &= \sqrt{\pi}w_0 e^{-\frac{\pi^2w_0^2x^2}{\lambda^2z^2}}
    \end{aligned}
$$

For y' integral:

$$
    \begin{aligned}
    &= \sqrt{\pi}w_0e^{-\frac{\pi^2w_0^2y^2}{\lambda^2z^2}} \\
    \mathcal{I}^{(z)} &= \frac{\mathcal{I}_0}{\lambda^2z^2} \pi^2w_0^4 e^{-2\pi^2w_0^2(x^2 + y^2)/\lambda^2z^2} \\
    &= \frac{\mathcal{I}_0}{\lambda^2z^2} \pi^2w_0^4 e^{-2(x^2 + y^2)/w^2}
    \end{aligned}
$$

where $w$ is the far-field laser beam radius, i.e. from the slit to the position of observation

$$
    w = \frac{\lambda}{\pi w_0}z
$$

The angular spread of the laser:

$$\Delta\theta = \frac{w}{z} = \frac{\lambda}{\pi w_0}$$

Compare slit of width $a$ where

$$\Delta\theta = \frac{\lambda}{a}$$
