"""Utility functions for the python interface to TPM library.

:Author: Prasanth Nair
:Contact: prasanthhn@gmail.com
"""
from pytpm import tpm
import math

def convert(x=0.0, y=0.0, s1=6, s2=19, epoch=tpm.J2000, 
            equinox=tpm.J2000, timetag=None, lon = -111.598333,
            lat = 31.956389, alt = 2093.093, T = 273.15, 
            P = 1013.25, H=0.0, W=0.55000):
    """Returns coordinates converted into target system.

    :param x: input ra or longitude in degrees
    :type x: float
    :param y: input dec or latitude in degrees
    :type y: float
    :param s1: starting TPM state
    :type s1: integer
    :param s2: ending TPM state
    :type s2: integer
    :param epoch: epoch of the input coordinates in JD (UTC)
    :type epoch: float
    :param equinox: equinox of the input coordinates in JD (UTC)
    :type equinox: float
    :param timetag: time of the target state as JD (UTC)
    :type timetag: float
    :param lon: longitude (east +, west -) of observer in degrees
    :type lon: float
    :param lat: latitude (north +, south -) of the observer in degrees
    :type lat: float
    :param alt: altitude of the observer in meter
    :type alt: float
    :param T: temperature at the observer's location in kelvin
    :type T: float
    :param P: atmospheric pressure at the observer's location in
        millibars
    :type P: float
    :param H: ambient humidity at the observer's location (0-1)
    :type H: float
    :param W: wavelength of observation in microns
    :type W: float

    This function calls the function tpm.convert() and returns
    coordinates in the final TPM state. 
    
    The input coordinates are specified using the paramters ``x`` and
    ``y``, both in degrees. The former is for the "longitudinal" angle,
    such as ra and the latter is for "latitudinal" angle, such as 
    declination. 

    ``s1`` and ``s2`` are the starting and ending TPM states. These are
    specified as integers but can also be specified using constants
    defined in the module ``tpm``. See the source code or the
    documentation for possible values. Default for starting state is the
    *Heliocentric FK5 mean equinox of J2000*, also accessible as 
    ``tpm.TPM_S06``, and that for the ending state is the *Topocentric
    Observed azimuth and elevation* for the given UTC time ``timetag``,
    also accessible as ``tpm.TPM_S19`` or ``tpm.TARGET_OBS_AZEL``.

    ``epoch`` and ``equinox`` are for the input coordinates and
    specified as UTC Julian Day numbers.

    ``timetag`` is the time at which the result should be calculated, or
    in other words the time of "observation". This is given as UTC
    Julian day number.

    The remaining parameters set the properties of the observer's site.
    These are of-course used only when the observer's location
    information is needed. The default values are for KPNO and are taken
    from the source code of the TPM C library.
   
    :Author: Prasanth Nair
    :Contact: prasanthhn@gmail.com
    """
    # tpm.convert takes radians.
    x = math.radians(x)
    y = math.radians(y)
    if timetag == None:
        timetag = tpm.utc_now()
    x1,y1 = tpm.convert(x,y,s1,s2,epoch,equinox,timetag,lon,lat,alt,
            T,P,H,W)
    return math.degrees(x1),math.degrees(y1)

# The functions below are defined are macros in the TPM header times.h.
# These provide shortcuts to various time and angle conversions.
def d2h(d):
    """Converts decimal degrees into hours.

    >>> d2h(180.0)
    12.0
    """
    return d/15.0

def h2d(h):
    """Converts decimal hours into degrees.
    
    >>> h2d(12.0)
    180.0
    """
    return h*15.0

def d2r(d):
    """Converts decimal degrees into radians.
    
    >>> y = d2r(180.0)
    >>> import math
    >>> assert y == math.pi
    """
    return d*(tpm.M_PI/180.0)

def r2d(r):
    """Converts decimal radians into degrees.
    
    >>> r2d(tpm.M_PI)
    180.0
    """
    return r*(180.0/tpm.M_PI)

def h2r(h):
    """Converts decimal hours into radians.
    
    >>> import math
    >>> assert h2r(12.0) == math.pi
    """
    return h*(tpm.M_PI/12.0) 

def r2h(r):
    """Converts decimal radians into hours.
    
    >>> import math
    >>> r2h(math.pi) 
    12.0
    """
    return r*(12.0/tpm.M_PI)

def d2as(d):
    """Converts decimal degrees into arcseconds.
    
    >>> d2as(1.0)
    3600.0
    """
    return d*3600.0

def as2d(a):
    """Converts arcseconds into decimal degrees.
    
    >>> as2d(3600.0)
    1.0
    """
    return a/3600.0

def as2h(a):
    """Converts arcseconds into decimal degrees.
    
    >>> as2h(3600.0*15.0)
    1.0
    """
    return d2h(as2d(a))

