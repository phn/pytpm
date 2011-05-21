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
    :param pmde: Proper motion in de as "/century.
    :type pmde: float
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
             radians, ``de`` for declination in radians, ``pmra`` for
             proper motion in ra (not pmra*cos(de)) in "/century,
             ``pmde`` for proper motion in de in "/century, ``px`` for
             parallax in arc-seconds and ``rv`` for radial velocity in
             km/s.
    :rtype: dict
    """
    cdef double ra=0.0, de=0.0, pmra=0.0, pmde=0.0, px=0.0, rv=0.0
    _tpm_astro.v62cat(&ra, &de, &pmra, &pmde, &px, &rv, v6.getV6(), C)
    return dict(ra=ra, de=de, pmra=pmra, pmde=pmde, px=px, rv=rv)
    
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
    (AZ, EL) system into (HA, DEC) system.

    The conversion from (AZ, EL) to (HA, DEC) does not require the full
    setup of TPM and hence this function can be directly used for the
    above conversion.
    """
    v = V6C()
    v.setV6(_tpm_astro.azel2hadec(v6.getV6(), latitude))
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
