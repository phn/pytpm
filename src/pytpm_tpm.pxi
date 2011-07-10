# -*- coding: utf-8 -*-
# The following line must be present in the pytpm.pyx file.
# cimport _tpm_vec

TPM_S00 = _tpm_tpm.TPM_S00     
TPM_S01 = _tpm_tpm.TPM_S01   
TPM_S02 = _tpm_tpm.TPM_S02   
TPM_S03 = _tpm_tpm.TPM_S03   
TPM_S04 = _tpm_tpm.TPM_S04   
TPM_S05 = _tpm_tpm.TPM_S05   
TPM_S06 = _tpm_tpm.TPM_S06   
TPM_S07 = _tpm_tpm.TPM_S07   
TPM_S08 = _tpm_tpm.TPM_S08
TPM_S09 = _tpm_tpm.TPM_S09   
TPM_S10 = _tpm_tpm.TPM_S10   
TPM_S11 = _tpm_tpm.TPM_S11   
TPM_S12 = _tpm_tpm.TPM_S12   
TPM_S13 = _tpm_tpm.TPM_S13   
TPM_S14 = _tpm_tpm.TPM_S14   
TPM_S15 = _tpm_tpm.TPM_S15   
TPM_S16 = _tpm_tpm.TPM_S16   
TPM_S17 = _tpm_tpm.TPM_S17   
TPM_S18 = _tpm_tpm.TPM_S18   
TPM_S19 = _tpm_tpm.TPM_S19     
TPM_S20 = _tpm_tpm.TPM_S20     
TPM_S21 = _tpm_tpm.TPM_S21     
N_TPM_STATES = _tpm_tpm.N_TPM_STATES

TPM_T00 = _tpm_tpm.TPM_T00 
TPM_T01 = _tpm_tpm.TPM_T01    
TPM_T02 = _tpm_tpm.TPM_T02    
TPM_T03 = _tpm_tpm.TPM_T03    
TPM_T04 = _tpm_tpm.TPM_T04    
TPM_T05 = _tpm_tpm.TPM_T05    
TPM_T06 = _tpm_tpm.TPM_T06    
TPM_T07 = _tpm_tpm.TPM_T07    
TPM_T08 = _tpm_tpm.TPM_T08    
TPM_T09 = _tpm_tpm.TPM_T09    
TPM_T10 = _tpm_tpm.TPM_T10    
TPM_T11 = _tpm_tpm.TPM_T11    
TPM_T12 = _tpm_tpm.TPM_T12    
TPM_T13 = _tpm_tpm.TPM_T13    
TPM_T14 = _tpm_tpm.TPM_T14    
TPM_T15 = _tpm_tpm.TPM_T15    
N_TPM_TRANS = _tpm_tpm.N_TPM_TRANS

TARGET_FK4 = _tpm_tpm.TARGET_FK4 
TARGET_FK5 = _tpm_tpm.TARGET_FK5      
TARGET_ECL = _tpm_tpm.TARGET_ECL      
TARGET_GAL = _tpm_tpm.TARGET_GAL      
TARGET_APP_HADEC = _tpm_tpm.TARGET_APP_HADEC 
TARGET_OBS_HADEC = _tpm_tpm.TARGET_OBS_HADEC
TARGET_APP_AZEL  = _tpm_tpm.TARGET_APP_AZEL 
TARGET_OBS_AZEL  = _tpm_tpm.TARGET_OBS_AZEL 
TARGET_OBS_WHAM  = _tpm_tpm.TARGET_OBS_WHAM
TARGET_HADEC     = _tpm_tpm.TARGET_HADEC 
TARGET_TOP_AZEL  = _tpm_tpm.TARGET_TOP_AZEL 

TPM_INIT   = _tpm_tpm.TPM_INIT 
TPM_FAST   = _tpm_tpm.TPM_FAST   
TPM_MEDIUM = _tpm_tpm.TPM_MEDIUM   
TPM_SLOW   = _tpm_tpm.TPM_SLOW   
TPM_REFRACTION = _tpm_tpm.TPM_REFRACTION
TPM_ALL = _tpm_tpm.TPM_ALL

