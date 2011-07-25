# -*- coding: utf-8 -*-
# The following line must be present in the tpm.pyx file.
# cimport tpm_astro

IAU_K = tpm_astro.IAU_K
IAU_DM = tpm_astro.IAU_DM 
IAU_AU = tpm_astro.IAU_AU  
IAU_C  = tpm_astro.IAU_C  
IAU_RE = tpm_astro.IAU_RE  
IAU_RM = tpm_astro.IAU_RM  
IAU_F  = tpm_astro.IAU_F  
IAU_KAPPA = tpm_astro.IAU_KAPPA
IAU_W   = tpm_astro.IAU_W 
GAL_RA  = tpm_astro.GAL_RA 
GAL_DEC = tpm_astro.GAL_DEC 
GAL_LON = tpm_astro.GAL_LON 
PRECESS_NEWCOMB    = tpm_astro.PRECESS_NEWCOMB 
PRECESS_ANDOYER    = tpm_astro.PRECESS_ANDOYER 
PRECESS_KINOSHITA  = tpm_astro.PRECESS_KINOSHITA 
PRECESS_LIESKE     = tpm_astro.PRECESS_LIESKE 
PRECESS_FK4        = tpm_astro.PRECESS_FK4 
PRECESS_FK5        = tpm_astro.PRECESS_FK5 
PRECESS_INERTIAL   = tpm_astro.PRECESS_INERTIAL 
PRECESS_ROTATING   = tpm_astro.PRECESS_ROTATING 

def tpm_data(TSTATE tstate, int action):
    """Compute and set dependent TSTATE data.

    Given a TSTATE and an action, this function will perform the action
    and set the various dependent properties of the TSTATE object.
    
    Parameters
    ----------
    tstate : tpm.TSTATE
        The TPM state structure to be changed.
    action : int
        The action to perform.

    Notes
    -----
    The `action` can be one of

    + ``TPM_INIT``
        Perform initialization.
    + ``TPM_FAST``
        Calculate all fast changing properties.
    + ``TPM_MEDIUM``
        Calculate all properties that change at a medium rate.
    + ``TPM_SLOW``
        Calculate all properties that change slowly.
    + ``TPM_REFRACTION``
        Cacluate refraction coefficients.
    + ``TPM_ALL``
        Perform all calculations except ``TPM_REFRACTION``.

    The TPM manual has more details on these quantities.
    
    """
    tpm_astro.tpm_data(&tstate._tstate, action)

# If I use tpm_tpm.N_TPM_STATES or N_TPM_STATES inplace of 22 then
# Cython gives the following error: Not allowed in a constant
# expression. Why?  In C code I can do V6 pvec[N_TPM_STATES]. Maybe
# Cython can't determine if N_TPM_STATES is a constant or not?
cdef struct s_pvec:
    tpm_vec.V6 pvec[22]
ctypedef s_pvec S_PVEC

cdef class PVEC(object):
    """Class for holding N_TPM_STATES element array of V6 vectors.

    This is a list like object with valid indexes from 0 to 21. Each
    index represents the state having the same number. Each index
    location stores a V6C vector corresponding to that state.
    """
    cdef S_PVEC _pvec

    def __cinit__(self):
        """Initialize the array of V6 vectors."""
        cdef int i = 0
        for i in range(N_TPM_STATES):
            self._pvec.pvec[i].v[POS].type = CARTESIAN
            self._pvec.pvec[i].v[POS].v[0] = 0.0
            self._pvec.pvec[i].v[POS].v[1] = 0.0
            self._pvec.pvec[i].v[POS].v[2] = 0.0
            self._pvec.pvec[i].v[VEL].type = CARTESIAN
            self._pvec.pvec[i].v[VEL].v[0] = 0.0
            self._pvec.pvec[i].v[VEL].v[1] = 0.0
            self._pvec.pvec[i].v[VEL].v[2] = 0.0

    def __init__(self):
        """Initialize the array of V6 vectors."""
        # Repeating the __cinit__ code.
        cdef int i = 0
        for i in range(N_TPM_STATES):
            self._pvec.pvec[i].v[POS].type = CARTESIAN
            self._pvec.pvec[i].v[POS].v[0] = 0.0
            self._pvec.pvec[i].v[POS].v[1] = 0.0
            self._pvec.pvec[i].v[POS].v[2] = 0.0
            self._pvec.pvec[i].v[VEL].type = CARTESIAN
            self._pvec.pvec[i].v[VEL].v[0] = 0.0
            self._pvec.pvec[i].v[VEL].v[1] = 0.0
            self._pvec.pvec[i].v[VEL].v[2] = 0.0

    cdef S_PVEC __get_pvec(self):
        """Return the underlying C array; only for use from Cython."""
        # No checks to see if all of the elements are Cartesian.
        return self._pvec

    cdef __set_pvec(self, S_PVEC spv):
        """Set the underlying C array; only for use from Cython."""
        # No checks to see if all of the elements are Cartesian.
        self._pvec = spv
        
    def __getitem__(self, int index):
        """Return V6 at given index; 0 <= index < N_TPM_STATES."""
        if type(index) != type(1):
            raise TypeError, "Index must be an integer."
        if not (0 <= index < N_TPM_STATES):
            raise IndexError, \
                "Index must be in 0 <= index < N_TPM_STATES."
        v6c = V6C()
        v6c.setV6(self._pvec.pvec[index])
        return v6c

    def __setitem__(self, int index, V6C v6c):
        """Set V6 at given index; 0 <= index < N_TPM_STATES."""
        if type(index) != type(1):
            raise TypeError, "Index must be an integer."
        if not (0 <= index < N_TPM_STATES):
            raise IndexError, \
                "Index must be in 0 <= index < N_TPM_STATES."
        if type(v6c) != type(V6C()):
            raise TypeError, "Value must be a V6C object."
        self._pvec.pvec[index] = v6c.getV6()
        

