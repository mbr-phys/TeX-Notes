---
title: "Stars and Galaxies"
author: "David Alaexander"
date: "Michaelmas 2017 - Epiphany 2018"
---

# Stars

_see DUO for pdf slides_

## Lecture 1

* Black body emission curve
    * LHS from peak lambda is Rayleigh Jeans tail
    * RHS from peak is Wien tail

$$
    \lambda_{max} = \frac{2.9 \times 10^{-3}}{T} \, m $$ $$
    \lambda_{max.\,Bet} = 8.3 \times 10^{-7}m \implies T \approx 3500\,K $$ $$
    \lambda_{max,Sun} = 5.5 \times 10^{-7}m \implies T \approx 5300\,K $$ $$
    \lambda_{max, Bel} = 3.0 \times 10^{-7} m \implies T \approx 9400\,K
$$

## Lecture 2

#### Excitation Energies

* Bohr model
* page 8 on slides

* n denotes the orbitals/electron shells
* $n = 1$ is the ground state

$$
    E = E_{high} - E_{low} = \frac{hc}{\lambda} = -13.6\Big(\frac{1}{n_{high}^2} - \frac{1}{n_{low}^2} \Big) $$ $$
    n = 2 \to 4 $$ $$
    E = 2.55\,eV \implies \lambda = 486.1\,nm \implies H\beta
$$

* this was absorption
* $H\beta$ is shorthand for Balmer series $\beta$
    * Optical light

$$
    n = 2 \to 1 $$ $$
    E = 10.2\,eV \implies \lambda = 121.6\,nm \implies Ly\alpha
$$

* this was emission
* $Ly\alpha$ is shorthand for Lyman series $\alpha$
    * UV light

* Photons emitted from de-excitation in random direction
    * statistics means we probably won't see this

#### Ratios of Excitation Levels

$$
    n = 2 \to 1 $$ $$
    \frac{N_2}{N_1} = \frac{g_2}{g_1} e^{-\frac{(E_2 - E_1)}{kT}} $$ $$
    g_1 = 2 ~;~ g_2 = 8 ~;~ T = 5800\,K $$ $$
    \frac{N_2}{N_1} = 5.1 \times 10^{-9}
$$

* 1 billionth of H atoms in first excited state, negligible

#### Ionisation Energies

* $\chi$ is the ionisation energy

$$
    \frac{N_{i + 1}}{N_i} = \frac{2Z_{i + 1}}{n_e Z_i} \Big(\frac{2\pi m_e kT}{h^2}\Big)^{\frac{3}{2}}e^{-\frac{\chi}{kT}} $$ $$
    E > -13.6\Big(\frac{1}{\infty^2} - \frac{1}{n_{low}^2} \Big)\, eV $$ $$
    n = 1 \to \infty \implies E > 13.6\,eV $$ $$
    n = 2 \to \infty \implies E > 3.4\,eV
$$

## Lecture 3

### Binary Star Systems

* slide 8, binary system
* look at the semi-major axes of the orbits of the two stars around the centre of mass of the system
    * $a_1$ and $a_2$ for $m_1$ and $m_2$

$$
    P^2 = \frac{4\pi^2 a^3}{G(m_1 + m_2)} $$ $$
    a = a_1 + a_2
$$

* Smaller semi-major axis means larger mass
* similar to see-saw

$$
    m_1 a_1 = m_2 a_2 \implies \frac{m_1}{m_2} = \frac{a_2}{a_1}
$$

* ratio of the semi-major axes gives ratio of masses
* actually measure $\alpha$, angle of separation:
    * for d, distance from us

$$
    \alpha_n = \frac{a_n}{d} \implies \frac{m_1}{m_2} = \frac{\alpha_2}{\alpha_1}
$$

#### Visual Binary Systems

##### Normal Example

* $d = 10\,pc ~;~ P = 200$ days
* $\alpha_1 = 0.02" ~;~ \alpha_2 = 0.08"$