cdef class TSTATE(object):
    """Class corresponding to TPM TSTATE structure."""
    cdef _tpm_tpm.TPM_TSTATE _tstate

    def __cinit__(self):
        # Can refer to _tpm_astro since it will be included at the top
        # of pytpm.pyx.
        _tpm_astro.tpm_data(&self._tstate, TPM_INIT)

    def __init__(self, utc=None, delta_at=None, delta_ut=0.0, lon=0.0,
                 lat=0.0, alt=0.0, xpole=0.0, ypole=0.0, T=273.15,
                 P=1013.25, H=0.0, wavelength=0.550):
        # If utc and delta_at is None, then just use the value set by
        # __cinit__.
        if utc is not None:
            self._tstate.utc = utc
        if delta_at is not None:
            self._tstate.delta_at = delta_at
        self._tstate.delta_ut = delta_ut
        self._tstate.lon = lon
        self._tstate.lat = lat
        self._tstate.alt = alt
        self._tstate.xpole = xpole
        self._tstate.ypole = ypole
        self._tstate.T = T
        self._tstate.P = P
        self._tstate.H = H
        self._tstate.wavelength = wavelength

    cdef _tpm_tpm.TPM_TSTATE __get_tstate(self):
        """Return underlying TSTATE; only for use from Cython."""
        return self._tstate

    cdef __set_tstate(self, _tpm_tpm.TPM_TSTATE t):
        """Set underlying TSTATE; only for use from Cython."""
        # No checking is done on the given tstate.
        self._tstate = t
        
    def __getutc(self):
        return self._tstate.utc
    
    def __setutc(self, utc):
        self._tstate.utc = utc
        
    utc = property(__getutc, __setutc,
                   doc="UTC as JD. Defines NOW, i.e., current time.")

    def __getdelta_at(self):
        return self._tstate.delta_at
    
    def __setdelta_at(self, delta_at):
        self._tstate.delta_at = delta_at
        
    delta_at = property(__getdelta_at, __setdelta_at,
                        doc="DELTA_AT = TAI - UTC (s)")

    def __getdelta_ut(self):
        return self._tstate.delta_ut
    
    def __setdelta_ut(self, delta_ut):
        self._tstate.delta_ut = delta_ut
        
    delta_ut = property(__getdelta_ut, __setdelta_ut,
                        doc="DELTA_UT = UT1 - UTC (s)")

    def __getlon(self):
        return self._tstate.lon
    
    def __setlon(self, lon):
        self._tstate.lon = lon
        
    lon = property(__getlon, __setlon, doc=
                   "East longitude in radians.")

    def __getlat(self):
        return self._tstate.lat
    
    def __setlat(self, lat):
        self._tstate.lat = lat
        
    lat = property(__getlat, __setlat, doc=
                   "Latitude in radians.")

    def __getalt(self):
        return self._tstate.alt
    
    def __setalt(self, alt):
        self._tstate.alt = alt
        
    alt = property(__getalt, __setalt, doc=
                   "Altitude above geoid in meters.")
    
    def __getxpole(self):
        return self._tstate.xpole
    
    def __setxpole(self, xpole):
        self._tstate.xpole = xpole
        
    xpole = property(__getxpole, __setxpole, doc=
                   "Polar motion in radians.")

    def __getypole(self):
        return self._tstate.ypole
    
    def __setypole(self, ypole):
        self._tstate.ypole = ypole
        
    ypole = property(__getypole, __setypole, doc=
                   "Polar motion in radians.")

    def __getT(self):
        return self._tstate.T
    
    def __setT(self, T):
        self._tstate.T = T
        
    T = property(__getT, __setT, doc="Ambient temperature in Kelvins.")

    def __getP(self):
        return self._tstate.P
    
    def __setP(self, P):
        self._tstate.P = P
        
    P = property(__getP, __setP, doc="Ambient pressure in millibars.")

    def __getH(self):
        return self._tstate.H
    
    def __setH(self, H):
        self._tstate.H = H
        
    H = property(__getH, __setH, doc="Ambient humidity (0-1).")

    def __getwavelength(self):
        return self._tstate.wavelength
    
    def __setwavelength(self, wavelength):
        self._tstate.wavelength = wavelength
        
    wavelength = property(__getwavelength, __setwavelength,
                          doc="Observing wavelength in microns.")

    def __gettai(self):
        return self._tstate.tai
    
    tai = property(__gettai, doc="International Atomic Time.")

    def __gettdt(self):
        return self._tstate.tdt
    
    tdt = property(__gettdt,
                   doc="Terrestrial Dynamic Time;Terrestrial Time.")

    def __gettdb(self):
        return self._tstate.tdb
    
    tdb = property(__gettdb, doc="Barycentric Dynamic Time.")

    def __getobliquity(self):
        return self._tstate.obliquity
    
    obliquity = property(__getobliquity, doc=
                         "Obliquity of the Ecliptic.")

    def __getnut_lon(self):
        return self._tstate.nut_lon
    
    nut_lon = property(__getnut_lon, doc="Nutation in longitude.")

    def __getnut_obl(self):
        return self._tstate.nut_obl
    
    nut_obl = property(__getnut_obl, doc="Nutation in obliquity.")

    def __getnm(self):
        m3 = M3()
        m3.setM3(self._tstate.nm)
        return m3
    
    nm = property(__getnm, doc="Nutation matrix for NOW.")

    def __getpm(self):
        m6 = M6()
        m6.setM6(self._tstate.pm)
        return m6
    
    pm = property(__getpm, doc="Precession matrix from J2000 to NOW.")

    def __getut1(self):
        return self._tstate.ut1
    
    ut1 = property(__getut1, doc="Universal time.")

    def __getgmst(self):
        return self._tstate.gmst
    
    gmst = property(__getgmst, doc="Greewich Mean Sidereal Time.")

    def __getgast(self):
        return self._tstate.gast
    
    gast = property(__getgast, doc="Greewich Apparent Sidereal Time.")

    def __getlast(self):
        return self._tstate.last
    
    last = property(__getlast, doc="Local Apparent Sidereal Time.")

    def __geteb(self):
        v6 = V6C()
        v6.setV6(self._tstate.eb)
        return v6
    
    eb = property(__geteb, doc="Barycentric Earth state vector.")
    
    def __geteh(self):
        v6 = V6C()
        v6.setV6(self._tstate.eh)
        return v6
    
    eh = property(__geteh, doc="Heliocentric Earth state vector.")

    def __getobs_m(self):
        v6 = V6C()
        v6.setV6(self._tstate.obs_m)
        return v6
    
    obs_m = property(__getobs_m, doc=
                     "Geocentric Earth-fixed mean state vector.")

    def __getobs_t(self):
        v6 = V6C()
        v6.setV6(self._tstate.obs_t)
        return v6
    
    obs_t = property(__getobs_t, doc=
                     "Geocentric Earth-fixed true state vector.")

    def __getobs_s(self):
        v6 = V6C()
        v6.setV6(self._tstate.obs_s)
        return v6
    
    obs_s = property(__getobs_s, doc=
                     "Geocentric space-fixed true state vector.")

    def __getrefa(self):
        return self._tstate.refa
    
    refa = property(__getrefa, doc="Refraction coefficient.")

    def __getrefb(self):
        return self._tstate.refb
    
    refb = property(__getrefb, doc="Refraction coefficient.")
