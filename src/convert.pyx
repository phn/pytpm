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

    :param ra: Input longitudinal angle, like ra, in degrees.
    :type ra: list of floats
    :param de: Input latitudinal angle, like de, in degrees.
    :type de: list of floats
    :param s1: Initial state.
    :type s1: integer
    :param s2: Final state.
    :type s2: integer
    :param epoch: Epoch of input coordinates as a Julian date.
    :type epoch: float
    :param equniox: Equinox of input or output coordinates.
    :type equinox: float
    :param utc: "Current" UTC time as a Julian date.
    :type utc: float
    :param delta_at: TAI - UTC in seconds.
    :type delta_at: float
    :param delta_ut: UT1 - UTC in seconds.
    :type delta_ut: float
    :param lon: Geodetic longitude in degeres.
    :type lon: float    
    :param lat: Geodetic latitude in degrees.
    :type lat: float
    :param alt: Altitude in meters.
    :type alt: float
    :param xpole: Polar motion in radians.
    :type xpole: float
    :param ypole: Ploar motion in radians.
    :type ypole: float
    :param T: Ambient temperature in Kelvin.
    :type T: float
    :param P: Ambient pressure in millibars.
    :type P: float
    :param H: Ambient humidity in the range 0-1.
    :type H: float
    :param wavelength: Wavelength of observation in microns.
    :type wavelength: float

    :return: List of output angles, (ra_like, de_like), in degrees
    :rtype:  List of 2-element tuples containing floats.

    Most often we just want to convert two angles from one coordinate
    system into another. We do not worry about proper motions and all
    conversions happen at the same "current time". This simplies the
    procedure a lot. Given a list of coordinates, most of the
    calculations need to be performed only once.

    This function performs such as coordinate conversion. It takes a
    list of ra like longitudinal angles in degrees, a list of de like
    latitudinal angles and all parameters needed for performing a
    particular transformation. All of these parameters have defualts.

    The default location is KPNO and the values are taken from the TPM
    C code.

    The TPM state data structure is initialized, the independent
    parameters are set and all the dependent parameters are
    calculated. That is using ``tpm_data(tstate, TPM_INIT)``. This
    calculation is done only once. Then each of the coordinates are
    converted, by creating a ``V6`` vector and calling ``tpm()``.

    The returned result is a list of tuples, where each tuple has the
    final ra like angle as the first element, and the final de like
    angle as the second element.
    
    For details on the parameters see the PyTPM reference documentation
    and the TPM manual. The latter gives an example for the usage of
    this function.
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

    x = [(tpm.r2d(tpm.r2r(i)), tpm.r2d(j)) for i,j in zip(ra_out, de_out)]
    return x