$$
    a_1 = \alpha_1 d = 0.2\,Au ~;~ a_2 = a_2 = \alpha_2 d = 0.8\,Au $$ $$
    a = a_1 + a_2 = 1\,Au $$ $$
    m_1 + m_2 = \frac{4\pi^2 a^3}{GP^2} = 3.4 M_\odot = M_{tot} $$ $$
    \frac{m_1}{m_2} = \frac{\alpha_2}{\alpha_1} = \frac{a_2}{a_1} = 4.0 = M_{rot} $$ $$
    m_1 = \Big[\frac{M_{rot}}{1 + M_{rot}}\Big]M_{tot} = 2.72 M_\odot $$ $$
    m_2 = \Big[\frac{1}{1 + M_{rot}}\Big]M_{tot} = 0.68 M_\odot
$$   

##### Inclination Example

* For angled systems that aren't flat against our observations:

$$  
    \hat{\alpha}_n = \alpha_n \cos i $$ $$
    m_1 + m_2 = \frac{4\pi^2}{G} \Big(\frac{d}{\cos i}\Big)\frac{\hat{\alpha}^3}{P^2} $$ $$
    \hat{\alpha} = \hat{\alpha}_1 + \hat{\alpha}_2
$$

* Has no effect on mass ratios observed - $\cos$ cancels
* Above equation means the actual masses will be affected by the inclination

#### Spectroscopic Binaries

* Correcting for inclination:

$$
    v_{nr}^{max} = v_n \sin i
$$

* Assume $e << 1$

$$
    v_n = \frac{2\pi a_n}{P} $$ $$
    \frac{m_1}{m_2} = \frac{v_2}{v_1}
$$

* Same sort of stuff as visual binaries, but $\sin$ instead of $\cos$ basically

##### Special Case: Eclipsing Spectroscopic Binaries

* $i \approx 90^\circ$
* don't need any corrections etc

## Lecture 4

$$
    P = \underbrace{\frac{\rho kT}{\mu m_H}}_{\text{ideal gas law}} + \frac{1}{3}aT^4
$$

* Hydrostatic Equilibrium:
    * Pressure force = Gravitational force

$$
    \begin{aligned}
        P\,on\,dA &= [P(r + dr) - P(r)]dA \\
        &= dP\,dA \\
        Gravitational &= g\,\underbrace{\underbrace{dA\, dr}_{volume} \rho}_{mass},~ g = \frac{GM_r}{r^2} \\
        dP\,dA &= -g\rho\, dA\, dr \\
        \frac{dP}{dr} &= -\frac{GM_r \rho}{r^2} \\
        \frac{dM_r}{dr} &= 4\pi r^2 \rho \\
        M_r &= \frac{4}{3}\pi r^2 \rho \\
        \frac{dP}{dr} &= -G \frac{4}{3}\pi r \rho^2 \\
        \int_{P_s}^{P_c} dP &= -\frac{4}{3}\pi G \rho^2 \int_{R}^{0} r\,dr \\
        P_c &= \frac{2}{3}\pi G \rho^2 r^2,~ P_s = 0 \,at\, r = R\\
        &= \frac{2}{3}\pi Gr^2 \Big[\frac{3}{4}\frac{M}{\pi r^3}\Big]^2 \\
        &= \frac{3}{8\pi}\frac{GM^2}{R^4}
    \end{aligned}
$$

* Example for our sun:

$$
    M = 2\times10^{30} kg ~;~ R \approx 7\times10^8 m $$ $$
    P_c \approx 10^{14} N\,m^{-2} $$ $$
    P_{c,\, true} \approx 2\times10^{16} N\,m^{-2}
$$

* out as assumed uniform density

## Lecture 5

### Virial Theorem

