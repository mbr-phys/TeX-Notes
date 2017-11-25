### Observational

_other stuff in notebook_

##### Lecture 3

* Parts of atmosphere are opaque due to water vapour, $O_3$, etc
* Correcting for atmospheric absorption:
    * **GET IMAGES FROM SLIDES**

$$ X = 1 ~\text{airmass} $$ $$
   X = \sec(z) ~\text{airmasses} $$ $$
   -\int_{I_C}^{I_O} \frac{dI}{I} = \int_{0}^{X}k\,dX  $$ $$
   \ln{\frac{I_{obs}}{I_{corr}}} = kX + c $$ $$  
   \frac{I_{obs}}{I_{corr}}  = e^{-kX} $$ $$
   m_{obs} - m_{corr} = -2.5\log{\frac{I_{obs}}{I_{corr}}} $$ $$
   m_{obs} - m_{corr} = -2.5\log{e^{-kX}} $$ $$
   = 2.5kX\log{e} $$ $$
   m_{corr} = m_obs - A_\lambda(z = 0) \sec{z}
$$

* Atmospheric refraction
    * **MATHS AND PICS IN SLIDES**
    * plane parallel atmosphere
    * apply laws of refraction
    * basic trig stuff
    * always in small angle approx range
    * $r = (n - 1)\tan{(z_0)}$
* Refractive index also has wavelength dep
* atmos ref turns into an atmos dispersion
* disperses more for smaller wavelength
    * 3 or 4 arcsecs
    * a lot
* Every object appears as a spectrum as colors separate
* atmos emission
    * fluorescent emission
        * air glow
    * emits thermal radiation for TE
    * Most emission is from OH molecules in upper atmos
        * vibrational and rotational movement
* want to try and stay away from regions with lots of this emission
* Other sources of emission:
    * light pollution
        * from ground
        * from satellites and aircraft
    * zodiacal light
        * light scattered from interplanetery dust
        * in plane of the Solar System
    * scattered light
        * e.g. from the moon
        * telescope scheduling to dark, grat, and bright time
* more diffcult observations at longer wavelengths
    * more background issues
* dust causes lots of interference
    * at longer wavelengths, interaction between dust and photons is smaller
    * interaction cross-section
* easier to see through dust a lot easier and see other galaxies etc at longer wavelengths
* Atmospheric turbulence
    * _twinkle twinkle little star_
    * Stars twinkle due to light getting bounced around in atmos
* Angular resolution of telescope limited by Fraunhofer Diffraction
    * _see last year_
    * Airy disk
    * assume stars as point sources
    * large telescope $\implies$ small airy disk
    * small telescope $\implies$ large airy disk
    * how close before two stars are seen as one?
* Characterise resolution with Rayleigh criterion
    * at some point the principle maximum of one star overlays with the principle minimum of the second
        * _diffraction limit_
    * $\theta_{dl} = 1.22\frac{\lambda}{D}$
        * integrate round a cylinder using Bessel fns to get this
        * covered sort of later on in other module
* Atmos is constantly moving
    * changing size, density, and temperature causes different path lengths ever dt for stars
    * sum up over lots of dt for observing
        * causes blurring though
    * no longer airy disk, severely blurry
* for atmos turbulence, the seeing is defined as minimum angle between two stars that can just be resolved
    * typically in arcsec
    * 50x worse than the diffraction limit
* Detectors
    * Charged Coupled Device
    * little silicon micro-circuits
    * little ray of capacitors
    * discrete energy bands
        * conduction band and valence band
        * difference of $\approx 1.1$eV
    * upper cut-off wavelengths governed by band gap voltage difference
    * lower wavelengths cut-off by absorption of photons into the silion
    * excellent Quantum efficiency
        * $> 90$%
    * high dynamic range
    * excellent linearity
    * excellent stability
    * still not enough pixels

##### Lecture 4

###### Back to CCDs:

* Well Depth
    * how many electrons can be stored in the upper state, usually 100s of thousands
* use binary for how many levels for the signal
    * i.e. 8 bit $= 2^8 = 256$ levels
* System Gain
    * how many photo-electrons are required for digital output of 1
    * small gain means reduced saturation signal

