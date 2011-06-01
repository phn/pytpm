# -*- coding: utf-8 -*-
# The following line must be present in the pytpm.pyx file.
# cimport _tpm_astro

IAU_K = _tpm_astro.IAU_K
IAU_DM = _tpm_astro.IAU_DM 
IAU_AU = _tpm_astro.IAU_AU  
IAU_C  = _tpm_astro.IAU_C  
IAU_RE = _tpm_astro.IAU_RE  
IAU_RM = _tpm_astro.IAU_RM  
IAU_F  = _tpm_astro.IAU_F  
IAU_KAPPA = _tpm_astro.IAU_KAPPA
IAU_W   = _tpm_astro.IAU_W 
GAL_RA  = _tpm_astro.GAL_RA 
GAL_DEC = _tpm_astro.GAL_DEC 
GAL_LON = _tpm_astro.GAL_LON 
PRECESS_NEWCOMB    = _tpm_astro.PRECESS_NEWCOMB 
PRECESS_ANDOYER    = _tpm_astro.PRECESS_ANDOYER 
PRECESS_KINOSHITA  = _tpm_astro.PRECESS_KINOSHITA 
PRECESS_LIESKE     = _tpm_astro.PRECESS_LIESKE 
PRECESS_FK4        = _tpm_astro.PRECESS_FK4 
PRECESS_FK5        = _tpm_astro.PRECESS_FK5 
PRECESS_INERTIAL   = _tpm_astro.PRECESS_INERTIAL 
PRECESS_ROTATING   = _tpm_astro.PRECESS_ROTATING 

def tpm_data(TSTATE tstate, int action):
    """Compute and set dependent TSTATE data.

    :param tstate: A TSTATE object.
    :type tstate: TSTATE
    :param action: The action to perform.
    :type action: integer

    :return: None
    :rtype: None

    Given a TSTATE and an action, this function will perform the action
    and set the various dependent properties of the TSTATE object.

    The ``action`` can be one of

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
    _tpm_astro.tpm_data(&tstate._tstate, action)

# If I use _tpm_tpm.N_TPM_STATES or N_TPM_STATES inplace of 22 then
# Cython gives the following error: Not allowed in a constant
# expression. Why?  In C code I can do V6 pvec[N_TPM_STATES].
cdef struct s_pvec:
    _tpm_vec.V6 pvec[22]
ctypedef s_pvec S_PVEC

cdef class PVEC(object):
    """Class for holding N_TPM_STATES element array of V6 vectors."""
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
    """Apply transition from state s1 to state s2.
    
    :param pvec: A PVEC object with appropriate V6 members.
    :type pvec: PVEC
    :param s1: Starting state (0 <= s1 < N_TPM_STATES).
    :type s1: integer
    :param s2: End state (0 <= s2 < N_TPM_STATES).
    :type s2: integer
    :param ep: Epoch of the postion and velocity of s1.
    :type ep: float
    :param eq: Equinox (of s1 and or s2, dependeing on transition).
    :type eq: float
    :param tstate: A TSTATE object with appropriate initial values.
    :type eq: TSTATE

    :return: Final state (should be s2).
    :rtype: integer
    
    This is the main TPM function, that call the looks up the state
    tables and performs all required transformations to take the state
    vector at ``pvec[s1]`` from state ``s1`` to state ``s2``. It stores
    the resulting state vector in ``pvec[s2]``.

    For more information see TPM manual and PyTPM reference.
    """
    if not 0 <= s1 < N_TPM_STATES:
        raise ValueError, "S1 must be in 0 <= S1 < N_TPM_STATES"
    if not 0 <= s2 < N_TPM_STATES:
        raise ValueError, "S2 must be in 0 <= S2 < N_TPM_STATES"
    cdef S_PVEC spvec
    cdef _tpm_tpm.TPM_TSTATE ststate
    
    spvec = pvec.__get_pvec()
    ststate = tstate.__get_tstate()
    t = _tpm_astro.tpm(spvec.pvec, s1, s2, ep, eq, &ststate)
    pvec.__set_pvec(spvec)
    tstate.__set_tstate(ststate)
    return t

def tpm_state(int s):
    """Return state name given state id.

    :param s: State id.
    :type s: integer

    :return: State name.
    :rtype: string

    Given an integer id for a state, this function returns a
    descriptive name for the state.

    >>> tpm.tpm_state(tpm.TPM_S06)
    'Helio. mean FK5'
    >>> tpm.tpm_state(tpm.TPM_S04)
    'IAU 1958 Galactic'
    >>> tpm.tpm_state(tpm.TPM_S20)
    'Topo. obs. HA/Dec'
    >>> tpm.tpm_state(tpm.TPM_S19)
    'Topo. obs. Az/El'
    """
    return _tpm_astro.tpm_state(s)

def delta_AT(utc):
    """Return Delta AT = TAI - UTC for the given UTC.

    :param utc: UTC as a Julian date.
    :type utc: float

    :return: Delta AT = TAI - UTC in seconds.
    :rtype: float

    **IMPORTANT**
    
    The file src/tpm/delta_AT.c must be updated when Delta AT is
    changed by the IERS and PyTPM Cython code must re-compiled.
    """
    return _tpm_astro.delta_AT(utc)

def delta_T(ut1):
    """Return Delta T = TT - UT1 for the given UT1.

    :param ut1: UT1 as a Julian date.
    :type ut1: float
    
    :return: Delta T = TT - UT1 in seconds.
    :rtype: float

    This function returns the ``TT - UT1`` value for the given UT1. The
    value returned is ``ET - UT1`` for dates before 1984.0 and ``TDT -
    UT1`` for dates on and after 1984.0. TDT was the name of TT between
    1984.0 and 2000.0.

    A built-in model is used for calculating this quantity.
    """
    return _tpm_astro.delta_T(ut1)

def delta_UT(utc):
    """Return Delta UT = UT1 - UTC for the given UTC.

    :param utc: UTC as a Julian date.
    :type utc: float

    :return: UT1 - UTC for in seconds.
    :rtype: float
    
    The value of ``UT1 - UTC`` is calculated by taking the difference
    of delta_ET and delta_T. The later is calculated using a built-in
    model. For the latter the input time argument must be UT1, but the
    error in using UTC should be small.
    """
    return _tpm_astro.delta_UT(utc)

def delta_ET(utc):
    """Return Delta ET = ET - UTC for the given UTC.

    :param utc: UTC as a Julian date.
    :type utc: float

    :return: Delta ET = ET - UTC in seconds.
    :rtype: float
    """
    return _tpm_astro.delta_ET(utc)

def delta_TT(utc):
    """Return Delta TT = TDT - UTC for the given UTC.

    :param utc: UTC as a Julian date.
    :type utc: float

    :return: Delta TT = TDT - UTC.
    :rtype: float
    """
    return _tpm_astro.delta_TT(utc)

def tdt2tdb(tdt):
    """Return TDB for the given TDT.

    :param tdt: TDT as a Julian date.
    :type tdt: float

    :return: TDB as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tdt2tdb(tdt)