def tpm(PVEC pvec, int s1, int s2, double ep, double eq, TSTATE tstate):
    """Apply transition between to states.

    On completion the `pvec` object will contain state vectors obtained
    during all transitions needed for the `s1` to `s2`
    transition. Specifically, `pvec[s2]` will have the V6C vector
    corresponding to the target state `s2`.
    
    Parameters
    ----------
    pvec : tpm.PVEC
        A PVEC object with appropriate V6 members.
    s1 : int
        Starting state (0 <= s1 < N_TPM_STATES).
    s2 : int
        End state (0 <= s2 < N_TPM_STATES).    
    ep : float
        Epoch of state vector corresponding to `s1`, as a Julian date.
    eq : float
        Equinox as a Julian date. It can be of s1 and or s2, depending
        on the specific transition.
    tstate : tpm.TSTATE
        A TSTATE object with appropriate initial values.

    Returns
    -------
    s : int
        Final state (must be equal to `s2`).

    Notes
    -----
    This is the main TPM function. It looks up the state tables and
    performs all required transformations to take the state vector at
    `pvec[s1]` from state `s1` to state `s2`. It stores the
    resulting state vector in `pvec[s2]`. Intermediate states are
    stored in their respective positions in `pvec`.

    For more information see the TPM manual.
    
    """
    if not 0 <= s1 < N_TPM_STATES:
        raise ValueError, "S1 must be in 0 <= S1 < N_TPM_STATES"
    if not 0 <= s2 < N_TPM_STATES:
        raise ValueError, "S2 must be in 0 <= S2 < N_TPM_STATES"
    cdef S_PVEC spvec
    cdef tpm_tpm.TPM_TSTATE ststate
    
    spvec = pvec.__get_pvec()
    ststate = tstate.__get_tstate()
    t = tpm_astro.tpm(spvec.pvec, s1, s2, ep, eq, &ststate)
    pvec.__set_pvec(spvec)
    tstate.__set_tstate(ststate)
    return t

def tpm_state(s):
    """Return state name given state id.

    Given an integer id for a state, this function returns a
    descriptive name for the state.
    
    Parameters
    ----------
    s : int
        State id.

    Returns
    -------
    n : str
        State name.

    Examples
    --------
    >>> tpm.tpm_state(tpm.TPM_S06)
    'Helio. mean FK5'
    >>> tpm.tpm_state(tpm.TPM_S04)
    'IAU 1958 Galactic'
    >>> tpm.tpm_state(tpm.TPM_S20)
    'Topo. obs. HA/Dec'
    >>> tpm.tpm_state(tpm.TPM_S19)
    'Topo. obs. Az/El'
    
    """
    return tpm_astro.tpm_state(s).decode("utf-8")

def delta_AT(utc):
    """Return Delta AT = TAI - UTC for the given UTC.

    .. warning:: 
    
        The file src/tpm/delta_AT.c must be updated when Delta AT is
        changed by the IERS, and PyTPM Cython code must re-compiled.

    Parameters
    ----------
    utc : float
        UTC as a Julian date.

    Returns
    -------
    d : float
        Delta AT = TAI - UTC in seconds.

    """
    return tpm_astro.delta_AT(utc)

def delta_T(ut1):
    """Return Delta T = TT - UT1 for the given UT1.

    Parameters
    ----------
    ut1 : float
        UT1 as a Julian date.

    Returns
    -------
    dt : float
        Delta T = TT - UT1 in seconds.

    Notes
    -----
    This function returns the ``TT - UT1`` value for the given UT1. The
    value returned is ``ET - UT1`` for dates before 1984.0 and ``TDT -
    UT1`` for dates on and after 1984.0. TDT was the name of TT between
    1984.0 and 2000.0.

    .. warning::
    
        A simple linear interpolation is carried out over a list of
        historical values.
        
    """
    return tpm_astro.delta_T(ut1)

def delta_UT(utc):
    """Return Delta UT = UT1 - UTC for the given UTC.

    Parameters
    ----------
    utc : float
        UTC as a Julian date.

    Returns
    -------
    dt  : float
        UT1 - UTC for in seconds.

    Notes
    -----
    The value of ``UT1 - UTC`` is calculated by taking the difference
    of delta_ET and delta_T. The later is calculated using a built-in
    model. For the latter the input time argument must be UT1, but the
    error in using UTC should be small.
    
    """
    return tpm_astro.delta_UT(utc)

def delta_ET(utc):
    """Return Delta ET = ET - UTC for the given UTC.

    Parameters
    ----------
    utc : float
        UTC as a Julian date.

    Returns
    -------
    dt : float
        Delta ET = ET - UTC in seconds.

    """
    return tpm_astro.delta_ET(utc)

