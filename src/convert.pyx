import tpm

cdef _convert(list ra, list de, int s1, int s2,
              double epoch, double equinox,
              double utc, double delta_ut, double delta_at,
              double lon, double lat, double alt,
              double xpole, double ypole,
              double T, double P, double H,
              double wavelength):
    """Utility function for coordinate conversion.

    Only for use from within Cython.
    """
    cdef int i
    tstate = tpm.TSTATE()
    pvec = tpm.PVEC()

    # Initialize TPM state.
    tpm.tpm_data(tstate, tpm.TPM_INIT)
    
    # Set independent quantities.
    tstate.utc = utc
    tstate.delta_ut = delta_ut
    tstate.delta_at = delta_at
    tstate.lon = lon
    tstate.lat = lat
    tstate.alt = alt
    tstate.xpole = xpole
    tstate.ypole = ypole
    tstate.T = T
    tstate.P = P
    tstate.H = H
    tstate.wavelength = wavelength

    tpm.tpm_data(tstate, tpm.TPM_ALL)

    ra_out = []
    de_out = []
    for i in range(len(ra)):
        v6 = tpm.V6S()
        v6.r = 1e9
        v6.alpha = ra[i] 
        v6.delta = de[i] 

        pvec[s1] = v6.s2c()
        tpm.tpm(pvec, s1, s2, epoch, equinox, tstate)
        v6 = pvec[s2].c2s()
    
        ra_out.append(v6.alpha)
        de_out.append(v6.delta)

    return ra_out, de_out

def convert(ra, de,
            int s1=tpm.TPM_S06, int s2=tpm.TARGET_OBS_AZEL,
            double epoch=tpm.J2000, double equinox=tpm.J2000,
            double utc=tpm.utc_now(),
            double delta_at=tpm.delta_AT(tpm.utc_now()),
            double delta_ut=tpm.delta_UT(tpm.utc_now()),
            double lon=-111.598333,
            double lat=31.956389,
            double alt=2093.093,
            double xpole=0.0, double ypole=0.0,
            double T=273.15, double P=1013.25, double H=0.0,
            double wavelength=0.550):
    """Utility function for performing coordinate conversions.

    :param ra: Input angle, like Right Ascension, in degrees
    :type ra: List of floats (degrees)
    :param de: Input angle, like Declination, in degrees
    :type de: List of floats (degrees)
    :param s1: Initial state
    :type s1: Integer
    :param s2: Final state
    :type s1: Integer
    :param epoch: Epoch of input coordinates as a Julian date
    :type epoch: Float (Julian date)
    :param equniox: Equinox of input or output coordinates
    :type equinox: Float (Julian date)
    :param utc: "Current" UTC time as a Julian date
    :type utc: Float (Julian date)
    :param delta_at: TAI - UTC in seconds
    :type delta_at: Float (seconds)
    :param delta_ut: UT1 - UTC in seconds
    :type delta_ut: Float (seconds)
    :param lon: Geodetic longitude in degrees
    :type lon: Float (degrees)
    :param lat: Geodetic latitude in degrees
    :type lat: Float (degrees)
    :param alt: Altitude in meters
    :type alt: Float (meters)
    :param xpole: Polar motion in radians
    :type xpole: Float (radians)
    :param ypole: Ploar motion in radians
    :type ypole: Float (radians)
    :param T: Ambient temperature in Kelvin
    :type T: Float (Kelvin)
    :param P: Ambient pressure in millibars
    :type P: Float (millibars)
    :param H: Ambient humidity in the range 0-1
    :type H: Float (fraction between 0-1)
    :param wavelength: Wavelength of observation in microns
    :type wavelength: Float (microns)

    :return: List of output angles, (ra_like, de_like), in degrees
    :rtype:  List of 2-element tuples containing floats

    This is a convienence function for perform corodinate
    transformations. This function takes all independent arguments for
    defining a a TPM STATE and then calculates all the dependent
    quantities of the TPM STATE once and only once. Then it performs
    the required conversion on the given list of coordinates, without
    changing the TPM STATE. It returns a list of 2-element tuples, with
    each tuple containing the ra like angle and the de like angles, in
    degrees.
    """
    try:
        len(ra)
        len(de)
    except TypeError:
        # Not a list. Assume that this is a single number.
        ra = [tpm.d2r(ra)]
        de = [tpm.d2r(de)]
    else:
        ra = [tpm.d2r(i) for i in ra]
        de = [tpm.d2r(i) for i in de]

    lon = tpm.d2r(lon)
    lat = tpm.d2r(lat)
    
    ra_out, de_out = _convert(ra, de, s1,  s2, epoch,  equinox,
                              utc,  delta_ut, delta_at, lon, lat,
                              alt, xpole,  ypole, T,  P,  H,
                              wavelength)
    
    return [(tpm.r2d(i), tpm.r2d(j)) for i,j in zip(ra_out, de_out)]
