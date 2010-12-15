# -*- coding: utf-8 -*-
"""Utility functions for the python interface to TPM library.

Except for the ``convert`` function, these are equivalent to the
several macros provided in TPM. The macros are provided as python
functions since they can't be wrapped with SWIG.

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


# The following are transformations defined in the astro.h header file
# in the TPM library.

# Definitive time transformations.
def utc2tai(utc):
    """Return TAI for the given UTC.

    :param utc: Coordinated Universal Time
    :type utc: float; Julian date

    :return: International Atomic Time
    :rtype: float; Julian date
    
    Returns the International Atomic Time for the given UTC; input and
    output are Julian dates.

    Note that the file delta_AT.c must be updated to reflect the
    latest value for TAI - UTC and the PyTPM library must be
    recompiled.
    
    >>> utc = 2451545.0
    >>> print utils.utc2tai(utc)
    2451545.00037
    """
    return utc + tpm.delta_AT(utc)/86400

def tai2tdt(tai):
    """Returns TDT for the given TAI.

    :param tai: International Atomic Time
    :type tai: float; Julian date

    :return: Terrestrial Dynamic Time
    :rtype: float; Julian date
    
    Returns the Terrestrial Dynamic Time for the given International
    Atomic Time, as a Julian date.

    >>> utc = 2451545.0
    >>> tai = utc + tpm.delta_AT(utc)
    >>> print utils.tai2tdt(tai)
    2451577.00037
    """
    return tai + 32.184/86400

def et2tdt(et):
    """Returns the input. ET is deprecated; use TDT.

    :param et: Ephemeris time
    :type et: float; Julian date

    :return: Terrestrial Dynamic Time
    :rtype: float; Julian date

    Ephemeris Time is deprecated and hence this function merely
    returns the input. Terrestrial Dynamic Time should be used instead
    of ET.
    """
    return et

def tdt2et(tdt):
    """Returns the input. ET is deprecated; use TDT.

    :param tdt: Terrestrial Dynamic Time
    :type tdt: float; Julian date

    :return: Ephemeris Time
    :rtype: float; Julian date

    Ephemeris Time is deprecated and hence this function merely
    returns the input. Terrestrial Dynamic Time should be used instead
    of ET.
    """
    return tdt

def tai2utc(tai):
    """Returns UTC for the given TAI.

    :param tai: International Atomic Time
    :type tai: float; Julian date

    :return: Coordianted Universal Time
    :rtype: float; Julian date
    
    Returns the International Atomic Time corresponding to the given
    Coordinated Universal TIme. Both input and output are Julian
    dates.

    Note that the file delta_AT.c must be updated to reflect the
    latest value for TAI - UTC and the PyTPM library must be
    recompiled.
    
    >>> print tai2utc(2451577.0)
    2451576.99963
    """
    return tai - tpm.delta_AT(tai)/86400

def tdt2tai(tdt):
    """Returns TAI for the given TDT

    :param tdt: Terrestrial Dynamic Time
    :type tdt: float; Julian date
    
    :return: International Atomic Time
    :rtype: float; Julian date

    Returns the International Atomic Time corresponding to the given
    Terrestrial Dynamic Time. Both input and output are Julian dates.

    >>> print tdt2tai(2451577)
    2451576.99963
    """
    return tdt - 32.184/86400


# Derived time transformations
def et2tai(et):
    """Returns TAI for given ET; ET is dreprecated, use TDT.

    :param et: Ephemeris Time
    :type et: float; Julian date

    :return: International Atomic Time
    :rtype: float; Julian date

    Returns the International Atomic Time for the given Ephemeris
    Time. The latter is dreprecated and hence the given value is
    assumed to be the Terrestrial Dynamic Time is used Both input and
    output are Julian dates.

    >>> print et2tai(2451576)
    2451575.99963
    """
    return tdt2tai(et2tdt(et))

def tai2et(tai):
    """Returns ET for the given TAI; ET is deprecated use TDT.

    :param tai: International Atomic Time
    :type tai: float; Julian date

    :return: Ephemeris Time
    :rtype: float; Julian date

    Returns the Ephemeris Time for the given International Atomic
    Time. The former is deprecated and hence the given value is
    assumed to be the Terrestrial Dynamic Time. Both input and output
    are Julian dates.

    >>> print tai2et(2451575.0)
    2451575.00037
    """
    return tdt2et(tai2tdt(tai))

# Convenience time transformations
def ut2gmst(ut):
    """Returns GMST for the given UT.

    :param ut: Universal Time
    :type ut: float; Julian date

    :return: Greewich Mean Sidereal Time
    :rtype: float; radians [0 - 2π]

    Returns the Greewich Mean Sidereal Time for the given Universal
    Time. Here UT is taken to be the same as UT1. The return value is
    in radians normalized to [0 - 2π].

    >>> ut = 2451545.0
    >>> print ut2gmst(ut)
    4.89496121282
    """
    return tpm.ut12gmst(ut)


# The functions below are defined are macros in the TPM header times.h.
# These provide shortcuts to various time and angle conversions.
def byear2jd(x):
    """Converts Besselian year into a Julian date.

    :param x: Besselian year
    :type x: float

    :return: Julian date
    :rtype: float

    >>> print "{0:15.7f}".format(byear2jd(1950.0))
    2433282.4234590
    >>> print "{0:15.7f}".format(byear2jd(2000.0))
    2451544.5333981
    >>> "{0:4.5f}".format((byear2jd(2000) - byear2jd(1950)) / tpm.CJ*100)
    '49.99893'
    >>> import tpm
    >>> "{0:4.1f}".format((byear2jd(2000) - byear2jd(1950)) / tpm.CB*100)
    '50.0'
    """
    return tpm.B1950 + (x - 1950.0) * (tpm.CB/100.0)

def jd2byear(x):
    """Converts Julian day number into Besselian years.

    :param x: Julian date
    :type x: float

    :return: Besselian year
    :rtype: float
    
    >>> print "{0:6.1f}".format(jd2byear(2451544.5333981))
    2000.0
    """
    return 1950.0 + (x - tpm.B1950) * (100.0/tpm.CB)

def jyear2jd(x):
    """Converts Julian year into Julian date.

    :param x: Julian year
    :type x: float

    :return: Julian date
    :rtype: float
    
    >>> jyear2jd(2000)
    2451545.0
    >>> jyear2jd(1950)
    2433282.5
    >>> (jyear2jd(2000.0) - jyear2jd(1950.0) ) / tpm.CJ * 100
    50.0
    """
    return tpm.J2000 + (x - 2000.0) * (tpm.CJ/100.0)

def jd2jyear(x):
    """Converts Julian date into Julian year.

    :param x: Julian date
    :rtype x: float

    :return: Julian year
    :rtype: float
        
    >>> jd2jyear(2451545.0)
    2000.0
    """
    return 2000.0 + (x - tpm.J2000) * (100.0/tpm.CJ)

def d2h(d):
    """Converts degrees into hours.

    :param d: Degrees
    :type d: float

    :return: Hours
    :rtype: float

    COnverts degrees into hours, according to the relation 360 degrees
    = 24 hours.
    
    >>> d2h(180.0)
    12.0
    """
    return d/15.0

def h2d(h):
    """Converts hours into degrees.

    :param h: Hours
    :type h: float

    :return: Degrees
    :rtype: float

    Converts hours into degrees, according to the relation 24 hours =
    360 degrees.
    
    >>> h2d(12.0)
    180.0
    """
    return h*15.0

def d2r(d):
    """Converts degrees into radians.

    :param d: Degrees
    :type d: float

    :return: Radians
    :rtype: float

    Converts an angle in degrees into one in radians, according to the
    relation 360 degrees = 2π radians.
    
    >>> y = d2r(180.0)
    >>> import math
    >>> assert y == math.pi
    """
    return d*(tpm.M_PI/180.0)

def r2d(r):
    """Converts radians into degrees.

    :param r: Radians
    :type r: float

    :return: Degrees
    :rtype: float

    Converts an angle in radians into one in degrees, according to the
    relation 2π radians = 360 degrees.
    
    >>> r2d(tpm.M_PI)
    180.0
    """
    return r*(180.0/tpm.M_PI)

def h2r(h):
    """Converts hours into radians.

    :param h: Hours
    :type h: float

    :return: Radians
    :rtype: float

    Converts hours into an angle in radians, according to the relation
    24 hours = 2π radians.
    
    >>> import math
    >>> assert h2r(12.0) == math.pi
    """
    return h*(tpm.M_PI/12.0) 

def r2h(r):
    """Converts radians into hours.

    :param r: Radians
    :type r: float

    :return: Hours
    :rtype: float

    Converts an angle in radians into hours, according to the relation
    2π radians = 24 hours.
    
    >>> import math
    >>> r2h(math.pi) 
    12.0
    """
    return r*(12.0/tpm.M_PI)

def d2as(d):
    """Converts degrees into arcseconds.

    :param d: Degrees
    :type d: float

    :return: Arc-seconds
    :rtype: float

    Converts an angle in degrees into arc-seconds, according to the
    relation 1 degree = 3600 arc-seconds.
        
    >>> d2as(1.0)
    3600.0
    """
    return d*3600.0

def as2d(a):
    """Converts arcseconds into degrees.

    :param a: Arc-seconds
    :type a: float

    :return: Degrees
    :rtype: float

    Converts an angle in arc-seconds into degrees, according to the
    relation 3600 arc-seconds = 1 degree.

    >>> as2d(3600.0)
    1.0
    """
    return a/3600.0

def as2h(a):
    """Converts arcseconds into hours.

    :param a: Arc-seconds
    :type a: float

    :return: Hours
    :rtype: float

    Converts arc-seconds into hours, according to the relation 24
    hours = 360 degrees = 360 * 3600 arc-seconds.
    
    >>> as2h(3600.0*15.0)
    1.0
    """
    return d2h(as2d(a))

def h2as(h):
    """Converts hours into arcseconds.

    :param h: Hours
    :type h: float

    :return: Arc-seconds
    :rtype: float

    Converts hours into arc-seconds according to the relation 24 hours
    = 360 degrees = 360 * 3600 arc-seconds.
    
    >>> h2as(1.0)
    54000.0
    """
    return d2as(h2d(h))

def r2as(r):
    """Converts radians into arcseconds.

    :param r: Radians
    :type r: float

    :return: Arc-seconds
    :rtype: float

    Converts radians into arc-seconds according to the relation 2π
    radians = 360 degrees = 360 * 3600 arc-seconds.
    
    >>> import math
    >>> r2as(math.pi)
    648000.0
    """
    return d2as(r2d(r))

def as2r(a):
    """Converts arcseconds into radians.

    :param a: Arc-seconds
    :type a: float

    :return: Radians
    :rtype: float

    Converts arc-seconds into radians, according to the relation 2π
    radians = 360 degrees = 360 * 3600 arc-seconds.
    
    >>> import math
    >>> assert as2r(3600.0*180.0) == math.pi
    """
    return d2r(as2d(a))

def d2hms(d):
    """Converts degrees into an HMS structure.

    :param d: Degrees
    :type d: float

    :return: Degrees converted into hours, minutes and seconds.
    :rtype: :class:`pytpm.tpm.HMS`

    Converts degrees into hours, minutes and seconds, according to the
    relation 360 degrees = 24 hours = 24 * 60 minutes = 24 * 3600
    seconds. 
    
    >>> hms = d2hms(180.0)
    >>> print hms.hh, hms.mm, hms.ss
    12.0 0.0 0.0
    """
    return tpm.h2hms(d2h(d))

def dms2h(dms):
    """Converts angle in a DMS structure into hours.

    :param dms: Angle in degrees, arc-minutes and arc-seconds.
    :type dms: :class:`pytpm.tpm.DMS`

    :return: Hours
    :rtype: float

    Convers angle in degrees, minutes and seconds, stored in a
    :class:`pytpm.tpm.DMS` structure into hours, according to the
    relation 24 hours = 360 degrees = 360 * 60 arc-minutes = 360 *
    3600 arc-seconds.
    
    >>> import tpm
    >>> dms = tpm.d2dms(180.0)
    >>> dms2h(dms)
    12.0
    """
    return d2h(tpm.dms2d(dms))

def dms2r(dms):
    """Converts a DMS structure into radians.

    :param dms: Angle in degrees, arc-minutes and arc-seconds
    :type dms: :class:`pytpm.tpm.DMS`

    :return: Radians
    :rtype: float

    Converts angle in degrees, minutes and seconds, stored in a
    :class:`pytpm.tpm.DMS` structure into angle in radians, according
    to the relation 360 degrees = 360 * 60 arc-minutes = 360 * 3600
    arc-seconds = 2π radians.
    
    >>> import tpm
    >>> import math
    >>> assert dms2r(tpm.d2dms(180.0)) == math.pi
    """
    return d2r(tpm.dms2d(dms))

def fmt_dms(dms):
    """Returns a string representation of the angle in a DMS structure.

    :param dms: Angle in degrees, arc-minutes and arc-seconds
    :type dms: :class:`pytpm.tpm.DMS`

    :return: String representation of angle
    :rtype: String
    
    Converts angle in degrees, arc-minutes and arc-seconds stored in a
    :class:`pytpm.tpm.DMS` structure into a string.

    >>> import tpm
    >>> dms = tpm.d2dms(180.0)
    >>> print fmt_dms(dms)
    +180D 00' 00.000"
    """
    return tpm.fmt_d(tpm.dms2d(dms))

def fmt_hms(hms):
    """Returns a string representation of the time in an HMS structure.

    :param hms: Hours, minutes and seconds
    :type hms: :class:`pytpm.tpm.HMS`

    :return: String represenation of hours, minutes and seconds
    :rtype: String

    Converts the time in hours, minutes and seconds stored in a
    :class:`pytpm.tpm.HMS` structure into a string representation of
    the time, of the format "HH MM SS.SS"

    >>> import tpm
    >>> print fmt_hms(tpm.h2hms(12.5))
     12H 30M 00.000S
    """
    return tpm.fmt_h(tpm.hms2h(hms))

def fmt_jd(jd):
    """Returns a string representation of the Julian Day in a JD structure.

    :param jd: Julian date
    :type jd: :class:`pytpm.tpm.JD`

    :return: String representation of Julian date
    :rtype: String

    Converts the Julian date in a :class:`pytpm.tpm.JD` structure into
    a string of the format "DAY HH MM SS.SS".
    
    >>> import tpm
    >>> jd = tpm.j2jd(2451545.5)
    >>> print fmt_jd(jd)
     2451545  12H 00M 00.000S
    """
    return tpm.fmt_j(tpm.jd2j(jd))

def fmt_r(r):
    """Returns a string, with the angle in radians converted into degrees.

    :param r: Radians
    :type r: Float

    :return: String of the format "DD MM SS.SS".
    :rtype: String

    Convert the angle given in radians into a string of the format "DD
    MM SS."
    
    >>> print fmt_r(1.0)
    +57D 17' 44.806"
    """
    return tpm.fmt_d(r2d(r))

def fmt_y(y):
    """Returns a string representation of the time given in years.

    :param y: Year, including fractional part.
    :type y: Float

    :return: String of the format "WEEKDAY MONTH DAY HH:MM:SS.SS YEAR"
    :rtype: String
    
    >>> print fmt_y(2000.2454)
    Wed Mar 29 19:35:36.959 2000
    >>> fmt_y(j2y(2400000.5))
    'Wed Nov 17 00:00:00.000 1858'
    """
    return tpm.fmt_ymd(tpm.y2ymd(y))

def h2dms(h):
    """Converts hours into an angle in a DMS structure.

    :param h: Hours
    :type h: Float

    :return: Angle in degrees, arc-minutes and arc-seconds.
    :rtype: :class:`pytpm.tpm.DMS`

    Converts hours into angle in degrees, arc-minutes and arc-seconds
    stored in a :class:`pytpm.tpm.DMS` structure.
    
    >>> dms = h2dms(12.0)
    >>> print dms.dd, dms.mm, dms.ss
    180.0 0.0 0.0
    """
    return tpm.d2dms(h2d(h))

def hms2d(hms):
    """Converts time in an HMS structure into an angle in degrees.

    :param hms: Hours, minutes and seconds
    :type hms: :class:`pytpm.tpm.HMS`

    :return: Degrees
    :rtype: Float

    Converts time in an :class:`pytpm.tpm.HMS` structure into an angle
    in degrees, according to the relation 24 hours = 24 * 60 minutes =
    24* 3600 seconds = 360 degrees.
    
    >>> import tpm
    >>> hms2d(tpm.h2hms(12.0))
    180.0
    """
    return h2d(tpm.hms2h(hms)) 

def hms2r(hms):
    """Converts time in an HMS structure into an angle in radians.

    :param hms: Hours, miutes and seconds
    :type hms: :class:`pytpm.tpm.HMS`

    :return: Radians
    :rtype: Float

    Converts hours, minutes and seconds stored in a
    :class:`pytpm.tpm.HMS` structure into an angle in radians,
    according to the relation 24 hours = 24*60 minutes = 24*3600
    seconds = 2π radians.
    
    >>> import tpm
    >>> import math
    >>> assert hms2r(tpm.h2hms(12.0)) == math.pi
    """
    return h2r(tpm.hms2h(hms))

def j2j(j):
    """Simply returns the input.

    Included here, as this macro is present in tpm/times.h.

    >>> j2j(2451545)
    2451545
    """
    return j


def jd2y(jd):
    """Converts Julian date in a JD structure into a Gregorian year. 

    :param jd: Julian date
    :type jd: :class:`pytpm.tpm.JD`

    :return: Gregorian year, including fractional part
    :rtype: Float

    Converts Julian date stored in a :class:`pytpm.tpm.JD` structure
    into the corresponding year in the Gregorian calendar.
    
    >>> import tpm
    >>> jd = tpm.ymd2jd(tpm.y2ymd(2000))
    >>> jd2y(jd)
    2000.0
    """
    return tpm.ymd2y(tpm.jd2ymd(jd))

def j2y(j):
    """Converts Julian date into a Gregorian year with fractional part.

    :param j: Julian date
    :type j: Float

    :return: Gregorian calendar year, with fractional part.
    :rtype: Float

    Converts the given Julian date into a year in the Gregorian
    calendar year, including the fractional part of the year.
    
    >>> j2y(tpm.jd2j(tpm.ymd2jd(tpm.y2ymd(2000))))
    2000.0
    """
    return jd2y(tpm.j2jd(j))

def j2ymd(j):
    """Converts Julian date into a Gregorian date, in a YMD structure.

    :param j: Julian date
    :type j: Float

    :return: Year, month, day, hours, minutes, seconds (Gregorian)
    :rtype: :class:`pytpm.tpm.YMD`

    Convert the given Julian date into a Gregorian calendar date,
    including year, month, day, hours, minutes and seconds, stored in
    a :class:`pytpm.tpm.YMD` structure.
    
    >>> ymd = j2ymd(2451545.0)
    >>> print tpm.fmt_ymd(ymd)
    Sat Jan  1 12:00:00.000 2000
    """
    return tpm.jd2ymd(tpm.j2jd(j))

def r2dms(r):
    """Converts angle in radians into degrees, in a DMS structure.

    :param r: Radians
    :type r: Float

    :return: Degrees, arc-minutes and arc-seconds
    :rtype: :class:`pytpm.tpm.DMS`

    Converts the given angle in radians into degrees, arc-minutes and
    arc-seconds stored in a :class:`pytpm.tpm.HMS` structure,
    according to the relation 2π radians = 360 degrees = 360 * 60
    arc-minutes = 360 * 3600 arc-seconds.

    >>> import tpm
    >>> dms = r2dms(tpm.M_PI)
    >>> print fmt_dms(dms)
    +180D 00' 00.000"
    """
    return tpm.d2dms(r2d(r))

def r2hms(r):
    """Converts angle in radians into time, in an HMS structure.

    :param r: Radians
    :type r: Float

    :return: Hours, minutes and seconds
    :rtype: :class:`pytpm.tpm.HMS`

    Converts angle in radians into hours, minutes and seconds, stored
    in a :class:`pytpm.tpm.HMS` structure, according to the relation
    2π radians = 24 hours = 24 * 60 arc-minutes = 24 * 3600 seconds.
    
    >>> import tpm
    >>> print fmt_hms(r2hms(tpm.M_PI))
     12H 00M 00.000S
    """
    return tpm.h2hms(r2h(r))

def y2jd(y):
    """Converts a Gregorian calendar year into a Julian date, in a JD structure.

    :param y: Gregorian calendar year, including fractional part.
    :type y: Float

    :return: Julian date in a :class:`pytpm.tpm.JD` structure.
    :rtype: :class:`pytpm.tpm.JD`

    Converts a Gregorian calendar year, including fractional part,
    into a Julian date stored in a :class:`pytpm.tpm.JD` structure.
    
    >>> jd = y2jd(2000.0) # 1999/12/31 00:00:00
    >>> jd = tpm.jd2jd(jd)
    >>> fmt_jd(jd)
    ' 2451543  12H 00M 00.000S'
    """
    return tpm.ymd2jd(tpm.y2ymd(y))

def y2j(y):
    """Converts a Gregorian calendar year into a Julian date.

    :param y: Gregorian calendar year, including fractional part
    :type y: Float

    :return: Julian date
    :rtype: Float

    Converts the given Gregorian calendar year, including fractional
    part, into a Julian date.
    
    >>> j = y2j(2000.0) # 1999/12/31 00:00:00
    >>> j
    2451543.5
    """
    return tpm.jd2j(y2jd(y))

def y2y(y):
    """Simply returns the input.

    Inlcuded here, as it is defined in tpm/times.h.
    """
    return y

def ymd2j(ymd):
    """Convert Gregorian calendar date in YMD into a Julian date.

    :param ymd: Gregorian calendar year, month, day, hour, minutes, seconds
    :type ymd: :class:`pytpm.tpm.YMD`

    :return: Julian date
    :rtype: Float

    Convert Gregorian calendar date, stored as year, month, day, hour,
    minutes and second, in a :class:`pytpm.tpm.YMD` structure, into
    the correponding Julian date.
    
    >>> import tpm
    >>> ymd = j2ymd(tpm.gcal2j(2000,1,1))
    >>> ymd = tpm.ymd2ymd(ymd)
    >>> ymd2j(ymd)
    2451545.0
    """
    return tpm.jd2j(tpm.ymd2jd(ymd))

def ymd_diff(ymd1,ymd2):
    """Returns the difference between two Gregorian dates, in YMD, as a JD.

    :param ymd1: Gregorian calendar year, month, day, hour, minutes, seconds
    :type ymd1: :class:`pytpm.tpm.YMD`
    :param ymd2: Gregorian calendar year, month, day, hour, minutes, seconds
    :type ymd2: :class:`pytpm.tpm.YMD`

    :return: Julian date
    :rtype: :class:`pytpm.tpm.JD`

    Returns the difference bewteen two Gregorian calendar dates, given
    as :class:`pytpm.tpm.YMD` structures, as a :class:`pytpm.tpm.JD`
    structure.
    
    >>> import tpm
    >>> ymd1 = j2ymd(tpm.gcal2j(2000,1,1))
    >>> ymd2 = j2ymd(tpm.gcal2j(2001,1,1))
    >>> jd = ymd_diff(ymd2, ymd1)
    >>> fmt_jd(jd)
    '     366  00H 00M 00.000S'
    """
    return tpm.jd_diff(tpm.ymd2jd(ymd1),tpm.ymd2jd(ymd2))


# The following are macros from times.h header in TPM for accessing and
# modifying data in various data structures.
# Note that the fields of data structures are 'pointers' and hence
# modifying the data structures inside functions also modifies them in
# the calling scope.

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