def ut12gmst(ut1):
    """Return GMST for the given UT1.

    :param ut1: UT1 as a Julian date.
    :type ut1: float

    :return: GMST as an angle in radians.
    :rtype: float

    Given a UT1 Julian date, this function returns the Greenwich Mean
    Sidereal Time as an angle in radians in the range (0, 2π).
    """
    return _tpm_astro.ut12gmst(ut1)
    
def et2tdt(et):
    """Return TDT for the given ET.

    :param et: ET as a Julian date.
    :type et: float

    :return: TDT as a Julian date.
    :rtype: float
    """
    return _tpm_astro.et2tdt(et)

def tai2tdt(tai):
    """Return TDT for the given TAI.

    :param tai: TAI as a Julian date.
    :type tai: float

    :return: TDT as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tai2tdt(tai)

def tdt2et(tdt):
    """Return ET for the given TDT.

    :param tdt: TDT as a Julian date.
    :type tdt: float

    :return: ET as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tdt2et(tdt)

def ut12et(ut1):
    """Return ET for the given UT1.

    :param ut1: UT1 as a Julian date.
    :type ut1: float

    :return: ET as a Julian date.
    :rtype: float
    """
    return _tpm_astro.ut12et(ut1)

def utc2et(utc):
    """Return ET for the given UTC.
    
    :param utc: UTC as a Julian date.
    :type utc: float

    :return: ET as a Julian date.
    :rtype: float
    """
    return _tpm_astro.utc2et(utc)

def utc2tdt(utc):
    """Return TDT for the given UTC.

    :param utc: UTC as a Julian date.
    :type utc: float

    :return: TDT as a Julian date.
    :rtype: float
    """
    return _tpm_astro.utc2tdt(utc)

def utc2ut1(utc):
    """Return UT1 for the given UTC.

    :param utc: UTC as a Julian date.
    :type utc: float

    :return: UT1 as a Julian date.
    :rtype: float
    """
    return _tpm_astro.utc2ut1(utc)
    
