import tpm

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
    """
    convert(v6=None,
            utc=-999, delta_at=-999, delta_ut=-999,
            s1=tpm.TPM_S06, s2=tpm.TARGET_OBS_AZEL,
            epoch=tpm.J2000, equinox=tpm.J2000,
            lon=-111.598333, lat=31.956389, alt=2093.093,
            xpole=0.0, ypole=0.0,
            T=273.15, P=1013.25, H=0.0, wavelength=0.550)

    Utility function for performing coordinate conversions.

    Parameters
    ----------
    v6 : tpm.V6C or a list of tpm.V6C vectors.
        The V6C vector to be trasnformed.
    utc : float
        "Current" UTC time as a Julian date.
    delta_at : float
        TAI - UTC in seconds.
    delta_ut : float
        UT1 - UTC in seconds.
    s1 : int
        Initial state.
    s2 : int
        Final state.
    epoch : float
        Epoch of input coordinates as a Julian date.
    equniox : float
        Equinox of input or output coordinates.
    lon : float
        Geodetic longitude in degeres.
    lat : float
        Geodetic latitude in degrees.
    alt : float
        Altitude in meters.
    xpole : float
        Polar motion in radians.
    ypole : float
        Ploar motion in radians.
    T : float
         Ambient temperature in Kelvin.
    P : float
        Ambient pressure in millibars.
    H : float
        Ambient humidity in the range 0-1.
    wavelength : float
        Wavelength of observation in microns.

    Returns
    -------
    v : tpm.V6C or list of tpm.V6C vectors.
        The transformed V6C vector.

    Notes
    -----
    The input v6 can be a single V6C object or a list/tuple of V6C
    objects. The independent parameters will be the same for all of the
    V6C object and the dependent parameters will be calculated only
    once.

    The default location is KPNO and the values are taken from the TPM
    C code.

    If `utc` is not provided then it is set to J2000.0 AND BOTH
    `delta_at` and `delta_ut` ARE SET TO THEIR VALUES AT
    J2000.0. That is, if `utc` is not given then the specified values
    for these two are ignored. If `utc` is given but `delta_at`
    and/or `delta_ut` is not given, then the missing value is set to
    that at the given `utc`.

    The TPM state data structure is initialized, the independent
    parameters are set, and all the dependent parameters are calculated
    using `tpm_data(tstate, TPM_INIT)`. This calculation is done only
    once. Then each of the coordinates are converted, by creating a
    `V6` vector and calling `tpm()`.

    The value returned is either a single V6C object or a list of V6C
    objects, depending on the input.
    
    For details on the parameters see the PyTPM reference documentation
    and the TPM manual. The latter gives an example for the usage of
    this function.
    
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
        # Not a list. Assume that this is a single vector.
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
    
cpdef precess(alpha=-999, delta=-999, start=-999, end=-999,
              pflag=tpm.PRECESS_FK5):
    """Precess list of alpha and delta values.

    Parameters
    ----------
    alpha : float or list of floats or 1D Numpy array.
        Longitudinal angle in degrees.
    dec : float or list of floats or 1D Numpy array.
        Latitudinal angle in degrees.
    start : float
        Starting time for precession, as a Julian date.
    end : float
        End time for precession, as a Julian date.
    pflag : int
        The precession model to use.

    Returns
    -------
    (a, d) : 2-element tuple or list of 2-element tuples
        Precessed longitudinal and latitudinal angles.

    Notes
    -----
    This function can be used to precess equatorial (ra,dec)
    coordinates using a particular model of precession. The input
    coordinates can be in the FK5 or FK4 systems. In the FK5 system
    there is only one precession model, which is selected using ``pflag
    == tpm.PRECESS_FK5``. The FK4 system has several models, and can be
    selected by setting appropriate constants as the value of
    `pflag`:

      PRECESS_ANDOYER, PRECESS_NEWCOMB, PRECESS_KINOSHITA,
      PRECESS_LIESKE

    See the tpm manual for definitions of these constants.

    """
    cdef int j
    cdef double i
    try:
        len(alpha)
    except TypeError:
        # Not a list. Assume that this is a single number.
        alpha = [tpm.d2r(alpha)]
    else:
        alpha = [tpm.d2r(i) for i in alpha]        
    try:
        len(delta)
    except TypeError:
        # Not a list. Assume that this is a single number.
        delta = [tpm.d2r(delta)]
    else:
        delta = [tpm.d2r(i) for i in delta]
        
    if len(alpha) != len(delta):
            raise ValueError(
                    "Both alpha and delta must be of equal length.")

    alpha_out = []
    delta_out = []
    for j in range(len(alpha)):
        v6 = tpm.V6S(r=1e10,alpha=alpha[j],delta=delta[j])
        v6 = v6.s2c()
        v6 = tpm.precess(start,end,v6,pflag)
        v6 = v6.c2s()
        alpha_out.append(v6.nalpha)
        delta_out.append(v6.ndelta)

    alpha_out = [tpm.r2d(i) for i in alpha_out]
    delta_out = [tpm.r2d(i) for i in delta_out]

    if len(alpha) == 1:
        return alpha_out[0], delta_out[0]
    else:
        return alpha_out, delta_out

cpdef precessv6(v6=None, start=-999, end=-999, pflag=tpm.PRECESS_FK5):
    """Precess a list of V6C vectors.

    Parameters
    ----------
    v6 : tpm.V6C or list of tpm.V6C 
        V6C vector to be precessed.
    start : float
        Starting time for precession, as a Julian date.
    end : float
        End time for precession, as a Julian date.
    pflag : int
        The precession model to use.

    Returns
    -------
    v6 : tpm.V6C or list of tpm.V6C objects.
        Precessed V6C vector.

    Notes
    -----
    This function can be used to precess equatorial in a V6C vector
    using a particular model of precession. The input coordinates can
    be in the FK5 or FK4 systems. In the FK5 system there is only one
    precession model, which is selected using ``pflag ==
    tpm.PRECESS_FK5``. The FK4 system has several models, and can be
    selected by setting appropriate constants as the value of `pflag`::

      PRECESS_ANDOYER, PRECESS_NEWCOMB, PRECESS_KINOSHITA,
      PRECESS_LIESKE

    See the tpm manual for definitions of these constants.
    
    """
    cdef int i
    if not v6:
        raise TypeError("precessv6 needs V6C object.")

    try:
        len(v6)
    except TypeError:
        # Not a list. Assume that this is a single vector.
        v6 = (v6,)

    for j,v in enumerate(v6):
        if type(v) != type(tpm.V6C()):
            if j == 0:
                raise TypeError("v6 must be an object of type tpm.V6C.")
            else:
                raise TypeError(
                    "v6[{0}] must be an object of type tpm.V6C.".format(j))
    
    v6_out = []
    for j in v6:
        v6_out.append(tpm.precess(start, end, j, pflag))

    if len(v6) == 1:
        return v6_out[0]
    else:
        return v6_out

def proper_motion(v6, end, start):
    """Apply proper motion to tpm.V6C vectors.

    Parameters
    ----------
    v6 : tpm.V6C or a list of tpm.V6C objects.
        V6C object containing positions and velocities.
    end : float
        Ending/final time in days (can be Julian date).
    start : float
        Starting/initial time in days (can be Julian date).

    Returns
    -------
    v : tpm.V6C or a list of tpm.V6C objects.
        V6C object containing the coordinates obtained after applying
        proper motion.

    Notes
    -----
    Given starting time and end time, this function applies proper
    motion to the coordinates in the given V6C object. A simple linear
    multiplication of velocity with time is performed, followed by 
    addition of this increment to the position coordinates.

    The difference, ``end - start``, should be the number of days in
    the time interval. Hence Julian dates can be used. The velocities
    in V6C are stored as AU/day and hence time interval must be in
    days.

    This function calls tpm.proper_motion repeatedly to perform the
    calculations. 
    
    """
    cdef int i
    if not v6:
        raise TypeError("proper_motion needs V6C object.")
    try:
        len(v6)
    except TypeError:
        # Not a list. Assume that this is a single vector.
        v6 = (v6,)

    for j,v in enumerate(v6):
        if type(v) != type(tpm.V6C()):
            if j == 0:
                raise TypeError("v6 must be an object of type tpm.V6C.")
            else:
                raise TypeError(
                    "v6[{0}] must be an object of type tpm.V6C.".format(j))
    
    v6_out = []
    for j in v6:
        v6_out.append(tpm.proper_motion(j, end=end, start=start))

    if len(v6) == 1:
        return v6_out[0]
    else:
        return v6_out
    