$$
    \begin{aligned}
        \frac{dP}{dr} &= -\frac{GM\rho}{r^2} \times V = \frac{4}{3}\pi r^3 \\
        V\frac{dP}{dr} &= -\frac{GM\rho}{r^2}\frac{4}{3}\pi r^3 \\
        &- \text{plug in }\frac{dm}{dr} = 4\pi r^2 \rho \\
        V\frac{dP}{dr} &= \frac{1}{3}\frac{GM}{r}\frac{dm}{dr} \\
        \int_{0}^{P(R)} V\,dP &= -\frac{1}{3} \underbrace{\int_{0}^{M} \frac{GM}{r}dm}_{\text{Total GPE} = U} \\
        LHS: \int U\,dV &= UV - \int V\,dU \\
        \int_{0}^{P(R)} V\,dP &= \underbrace{[PV]_{0}^{R_{0}}}_{= 0} - \int_{0}^{V(R)} P\,dV = -\frac{1}{3} U \\
        -3 \int_{0}^{V(R)} P\,dV &= U, ~ dV = \frac{dm}{\rho} \implies \\
        -3 \int_{0}^{M} \frac{P}{\rho} dm &= U ~ \text{ - generalised form of Virial Theorem} \\
        \text{Ideal Gas: } P &= nkT = \frac{\rho kT}{\mu m_{H}} \\
        \text{Average KE: } &= \frac{3}{2}kT \\
        \text{KE per kilo: } &= \frac{3}{2} \frac{kT}{\mu m_{H}} \\
        E_{KE} &= \frac{3}{2} \frac{kT}{\mu m_{H}} = \frac{3}{2}\frac{P}{\rho} \\
        -3 \int_{0}^{M}\frac{P}{\rho}dm &= U,~ \frac{P}{\rho} = \frac{2}{3}E_{KE} \\
        \underbrace{\int_{0}^{M} E_{KE} \,dm}_{\text{Total KE, assume ideal gas}} &= -\frac{1}{2} U \\
        \implies K &= -\frac{1}{2}U
    \end{aligned}
$$

### Energy from Gravitational Collapse