###### Photometry

* Process of obtaining quatative (numerical) values of the birghtness of celestial objects
* CCD gives output prop to number of photons incident on each pixel
* Photometry takes raw data and corrects for noise from other sources
* Noise is just any interference for the image
* SNR (signal to noise ratio) defined as ratio of useful to non-useful data
* Poisson stats
    * arrival of photons governed by this
    * studied for how cameras observe sky stuff
    * see stats last year
    * Hughes and Hase and labs stuff

$$
    P(n,N) = \frac{\exp(-N)N^n}{n!}
$$

* High means approximates Gaussian stats
* mean is N
    * also Variance
    * std dev is $\sqrt{N}$
* Telescope experiments can take eight hours or so
    * so use Poisson errors for easy error in counts
* Small error associated with read out

###### Basic Data Reduction to Correct for Background in CCD

* Bias
    * a zero second readout whihc results in a constant offset
    * allows for understanding of the "noise" quantity
* Dark
    * CCD band stuff
    * CCD will be in TE so will promote thermal photons
    * thermal photons can hit detector and skew results
    * this will increase in time
* Flat Field
    * variations in sensitivity
    * varied energy ever so slightly across CCD
    * quantum efficiency
    * slight changes across the CCD in efficiency causes a  non-uniform field across CCD
* Also have sky background counts
    * these are often the most significant contributor

$$
    \text{Final Frame} = \frac{\text{Object Frame} - (\text{dark+bias})}{\text{Flat Field} - \text{(dark+bias)}} $$ $$
    \text{Final Frame} = \frac{\text{Object Frame} - (\text{dark+bias})}{\text{Flat Field} - \text{(dark+bias)}} - \frac{\text{Sky Frame} - (\text{dark+bias})}{\text{Flat Field} - (\text{dark+bias})} $$ $$
    \implies \text{Final Frame} = \frac{\text{Object Frame} - \text{Sky Frame}}{\text{Flat Field} - \text{(dark+bias)}}
$$

###### Noise Sources

* Basic sources of noise are:
    1. Readout noise, $\sigma_{rd}$ electrons (Gaussian)
    2. Photon noise on the signl from the object (Poisson)
        * $= \sqrt{f_{abj}t}$
    3. Photon noise on the signal from the sky background (Poisson)
        * $= \sqrt{f_{bg}t}$
    4. Photon noise on the dark current (Poisson)
        * $\sqrt{dt}$
* Uncorrelated noise sources can be added in quadrature
    * $\sigma_{\text{total}} = \sqrt{\sigma_{1}^{2} + \sigma_{2}^{2}}$
* Signal/Noise

$$
    SNR = \frac{S}{\sqrt{S + D + B + \sigma_{rd}^2}}
$$

* S - signal
* B - background
* D - dark
* $\sigma_{rd}$ - read error
* Prev equation assumes all the terms are in photo-electrons
* Will need to be accounted for if in ADU
* counts in number of photons
* gain can be set to more than 1
    * confuses simple SNR eqn and changes what you plug in

###### SNR Approximations

* Common approximations:
    1. Photon noise limited on the object
        * signal dominates so can ignore other terms for SNR
    2. Sky Limited
        * sky background dominates, only count background
    3. Read Noise Limited
        * read background dominates, only count read term

#### Lecture 5

##### Spectroscopy

* Most useful tool in astro
* measurement of intensity of a light source
    * function of wavelength
* Different specta:
    1. light from source straight to detector
        * continous spectrum
    2. light from source travels through a cloud of gas straight to detector
        * continuous spectrum with dark lines
    3. light from source travels into cloud and scatters through it to detector
        * bright line spectrum on black background
* Types of spectrograph
    1. Refraction (prisms)
    2. Diffraction gratings
    3. Interference  (Fabry-Perot interferometer)
    * focus on diffraction grating
* Diffraction grating
    1. Slit
        * need this to focus light from source of interest and block everything else
    2. Collimating lens
        * make sure light lands parallel to diffraction grating
    3. Diffraction grating
    4. Camera
* Condition for constructive interference:

$$
    n\lambda = d\sin\theta $$ $$
    \frac{d\theta}{d\lambda} = \frac{n}{d\cos\theta}
$$

* $\frac{d\theta}{d\lambda}$ is known as angular dispersion (rad/nm)
    * higher dispersions from higher spectral orders and smaller line spacings
    * more convenient for Reciprocal Linear dispersion ($\frac{d\lambda}{dx}$)
    * measuring wavelength per unit x at detector (nm/mm)
    * multiply $\frac{d\theta}{d\lambda}$ by plate scale $\frac{d\theta}{dx} = \frac{1}{f_{cam}}$

$$
    \frac{d\lambda}{dx} = \frac{d\lambda}{d\theta}\frac{d\theta}{dx} = \frac{d}{f_{cam}n}\cos\theta
$$

###### Grating Equation

* For angles of incidence to grating
* For diffraction grating or reflection

$$
    n\lambda = d(\sin\alpha + \sin\beta) $$ $$
    n\lambda\rho = \sin\alpha + \sin\beta ~;~ \rho = \frac{1}{d}
$$

###### Resolving Power

* Recall angle for blurred star

$$
    \theta = 1.22\frac{\lambda}{D}
$$

* Resolving power of a spectrograph is wavelength over band pass:
    * $\lambda$ is the wavelength
    * $\Delta\lambda$ is the minimum discernible difference in $\lambda$

$$
    R = \frac{\lambda}{\Delta\lambda} = nN $$ $$
    R = \frac{n\rho\lambda W}{\chi D_{T}}
$$

* Where
    * n is diffraction order#
    * N is number of lines
    * $\rho$ is the ruling density (lines/mm)
    * $\lambda$ is the wavelength
    * W is the grating size
    * $\chi$ is the angular size of the image of a star on slit
    * $D_{T}$ is the telescope size
* Don't want too narrow a slit
    * optimise width of slit for photons from star
    * spectral resolution gets blurred
* Second equation above is for a practical spectrograph
    * At most wavelengths, this value of R is much less than that given by $nN$

###### CDs, DVDs, and Blu-Rays

* basically diffractions gratings
* DVDs store more info than CDs based on diffraction types
* Blu-Rays need UV light to make sense


#### Lecture 6

##### Measuring Stars

* Black  body radiation

$$
    E(\lambda, T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{\tfrac{hc}{\lambda kT}} - 1}
$$

* Characteristic temperature is where $\frac{dE}{d\lambda} = 0$, bump at top of curve
* Colours of stars depends on plot, nearest colour to peak is visible colour

$$
    L = 4\pi R^2 \sigma T^4
$$

* Calc distance to star?
    * use parallax
    *  define 1 parsec as distance corresponding to parallax of $\theta = 1"$
    * 1 psc $= 206265 AU$

##### Interferometry

* Combines light from two telescopes   
    * makes it possible to measure stars
    * interfere the light and measure phase difference
    * diffraction limit: $1.22\frac{\lambda}{D}$
* As star tracks across sky, path length changes
    * phase will shift in and out of phase with movement
    * more complicated for two light sources
    * get a more complex fringe pattern
        * modulated by $\frac{\lambda}{D}$ for each telescope
* Moving telescopes apart changes fringe pattern
    * at some point apart, the fringe pattern will disappear and will resolve the star
    * can then use maths to find $\theta$ and find the radius using that and the distance away
    * VLT uses more than two telescopes
* Aperture synthesis
    * a trick we need for observations
    * path length will not change between two telescopes, if they come over parallel
    * Will have a 'y' pattern of telescope arrays so that path length will always be changing no matter what way it is passing over the sky

#### Lecture 7

* Zero-point mag gives one count

* **See example sheet from Lecture 6 for some good notes**

##### Multi-Wavelength Techniques

* Missing a huge fraction of images outside visual
    * how do we see the rest of it?

* X-ray radiations
    * electrons wizzing around
    * Accelerated to high energies in plasma state
    * effecitvely in about a million K
    * protons will make electrons change path, and emit energy
    * accretion disks generate some of this
* Difficulties
    * X-rays have too high energies
    * mirrors absorb it and don't work
    * very shallow angle mirrors focus instead
    * Grazing incidence