def delta_TT(utc):
    """Return Delta TT = TDT - UTC for the given UTC.

    Parameters
    ----------
    utc : float
        UTC as a Julian date.

    Returns
    -------
    dt : float
        Delta TT = TDT - UTC.

    """
    return tpm_astro.delta_TT(utc)

def tdt2tdb(tdt):
    """Return TDB for the given TDT.

    Parameters
    ----------
    tdt : float
        TDT as a Julian date.

    Returns
    -------
    dt : float
        TDB as a Julian date.

    """
    return tpm_astro.tdt2tdb(tdt)

def ut12gmst(ut1):
    """Return GMST for the given UT1.

    Given a UT1 Julian date, this function returns the Greenwich Mean
    Sidereal Time as an angle in radians in the range (0, 2π).
    
    Parameters
    ----------
    ut1 : float
        UT1 as a Julian date.

    Returns
    -------
    gmst : float
        GMST as an angle in radians in the range 0-2π.
    
    """
    return tpm_astro.ut12gmst(ut1)
    
def et2tdt(et):
    """Return TDT for the given ET.

    Parameters
    ----------
    et : float
        ET as a Julian date.

    Returns
    -------
    tdt : float
        TDT as a Julian date.
        
    """
    return tpm_astro.et2tdt(et)

def tai2tdt(tai):
    """Return TDT for the given TAI.

    Parameters
    ----------
    tai : float
        TAI as a Julian date.

    Returns
    -------
    tdt : float
        TDT as a Julian date.

    """
    return tpm_astro.tai2tdt(tai)

def tdt2et(tdt):
    """Return ET for the given TDT.

    Parameters
    ----------
    tdt : float
        TDT as a Julian date.

    Returns
    --------
    et : float
        ET as a Julian date.

    """
    return tpm_astro.tdt2et(tdt)

def ut12et(ut1):
    """Return ET for the given UT1.

    Parameters
    ----------
    ut1 : float
        UT1 as a Julian date.

    Returns
    -------
    et : float
        ET as a Julian date.

    """
    return tpm_astro.ut12et(ut1)

def utc2et(utc):
    """Return ET for the given UTC.

    Parameters
    ----------
    utc : float
        UTC as a Julian date.

    Returns
    -------
    et : float
        ET as a Julian date.

    """
    return tpm_astro.utc2et(utc)

def utc2tdt(utc):
    """Return TDT for the given UTC.

    Parameters
    ----------
    utc : float
         UTC as a Julian date.

    Returns
    -------
    tdt : float
        TDT as a Julian date.
        
    """
    return tpm_astro.utc2tdt(utc)

def utc2ut1(utc):
    """Return UT1 for the given UTC.

    Parameters
    ----------
    utcv: float
        UTC as a Julian date.

    Returns
    -------
    ut1 : float
        UT1 as a Julian date.

    """
    return tpm_astro.utc2ut1(utc)
    
def et2ut1(et):
    """Return UT1 for the given ET.

    Parameters
    ----------
    et : float
        ET as a Julian date.

    Returns
    -------
    ut1 : float
        UT1 as a Julian date.

    """
    return tpm_astro.et2ut1(et)

def et2utc(et):
    """Return UTC for the given ET.

    Parameters
    ----------
    et : float
        ET as a Julian date.

    Returns
    -------
    utc : float
        UTC as a Julian date.

    """
    return tpm_astro.et2utc(et)

def tai2utc(tai):
    """Return UTC for the given TAI.

    Parameters
    ----------
    tai : float
        TAI as a Julian date.

    Returns
    -------
    utc : float
        UTC as a Julian date.

    """
    return tpm_astro.tai2utc(tai)

def tdt2tai(tdt):
    """Return TAI for the given TDT.

    Parameters
    ----------
    tdt : float
        TDT as a Julian date.

    Returns
    -------
    tai : float
        TAI as a Julian date.

    """
    return tpm_astro.tdt2tai(tdt)

def tdt2utc(tdt):
    """Return UTC for the given TDT.

    Parameters
    ----------
    tdt : float
        TDT as a Julian date.

    Returns
    -------
    utc : float
        UTC as a Julian date.

    """
    return tpm_astro.tdt2utc(tdt)

def ut12utc(ut1):
    """Return UTC for the given UT1.

    Parameters
    ----------
    ut1 : float
        UT1 as a Julian date.

    Returns
    -------
    utc : float
        UTC as a Julian date.

    """
    return tpm_astro.ut12utc(ut1)

def et2tai(et):
    """Return TAI for the given ET.

    Parameters
    ----------
    et : float
        ET as a Julian date.

    Returns
    -------
    tai : float
         TAI as a Julian date.

    """
    return tpm_astro.et2tai(et)

def et2tdb(et):
    """Return TDB for the given ET.

    Parameters
    ----------
    et : float
        ET as a Julian date.

    Returns
    -------
    tdb : float
        TDB as a Julian date.

    """
    return tpm_astro.et2tdb(et)

def tai2et(tai):
    """Return ET for the given TAI.

    Parameters
    ----------
    tai : float
        TAI as a Julian date.     

    Returns
    -------
    et : float
        ET as a Julian date.

    """
    return tpm_astro.tai2et(tai)