def et2ut1(et):
    """Return UT1 for the given ET.

    :param et: ET as a Julian date.
    :type et: float

    :return: UT1 as a Julian date.
    :rtype: float
    """
    return _tpm_astro.et2ut1(et)

def et2utc(et):
    """Return UTC for the given ET.

    :param et: ET as a Julian date.
    :type et: float

    :return: UTC as a Julian date.
    :rtype: float
    """
    return _tpm_astro.et2utc(et)

def tai2utc(tai):
    """Return UTC for the given TAI.

    :param tai: TAI as a Julian date.
    :type tai: float

    :return: UTC as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tai2utc(tai)

def tdt2tai(tdt):
    """Return TAI for the given TDT.

    :param tdt: TDT as a Julian date.
    :type tdt: float

    :return: TAI as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tdt2tai(tdt)

def tdt2utc(tdt):
    """Return UTC for the given TDT.

    :param tdt: TDT as a Julian date.
    :type tdt: float

    :return: UTC as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tdt2utc(tdt)

def ut12utc(ut1):
    """Return UTC for the given UT1.

    :param ut1: UT1 as a Julian date.
    :type ut1: float

    :return: UTC as a Julian date.
    :rtype: float
    """
    return _tpm_astro.ut12utc(ut1)

def et2tai(et):
    """Return TAI for the given ET.

    :param et: ET as a Julian date.
    :type et: float

    :return: TAI as a Julian date.
    :rtype: float
    """
    return _tpm_astro.et2tai(et)

def et2tdb(et):
    """Return TDB for the given ET.

    :param et: ET as a Julian date.
    :type et: float

    :return: TDB as a Julian date.
    :rtype: float
    """
    return _tpm_astro.et2tdb(et)

def tai2et(tai):
    """Return ET for the given TAI.

    :param tai: TAI as a Julian date.
    :type tai: float

    :return: ET as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tai2et(tai)

def tai2tdb(tai):
    """Return TDB for the given TAI.

    :param tai: TAI as a Julian date.
    :type tai: float

    :return: TDB as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tai2tdb(tai)

def tai2ut1(tai):
    """Return UT1 for the given TAI.

    :param tai: TAI as a Julian date.
    :type tai: float

    :return: UT1 as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tai2ut1(tai)

#def tdb2et(tdb):
#    """Return ET for the given TDB."""
#    return _tpm_astro.tdb2et(tdb)
# 
#def tdb2tai(tdb):
#    """Return TAI for the given TDB."""
#    return _tpm_astro.tdb2tai(tdb)
# 
#def tdb2ut1(tdb):
#    """Return UT1 for the given TDB."""
#    return _tpm_astro.tdb2ut1(tdb)
# 
#def tdb2utc(tdb):
#    """Return UTC for the given TDB."""
#    return _tpm_astro.tdb2utc(tdb)

def tdt2ut1(tdt):
    """Return UT1 for the given TDT.

    :param tdt: TDT as a Julian date.
    :type tdt: float

    :return: UT1 as a Julian date.
    :rtype: float
    """
    return _tpm_astro.tdt2ut1(tdt)

def ut12tai(ut1):
    """Return TAI for the given UT1.

    :param ut1: UT1 as a Julian date.
    :type ut1: float

    :return: TAI as a Julian date.
    :rtype: float
    """
    return _tpm_astro.ut12tai(ut1)

def ut12tdb(ut1):
    """Return TDB for the given UT1.

    :param ut1: UT1 as a Julian date.
    :type ut1: float

    :return: TDB as a Julian date.
    :rtype: float
    """
    return _tpm_astro.ut12tdb(ut1)

def ut12tdt(ut1):
    """Return TDT for the given UT1.

    :param ut1: UT1 as a Julian date.
    :type ut1: float

    :return: TDT as a Julian date.
    :rtype: float
    """
    return _tpm_astro.ut12tdt(ut1)

def utc2tdb(utc):
    """Return TDB for the given UTC.

    :param utc: UTC as a Julian date.
    :type utc: foat

    :return: TDB as a Julian date.
    :rtype: float
    """
    return _tpm_astro.utc2tdb(utc)

def et2ut(et):
    """Return UT for the given ET; same as et2ut1(et)."""
    return _tpm_astro.et2ut(et)

def ut2et(ut):
    """Return ET for the given UT; same as ut12et(ut)."""
    return _tpm_astro.ut2et(ut)