def h2as(h):
    """Converts hours into arcseconds.
    
    >>> h2as(1.0)
    54000.0
    """
    return d2as(h2d(h))

def r2as(r):
    """Converts arcseconds into radians.
    
    >>> import math
    >>> r2as(math.pi)
    648000.0
    """
    return d2as(r2d(r))

def as2r(a):
    """Converts arcseconds into radians.
    
    >>> import math
    >>> assert as2r(3600.0*180.0) == math.pi
    """
    return d2r(as2d(a))

def d2hms(d):
    """Converts decimal degrees into an HMS structure.
    
    >>> hms = d2hms(180.0)
    >>> print hms.hh, hms.mm, hms.ss
    12.0 0.0 0.0
    """
    return tpm.h2hms(d2h(d))

def dms2h(dms):
    """Converts a DMS structure into hours.
    
    >>> import tpm
    >>> dms = tpm.d2dms(180.0)
    >>> dms2h(dms)
    12.0
    """
    return d2h(tpm.dms2d(dms))

def dms2r(dms):
    """Converts a DMS structure into radians.
    
    >>> import tpm
    >>> import math
    >>> assert dms2r(tpm.d2dms(180.0)) == math.pi
    """
    return d2r(tpm.dms2d(dms))

def fmt_dms(dms):
    """Returns a string representation of the angle in a DMS structure.

    >>> import tpm
    >>> dms = tpm.d2dms(180.0)
    >>> print fmt_dms(dms)
    +180D 00' 00.000"
    """
    return tpm.fmt_d(tpm.dms2d(dms))

def fmt_hms(hms):
    """Returns a string representation of the time in an HMS structure.

    >>> import tpm
    >>> print fmt_hms(tpm.h2hms(12.5))
     12H 30M 00.000S
    """
    return tpm.fmt_h(tpm.hms2h(hms))

def fmt_jd(jd):
    """Returns a string representation of the Julian Day in a JD structure.

    >>> import tpm
    >>> jd = tpm.j2jd(2451545.5)
    >>> print fmt_jd(jd)
     2451545  12H 00M 00.000S
    """
    return tpm.fmt_j(tpm.jd2j(jd))

def fmt_r(r):
    """Returns a string representation of the angle given in radians.

    >>> print fmt_r(1.0)
    +57D 17' 44.806"
    """
    return tpm.fmt_d(r2d(r))

def fmt_y(y):
    """Returns a string representation of the time given in years.

    >>> import tpm
    >>> print fmt_y(2000.2454)
    Wed Mar 29 19:35:36.959 2000
    """
    return tpm.fmt_ymd(tpm.y2ymd(y))

def h2dms(h):
    """Converts hours into a DMS structure.

    >>> dms = h2dms(12.0)
    >>> print dms.dd, dms.mm, dms.ss
    180.0 0.0 0.0
    """
    return tpm.d2dms(h2d(h))

def hms2d(hms):
    """Converts time in an HMS structure into an angle in decimal degrees.

    >>> import tpm
    >>> hms2d(tpm.h2hms(12.0))
    180.0
    """
    return h2d(tpm.hms2h(hms)) 

def hms2r(hms):
    """Converts time in an HMS structure into an angle in radians.

    >>> import tpm
    >>> import math
    >>> assert hms2r(tpm.h2hms(12.0)) == math.pi
    """
    return h2r(tpm.hms2h(hms))

def j2j(j):
    """Simply returns the input.

    Inlcuded as this is present in tpm/times.h.
    """
    return j

def jd2rdb(jd):
    """Convert time in JD structure into RDB time.

    >>> import tpm
    >>> jd2rdb(tpm.j2jd(2451545.0))
    101.12
    """
    return tpm.ymd2rdb(tpm.jd2ymd(jd))

def j2rdb(j):
    """Convert time in Julian day number into RDB time.

    >>> j2rdb(2451545.0)
    101.12
    """
    return jd2rdb(tpm.j2jd(j))

def jd2y(jd):
    """Converts time in a JD structure into a Gregorian year. 

    >>> import tpm
    >>> jd = tpm.ymd2jd(tpm.y2ymd(2000))
    >>> jd2y(jd)
    2000.0
    """
    return tpm.ymd2y(tpm.jd2ymd(jd))

def j2y(j):
    """Converts Julian day number into a Gregorian year.

    >>> j2y(tpm.jd2j(tpm.ymd2jd(tpm.y2ymd(2000))))
    2000.0
    """
    return jd2y(tpm.j2jd(j))

def j2ymd(j):
    """Converts a Julian day number into a YMD structure.
    
    >>> ymd = j2ymd(2451545.0)
    >>> print tpm.fmt_ymd(ymd)
    Sat Jan  1 12:00:00.000 2000
    """
    return tpm.jd2ymd(tpm.j2jd(j))

