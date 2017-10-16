### Astro
---
#### Observational
_other stuff in notebook_
##### Lecture 3
* Parts of atmosphere are opaque due to water vapour, $O_3$, etc
* Correcting for atmospheric absorption:
    * **GET IMAGES FROM SLIDES**
$$ X = 1 ~\text{airmass} \\
   X = \sec(z) ~\text{airmasses} \\
   -\int_{I_C}^{I_O} \frac{dI}{I} = \int_{0}^{X}k\,dX  \\
   \ln{\frac{I_obs}{I_{corr}}} = kX + c \\  
   \frac{I_{obv}}{I_{corr}}  = e^{-kX} \\
   m_{obv} - m_{corr} = -2.5\log{\frac{I_{obv}}{I_{corr}}} \\
   m_{obs} - m_{corr} = -2.5\log{e^{-kX}} \\
   = 2.5kX\log{e} \\
   m_{corr} = m_obv - A_\lambda(z = 0) \sec{z}
$$
* Atmospheric refraction
    * **MATHS AND PICS IN SLIDES**
    * plane parallel atmosphere
    * apply laws of refraction
    * basic trig stuff
    * always in small angle approx range
    * $ r = (n - 1)\tan{(z_0)}$
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
        * $ > 90$%
    * high dynamic range
    * excellent linearity
    * excellent stability
    * still not enough pixels
---