def ut2gmst(ut):
    """Return GMST for the given UT; same as ut12gmst(ut)"""
    return _tpm_astro.ut2gmst(ut)

def cat2v6(ra, de, pmra, pmdec, px, rv, C=36525.0):
    """Create a V6C vector from catalog entry.

    :param ra: Right Ascension in radians.
    :type ra: float
    :param de: Declination in radians.
    :type de: float
    :param pmra: Proper motion in ra (not pmra*cos(de)) as "/century.
    :type pmra: float 
    :param pmdec: Proper motion in de as "/century.
    :type pmdec: float
    :param px: Parallax in arc-seconds.
    :type px: float
    :param rv: Radial velocity in km/s.
    :type rv: float
    :param C: Days in a century, used in pmra and pmde.
    :type C: float

    :return: V6C vector
    :rtype: V6C

    This function is used to convert a catalog entry for an object into
    a ``V6C`` vector.

    Internally TPM uses velocities in AU/day, and needs to know how
    many days are in a century. The porper motions can be in
    arc-seconds per Julian century or arc-seconds per tropical century.
    A Julian century has 36525 days (``tpm.CJ``) and a tropical century
    has 36524.21987817305 days (``tpm.CB``).
    """
    v6 = V6C()
    v6.setV6(_tpm_astro.cat2v6(ra, de, pmra, pmdec, px, rv, C))
    return v6
    
def v62cat(V6C v6, C=36525.0):
    """Return catalog quantites given a V6C vector.
    
    :param v6: A V6C object.
    :type v6: V6C
    :param C: Number of days in a century.
    :type C: float

    :return: A dictionary containing catalog quantities for the
             object. The keys are: ``ra`` for right ascension in
             radians, ``dec`` for declination in radians, ``pmra`` for
             proper motion in ra (not pmra*cos(dec)) in "/century,
             ``pmdec`` for proper motion in dec in "/century, ``px`` for
             parallax in arc-seconds and ``rv`` for radial velocity in
             km/s.
    :rtype: dict
    """
    cdef double ra=0.0, dec=0.0, pmra=0.0, pmdec=0.0, px=0.0, rv=0.0
    _tpm_astro.v62cat(&ra, &dec, &pmra, &pmdec, &px, &rv, v6.getV6(), C)
    return dict(ra=ra, dec=dec, pmra=pmra, pmdec=pmdec, px=px, rv=rv)
    
def proper_motion(V6C v6, end, start):
    """Apply proper motion to the given V6C vector.

    :param v6: A V6C object.
    :type v6: V6C
    :param end: End (to) time in days (can be Julian date).
    :type end: float
    :param start: Starting (from) time in days (can be Julian date).
    :type start: float

    :return: A V6C object containing the new position.
    :rtype: V6C

    Given starting time and end time, theis function applies proper
    motion to the coordinates in the given V6C object. A simple linear
    multiplication of velocity with time is performed, followed by 
    addition of this increment to the position coordinates.

    The difference, ``end - start``, should be the number of days in
    the time interval. Hence Julian dates can be used. The velocities
    in V6C are stored as AU/day and hence time interval must be in
    days.
    """
    cdef _tpm_astro.V6 _v6
    v61 = V6C()
    _v6 = _tpm_astro.proper_motion(v6.getV6(), end, start)
    v61.setV6(_v6)
    return v61

def aberrate(V6C p, V6C e, int flag):
    """Apply aberration of light to a state vector.

    :param p: The vector to which aberration must be applied.
    :type p: V6C
    :param e: The vector with aberration causing velocity component.
    :type e: V6C
    :param flag: Add aberration to ``p`` if flag >0 else subtract it.
    :type flag: intger
    
    :return: The result of applying aberration to ``p``.
    :rtype: V6C

    The velocity components in ``e`` is taken to be the oberver's
    velocity and the aberration correction is applied to the position
    components in ``p``. The aberration is added to ``p`` is ``flag >
    0`` else it is subtracted from ``p``. The velocity component of
    ``p`` is, of-course, unchanged.

    If ``e`` is the barycentric state vector of the Earth's, center
    then we have geocentric aberration. If it is the sum of the above
    with the observer's geocentric space-fixed mean state vector, then
    we have topocentric aberration.

    The algorithm uses vectors and hence the ``e`` can be for any
    observer, not just Earth based observers.
    """
    cdef _tpm_astro.V6 _v6
    _v6 = _tpm_astro.aberrate(p.getV6(), e.getV6(), flag)
    v6 = V6C()
    v6.setV6(_v6)
    return v6