def tai2tdb(tai):
    """Return TDB for the given TAI.

    Parameters
    ----------
    tai : float
        TAI as a Julian date.

    Returns
    -------
    tdb : float
        TDB as a Julian date.

    """
    return tpm_astro.tai2tdb(tai)

def tai2ut1(tai):
    """Return UT1 for the given TAI.

    Parameters
    ----------
    tai : float
        TAI as a Julian date.

    Returns
    -------
    ut1 : float
         UT1 as a Julian date.

    """
    return tpm_astro.tai2ut1(tai)

#def tdb2et(tdb):
#    """Return ET for the given TDB."""
#    return tpm_astro.tdb2et(tdb)
# 
#def tdb2tai(tdb):
#    """Return TAI for the given TDB."""
#    return tpm_astro.tdb2tai(tdb)
# 
#def tdb2ut1(tdb):
#    """Return UT1 for the given TDB."""
#    return tpm_astro.tdb2ut1(tdb)
# 
#def tdb2utc(tdb):
#    """Return UTC for the given TDB."""
#    return tpm_astro.tdb2utc(tdb)

def tdt2ut1(tdt):
    """Return UT1 for the given TDT.

    Parameters
    ----------
    tdt : float
        TDT as a Julian date.

    Returns
    -------
    ut1 : float
        UT1 as a Julian date.

    """
    return tpm_astro.tdt2ut1(tdt)

def ut12tai(ut1):
    """Return TAI for the given UT1.

    Parameters
    ----------
    ut1 : float
        UT1 as a Julian date.

    Returns
    -------
    tai : float
        TAI as a Julian date.

    """
    return tpm_astro.ut12tai(ut1)

def ut12tdb(ut1):
    """Return TDB for the given UT1.

    Parameters
    ----------
    ut1 : float
        UT1 as a Julian date.

    Returns
    -------
    tdb : float
         TDB as a Julian date.

    """
    return tpm_astro.ut12tdb(ut1)

def ut12tdt(ut1):
    """Return TDT for the given UT1.

    Parameters
    ----------
    ut1 : float
        UT1 as a Julian date.

    Returns
    -------
    tdt : float
         TDT as a Julian date.

    """
    return tpm_astro.ut12tdt(ut1)

def utc2tdb(utc):
    """Return TDB for the given UTC.

    Parameters
    ----------
    utc : float
        UTC as a Julian date.

    Returns
    -------
    tdb : float
         TDB as a Julian date.

    """
    return tpm_astro.utc2tdb(utc)

def et2ut(et):
    """Return UT for the given ET; same as et2ut1(et)."""
    return tpm_astro.et2ut(et)

def ut2et(ut):
    """Return ET for the given UT; same as ut12et(ut)."""
    return tpm_astro.ut2et(ut)

def ut2gmst(ut):
    """Return GMST for the given UT; same as ut12gmst(ut)"""
    return tpm_astro.ut2gmst(ut)

def cat2v6(alpha, delta, pma, pmd, px, rv, C=36525.0):
    """Create a V6C vector from a catalog entry.

    Parameters
    ----------
    alpha : float
        Longitudinal angle (e.g., RA) in radians.
    delta : float
        Latitudinal angle (e.g., Dec) in radians.
    pma : float
        Proper motion in `alpha` (not pmra*cos(delta)) in "/century.
    pmd : float
        Proper motion in `delta` in "/century.
    px : float
        Parallax in arc-seconds.
    rv : float
        Radial velocity in km/s.
    C : float
        Days in a century, as used in pmra and pmde.

    Returns
    -------
    v6 : tpm.V6C
        V6C vector containing the Cartesian position and velocities of
        the catalog position.

    Notes
    -----
    This function is used to convert a catalog entry for an object into
    a `V6C` vector.

    Internally TPM uses velocities in AU/day, and needs to know how
    many days are in a century. The proper motions can be in
    arc-seconds per Julian century or arc-seconds per tropical century.
    A Julian century has 36525 days (`tpm.CJ`) and a tropical century
    has 36524.21987817305 days (`tpm.CB`).
    
    """
    v6 = V6C()
    v6.setV6(tpm_astro.cat2v6(alpha, delta, pma, pmd, px, rv, C))
    return v6
    
def v62cat(V6C v6, C=36525.0):
    """Return catalog quantites given a V6C vector.

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C object containing the position and velocity of an
        object. It is assumed that the positions are in AU and
        velocities are in AU/day.
    C : float
        Number of days in a century. To convert the velocities into
        "/centruy from AU/day, it is necessary to know the numb`er of
        days in a century. For Julian centuries this is 36525 days
        (`tpm.CJ`) and for tropical centuries this is ~36524.22
        (`tpm.CB`).

    Returns
    -------
    d : dict
        The keys and values are:
          + alpha : float
                Longitudinal coordinate (e.g., RA) in radians.
          + delta : float
                Latitudinal coordinate (e.g., Dec) in radians.
          + pma : float
                Proper motion in `alpha` (not alpha*cos(delta) in
                "/century
          + pmd : float
                Proper motion in `delta` in "/century.
          + px : float
                Parallax in arc-seconds.
          + rv : float
                Radial velocity in km/s.
                  
    """
    cdef double alpha=0.0, delta=0.0, pma=0.0, pmd=0.0, px=0.0, rv=0.0
    tpm_astro.v62cat(&alpha, &delta, &pma, &pmd, &px, &rv,
                      v6.getV6(), C)
    return dict(alpha=alpha, delta=delta, pma=pma, pmd=pmd, px=px,
                rv=rv)
    