def r2dms(r):
    """Converts angle in radians into a DMS structure.

    >>> import tpm
    >>> dms = r2dms(tpm.M_PI)
    >>> print fmt_dms(dms)
    +180D 00' 00.000"
    """
    return tpm.d2dms(r2d(r))

def r2hms(r):
    """Converts angle in radians into an HMS structure.

    >>> import tpm
    >>> print fmt_hms(r2hms(tpm.M_PI))
     12H 00M 00.000S
    """
    return tpm.h2hms(r2h(r))

def rdb2jd(rdb):
    """Converts RDB time into a JD structure.

    >>> import tpm
    >>> jd = rdb2jd(tpm.ymd2rdb(tpm.jd2ymd(tpm.j2jd(2451545.0))))
    >>> fmt_jd(jd)
     2451545.0  00H 00M 00.000S
    """
    return tpm.ymd2jd(tpm.rdb2ymd(rdb))

def rdb2j(rdb):
    """Converts RDB time into Julian day number.

    >>> rdb2j(101.12)
    2451545.0
    """
    return tpm.jd2j(rdb2jd(rdb))

def rdb2rdb(rdb):
    """
    """
    return tpm.ymd2rdb(tpm.rdb2ymd(rdb))

def rdb2y(rdb):
    return tpm.ymd2y(tpm.rdb2ymd(rdb))

def rdb_diff(rdb1, rdb2):
    return tpm.jd_diff(rdb2jd(rdb1),rdb2jd(rdb2))

def y2jd(y):
    return tpm.ymd2jd(tpm.y2ymd(y))

def y2j(y):
    return tpm.jd2j(y2jd(y))

def y2rdb(y):
    return tpm.ymd2rdb(tpm.y2ymd(y))

def y2y(y):
    return y

def ymd2j(ymd):
    return tpm.jd2j(tpm.ymd2jd(ymd))

def ymd_diff(ymd1,ymd2):
    return jd_diff(tpm.ymd2jd(ymd1),tpm.ymd2jd(ymd2))

# The following are transformations defined in the astro.h header file
# in the TPM library.

# Definitive time transformations.
def et2tdt(et):
    return et

def tai2tdt(tai):
    return tai + 32.184/86400

def tdt2et(tdt):
    return tdt

def utc2tai(utc):
    return utc + tpm.delta_AT(utc)/86400

# Approximate time transformations
def tai2utc(tai):
    return tai - tpm.delta_AT(tai)/86400

def tdt2tai(tdt):
    return tdt - 32.184/86400

# Derived time transformations
def et2tai(et):
    return tdt2tai(et2tdt(et))

def tai2et(tai):
    return tdt2et(tai2tdt(tai))

# Convenience time transformations
def ut2gmst(ut):
    return tpm.ut12gmst(ut)

# The following are macros from times.h header in TPM for accessing and
# modifying data in various data structures.
# Note that the fields of data structures are 'pointers' and hence
# modifying the data structures inside functions also modifies them in
# the calling scope.
def byear2j(x):
    """Macro BYEAR2JD in src/tpm/times.h"""
    return tpm.B1950 + (x - 1950.0) * (tpm.CB/100.0)

def j2byear(x):
    """Macro JD2BYEAR in src/tpm/times.h"""
    return 1950.0 + (x - tpm.B1950) * (100.0/tpm.CB)

def jyear2j(x):
    """Macro JYEAR2JD in src/tpm/times.h"""
    return tpm.J2000 + (x - 2000.0) * (tpm.CJ/100.0)

def j2jyear(x):
    """Macro JD2JYEAR in src/tpm/times.h"""
    return 2000.0 + (x - tpm.J2000) * (100.0/tpm.CJ)

def dmsDecDegrees(s, x):
    s.dd -= x

def dmsDecMinutes(s, x):
    s.mm -= x

def dmsDecSeconds(s, x):
    s.ss -= x
    
def dmsDivDegrees(s, x):
    s.dd /= x

def dmsDivMinutes(s, x):
    s.mm /= x   

def dmsDivSeconds(s, x):
    s.ss /= x

def dmsGetDegrees(s):
    return s.dd

def dmsGetMinutes(s):
    return s.mm

def dmsGetSeconds(s):
    return s.ss

def dmsIncDegrees(s, x):
    s.dd += x

def dmsIncMinutes(s, x):
    s.mm += x

def dmsIncSeconds(s, x):
    s.ss += x

def dmsMulDegrees(s, x):
    s.dd *= x

def dmsMulMinutes(s, x):
    s.mm *= x

def dmsMulSeconds(s, x):
    s.ss *= x

def dmsSetDegrees(s, x):
    s.dd = x

def dmsSetMinutes(s, x):
    s.mm = x

