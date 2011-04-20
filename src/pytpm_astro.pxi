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
    """Compute and set dependent TSTATE data."""
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
    
    :param pvec: a PVEC object with appropriate V6 members.
    :type pvec: PVEC
    :param s1: starting state
    :type s1: integer (0 <= s1 < N_TPM_STATES)
    :param s2: end state
    :type s2: integer (0 <= s2 < N_TPM_STATES)
    :param ep: epoch of the postion and velocity of s1
    :type ep: float
    :param eq: equinox (of s1 and or s2)
    :type eq: float
    :tstate: a TSTATE object with appropriate initial values.
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
    """Return state name given state id."""
    return _tpm_astro.tpm_state(s)

def delta_AT(utc):
    """Return Delta AT = TAI - UTC for the given UTC.

    The file src/tpm/delta_AT.c must be updated when Delta AT is
    changed by IERS.
    """
    return _tpm_astro.delta_AT(utc)

def delta_T(ut1):
    """Return Delta T = TT - UT1 for the given UT1.

    Delta T = ET - UT1 for dates before 1984.0 and Delta T = TDT - UT1
    for dates on and after 1984.0. TDT was the name of TT between
    1984.0 and 2000.0.

    A built-in model is used for calculating this quantity.
    """
    return _tpm_astro.delta_T(ut1)

def delta_UT(utc):
    """Return Delta UT = UT1 - UTC for the given UTC.

    This is calculated by taking the difference of delta_ET and
    delta_T. The later is calculated using a built-in model. For the
    latter the input time argument must be UT1, but the error in using
    UTC should be small.
    """
    return _tpm_astro.delta_UT(utc)

def delta_ET(utc):
    """Return Delta ET = ET - UTC for the given UTC."""
    return _tpm_astro.delta_ET(utc)

def delta_TT(utc):
    """Return Delta TT = TDT - UTC for the given UTC."""
    return _tpm_astro.delta_TT(utc)

def tdt2tdb(tdt):
    """Return TDB for the given TDT."""
    return _tpm_astro.tdt2tdb(tdt)

def ut12gmst(ut1):
    """Return GMST for the given UT1."""
    return _tpm_astro.ut12gmst(ut1)
    
def et2tdt(et):
    """Return TDT for the given ET."""
    return _tpm_astro.et2tdt(et)

def tai2tdt(tai):
    """Return TDT for the given TAI."""
    return _tpm_astro.tai2tdt(tai)

def tdt2et(tdt):
    """Return ET for the given TDT."""
    return _tpm_astro.tdt2et(tdt)

def ut12et(ut1):
    """Return ET for the given UT1."""
    return _tpm_astro.ut12et(ut1)

def utc2et(utc):
    """Return ET for the given UTC."""
    return _tpm_astro.utc2et(utc)

def utc2tdt(utc):
    """Return TDT for the given UTC."""
    return _tpm_astro.utc2tdt(utc)

def utc2ut1(utc):
    """Return UT1 for the given UTC."""
    return _tpm_astro.utc2ut1(utc)
    
def et2ut1(et):
    """Return UT1 for the given ET."""
    return _tpm_astro.et2ut1(et)

def et2utc(et):
    """Return UTC for the given ET."""
    return _tpm_astro.et2utc(et)

def tai2utc(tai):
    """Return UTC for the given TAI."""
    return _tpm_astro.tai2utc(tai)

def tdt2tai(tdt):
    """Return TAI for the given TDT."""
    return _tpm_astro.tdt2tai(tdt)

def tdt2utc(tdt):
    """Return UTC for the given TDT."""
    return _tpm_astro.tdt2utc(tdt)

def ut12utc(ut1):
    """Return UTC for the given UT1."""
    return _tpm_astro.ut12utc(ut1)

def et2tai(et):
    """Return TAI for the given ET."""
    return _tpm_astro.et2tai(et)

def et2tdb(et):
    """Return TDB for the given ET."""
    return _tpm_astro.et2tdb(et)

def tai2et(tai):
    """Return ET for the given TAI."""
    return _tpm_astro.tai2et(tai)

def tai2tdb(tai):
    """Return TDB for the given TAI."""
    return _tpm_astro.tai2tdb(tai)

def tai2ut1(tai):
    """Return UT1 for the given TAI."""
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
    """Return UT1 for the given TDT."""
    return _tpm_astro.tdt2ut1(tdt)

def ut12tai(ut1):
    """Return TAI for the given UT1."""
    return _tpm_astro.ut12tai(ut1)

def ut12tdb(ut1):
    """Return TDB for the given UT1."""
    return _tpm_astro.ut12tdb(ut1)

def ut12tdt(ut1):
    """Return TDT for the given UT1."""
    return _tpm_astro.ut12tdt(ut1)

def utc2tdb(utc):
    """Return TDB for the given UTC."""
    return _tpm_astro.utc2tdb(utc)

def et2ut(et):
    """Return UT for the given ET; same as et2ut1(et)"""
    return _tpm_astro.et2ut(et)

def ut2et(ut):
    """Return ET for the given UT; same as ut12et(ut)."""
    return _tpm_astro.ut2et(ut)

def ut2gmst(ut):
    """Return GMST for the given UT; same as ut12gmst(ut)"""
    return _tpm_astro.ut2gmst(ut)

def cat2v6(ra, de, pmra, pmdec, px, rv, C=36525.0):
    """Create a V6C vector from catalog entry.

    :param ra: Right Ascension
    :type ra: Float (radians)
    :param de: Declination
    :type de: Float (radians)
    :param pmra: Proper motion in ra (not pmra*cos(de))
    :type pmra: Float (arcseconds/century)
    :param pmde: Proper motion in de
    :type pmde: Float (arcseconds/century)
    :param px: Parallax
    :type px: Float (arcseconds)
    :param rv: Radial velocity
    :type rv: Float (km/s)
    :param C: Days in a century
    :type C: Float (days)

    :return: V6C vector
    :rtype: tpm.V6C
    
    A Julian century has 36525 days (tpm.CJ) and a tropical century has
    36524.21987817305 days (tpm.CB).
    """
    v6 = V6C()
    v6.setV6(_tpm_astro.cat2v6(ra, de, pmra, pmdec, px, rv, C))
    return v6
    
def v62cat(V6C v6, C=36525.0):
    """Return catalog quantites given a V6C vector."""
    cdef double ra=0.0, de=0.0, pmra=0.0, pmde=0.0, px=0.0, rv=0.0
    _tpm_astro.v62cat(&ra, &de, &pmra, &pmde, &px, &rv, v6.getV6(), C)
    return dict(ra=ra, de=de, pmra=pmra, pmde=pmde, px=px, rv=rv)
    
def proper_motion(V6C v6, start, end):
    """Apply proper motion to the given V6C vector."""
    cdef _tpm_astro.V6 _v6
    v61 = V6C()
    _v6 = _tpm_astro.proper_motion(v6.getV6(), start, end)
    v61.setV6(_v6)
    return v61