def proper_motion(V6C v6, end, start):
    """Apply proper motion to the given V6C vector.

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C object containing positions and velocities.
    end : float
        Ending/final time in days (can be Julian date).
    start : float
        Starting/initial time in days (can be Julian date).

    Returns
    -------
    v : tpm.V6C
        A V6C object containing the new position.

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
    
    """
    cdef tpm_astro.V6 _v6
    v61 = V6C()
    _v6 = tpm_astro.proper_motion(v6.getV6(), end, start)
    v61.setV6(_v6)
    return v61

def aberrate(V6C p, V6C e, int flag):
    """Apply aberration of light to a state vector.

    Parameters
    ----------
    p : tpm.V6C
        The vector to which aberration must be applied.
    e : tpm.V6C
        The vector with aberration causing velocity component.
    flag : int
        Add aberration to `p` if flag > 0 else subtract it.

    Returns
    -------
    v : tpm.V6C
        The result of applying aberration to `p`.

    Notes
    -----
    The velocity components in `e` is taken to be the oberver's
    velocity and the aberration correction is applied to the position
    components in `p`. The aberration is added to `p` is `flag >
    0` else it is subtracted from `p`. The velocity component of
    `p` is, of-course, unchanged.

    If `e` is the barycentric state vector of the Earth's, center
    then we have geocentric aberration. If it is the sum of the above
    with the observer's geocentric space-fixed mean state vector, then
    we have topocentric aberration.

    The algorithm uses vectors and hence the `e` can be for any
    observer, not just Earth based observers.
    """
    cdef tpm_astro.V6 _v6
    _v6 = tpm_astro.aberrate(p.getV6(), e.getV6(), flag)
    v6 = V6C()
    v6.setV6(_v6)
    return v6

def azel2hadec(V6C v6, double latitude):
    """Convert V6C from (AZ, EL) to (HA, DEC).

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C vector containing Cartesian coordinates in Az-El system.
    latitude : float
        Latitude in radians. Northern latitudes are positive.

    Returns
    -------
    v : tpm.V6C
        State vector converted into Ha-Dec system.


    Notes
    -----
    Two simple rotations are performed on `v6` to convert it from
    (AZ, EL) system into (HA, DEC) system.  Azimuth is measured
    north of east.

    The conversion from (AZ, EL) to (HA, DEC) does not require the full
    setup of TPM and hence this function can be directly used for the
    above conversion.
    """
    v = V6C()
    v.setV6(tpm_astro.azel2hadec(v6.getV6(), latitude))
    return v

def hadec2azel(V6C v6, double latitude):
    """Convert V6C from (HA, DEC) to (AZ, EL).

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C vector containing Cartesian cooridinates in Ha-Dec system.
    latitude : float
        Latitude in radians.

    Return
    ------
    v : tpm.V6C
        State vector converted into (AZ, EL) system.

    Notes
    -----
    Two simple rotations are performed on ``v6`` to convert it from
    (HA, DEC) system into (AZ, EL) system.  Azimuth is measured
    north of east.

    The conversion from (HA, DEC) to (AZ, EL) does not require the full
    setup of TPM and hence this function can be directly used for the
    above conversion.
    """
    v = V6C()
    v.setV6(tpm_astro.hadec2azel(v6.getV6(), latitude))
    return v

def evp(double tdb):
    """J2000 Barycentric and Heliocentric state vectors for Earth.

    Parameters
    ----------
    tdb : float
        Barycentric Dynamic Time as a Julian date.

    Returns
    -------
    v : 2 element tuple of tpm.V6C
        The first element of the tuple is the Barycentric vector and
        the second is the Heliocentric vector. The positions are in AU
        and velocities are in AU/day.

    Notes
    -----
    Calculates Earth's J2000 Barycentric and Heliocentric state
    vectors, for the given Barycentric Dynamic Time `tdb`. The state
    vector is calculated using a built-in model. See src/tpm/evp.c.

    """
    cdef tpm_vec.V6 _vb, _vh
    tpm_astro.evp(tdb, &_vb, &_vh)
    v6b = V6C()
    v6b.setV6(_vb)
    v6h = V6C()
    v6h.setV6(_vh)
    return v6b, v6h

def ecl2equ(V6C v6, double obl):
    """Convert Ecliptic to FK5 Equatorial coordinates.

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C vector with Cartesian coordinates in the Ecliptic system.
    obl : float
        Obliquity of the ecliptic at the time of interest.

    Returns
    -------
    v : tpm.V6C
        A V6C vector with Cartesian coordinates in FK5 equatorial
        coordinates.

    Notes
    -----
    A simple rotation through `obl` is performed to convert Ecliptic
    coordinates into FK5 equatorial coordinates.
    
    """
    v = V6C()
    v.setV6(tpm_astro.ecl2equ(v6.getV6(), obl))
    return v

