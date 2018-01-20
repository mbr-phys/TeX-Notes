---
title: "Stars and Galaxies"
author: "Mark Swinbank"
date: "Michaelmas 2017"
---

# Observational Techniques

_other stuff in notebook_

## Lecture 3

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

## Lecture 4

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

#### Basic Data Reduction to Correct for Background in CCD

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

#### Noise Sources

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

#### SNR Approximations

* Common approximations:
    1. Photon noise limited on the object
        * signal dominates so can ignore other terms for SNR
    2. Sky Limited
        * sky background dominates, only count background
    3. Read Noise Limited
        * read background dominates, only count read term

## Lecture 5

### Spectroscopy

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

#### Grating Equation

* For angles of incidence to grating
* For diffraction grating or reflection

$$
    n\lambda = d(\sin\alpha + \sin\beta) $$ $$
    n\lambda\rho = \sin\alpha + \sin\beta ~;~ \rho = \frac{1}{d}
$$

#### Resolving Power

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

#### CDs, DVDs, and Blu-Rays

* basically diffractions gratings
* DVDs store more info than CDs based on diffraction types
* Blu-Rays need UV light to make sense


## Lecture 6

### Measuring Stars

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

### Interferometry

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

## Lecture 7

* Zero-point mag gives one count

* **See example sheet from Lecture 6 for some good notes**

### Multi-Wavelength Techniques

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

## Lecture 8

### Radios Ctd

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

### Telescope Tech

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

### Exoplanets

* How do we observe planets against photon noise of stars?
    * observe stellar spectrum and planet spectrum for comparison
    * heavier molecules are more difficult to observe as they're lower down
        * refraction issues
    * detecting $O_3$ would be a key trigger for life
        * not able to do it yet