* UV radiation
    * temperatures of around $50 \, kK$
    * massive stars
    * clumpy as all around clumps of new big stars forming in groups
* Difficulties
    * CCDs have lower QE for these lower energies
    * hard to move energy level difference in CCDs to measure UV accurately
    * swamped by other photons
    * use a blocking filter to try and filter visual photons away and just get UV

* Infra-red radiation
    * begin to suffer from sky background here
    * to do it accurately, you need to be in space
    * see a 'fuzz' tracing spiral arms on galaxies
        * hot dust in the interstellar medium being heated by stars
        * emission from cooler stars
        * globular clusters of old stars

* Sub-millimeter radiation
    * looking at $T = 3 \to 10 \, K$
    * challenging to detect such low energies
    * very sensitive thermometers
    * liquid helium at a few micro-Kelvin
    * changes resistance and allows current to flow for a second

* Why
    * Pillars of Creation
    * lots of dusty regions
        * actively forming stars in the dust clouds
        * carbonaceous material - graphite, diamonds etc
        * silicates
        * ices
    * optical photons increases dust temperature slightly, still around 10 K though
        * emits 100 micron wavelength photons to lose temperature
    * looking at Pillars in sub-millimeter shows clouds glowing now
    * can observe nebulae very differently in sub-millimeter

* Radio radiation
    * 3 components
        * local thunderstorms
        * distant thunderstorms - radio waves bounce round atmosphere
        * constant hiss with period of 23 hours 56 minutes and 4.1 seconds
        * sidereal day
    * This hiss is the galactic emission
    * surface of telescopes need to be 'smooth'
    * smoothness isn't as necessary for radios
        * easy to build big telescopes for radio without this concern
    * very difficult to get a high resolution radio telescope

#### Lecture 8

##### Radios Ctd

* Biggest telescope is FAST
    * 500m diameter
* Why observe in radio?
    * 21cm
        * Neutral H emission
    * electron can have parallel or anti-parallel spin
        * two sub ground states
    * anti-parallel is lower energy than parallel so will eventually flip to this one
        * very small energy difference
        * hyper-fine energy splitting
        * this takes a few millions years though
    * lots of H in galaxies
        * probability adds up to observe this
        * pointing radio telescopes sees this

##### Telescope Tech

* 'Twinkling star'
    * caused by atmosphere moving around and bumping image around
    * break it up into sub-images
        * speckles
    * whole image will also move around
* Fried parameter
    * $r_0 \approx 10\,cm$
    * size of turbulent cells
    * coherence time  
        * $t_0 = \frac{r_0}{v}$
        * v is wind speed
        * this means that a star will only be stable for about $10\, ms$
* Correcting this
    * light comes in normally
    * hits third mirror that can change angle with actuators
    * then hits a beam splitter
        * 50% to computer analyser
        * 50% to somewhere else
    * computer constantly measures image and changes actuators to correct image for turbulence
        * uses fast Fourier transforms to get back to real image
        * happens every millisecond or so
    * this requires bright star though
    * shine lasers up to $15\,km$ into atmosphere to focus
        * this creates a fake star for corrections - 'natural guide star'

##### Exoplanets

* How do we observe planets against photon noise of stars?
    * observe stellar spectrum and planet spectrum for comparison
    * heavier molecules are more difficult to observe as they're lower down
        * refraction issues
    * detecting $O_3$ would be a key trigger for life
        * not able to do it yet

## Stars

### Lecture 1

* Black body emission curve
    * LHS from peak lambda is Rayleigh Jeans tail
    * RHS from peak is Wien tail

$$
    \lambda_{max} = \frac{2.9 \times 10^{-3}}{T} \, m $$ $$
    \lambda_{max.\,Bet} = 8.3 \times 10^{-7}m \implies T \approx 3500\,K $$ $$
    \lambda_{max,Sun} = 5.5 \times 10^{-7}m \implies T \approx 5300\,K $$ $$
    \lambda_{max, Bel} = 3.0 \times 10^{-7} m \implies T \approx 9400\,K
$$

### Lecture 2

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