def equ2ecl(V6C v6, double obl):
    """Convert FK5 equatorial coordinates to Ecliptic coordinates.

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C vector with Cartesian coordinates in the FK5 equatorial
        system. 
    obl : float
         Obliquity at the time of interest.

    Returns
    --------
    v : tpm.V6C
        A V6C vector with Cartesian coordinates in the Ecliptic system.

    Notes
    -----
    A simple rotation is performed to convert the given state vector
    from FK5 Equatorial system into Ecliptic system, using the given
    obliquity.
    
    """
    v = V6C()
    v.setV6(tpm_astro.equ2ecl(v6.getV6(), obl))
    return v
    
def ellab(double tdt, V6C star, int flag):
    """Add or remove elliptic aberration.

    Parameters
    ----------
    tdt : float
        Terrestrial Time (same as Terrestrial Dynamic Time).
    star : tpm.V6C
        A state vector for the object.
    flag : int
        Add correction if flag > 0 else subtract.

    Returns
    -------
    v : tpm.V6C
        A V6C vector with elliptic aberration applied to the input.

        
    Notes
    -----
    This function applies elliptic aberration to the the given state
    vector, and return the resulting state vector. If ``flag > 0``
    then the correction is added, otherwise it is subtracted.
    
    """
    v = V6C()
    v.setV6(tpm_astro.ellab(tdt, star.getV6(), flag))
    return v

def equ2gal(V6C v6):
    """Convert FK4 Equatorial to Galactic.

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C vector with Cartesian coordinates in FK4 Equatorial system.

    Returns
    -------
    v : tpm.V6C
        A V6C vector with Cartesian coordinates in the Galactic system.

    Notes
    -----
    Applies three rotations after subtracting E-terms of
    aberration. Galactic pole is (192.25, 27.4) degrees and longitude
    of ascending node of the Galactic plane on the equator is 33
    degrees.
    
    """
    v = V6C()
    v.setV6(tpm_astro.equ2gal(v6.getV6()))
    return v
    
def gal2equ(V6C v6):
    """Convert state vector from Galactic to FK4 Equatorial.

    Parameters
    ----------
    v6 : tpm.V6C
        A V6C vector with Cartesian coordinates in the Galactic system.

    Returns
    -------
    v : tpm.V6C
        A V6C vector with Cartesian coordinates in the FK4 Equatorial
        system. 

    Notes
    -----
    Applies three rotations and then adds E-terms of
    aberration. Galactic pole is (192.25, 27.4) degrees and longitude
    of ascending node of the Galactic plane on the equator is 33
    degrees.
    
    """
    v = V6C()
    v.setV6(tpm_astro.gal2equ(v6.getV6()))
    return v
    
def eterms(double ep):
    """Return a V6C vector containing the e-terms of aberration.

    Parameters
    ----------
    ep : float
        Epoch as a Julian date.

    Returns
    -------
    v : tpm.V6C
        a V6C vector containing the e-terms of aberration.

    Notes
    -----
    The state vector returned can be used to add or subtract the
    e-terms with another state vector.
    
    """
    v6 = V6C()
    v6.setV6(tpm_astro.eterms(ep))
    return v6

def fk425(V6C v6):
    """Precess a V6C vector from FK4 system to FK5 system.

    Parameters
    ----------
    v6 : tpm.V6C
        FK4 V6C vector to be transformed.

    Returns
    -------
    v : tpm.V6C
        FK5 V6C vector.

    Notes
    -----
    Perform FK4 to FK5 transformation of the given state vector. See
    TPM manual and src/tpm/fk425.c for more details.
    
    """
    v = V6C()
    v.setV6(tpm_astro.fk425(v6.getV6()))
    return v

def fk524(V6C v6):
    """Precess state vector from FK5 to FK4.

    Parameters
    ----------
    v6 : tpm.V6C
        FK5 V6C vector to be transformed.

    Returns
    -------
    v : tpm.V6C
        FK4 V6C vector.

    Notes
    -----    
    Perform FK4 to FK5 transformation of the given state vector. See
    TPM manual and src/tpm/fk524.c for more details.
    
    """
    v = V6C()
    v.setV6(tpm_astro.fk524(v6.getV6()))
    return v

def geod2geoc(lon, lat, alt):
    """Convert geodetic position to geocentric position.

    Parameters
    ----------
    lon : float
        Longitude in radians (east positive).
    lat : float
        Latitude in radians (north positive).
    alt : float
         Altitude in meters.

    Returns
    -------
    v : tpm.V6C
        A V6C geocentric vector. Lengths should be in meters and
        velocities should be in meters/s.

    Notes
    -----
    Converts the given geodetic position to a geocentric one and
    returns the results in a V6C state vector. The units are meters and
    meters/second.
    
    """
    v6 = V6C()
    v6.setV6(tpm_astro.geod2geoc(lon, lat, alt))
    return v6

def ldeflect(V6C star, V6C earth, int flag):
    """Apply General Relativity deflection of light.

    Parameters
    ----------
    star : tpm.V6C
        A V6C vector for the object of interest.
    earth : tpm.V6C
        V6C vector for Earth.
    flag : int
        Correction is added is flag > 0 else subtracted. 

    Returns
    -------
    v : tpm.V6C
        Light deflection corrected V6C vector.

    Notes
    -----
    Applies the relativisty light deflection due to the Sun, to the
    state vector in `star`.
    
    """
    v6 = V6C()
    v6.setV6(tpm_astro.ldeflect(star.getV6(), earth.getV6(), flag))
    return v6