def azel2hadec(V6C v6, double latitude):
    """Convert V6C from (AZ, EL) to (HA, DEC).

    :param v6: A state vector.
    :type v6: V6C
    :param latitude: Latitude in radians.
    :type latitude: float

    :return: State vector converted into (HA, DEC) system.
    :rtype: V6C

    Two simple rotations are performed on ``v6`` to convert it from
    (AZ, EL) system into (HA, DEC) system.  Azimuth is measured
    **Eastwards from North**. 

    The conversion from (AZ, EL) to (HA, DEC) does not require the full
    setup of TPM and hence this function can be directly used for the
    above conversion.
    """
    v = V6C()
    v.setV6(_tpm_astro.azel2hadec(v6.getV6(), latitude))
    return v

def hadec2azel(V6C v6, double latitude):
    """Convert V6C from (HA, DEC) to (AZ, EL).

    :param v6: A state vector.
    :type v6: V6C
    :param latitude: Latitude in radians.
    :type latitude: float

    :return: State vector converted into (AZ, EL) system.
    :rtype: V6C

    Two simple rotations are performed on ``v6`` to convert it from
    (HA, DEC) system into (AZ, EL) system.  Azimuth is measured
    **Eastwards from North**. 

    The conversion from (HA, DEC) to (AZ, EL) does not require the full
    setup of TPM and hence this function can be directly used for the
    above conversion.
    """
    v = V6C()
    v.setV6(_tpm_astro.hadec2azel(v6.getV6(), latitude))
    return v

def evp(double tdb):
    """J2000 Barycentric and Heliocentric state vectors for Earth.

    :param tdb: Barycentric Dynamic Time as a Julian date.
    :type tdb: float

    :return: A tuple of Barycentric and Heliocentric state vectors.
    :rtype: (V6C, V6C)

    Calculates Earth's J2000 Barycentric and Heliocentric state
    vectors, for the given Barycentric Dynamic Time ``tdb``. The state
    vector is calculated using a built-in model.

    The first element of the tuple is the Barycentric vector and the
    second is the Heliocentric vector.
    """
    cdef _tpm_vec.V6 _vb, _vh
    _tpm_astro.evp(tdb, &_vb, &_vh)
    v6b = V6C()
    v6b.setV6(_vb)
    v6h = V6C()
    v6h.setV6(_vh)
    return v6b, v6h

def ecl2equ(V6C v6, double obl):
    """Convert V6 from Ecliptic to FK5 Equatorial coordinates.
    
    :param v6: A state vector in Ecliptic system.
    :type v6: V6C
    :param obl: Obliquity at the time of interest.
    :type obl: float

    :return: A state vector in FK5 equatorial coordinates.
    :rtype: V6C

    A simple rotation through ``obl`` is performed to convert Ecliptic
    coordinates into FK5 equatorial coordinates.
    """
    v = V6C()
    v.setV6(_tpm_astro.ecl2equ(v6.getV6(), obl))
    return v

def equ2ecl(V6C v6, double obl):
    """Convert FK5 equatorial coordinates into Ecliptic coordinates.

    :param v6: State vector to be transformed.
    :type v6: V6C
    :param obl: Obliquity at the time of interest.
    :type obl: float

    :return: State vector in Ecliptics coordinates.
    :rtype: V6C

    A simple rotation is performed to convert the given state vector
    from FK5 Equatorial system into Ecliptic system, using the given
    obliquity. 
    """
    v = V6C()
    v.setV6(_tpm_astro.equ2ecl(v6.getV6(), obl))
    return v
    
def ellab(double tdt, V6C star, int flag):
    """Add or remove elliptic aberration.

    :param tdt: Terrestrial Time (same as Terrestrial Dynamic Time).
    :type tdt: float
    :param star: A state vector for the object.
    :type star: V6C
    :param flag: Add correction if flag > 0 else subtract.
    :type flag: integer

    :return: A state vector with elliptic aberration applied to input.
    :rtype: V6C

    This function applies elliptic aberration to the the given state
    vector, and return the resulting state vector. If ``flag > 0``
    then the correction is added else it is subtracted.
    """
    v = V6C()
    v.setV6(_tpm_astro.ellab(tdt, star.getV6(), flag))
    return v

def equ2gal(V6C v6):
    """Convert state vector from FK4 Equatorial to Galactic.

    :param v6: State vector in FK4 Equatorial coordinates.
    :type v6: V6C

    :return: State vector in Galactic coordinates.
    :rtype: V6C

    Applies three rotations after subtracting E-terms of
    aberration. Galactic pole is (192.25, 27.4) degrees and longitude
    of ascending node of the Galactic plane on the equator is 33
    degrees. 
    """
    v = V6C()
    v.setV6(_tpm_astro.equ2gal(v6.getV6()))
    return v
    