def dmsSetSeconds(s, x):
    s.ss = x

def hmsDecHours(s, x):
    s.hh -= x

def hmsDecMinutes(s, x):
    s.mm -= x
    
def hmsDecSeconds(s, x):
    s.ss -= x

def hmsDivHours(s, x):
    s.hh /= x

def hmsDivMinutes(s, x):
    s.mm /= x

def hmsDivSeconds(s, x):
    s.ss /= x

def hmsGetHours(s):
    return s.hh

def hmsGetMinutes(s):
    return s.mm

def hmsGetSeconds(s):
    return s.ss

def hmsIncHours(s, x):
    s.hh += x

def hmsIncMinutes(s, x):
    s.mm += x

def hmsIncSeconds(s, x):
    s.ss += x

def hmsMulHours(s, x):
    s.hh *= x

def hmsMulMinutes(s, x):
    s.mm *= x

def hmsMulSeconds(s, x):
    s.ss *= x

def hmsSetHours(s, x):
    s.hh = x

def hmsSetMinutes(s, x):
    s.mm = x

def hmsSetSeconds(s, x):
    s.ss = x

def jdDecDay(s, x):
    s.dd -= x

def jdDecHours(s, x):
    s.hms.hh -= x

def jdDecMinutes(s, x):
    s.hms.mm -= x

def jdDecSeconds(s, x):
    s.hms.ss -= x

def jdDivDay(s, x):
    s.dd /= x

def jdDivHours(s, x):
    s.hms.hh /= x

def jdDivMinutes(s, x):
    s.hms.mm /= x

def jdDivSeconds(s, x):
    s.hms.ss /= x

def jdGetDay(s): 
    return s.dd

def jdGetHours(s):
    return s.hms.hh

def jdGetMinutes(s):
    return s.hms.mm

def jdGetSeconds(s):
    return s.hms.ss

def jdIncDay(s, x):
    s.dd += x

def jdIncHours(s, x):
    s.hms.hh += x

def jdIncMinutes(s, x):
    s.hms.mm += x

def jdIncSeconds(s, x):
    s.hms.ss += x

def jdMulDay(s, x):
    s.dd *= x

def jdMulHours(s, x):
    s.hms.hh *= x

def jdMulMinutes(s, x):
    s.hms.mm *= x

def jdMulSeconds(s, x):
    s.hms.ss *= x

def jdSetDay(s, x):
    s.dd = x

def jdSetHours(s, x):
    s.hms.hh = x

def jdSetMinutes(s, x):
    s.hms.mm = x

def jdSetSeconds(s, x):
    s.hms.ss = x

def ymdDecDay(s, x):
    s.dd -= x

def ymdDecHours(s, x):
    s.hms.hh -= x

def ymdDecMinutes(s, x):
    s.hms.mm -= x

def ymdDecMonth(s, x):
    s.m -= x

def ymdDecSeconds(s, x):
    s.hms.ss -= x

def ymdDecYear(s, x):
    s.y -= x

def ymdDivDay(s, x):
    s.dd /= x

def ymdDivHours(s, x):
    s.hms.hh /= x

def ymdDivMinutes(s, x):
    s.hms.mm /= x

def ymdDivMonth(s, x):
    s.m /= x

def ymdDivSeconds(s, x):
    s.hms.ss /= x
    
def ymdDivYear(s, x):
    s.y /= x

def ymdGetDay(s):
    return s.dd

def ymdGetHours(s):
    return s.hms.hh

def ymdGetMinutes(s):
    return s.hms.mm

def ymdGetMonth(s):
    return s.m

def ymdGetSeconds(s):
    return s.hms.ss

def ymdGetYear(s):
    return s.y

def ymdIncDay(s, x):
    s.dd += x

def ymdIncHours(s, x):
    s.hms.hh += x

def ymdIncMinutes(s, x):
    s.hms.mm += x
    
def ymdIncMonth(s, x):
    s.m += x

def ymdIncSeconds(s, x):
    s.hms.ss += x

def ymdIncYear(s, x):
    s.y += x

def ymdMulDay(s, x):
    s.dd *= x

def ymdMulHours(s, x):
    s.hms.hh *= x

def ymdMulMinutes(s, x):
    s.hms.mm *= x

def ymdMulMonth(s, x):
    s.m *= x

def ymdMulSeconds(s, x):
    s.hms.ss *= x

def ymdMulYear(s, x):
    s.y *= x

def ymdSetDay(s, x):
    s.dd = x

def ymdSetHours(s, x):
    s.hms.hh = x

def ymdSetMinutes(s, x):
    s.hms.mm = x

def ymdSetMonth(s, x):
    s.m = x

def ymdSetSeconds(s, x):
    s.hms.ss = x

def ymdSetYear(s, x):
    s.y = x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
