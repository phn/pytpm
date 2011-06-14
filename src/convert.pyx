import tpm

cdef _convert(list ra, list dec, int s1, int s2,
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
    dec_out = []
    for i in range(len(ra)):
        v6 = tpm.V6S()
        v6.r = 1e9
        v6.alpha = ra[i] 
        v6.delta = dec[i] 

        pvec[s1] = v6.s2c()
        tpm.tpm(pvec, s1, s2, epoch, equinox, tstate)
        v6 = pvec[s2].c2s()
    
        ra_out.append(v6.nalpha)
        dec_out.append(v6.ndelta)

    return ra_out, dec_out

def convert(ra=-999, dec=-999, double utc=-999, double delta_at=-999,
            double delta_ut=-999,
            int s1=tpm.TPM_S06, int s2=tpm.TARGET_OBS_AZEL,
            double epoch=tpm.J2000, double equinox=tpm.J2000,
            double lon=-111.598333,
            double lat=31.956389,
            double alt=2093.093,
            double xpole=0.0, double ypole=0.0,
            double T=273.15, double P=1013.25, double H=0.0,
            double wavelength=0.550):
    """Utility function for performing coordinate conversions.

    :param ra: Input longitudinal angle or angles, like ra, in degrees.
    :type ra: float
    :param de: Input latitudinal angle or angles, like dec, in degrees.
    :type de: float
    :param utc: "Current" UTC time as a Julian date.
    :type utc: float
    :param delta_at: TAI - UTC in seconds.
    :type delta_at: float
    :param delta_ut: UT1 - UTC in seconds.
    :type delta_ut: float
    :param s1: Initial state.
    :type s1: integer
    :param s2: Final state.
    :type s2: integer
    :param epoch: Epoch of input coordinates as a Julian date.
    :type epoch: float
    :param equniox: Equinox of input or output coordinates.
    :type equinox: float
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

    :return: Output angles, (ra_like, dec_like), in degrees
    :rtype:  One 2-element tuple, or a list of 2-element tuples, of floats

    Most often we just want to convert two angles from one coordinate
    system into another. We do not worry about proper motions and all
    conversions happen at the same "current time". This simplies the
    procedure a lot. Given a list of coordinates, most of the
    calculations need to be performed only once.

    This function performs such as coordinate conversion. It takes a
    list of ra like longitudinal angles in degrees, a list of dec like
    latitudinal angles and all parameters needed for performing a
    particular transformation. All of these parameters have defualts.

    The default location is KPNO and the values are taken from the TPM
    C code.

    If ``utc`` is not provided then it is set to J2000.0 AND BOTH
    ``delta_at`` and ``delta_ut`` ARE SET TO THEIR VALUES AT
    J2000.0. That is, if ``utc`` is not given then the specified values
    for these two are ignored. If ``utc`` is given but ``delta_at``
    and/or ``delta_ut`` is not given, then the missing value is set to
    that at the given ``utc``.

    The TPM state data structure is initialized, the independent
    parameters are set, and all the dependent parameters are calculated
    using ``tpm_data(tstate, TPM_INIT)``. This calculation is done only
    once. Then each of the coordinates are converted, by creating a
    ``V6`` vector and calling ``tpm()``.

    The returned result is a list of tuples, where each tuple has the
    final ra like angle as the first element, and the final de like
    angle as the second element. If the input coordinates are single
    values and not lists, then the output is a single 2-element tuple.
    
    For details on the parameters see the PyTPM reference documentation
    and the TPM manual. The latter gives an example for the usage of
    this function.
    """
    # -999 given so that the function has keyword arguments; If default
    # value is not present then Cython will not create keywords.

    # This check is problamatic for Numpy array.
    try:
        if ra == -999 or dec == -999:
            raise TypeError, "ra and dec cannot be empty."
    except ValueError:
        # Must be Numpy array
        pass

    if utc == -999:
        # UTC not supplied set all three time scale values, ignoring
        # the given values of delta_at and delta_ut.
        utc = tpm.J2000
        delta_at = tpm.delta_AT(utc)
        delta_ut = tpm.delta_UT(utc)
    else:
        if delta_at == -999:
            delta_at = tpm.delta_AT(utc)
        if delta_ut == -999:
            delta_ut = tpm.delta_UT(utc)

    try:
        len(ra)
    except TypeError:
        # Not a list. Assume that this is a single number.
        ra = [tpm.d2r(ra)]
    else:
        ra = [tpm.d2r(i) for i in ra]        
    try:
        len(dec)
    except TypeError:
        # Not a list. Assume that this is a single number.
        dec = [tpm.d2r(dec)]
    else:
        dec = [tpm.d2r(i) for i in dec]
        
    if len(ra) != len(dec):
            raise ValueError, "Both ra and dec must be of equal length."

    lon = tpm.d2r(lon)
    lat = tpm.d2r(lat)

    ra_out, dec_out = _convert(ra, dec, s1,  s2, epoch,  equinox,
                              utc,  delta_ut, delta_at, lon, lat,
                              alt, xpole,  ypole, T,  P,  H,
                              wavelength)

    x = [(tpm.r2d(i), tpm.r2d(j)) for i,j in zip(ra_out, dec_out)]
    if len(x) == 1:
        return x[0]
    return x

cpdef convertv6(v6=None, double utc=-999, double delta_at=-999,
            double delta_ut=-999,
            int s1=tpm.TPM_S06, int s2=tpm.TARGET_OBS_AZEL,
            double epoch=tpm.J2000, double equinox=tpm.J2000,
            double lon=-111.598333,
            double lat=31.956389,
            double alt=2093.093,
            double xpole=0.0, double ypole=0.0,
            double T=273.15, double P=1013.25, double H=0.0,
            double wavelength=0.550):
    """Utility function for performing coordinate conversions.

    :param v6: The V6C vector(s) to be transformed.
    :type v6: V6C
    :param utc: "Current" UTC time as a Julian date.
    :type utc: float
    :param delta_at: TAI - UTC in seconds.
    :type delta_at: float
    :param delta_ut: UT1 - UTC in seconds.
    :type delta_ut: float
    :param s1: Initial state.
    :type s1: integer
    :param s2: Final state.
    :type s2: integer
    :param epoch: Epoch of input coordinates as a Julian date.
    :type epoch: float
    :param equniox: Equinox of input or output coordinates.
    :type equinox: float
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

    :return: The transformed V6C vector.
    :rtype: V6C

    The input v6 can be a single V6C object or a list/tuple of V6C
    objects. The independent parameters will be the same for all of the
    V6C object and the dependent parameters will be calculated only
    once.
    
    The default location is KPNO and the values are taken from the TPM
    C code.

    If ``utc`` is not provided then it is set to J2000.0 AND BOTH
    ``delta_at`` and ``delta_ut`` ARE SET TO THEIR VALUES AT
    J2000.0. That is, if ``utc`` is not given then the specified values
    for these two are ignored. If ``utc`` is given but ``delta_at``
    and/or ``delta_ut`` is not given, then the missing value is set to
    that at the given ``utc``.
    """
    cdef int i
    if not v6:
        raise TypeError("convertv6 needs V6C object.")
    if utc == -999:
        # UTC not supplied set all three time scale values, ignoring
        # the given values of delta_at and delta_ut.
        utc = tpm.J2000
        delta_at = tpm.delta_AT(utc)
        delta_ut = tpm.delta_UT(utc)
    else:
        if delta_at == -999:
            delta_at = tpm.delta_AT(utc)
        if delta_ut == -999:
            delta_ut = tpm.delta_UT(utc)
    try:
        len(v6)
    except TypeError:
        # Not a list. Assume that this is a single number.
        v6 = (v6,)
    for j,v in enumerate(v6):
        if type(v) != type(tpm.V6C()):
            if j == 0:
                raise TypeError("v6 must be an object of type tpm.V6C.")
            else:
                raise TypeError(
                    "v6[{0}] must be an object of type tpm.V6C.".format(j))

    tstate = tpm.TSTATE()
    # Initialize TPM state.
    tpm.tpm_data(tstate, tpm.TPM_INIT)
    
    # Set independent quantities.
    tstate.utc = utc
    tstate.delta_ut = delta_ut
    tstate.delta_at = delta_at
    tstate.lon = tpm.d2r(lon) 
    tstate.lat = tpm.d2r(lat) 
    tstate.alt = alt
    tstate.xpole = xpole
    tstate.ypole = ypole
    tstate.T = T
    tstate.P = P
    tstate.H = H
    tstate.wavelength = wavelength

    # Calculate all dependent parameters.
    tpm.tpm_data(tstate, tpm.TPM_ALL)
            
    pvec = tpm.PVEC()
    v6_out = []
    for v in v6:
        pvec[s1] = v

        temp =  tpm.tpm(pvec, s1, s2, epoch, equinox, tstate)
        assert s2 == temp
        v6_out.append(pvec[s2])

    if len(v6) == 1:
        return v6_out[0]
    return v6_out
    
cpdef precess(ra=-999,dec=-999,double start=-999,double end=-999,
              int pflag=tpm.PRECESS_FK5):
    """Precess list of ra and dec values.

    :param ra: Right Ascension, scalar or list.
    :type ra: float
    :param dec: Declination, scalar of list.
    :type dec: float
    :param start: Starting time for precession, as a Julian date.
    :type start: float
    :param end: End time for precession, as a Julian date.
    :type end: float
    :param pflag: The precession model to use.
    :type pflag: integer

    This function can be used to precess equatorial (ra,dec)
    corodinates using a particular model of precession. The input
    coordinates can be in the FK5 or FK4 systems. In the FK5 system
    there is only one precession model, which is selected using ``pflag
    == tpm.PRECESS_FK5``. The FK4 system has several models, and can be
    selected by setting appropriate constants as the value of
    ``pflag``:

      PRECESS_ANDOYER, PRECESS_NEWCOMB, PRECESS_KINOSHITA,
      PRECESS_LIESKE

    See the tpm manual for definitions of these constants.
    """
    cdef int j
    cdef double i
    try:
        len(ra)
    except TypeError:
        # Not a list. Assume that this is a single number.
        ra = [tpm.d2r(ra)]
    else:
        ra = [tpm.d2r(i) for i in ra]        
    try:
        len(dec)
    except TypeError:
        # Not a list. Assume that this is a single number.
        dec = [tpm.d2r(dec)]
    else:
        dec = [tpm.d2r(i) for i in dec]
        
    if len(ra) != len(dec):
            raise ValueError, "Both ra and dec must be of equal length."

    ra_out = []
    dec_out = []
    for j in range(len(ra)):
        v6 = tpm.V6S(r=1e10,alpha=ra[j],delta=dec[j])
        v6 = v6.s2c()
        v6 = tpm.precess(start,end,v6,pflag)
        v6 = v6.c2s()
        ra_out.append(v6.nalpha)
        dec_out.append(v6.ndelta)

    ra_out = [tpm.r2d(i) for i in ra_out]
    dec_out = [tpm.r2d(i) for i in dec_out]

    return ra_out, dec_out