def gal2equ(V6C v6):
    """Convert state vector from Galactic to FK4 Equatorial.

    :param v6: State vector in Galactic coordinates.
    :type v6: V6C

    :return: State vector in FK4 Equatorial coordinates.
    :rtype: V6C

    Applies three rotations and then adds E-terms of
    aberration. Galactic pole is (192.25, 27.4) degrees and longitude
    of ascending node of the Galactic plane on the equator is 33
    degrees.
    """
    v = V6C()
    v.setV6(_tpm_astro.gal2equ(v6.getV6()))
    return v
    
def eterms(double ep):
    """Return state vector contaiing e-terms of aberration.

    :param ep: Epoch, as a Julian date, for the calculations.
    :type ep: float

    :return: State vector containing the e-terms.
    :rtype: V6C

    The state vector returned can be used to add or subtract the
    e-terms with another state vector.
    """
    v6 = V6C()
    v6.setV6(_tpm_astro.eterms(ep))
    return v6

def fk425(V6C v6):
    """Precess state vector from FK4 to FK5.

    :param v6: FK4 State vector to be transformed.
    :type v6: V6C

    :return: FK5 state vector.
    :rtype: V6C

    Perform FK4 to FK5 transformation of the given state vector. See
    TPM manual and src/tpm/fk425.c for more details.
    """
    v = V6C()
    v.setV6(_tpm_astro.fk425(v6.getV6()))
    return v

def fk524(V6C v6):
    """Precess state vector from FK5 to FK4.

    :param v6: FK5 State vector to be transformed.
    :type v6: V6C

    :return: FK4 state vector.
    :rtype: V6C

    Perform FK4 to FK5 transformation of the given state vector. See
    TPM manual and src/tpm/fk524.c for more details.
    """
    v = V6C()
    v.setV6(_tpm_astro.fk524(v6.getV6()))
    return v

def geod2geoc(double lon, double lat, double alt):
    """Convert geodetic position to geocentric position.

    :param lon: Longitude in radians (east positive).
    :type lon: float
    :param lat: Longitude in radians (north positive).
    :type lat: float
    :param alt: Altitude in meters.
    :type alt: float

    :return: A V6C geocentric state vector (meters, meters/s)
    :rtype: V6C

    Converts the given geodetic position to a geocentric one and
    returns the results in a V6C state vector. The units are meters and
    meters/second.
    """
    v6 = V6C()
    v6.setV6(_tpm_astro.geod2geoc(lon, lat, alt))
    return v6

def ldeflect(V6C star, V6C earth, int flag):
    """Apply General Relativity deflection of light.

    :param star: State vector the object of interest.
    :type star: V6C
    :param earth: State vector for Earth.
    :type earth: V6C
    :param flag: Correction is added is flag > 0 else subtracted.
    :type flag: integer

    :return: Light deflection corrected state vector.
    :rtype: V6C

    Applies the relativisty light deflection due to the Sun, to the
    state vector in ``star``.
    """
    v6 = V6C()
    v6.setV6(_tpm_astro.ldeflect(star.getV6(), earth.getV6(), flag))
    return v6