def precess(double start, double end, V6C v6, int pflag):
    """Precess a state vector within an inertial frame.

    Parameters
    ----------
    start : float
        Initial epoch as a Julian date.
    end : float
        Final epoch as a Julian date.
    v6 : tpm.V6C
        The V6C vector to be precessed.
    pflag : int
        Precession model to use.

    Returns
    -------
    v : tpm.V6C
        Precessed V6C vector.

    Notes
    -----
    This function precesses the given state vector, `v6` from
    `start` to `end` using the given precession model
    `pflag`. The precession is carried out within an inertial
    frame. So this cannot do FK4 to FK5, for example.

    The values for `pflag` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    
    """
    v = V6C()
    v.setV6(tpm_astro.precess(start, end, v6.getV6(), pflag))
    return v

def precess_m(start, end, pflag, sflag):
    """Precession matrix for time between end and start.

    Parameters
    ----------
    start : float
        Starting (initial) epoch as a Julian date.
    end : float
         Ending (final) point as a Julian date.
    pflag : int
        Precession model to use.
    sflag : int
        Rotating frame or inertial frame.

    Notes
    -----
    Returns the precession matrix for precession from `start` time to
    `end` time. The model used for cacluating precession angles is
    specified using the `pflag` parameter. The possible values are::

      PRECESS_NEWCOMB	
      PRECESS_ANDOYER	
      PRECESS_KINOSHITA	
      PRECESS_LIESKE	
      PRECESS_FK4	
      PRECESS_FK5	

    If `sflag != PRECESS_ROTATING`, then the "P-dot" term in the
    precession matrix is set to null. The other possibility is
    `PRECESS_INERTIAL`, when the "P-dot" term is not set to null.
    
    """
    m6 = M6()
    m6.setM6(tpm_astro.precess_m(start, end, pflag, sflag))
    return m6

def eccentricity(tdt):
    """Eccentricity of Earth's orbit.

    Parameters
    ----------
    tdt : float
        Terrestrial Dynamic Time (same as TT) as Julian date.

    Parameters
    ----------
    e : float
        Eccentricity of Earth's orbit.

    Notes
    -----
    Returns the eccentricity of Earth's orbit at the given time. Time
    is a TDT (same as TT) as a Julian date.
    
    """
    return tpm_astro.eccentricity(tdt)

def eccentricity_dot(tdt):
    """Rate of change in the eccentricity of Earth's orbit.

    Parameters
    ----------
    tdt : float
        Terrestrial Dynamic Time (same as TT) as Julian date.

    Returns
    -------
    edot : float
        Rate of change in the eccentricity of Earth's orbit.

    Notes
    -----
    Returns the rate of change (per Julian century) in the eccentricity
    of Earth's orbit at the given time. Time is TDT (same as TT) as a
    Julian date.
    
    """
    return tpm_astro.eccentricity_dot(tdt)

def obliquity(tdt):
    """Mean obliquity of Ecliptic(epoch J2000).

    Parameters
    ----------
    tdt : float
        Terrestrial Dynamic Time (same as TT) as a Julian date.

    Returns
    -------
    obl : float
        Obliquity of the Ecliptic in radians.

    Notes
    -----
    The obliquity of the mean Ecliptic of J2000, at the given TDT (same
    as TT) is returned. The returned value is in radians.
    
    """
    return tpm_astro.obliquity(tdt)

def obliquity_dot(tdt):
    """Rate of change of mean obliquity of Ecliptic(epoch J2000).

    Parameters
    ----------
    tdt : float
        Terrestrial Dynamic Time (same as TT) as a Julian date.

    Returns
    -------
    odot : float
        Rate of change of obliquity of the Ecliptic in ra/jcen.

    Notes
    -----
    Returns the rate of change (radians per Julian century) in the
    obliquity of Ecliptic at the given time. Time is a TDT (same as TT)
    as a Julian date.
    
    """
    return tpm_astro.obliquity_dot(tdt)

def refco(lat=0.557744205098, alt=2093.093,
          T=273.15, P=1013.25, rh=0.0,
          wavelength=0.550, eps=1e-8):
    """Refractions coefficients for use with ``refract()``.

    Parameters
    ----------
    lat : float
        Observer's latitude (radians).
    alt : float
        Observer's altitude above sea level (meters).
    T : float
        Ambient temperature (Kelvin).
    rh : int
        Relative humidity (0-1).
    wavelength : float
        Wavelength in microns.
    eps : float
        Fractional accuracy.

    Returns
    -------
    r : 2-element tuple of floats
        (refa, refb)

    Notes
    -----
    The values returned are used for calculating change in zenith
    distance that must be applied to correct for refraction. These
    values are passed to the function `refract` for this calculation.

    The default location is KPNO.

    See src/tpm/refco.c for more details.
    
    """
    cdef double refa
    cdef double refb
    refa = 0.0
    refb = 0.0
    tpm_astro.refco( lat,  alt,  T,  P, rh,  wavelength,  eps,
                      &refa,  &refb)
    return (refa, refb)