$$
    \begin{aligned}
        dU_{g,i} &= -\frac{GM_{r}dm_{i}}{r} \text{ - GPE of point mass} \\
        \text{Consider }& \text{shells of material} \\
        dm &= 4\pi r^2 \rho dr \\
        dU_{g} &= -\frac{GM_r 4\pi r^2 \rho}{r}dr \text{ - GPE of a shell} \\
        U_g &= -4\pi G \int_{0}^{R} M_r \rho_r dr \\
        M_r &= \frac{4}{3}\pi r^3 \bar{\rho} \text{ - avg density isn't too bad here} \\
        U_g &= -\frac{16}{3}\pi^2 G\bar{\rho}^2 \int_{0}^{R} r^4 dr \\
        &= -\frac{16}{15}\pi^2 G\bar{\rho}^2 R^5 \\
        \text{Convert} &\text{ back to mass} \\
        U &= -\frac{9}{15}\frac{GM^2}{R} \text{ - GPE of the star} \\
        K &= -\frac{1}{2} U \\
        \implies E &= \frac{3}{10}\frac{GM^2}{R} \\
        E &\approx \frac{3}{10} GM^2 \Big[\frac{1}{R} - \frac{1}{R_{initial}}\Big] \\
        &= \frac{3}{10}\frac{GM^2}{R} \iff R << R_{initial}
    \end{aligned}
$$

## Lecture 6

### Binding Energies of Fusion

$$
    \begin{aligned}
    E_b(Z,N) &= \Delta mc^2 = [Zm_p + Nm_n - m(Z, N)]c^2 \\
    E_b(4,0) &= [4m_p - m_{He,4}]c^2 = 26.731\,MeV \\
    \frac{4m_p}{m_{He,4}} &= 1.007 \implies  e = 0.7\% \\
    E_{\odot} &= (0.1\times M_\odot)\times0.007\times c^2  \\
    &= 1.3\times10^{44}J \\
    t &\approx \frac{E_\odot}{L_\odot} = 10^{10}yr
    \end{aligned}
$$

### Coulomb Barrier

* looking at probability that two particles are close enough for nuclear force to be important
* see figure on page 7 of slides
* using classical physics, we get

$$
    \begin{aligned}
    E &= \frac{1}{2}mv^2 = \frac{3}{2}kT = \frac{1}{4\pi\epsilon_0}\frac{Z_1Z_2e^2}{r} \\
    T &= \frac{1}{6\pi\epsilon_0}\frac{Z_1Z_2e^2}{rk} = \underbrace{1.1\times10^{10}K}_{r = 10^{-15}m ~;~ Z_1 = Z_2 = 1}
    \end{aligned}
$$

* too high for our Sun
* use deBroglie wavelength and consider quantum effects

$$
    \begin{aligned}
    \lambda &= \frac{h}{p},~ p = mv ~[m = \mu_m] \\
    E &= \frac{1}{2}mv^2 ~;~ v^2 = \frac{p^2}{m^2} \\
    E &= \frac{p^2}{2m} \\
    p^2 &= \Big(\frac{h}{\lambda}\Big)^2 \\
    E &= \frac{(\frac{h}{\lambda})^2}{2m} = \frac{h^2}{\lambda^2}\frac{1}{2m} \\
    &= \frac{1}{4\pi \epsilon_0}\frac{Z_1Z_2e^2}{\lambda} = \frac{h^2}{\lambda^2}\frac{1}{2m} \\
    \frac{1}{\lambda} &= \frac{2}{4\pi\epsilon_0}\frac{Z_1Z_2e^2 m}{h^2} \\
    \text{replace }&\frac{1}{r} \text{ with }\frac{1}{\lambda} \\
    T &= \frac{1}{12\pi^2 \epsilon_{0}^2} \frac{Z_1^2Z_2^2e^4 m}{kh^2} = 9.8\times10^6 K
    \end{aligned}
$$

* this happens due to quantum tunneling

### Probability of Nuclear Reactions

* see graph on page 13 of slides
* nuclear reaction probability is the product of Maxwell-Boltzmann and Tunneling Probability

## Lecture 7

### Nuclear Conservation Rules

1. electric charge must be conserved
2. nucleon umber must be conserved
    * $p, n = + 1$
3. lepton number must be conserved
    * $e^\mp = \pm 1$
    * $\nu_{e}^\mp = \pm 1$

$$
    ^{A}_{Z}X
$$

* A - atomic number for element X (nucleon number)
* Z - number of protons (electric charge)

### Proton-Proton Chains

$$
    \begin{aligned}
    {}^{1}_{1}H &+ {}^{1}_{1}H \to {}^{2}_{1}H + e^+ + \nu_e \\
    {}^{2}_{1}H &+ {}^{1}_{1}H \to {}^{3}_{2}He + \gamma \\
    {}^{3}_{2}He &+ {}^{3}_{2}He \to {}^{4}_{2}He + {}^{1}_{1}H + {}^{1}_{1}H \\
    \implies 4{}^{1}_{1}H &\to {}^{4}_{2}He + \underbrace{2e^+ + 2\nu_e + 2\gamma}_{26.7\,MeV}
    \end{aligned}
$$

### CNO Cycle

$$
    \begin{aligned}
    {}^{12}_{6}C &+ {}^{1}_{1}H \to {}^{13}_{7}N + \gamma \\
    {}^{13}_{7}N  &\to \underbrace{{}^{13}_{6}C + e^+ + \nu_e}_{\beta\text{ decay}} \\
    {}^{13}_{6}C &+ {}^{1}_{1}H \to {}^{14}_{7}N + \gamma \\
    {}^{14}_{7}N &+ {}^{1}_{1}H \to {}^{15}_{8}O + \gamma \\
    {}^{15}_{8}O &\to \underbrace{{}^{15}_{7}N + e^+ \nu_e}_{\beta\text{ decay}} \\
    {}^{15}_{7}N &+ {}^{1}_{1}H \to {}^{12}_{6}C + {}^{4}_{2}He \\
    \text{Total: }4{}^{1}_{1}H &\to {}^{4}_{2}He + \underbrace{2e^+ + 2\nu_e + 3\gamma}_{E = 26.7\,MeV}
    \end{aligned}
$$

## Lecture 8

### Energy produced in Stars

$$
    \begin{aligned}
    dL &= \epsilon\,dm ~~ [W] \\
    \epsilon_{i,X} &= \epsilon_0 X_i X_X \rho^\alpha T^\beta ~~ [W\,kg^{-1}] \\
    dm &= 4\pi r^2\rho\,dr \\
    \implies \frac{dL}{dr} &= 4\pi r^2 \rho \epsilon
    \end{aligned}
$$

#### Slide 5 diagram

 * Solid line just to do with fusion then no fusion
 * Dashed line has that shape as volume increase so dL/dr does but then temperature starts falling so fusion decreases

### Energy Seen on Earth

* Electrons lose energy travelling through sun

$$
    \frac{\lambda_{surface}}{\lambda_{core}} \approx 3\times10^6
$$

### Mean Free Paths

* $vt$ - distance travelled
* $n$ - particles per unit volume
* $nvt$ - particle per unit area
* $n\sigma vt$ - number of interactions

$$
    \begin{aligned}
    l &= \frac{vt}{n\sigma vt} \\
    &= \frac{1}{n\sigma}
    \end{aligned}
$$

* This is the mean distance before a collision

$$
    \begin{aligned}
    d &= \sum_i l_i \\
    d^2 &= d \cdot d \\
    &= \sum_j \sum_i l_i \cdot l_j
    \end{aligned}
$$

* When $i \neq j$, $l_i \cdot l_j = 0$

$$
    \begin{aligned}
    d^2 &= Nl^2 \\
    \implies N = \bigg(\frac{d}{l}\bigg)^2
    \end{aligned}
$$

* Use ideal gas law to help in questions of this

$$
    \begin{aligned}
    t_{total} &= t_{travel} + Nt_{scatter} \\
    &= \frac{Nl}{c} + N\times 10^8 \\
    &= 5700\;yrs + \cdots = 10^6 \, yrs
    \end{aligned}
$$

### Radiation

$$
    \begin{aligned}
    P &= \frac{1}{3}a T^4 \\
    \frac{dP}P{dr} &= \frac{dP}{dT}\frac{dT}{dr} \\
    \frac{dP}{dr} &= \frac{4}{3}a T^3 \frac{dT}{dr} \\
    \frac{dP}{dr} &= -\frac{\kappa\rho}{c}F_{rad} \\
    \kappa rho &= n\sigma \\
    \frac{dT}{dr} &= -\frac{3}{4ac}\frac{\kappa\rho F_{rad}}{T^3} \\
    L &= 4\pi r^2 F_{rad} \\
    \frac{dT}{dr} &= -\frac{3}{16\pi ac}\frac{\kappa\rho L_r}{T^3 r^2}
    \end{aligned}
$$

## Lecture 9

### Opacity

$$
    \begin{aligned}
    dI_\lambda &= - \kappa_\lambda \rho I_{\lambda} ds \\
    \int_{I_{\lambda, 0}}^{I_{\lambda, f}} \frac{dI_{\lambda}}{I_{\lambda}} &= - \int \kappa_{\lambda} \rho ds \\
    \implies I_{\lambda, f} &= I_{\lambda, 0}e^{-\int_0^s \kappa_{\lambda}\rho ds} \\
    I_{\lambda, f} &= I_{\lambda, 0}\underbrace{e^{-\kappa_\lambda \rho s}}_{\text{optical depth, }\tau} \\
    &= I_{\lambda, 0}e^{-\tau}, ~ \tau = \kappa_{\lambda}\rho s
    \end{aligned}
$$

* $\tau < 1$ - optically thin
* $\tau > 1$ - optically thick

#### Different sources of Opacity

* Two classes of opacity:
    1. Absorption - photon energy lost of KE of gas or degraded
    2. Scattering - photon reemitted at different direction, sometimes degraded

1. Bound-Bound transitions
    * typical temperature roughly $\leq 10^5$K
    * most effective for neutral gas
    * scattering and absorption
2. Bound-free transitions
    * typical temperature of $10^4 \to 10^6$K
    * partially ionised gas
    * absorption
3. Free-free emission
    * typical temperature of $10^4 \to 10^6$K
    * partially ionised gas
    * absorption
4. Electron scattering
    * dominant at roughly $\geq 10^6$K
    * fully ionised gas
    * scattering

## Lecture 10

### Schwarzchild Criterion for Convection

* slide 4 - 9

$$
    \gamma = \frac{C_p}{C_V} = \frac{s + 2}{s}
$$

* s is degrees of freedom

$$
    \begin{aligned}
    P &= k_a \rho^\gamma \\
    \frac{dP}{P} &= \frac{\gamma d\rho}{\rho} \\
    \gamma &= \frac{\rho}{P}\frac{dP}{d\rho} \\
    \text{Surrou}&\text{nding gas} \\
    P &= nkT = \frac{\rho kT}{\mu m_H} \\
    \frac{dP}{P} &= \frac{d\rho}{\rho} + \frac{dT}{T} \\
    \frac{d\rho}{\rho} &= \frac{dP}{P} - \frac{dT}{T} \\
    \frac{dP}{d\rho}_{sur} &> \frac{dP}{d\rho}_{adiab} \Bigg[\times \frac{\rho}{P} \\
    \frac{\rho}{P}\frac{dP}{d\rho}_{sur} &> \frac{\rho}{P} \frac{dP}{d\rho}_{adiab} \\
    \frac{\rho}{P}\frac{dP}{d\rho}_{sur} &> \gamma_{ad} \\
    \frac{P}{dP}\Big(\frac{dP}{P} &- \frac{dT}{T}\Big)_{sur} < \frac{1}{\gamma_{adiab}} \\
    \frac{P}{dP}\frac{dP}{P} &- \frac{P}{dP}\frac{dT}{T} < \frac{1}{\gamma_{adiab}} \\
    1 - \Big(\frac{P}{dP}&\frac{dT}{T}\Big)_{sur} < \frac{1}{\gamma_{adiab}} \\
    \frac{T}{P} \Big(\frac{dP}{dT}\Big)_{sur} &< \frac{\gamma_{adiab}}{\gamma_{adiab} - 1} \\
    \Big|\frac{dT}{dr}\Big|_{sur} &> \Big(\frac{\gamma_{adiab} - 1}{\gamma_{adiab}}\Big)\frac{T}{P} \Big|\frac{dP}{dr}\Big|_{sur_{}}
    \end{aligned}
$$

#### Convection in the Sun

For the sun:

$$
    \begin{aligned}
    -\frac{3}{16\pi a c}\frac{k\rho L_r}{T^3 r^2} &>  \Big(\frac{\gamma_{} - 1}{\gamma_{}}\Big)\frac{T}{P} \frac{dP}{dr} \\
    \frac{dP}{dr} &= -\frac{GM_r \rho}{r^2} \\
    \frac{L_r}{M_r} &> \frac{16 \pi a c G}{\kappa\rho} \frac{aT^4}{3} \frac{\gamma - 1}{\gamma} \\
    &> \frac{16 \pi acG}{\kappa\rho}P_{rad}\frac{\gamma - 1}{\gamma} \\
    &> 1.9\times10^{-3}\,W\,kg^{-1}
    \end{aligned}
$$

#### Mixing length

$$
    \begin{aligned}
    l &= \alpha Hp \\
    \frac{dP}{dr} = - \frac{GM_r \rho}{r^2} &\implies \frac{1}{Hp} = -\frac{1}{P}\frac{dP}{dr} \\
    Hp &= \frac{Pr^2}{GM_r \rho} \\
    l&= \frac{\alpha Pr^2}{GM_r \rho}
    \end{aligned}
$$

## Lecture 12

### Cepheid Variables

$$
    \begin{aligned}
    \log\bigg(\frac{L}{L_{\odot}}\bigg) &= 1.15\log_{10}\Pi^d + 2.47 \\
    \Pi^d = 10\,\text{days} &\implies L = 4200\,L_{\odot} \\
    \text{observed} <f> &= 10^{-15} W\,m^{-2} \\
    L &= 4\pi d^2 <f> \\
    d &= \sqrt{\frac{L}{4\pi<f>}}
    \end{aligned}
$$

### Stellar Pulsation

$$
    \begin{aligned}
    V_s &= \sqrt{\frac{\gamma P}{\rho}}, ~ \gamma = \frac{C_p}{C_V} \\
    \Pi &= 2\int_0^R \frac{dr}{V_s} \\
    \frac{dP}{dr} &= -\frac{GM_r \rho}{r^2} \\
    \text{const } p &\implies \mu = \frac{4}{3}\pi r^3 \rho \\
    \frac{dP}{dr} &= -\frac{4}{3}G\pi r \rho^2 \\
    dP &= -\frac{4}{3}G\pi\rho^2 \int_0^R r\,dr \\
    P(r) &= \frac{4}{3}G\pi\rho^2 \bigg[\frac{R^2}{2} - \frac{r^2}{2}\bigg] \\
    \Pi &= 2 \int_0^R \frac{dr}{V_s} \\
    &= 2\int_0^R \frac{dr}{\sqrt{\frac{2}{3}\gamma G\rho (R^2 - r^2)}} \\
    &= 2\sqrt{\frac{3}{2\gamma\pi G \rho}} \Bigg[\sin^{-1} \bigg(\frac{r}{R}\bigg)\Bigg]^{R}_{0} \\
    &= \sqrt{\frac{3\pi}{2G\rho\gamma}}
    \end{aligned}
$$

## Lecture 13

### Jeans Mass

* For the gravitational collapse of a gas cloud:

$$
    \begin{aligned}
    GE = U &= -\frac{3}{5}\frac{GM^2}{R} \\
    KE = K &= \frac{3}{2}NkT \\
    &= \frac{3}{2}\frac{M_c}{\mu m_H}kT \\
    2K &< |U| \\
    2\Bigg(\frac{3}{2}\frac{M_c kT}{\mu m_H}\Bigg) &< \frac{3}{5}\frac{GM_c^2}{R_c} \\
    R_c &= \Bigg(\frac{3}{4}\frac{M_c}{\pi \rho_0}\Bigg)^{\frac{1}{3}} \\
    2\Bigg(\frac{3}{2}\frac{M_c kT}{\mu m_H}\Bigg) &< \frac{3}{5}GM_c^2 \Bigg(\frac{4}{3}\frac{\pi \rho_0}{M_c}\Bigg)^{\frac{1}{3}} \\
    \frac{5M_c kT}{\mu mH G} &< M_c^2 \Bigg(\frac{4}{3}\frac{\pi \rho_0}{M_c}\Bigg)^{\frac{1}{3}} \\
    M_c &< M_J \\
    M_J &\approx \Bigg(\frac{5kT}{G\mu m_H}\Bigg)^{\frac{3}{2}} \Bigg(\frac{3}{4\pi\rho_0}\Bigg)^{\frac{1}{2}}
    \end{aligned}
$$

### Free-fall gravitational collapse

1. $M_c > M_J$
    * free fall collapse
    * optically thin
    * pressure increase
    * temperature constant

2. Fragmentation
    * optically thin
    * individual regions exceed local $M_J$


3. $M_J$ minimised: Protostar
    * optically thick
    * pressure increase
    * temperature increase
    * Slow contraction (Kelvin-Helmholtz timescale)

## Lecture 14

### Stellar Evolution

1. Increase in $\mu$ (mean molecular mass) with time:

$$
    P = nkT = \frac{\rho kT}{\mu m_H}
$$

As $\mu$ increases, $\rho$ and T also increase for the pressure to remain constant.

Recall:

$$
    \epsilon_{i,X} = \epsilon_0 X_i X_X \rho^\alpha T^\beta, \alpha \approx 1
$$

For proton-proton chain, $\beta \approx 4$  
For CNO, $\beta \approx 17$

Luminosity increases with time.

### Lifetime of Nuclear Fusion

$$
    \begin{aligned}
    t &= \frac{E_{tot}}{L} = \frac{X\zeta Mc^2}{L} \\
    \zeta_{pp} &= \frac{4m_p - m_{He}}{m_{He}} \approx 0.007 \\
    t_{\odot} &= 10^{10} \text{ yrs} \\
    L_{ms} &= L_\odot \left(\frac{M_\odot}{M}\right)^{\alpha} \\
    t_{ms} &= \frac{X\zeta Mc^2}{L_\odot}\left(\frac{M_\odot}{M}\right)^{\alpha} \\
    &= 10^{10}\frac{M}{M_\odot}\left(\frac{M_\odot}{M}\right)^{\alpha} \\
    \therefore t_{ms} &= 10^{10}\left(\frac{M_\odot}{M}\right)^{\alpha - 1}
    \end{aligned}
$$

## Lecture 15

### Eddington Limit

$$
    \begin{aligned}
    L_{Edd} &= \frac{4\pi cGM}{\kappa}, M = 100M_\odot, \kappa = \kappa_{es} = 0.04\,kg\,m^{-2} \\
    &= 3\times10^6 L_{\odot}
    \end{aligned}
$$

### Photodisintegration

$$
    \begin{aligned}
    \lambda_{max} &= \frac{2.9\times10^{-3}}{T}, ~ E = \frac{hc}{\lambda} \\
    T_c &\geq 3\times10^9 K \implies E \geq 1\,MeV
    \end{aligned}
$$

#### Last Days of Fusion

* Shell fusion
* Silicon to Iron in Core
* $P_{core} =$ high

#### Endothermic Release

* Iron breaking down into Helium and Helium breaking down in protons and neutrons
* still shell fusion ongoing
* $P_{core} =$ rapidly decreasing

#### Electron capture

* very high density
* shell fusion
* $p + e^- \implies n + \nu_e$
* $P_{core} =$ rapidly decreasing
* neutrino burst

#### Rapid core collapse

* shell fusion
* $P_{core} \approx 0$

#### Core rebound

* shell fusion
* $\rho > 8\times10^{18}\,kg\,m^{-3}$
* the strong force repels collapse and rebounds outwards

#### Supernova

* previous step drives supernova
* strong force drives high energy pushing
* generates a shock wave - more photodisintegration
* electron capture repeats and another neutrino burst
* nuclear synthesis of heavier elements, including beyond iron (endothermic)

## Lecture 16

### Electron Degeneracy Pressure

$$
    \begin{aligned}
    \Delta x\Delta p_x &\approx \hbar \\
    p_min &\approx \Delta p_x \approx \frac{\hbar}{\Delta x} \\
    P &\approx \frac{1}{2}n_e pv \\
    n_e &= \frac{\# e}{vol} = \frac{Z}{A} \frac{\rho}{m_H} \\
    p_x &= \Delta p_x = \frac{\hbar}{\Delta x} \\
    \Delta x &= n_e^{-1/3} \implies p_x = \hbar n_e^{1/3} \\
    p^2 &= p_x^2 + p_y^2 + p_z^2 = 3p_x^2 \\
    \implies p &= \sqrt{3}p_x = \sqrt{3}\hbar n_e^{1/3} \\
    p &= mv = m_e v \\
    \implies v &= \frac{p}{m_e} = \frac{\sqrt{3}}{m_e}\hbar n_e^{1/3} \\
    P &= \frac{1}{3}n_e pv \\
    p &= \sqrt{3}\hbar \left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{1/3} \\
    v &= \frac{\sqrt{3}}{m_e}\hbar \left[\left(\frac{Z}{A}\right) \frac{\rho}{m_H}\right]^{1/3} \\
    \therefore P &= \frac{\hbar^2}{m_e}\left[\left(\frac{Z}{A}\right) \frac{\rho}{m_H}\right]^{5/3}
    \end{aligned}
$$

### White Dwarf Cooling

$$
    \begin{aligned}
    t_{cool} = \frac{E_{WD}}{L_{WD}} = \left(\frac{3kT_{c,WD}}{2}\right) \left(\frac{M_{WD}}{Am_H}\right) \left(\frac{1}{L_{WD}}\right)
    \end{aligned}
$$

## Lecture 17

### Rotation Period of Pulsars

$$
    \begin{aligned}
    \text{Centripetal Acceleration} &= \text{Gravitational Acceleration} \\
    \omega^2_{max}R &= \frac{GM}{R} \\
    M &= \frac{4}{3}\pi R^3\rho \\
    \omega_{max}^2 R &= G \frac{4}{3}\pi R \rho \\
    \omega &= 2\pi f = \frac{2\pi}{P} \\
    \frac{4\pi^2}{P^2}R &= \frac{4}{3}G\pi R\rho \\
    P_{min} &= \left(\frac{3\pi}{G\rho}\right)^{1/2}
    \end{aligned}
$$

### Stellar Core Rotation

Conservation of angular momentum:

$$
    \begin{aligned}
    I_i\omega_i &= I_f\omega_f, ~ I = CMR^2 \\
    CMR_i^2\omega_i &= CMR_f^2\omega_f, ~ \omega = \frac{2\pi}{P} \\
    \frac{2\pi}{P_f} &= \frac{2\pi}{P_i}\left(\frac{R_i}{R_f}\right)^2 \\
    P_f &= P_i\left(\frac{R_f}{R_i}\right)^2
    \end{aligned}
$$