def precess(double start, double end, V6C v6, int pflag):
    """Precess a state vector within an inertial frame.

    :param start: Initial epoch as a Julian date.
    :type start: float
    :param end: Final epoch as a Julian date.
    :type end: float
    :param v6: The state vector to be precessed.
    :type v6: V6C
    :param pflag: Precession model to use.
    :type pflag: integer

    :return: Precessed state vector.
    :rtype: V6C

    This function precesses the given state vector, ``v6`` from
    ``start`` to ``end`` using the given precession model
    ``pflag``. The precession is carried out within an inertial
    frame. So this cannot do FK4 to FK5, for example.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    v = V6C()
    v.setV6(_tpm_astro.precess(start, end, v6.getV6(), pflag))
    return v

def precess_m(double start, double end, int pflag, int sflag):
    """Precession matrix for time between end and start.

    :param start: Starting point as a Julian date.
    :type start: float
    :param end: End point as a Julian date.
    :type start: float
    :param pflag: Precession model to use.
    :type pflag: integer
    :param sflag: Rotating frame or inertial frame
    :type sflag: integer

    Returns the precession matrix for precession from ``start`` time to
    ``end`` time. The model used for cacluating precession angles is
    specified using the ``pflag`` parameter. The possible values are::

      PRECESS_NEWCOMB	
      PRECESS_ANDOYER	
      PRECESS_KINOSHITA	
      PRECESS_LIESKE	
      PRECESS_FK4	
      PRECESS_FK5	

    If ``sflag != PRECESS_ROTATING``, then the "P-dot" term in the
    precession matrix is set to null. The other possibility is
    ``PRECESS_INERTIAL``, when the "P-dot" term is not set to null.
    """
    m6 = M6()
    m6.setM6(_tpm_astro.precess_m(start, end, pflag, sflag))
    return m6

def eccentricity(double tdt):
    """Eccentricity of Earth's orbit.

    :param tdt: Terrestrial Dynamic Time (same as TT) as Julian date.
    :type tdt: float

    :return: Eccentricity of Earth's orbit.
    :rtype: float

    Returns the eccentricity of Earth's orbit at the given time. Time
    is a TDT (same as TT) as a Julian date.
    """
    return _tpm_astro.eccentricity(tdt)

def eccentricity_dot(double tdt):
    """Rate of change in the eccentricity of Earth's orbit.

    :param tdt: Terrestrial Dynamic Time (same as TT) as Julian date.
    :type tdt: float

    :return: Rate of change in the eccentricity of Earth's orbit.
    :rtype: float

    Returns the rate of change (per Julian century) in the eccentricity
    of Earth's orbit at the given time. Time is a TDT (same as TT) as a
    Julian date.
    """
    return _tpm_astro.eccentricity_dot(tdt)

def obliquity(double tdt):
    """Mean obliquity of Ecliptic(epoch J2000).

    :param tdt: Terrestrial Dynamic Time (same as TT) as a Julian date.
    :type tdt: float

    :return: Obliquity of the Ecliptic in radians.
    :rtype: float

    The obliquity of the mean Ecliptic of J2000, at the given TDT (same
    as TT) is returned. The returned value is in radians.
    """
    return _tpm_astro.obliquity(tdt)

def obliquity_dot(double tdt):
    """Rate of change of mean obliquity of Ecliptic(epoch J2000).

    :param tdt: Terrestrial Dynamic Time (same as TT) as a Julian date.
    :type tdt: float

    :return: Rate of change of obliquity of the Ecliptic in ra/jcen.
    :rtype: float

    Returns the rate of change (radians per Julian century) in the
    obliquity of Ecliptic at the given time. Time is a TDT (same as TT)
    as a Julian date.
    """
    return _tpm_astro.obliquity_dot(tdt)

def refco(double lat=0.557744205098, double alt=2093.093,
          double T=273.15, double P=1013.25, double rh=0.0,
          double wavelength=0.550, double eps=1e-8):
    """Refractions coefficients for use with ``refract()``.

    :param lat: Observer's astronomical latitude (radians).
    :type lat: float
    :param alt: Observer's altitude above sea level (meters).
    :type alt: float
    :param T: Ambient temperature (Kelvin).
    :type T: float
    :param rh: Relative humidity (0-1).
    :type rh: integer
    :param wavelength: Wavelength in microns.
    :type wavelength: float
    :param eps: Fractional accuracy.
    :type eps: float

    :return: Refraction coefficients, as a 2-element tuple.
    :rtype: (float, float)

    The values returned are used for calculating change in zenith
    distance that must be applied to correct for refraction. These
    values are passed to the function ``refract()`` for this
    calculation.

    The default location is KPNO.

    See src/tpm/refco.c for more details.
    """
    cdef double refa
    cdef double refb
    refa = 0.0
    refb = 0.0
    _tpm_astro.refco( lat,  alt,  T,  P, rh,  wavelength,  eps,
                      &refa,  &refb)
    return (refa, refb)

def refract(double zx, double refa, double refb, int flag):
    """Returns change in zenith distance due to refraction.

    :param zx: Raw zenith distance, apparent or observed (radians).
    :type zx: float
    :param refa: Refraction coefficient from ``refco``.
    :type refa: float
    :param refa: Refraction coefficient from ``refco``.
    :type refa: float
    :param flag: Apply refraction if flag > 0, else remove.
    :type flag: integer

    :return: Correction to zenith distance due to refraction.
    :rtype: float
    
    Given a zenith distance ``zx``, this function returns the amount of
    change in this quantity due to refraction. This correction must be
    added to ``zx`` to find the resultant zenith distance.
    """
    return _tpm_astro.refract(zx, refa, refb, flag)
    
def solar_perigee(double tdt):
    """Mean longitude of the perigee of solar orbit.

    :param tdt: Terresttrial Dynamic Time (same as TT).
    :type tdt: float

    :return: Longitude in radians.
    :rtype: float
    """
    return _tpm_astro.solar_perigee(tdt)

def solar_perigee_dot(double tdt):
    """Rate of change of solar perigee.

    :param tdt: Terresttrial Dynamic Time (same as TT).
    :type tdt: float

    :return: Rate of change of longitude in radians/julian century.
    :rtype: float
    """
    return _tpm_astro.solar_perigee_dot(tdt)

def theta(double start, double end, int pflag):
    """FK4 and FK5 precession angles.

    :param start: Starting time as a Julian date.
    :type start: float
    :param end: Ending time as a Julian date.
    :type end: float
    :param pflag: The model to use.
    :type pflag: integer

    :return: Precession angle for the given time period.
    :rtype: float

    Returns the precession angle for the model indicated by ``pflag``
    for the time ``end``, starting from the time ``start``.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    return _tpm_astro.theta(start, end, pflag)