def refract(zx, refa, refb, flag):
    """Returns change in zenith distance due to refraction.

    Parameters
    ----------
    zx : float
        Raw zenith distance, apparent or observed (radians).
    refa : float
        Refraction coefficient from ``refco``.
    refa : float
        Refraction coefficient from ``refco``.
    flag : float
        Apply refraction if flag > 0, else remove.

    Returns
    -------
    z : float
        Correction to zenith distance due to refraction.

    Notes
    -----
    Given a zenith distance ``zx``, this function returns the amount of
    change in this quantity due to refraction. This correction must be
    added to ``zx`` to find the resultant zenith distance.
    
    """
    return tpm_astro.refract(zx, refa, refb, flag)
    
def solar_perigee(tdt):
    """Mean longitude of the perigee of solar orbit.

    Parameters
    ----------
    tdt : float
        Terresttrial Dynamic Time (same as TT).

    Returns
    -------
    s : float
        Longitude in radians.

    """
    return tpm_astro.solar_perigee(tdt)

def solar_perigee_dot(tdt):
    """Rate of change of solar perigee.

    Parameters
    ----------
    tdt : float
        Terresttrial Dynamic Time (same as TT).

    Returns
    -------
    s : float
        Rate of change of longitude in radians/julian century.

    """
    return tpm_astro.solar_perigee_dot(tdt)

def theta(start, end, pflag):
    """FK4 and FK5 precession angles.

    Parameters
    ----------
    start : float
        Starting (initial) time as a Julian date.
    end : float
        Ending (final) time as a Julian date.
    pflag : int
        The model to use.

    Returns
    -------
    theta : float
        Precession angle for the given time period.

    Notes
    -----
    Returns the precession angle for the model indicated by `pflag`
    for the time `end`, starting from the time `start`.

    The values for `pflag` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    
    """
    return tpm_astro.theta(start, end, pflag)

def thetadot(start, end, pflag):
    """Rate of change of FK4 and FK5 precession angles.

    Parameters
    ----------
    start : float
        Starting (initial) time as a Julian date.
    end : float
        Ending (final) time as a Julian date.
    pflag : int
        The model to use.

    Returns
    -------
    td : float
        Rate of change of precession angle for the given time period.

    Notes
    -----
    Returns the rate of change of precession angle for the model
    indicated by `pflag` for the time `end`, starting from the time
    `start`.

    The values for `pflag` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    
    """
    return tpm_astro.thetadot(start, end, pflag)

def zee(start, end, pflag):
    """FK4 and FK5 precession angles.

    Parameters
    ----------
    start : float
        Starting (initial) time as a Julian date.
    end : float
        Ending (final) time as a Julian date.
    pflag : int
        The model to use.

    Returns
    -------
    z :float
         Precession angle for the given time period.

    Notes
    -----
    Returns the precession angle for the model indicated by `pflag`
    for the time `end`, starting from the time `start`.

    The values for `pflag` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    
    """
    return tpm_astro.zee(start, end, pflag)

def zeedot(start, end, pflag):
    """Rate of change of FK4 and FK5 precession angles.

    Parameters
    ----------
    start : float
        Starting (initial) time as a Julian date.
    end : float
        Ending (final) time as a Julian date.
    pflag : int
        The model to use.

    Returns
    -------
    zd :float
         Rate of change of precession angle for the given time period.

    Notes
    -----
    Returns the rate of change of precession angle for the model
    indicated by `pflag` for the time `end`, starting from the time
    `start`.

    The values for `pflag` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    return tpm_astro.zeedot(start, end, pflag)

def zeta(start, end, pflag):
    """FK4 and FK5 precession angles.

    Parameters
    ----------
    start : float
        Starting (initial) time as a Julian date.
    end : float
        Ending (final) time as a Julian date.
    pflag : int
        The model to use.

    Returns
    -------
    zd :float
         Precession angle for the given time period.

    Notes
    -----
    Returns the precession angle for the model indicated by `pflag`
    for the time `end`, starting from the time `start`.

    The values for `pflag` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    
    """
    return tpm_astro.zeta(start, end, pflag)

def zetadot(start, end, pflag):
    """Rate of change of FK4 and FK5 precession angles.

    Parameters
    ----------
    start : float
        Starting (initial) time as a Julian date.
    end : float
        Ending (final) time as a Julian date.
    pflag : int
        The model to use.

    Returns
    -------
    zd :float
         Rate of change of precession angle for the given time period.

    Notes
    -----
    Returns the rate of change of precession angle for the model
    indicated by ``pflag`` for the time ``end``, starting from the time
    ``start``.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    
    """
    return tpm_astro.zetadot(start, end, pflag)

def nutations(tdt):
    """Nutations in longitude and obliquity.

    Parameters
    ----------
    tdt : float
        Terrestrial Dynamic Time (same as TDT).

    Returns
    -------
    n : 2-element tuple of floats
        The first element is the nutation in longitude and the second
        element is the nutation in obliquity. Both are in radians.

    """
    cdef double delta_phi, delta_eps
    delta_phi = 0.0
    delta_eps = 0.0
    tpm_astro.nutations(tdt, &delta_phi, &delta_eps)
    return (delta_phi, delta_eps)