def thetadot(double start, double end, int pflag):
    """Rate of change of FK4 and FK5 precession angles.

    :param start: Starting time as a Julian date.
    :type start: float
    :param end: Ending time as a Julian date.
    :type end: float
    :param pflag: The model to use.
    :type pflag: integer

    :return: Rate of change of precession angle for the given time period.
    :rtype: float

    Returns the rate of change of precession angle for the model
    indicated by ``pflag`` for the time ``end``, starting from the time
    ``start``.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    return _tpm_astro.thetadot(start, end, pflag)

def zee(double start, double end, int pflag):
    """FK4 and FK5 precession angles.

    :param start: Starting time as a Julian date.
    :type start: float
    :param end: Ending time as a Julian date.
    :type end: float
    :param pflag: The model to use.
    :type pflag: integer

    :return: Precession angle for the given time period.
    :rtype: float

    Returns the precession angle for the model indicated by ``pflag``
    for the time ``end``, starting from the time ``start``.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    return _tpm_astro.zee(start, end, pflag)

def zeedot(double start, double end, int pflag):
    """Rate of change of FK4 and FK5 precession angles.

    :param start: Starting time as a Julian date.
    :type start: float
    :param end: Ending time as a Julian date.
    :type end: float
    :param pflag: The model to use.
    :type pflag: integer

    :return: Rate of change of precession angle for the given time period.
    :rtype: float

    Returns the rate of change of precession angle for the model
    indicated by ``pflag`` for the time ``end``, starting from the time
    ``start``.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    return _tpm_astro.zeedot(start, end, pflag)

def zeta(double start, double end, int pflag):
    """FK4 and FK5 precession angles.

    :param start: Starting time as a Julian date.
    :type start: float
    :param end: Ending time as a Julian date.
    :type end: float
    :param pflag: The model to use.
    :type pflag: integer

    :return: Precession angle for the given time period.
    :rtype: float

    Returns the precession angle for the model indicated by ``pflag``
    for the time ``end``, starting from the time ``start``.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    return _tpm_astro.zeta(start, end, pflag)

def zetadot(double start, double end, int pflag):
    """Rate of change of FK4 and FK5 precession angles.

    :param start: Starting time as a Julian date.
    :type start: float
    :param end: Ending time as a Julian date.
    :type end: float
    :param pflag: The model to use.
    :type pflag: integer

    :return: Rate of change of precession angle for the given time period.
    :rtype: float

    Returns the rate of change of precession angle for the model
    indicated by ``pflag`` for the time ``end``, starting from the time
    ``start``.

    The values for ``pflag`` can be::
    
      PRECESS_NEWCOMB, PRECESS_ANDOYER, PRECESS_KINOSHITA,
      PRECESS_LIESKE and PRECESS_FK5.

    See TPM manual for definition of these constants.
    """
    return _tpm_astro.zetadot(start, end, pflag)

def nutations(tdt):
    """Nutations in longitude and obliquity.

    :param tdt: Terrestrial Dynamic Time (same as TDT).
    :type tdt: float

    :return: Nutations in radians (delta_phi, delta_eps).
    :rtype: (float, float)
    """
    cdef double delta_phi, delta_eps
    delta_phi = 0.0
    delta_eps = 0.0
    _tpm_astro.nutations(tdt, &delta_phi, &delta_eps)
    return (delta_phi, delta_eps)
