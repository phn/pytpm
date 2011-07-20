=======================
 Introduction to PyTPM
=======================

.. _KPNO: http://www.noao.edu/kpno


PyTPM provides facilities for converting astronomical coordinates
between different coordinate systems. In addition it provides several
utility functions related to date and time, calendars, string
formatting and so on. In this document we will discuss some of the top
level functionality provided by PyTPM.

For a detailed list of functions and constants defined in PyTPM see the
section on :doc:`functions`. For detailed information on the data
structures defined in PyTPM, see the section
on :doc:`data_structures`. For an overview of TPM and comparison
between TPM and PyTPM see :doc:`conversions`.

Please read the :download:`TPM manual <TPM/tpm.pdf>` before using the
advanced facilities of PyTPM.

.. contents::

Facilities in TPM that are wrapped by PyTPM are provided in the
sub-module ``pytpm.tpm``. The ``pytpm.convert`` module contains the
function ``convert()``, that is a convenience function for performing
the most common type of coordinate conversion.

.. code-block:: python

    >>> import pytpm
    >>> from pytpm import tpm, convert

Convert astronomical coordinates between different systems
==========================================================

PyTPM can be used to convert *positions and velocities* in a given
astronomical coordinate system into another. Examples of doing this are
in the ``examples`` folder. You should read the TPM manual before
attempting to use these advanced features.

For the most common coordinate conversion, i.e., converting two angles
in one system into those in another system, a convenience function is
provided with PyTPM: ``pytpm.convert.convert()``.  

The signature of this function is

.. code-block:: python

     convert(ra, de,
            int s1=tpm.TPM_S06, int s2=tpm.TARGET_OBS_AZEL,
            double epoch=tpm.J2000, double equinox=tpm.J2000,
            double utc=tpm.J2000,
            double delta_at=tpm.delta_AT(tpm.J2000),
            double delta_ut=tpm.delta_UT(tpm.J2000),
            double lon=-111.598333,
            double lat=31.956389,
            double alt=2093.093,
            double xpole=0.0, double ypole=0.0,
            double T=273.15, double P=1013.25, double H=0.0,
            double wavelength=0.550)

.. autofunction:: pytpm.convert.convert 

The arguments to this function are given in the table below; all
arguments, except for the input angles, have defaults. Also note that
not all values are needed for many types of coordinate conversions.

+------------+----------------------------------------------------+
| Parameter  | Description                                        |
+============+====================================================+
| ra         | input RA like angle in degrees (RA, longitude, Az);|
|            | scalar or a list.                                  |
+------------+----------------------------------------------------+
| de         | input DE like angle in degrees (DE, latitude, El); |
|            | scalar or a list.                                  |
+------------+----------------------------------------------------+
| s1         | start state                                        |
+------------+----------------------------------------------------+
| s2         | end state                                          |
+------------+----------------------------------------------------+
| epoch      | epoch of the coordinates as a Julian date          |
+------------+----------------------------------------------------+
| equinox    | equinox of the coordinates as Julian date          |
+------------+----------------------------------------------------+
| utc        | time of "observation" as a Julian date;            |
|            | exact meaning depends on the type of conversion;   |
|            | defaults to the epoch J2000.0                      |
+------------+----------------------------------------------------+
| delta_ut   | UT1 - UTC in seconds.                              |
+------------+----------------------------------------------------+
| delta_at   | TAI - UTC in seconds.                              |
+------------+----------------------------------------------------+
| lon        | geodetic longitude in degrees                      |
+------------+----------------------------------------------------+
| lat        | geodetic latitude in degrees                       |
+------------+----------------------------------------------------+
| alt        | altitude in meters                                 |
+------------+----------------------------------------------------+
| xpole      | ploar motion in radians                            |
+------------+----------------------------------------------------+
| ypole      | ploar motion in radians                            |
+------------+----------------------------------------------------+
| T          | temperature in kelvin                              |
+------------+----------------------------------------------------+
| P          | pressure in milli-bars                             |
+------------+----------------------------------------------------+
| H          | relative humidity (0-1)                            |
+------------+----------------------------------------------------+
| wavelength | wavelength of observation in microns               |
+------------+----------------------------------------------------+

The default location is the KPNO_ observatory and the data is taken
from the TPM source code, to be consistent with it.

In TPM, and hence in PyTPM, a coordinate system is referred to as a
*state*. Each state is given a name, which is just an integer
constant. The state is defined by data in a state data structure
(*TSTATE* in PyTPM). There are 21 states, plus a "null" state. These
are given below. The states can be identified using integers or the
special integer constants.

+---------+------------------------------------------------+
| State   | Description                                    |
+=========+================================================+
| TPM_S00 | Null                                           |
+---------+------------------------------------------------+
| TPM_S01 | Heliocentric mean FK4 system, any equinox      |
+---------+------------------------------------------------+
| TPM_S02 | Heliocentric mean FK5 system, any equinox      |
+---------+------------------------------------------------+
| TPM_S03 | IAU 1980 Ecliptic system                       |
+---------+------------------------------------------------+
| TPM_S04 | IAU 1958 Galactic system                       |
+---------+------------------------------------------------+
| TPM_S05 | Heliocentric mean FK4 system, B1950 equinox    |
+---------+------------------------------------------------+
| TPM_S06 | Heliocentric mean FK5 system, J2000 equinox    |
+---------+------------------------------------------------+
| TPM_S07 | Geocentric mean FK5 system, J2000 equinox      |
+---------+------------------------------------------------+
| TPM_S08 | TPM_S07 + light deflection                     |
+---------+------------------------------------------------+
| TPM_S09 | TPM_S08 + Aberration                           |
+---------+------------------------------------------------+
| TPM_S10 | TPM_S09 + precession                           |
+---------+------------------------------------------------+
| TPM_S11 | Geocentric apparent FK5, current equinox       |
+---------+------------------------------------------------+
| TPM_S12 | Topocentric mean FK5, J2000 equinox            |
+---------+------------------------------------------------+
| TPM_S13 | TPM_S12 + light definition                     |
+---------+------------------------------------------------+
| TPM_S14 | TPM_S13 + aberration                           |
+---------+------------------------------------------------+
| TPM_S15 | TPM_S14 + precession                           |
+---------+------------------------------------------------+
| TPM_S16 | Topocentric apparent FK5, current equinox      |
+---------+------------------------------------------------+
| TPM_S17 | Topocentric apparent FK5, current equnix       |
+---------+------------------------------------------------+
| TPM_S18 | Topocentric apparent (Hour Angle, Declination) |
+---------+------------------------------------------------+
| TPM_S19 | Topocentric observed (Azimuth, Elevation)      |
+---------+------------------------------------------------+
| TPM_S20 | Topocentric observed (Hour Angle, Declination) |
+---------+------------------------------------------------+
| TPM_S21 | Topocentric observed WHAM (longitude, latitude)|
+---------+------------------------------------------------+

Some of these states have additional special names.

+-------------------+-------------------+
| Name              | State             |
+===================+===================+
| TARGET_FK4        |      (TPM_S01)    |  
+-------------------+-------------------+
| TARGET_FK5        |      (TPM_S02)    |
+-------------------+-------------------+
| TARGET_ECL        |      (TPM_S03)    |
+-------------------+-------------------+
| TARGET_GAL        |      (TPM_S04)    |
+-------------------+-------------------+
| TARGET_APP_HADEC  |      (TPM_S17)    |
+-------------------+-------------------+
| TARGET_OBS_HADEC  |      (TPM_S20)    |
+-------------------+-------------------+
| TARGET_APP_AZEL   |      (TPM_S18)    |
+-------------------+-------------------+
| TARGET_OBS_AZEL   |      (TPM_S19)    |
+-------------------+-------------------+
| TARGET_OBS_WHAM   |      (TPM_S21)    |
+-------------------+-------------------+


To convert RA and DE from FK5 (equinox and epoch J2000) to Galactic
coordinates, we execute:

.. code-block:: python

    >>> ra = 359.97907800
    >>> de = -65.57713200
    >>> from pytpm import tpm, convert
    >>> ra = 359.979087800
    >>> de = -65.57713200
    >>> l,b = convert.convert(ra, de, s1=tpm.TPM_S06, s2=tpm.TPM_S04)
    >>> l
    311.3003294489278
    >>> b
    -50.70581755128377
    >>> 

The following code converts the `coordinates of M100`_ between
different systems.

.. _coordinates of M100: http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=M100&submit=SIMBAD+search

.. code-block:: python

 >>> from pytpm import tpm, convert
  
 >>> # FK5 epoch=J2000, equinox=J2000 to Galactic coordinates epoch=J2000
 >>> ra2000 = tpm.HMS(hh=12,mm=22,ss=54.899).to_degrees()
 >>> de2000 = tpm.DMS(dd=15,mm=49,ss=20.57).to_degrees()
 >>> l,b = convert.convert(ra2000, de2000, s1=tpm.TPM_S06, s2=tpm.TPM_S04)
 >>> l,b
 (271.13613956177846, 76.89886897513605)

 >>> # FK4 epoch=B1950, equinox=B1950 to Galactic coordinates epoch=B1950
 >>> ra1950 = tpm.HMS(hh=12,mm=20,ss=22.94).to_degrees()
 >>> de1950 = tpm.DMS(dd=16, mm=5, ss=58.2).to_degrees()
 >>> l,b = convert.convert(ra1950, de1950, s1=tpm.TPM_S05, s2=tpm.TPM_S04)
 >>> l,b
 (271.13611058008075, 76.89892111282573)
  
 >>> # FK4 epoch=B1950 equinox=B1950 to FK5 epoch=J2000, equinox=J2000
 >>> ra,de = convert.convert(ra1950,de1950, s1=tpm.TPM_S05, s2=tpm.TPM_S06,
   ....:  equinox=tpm.B1950, epoch=tpm.B1950)
 >>> print tpm.HMS(d=ra), tpm.DMS(dd=de)
 12H 22M 54.895S +15D 49' 20.528"
  
 >>> # FK5 epoch=J2000, equinox=J2000 to FK4 epoch=B1950, equinox=B1950
 >>> ra,de = convert.convert(ra2000,de2000, s1=tpm.TPM_S06, s2=tpm.TPM_S05,
   ....:  epoch=tpm.J2000, equinox=tpm.J2000)
 >>> print tpm.HMS(d=ra), tpm.DMS(dd=de)
 12H 20M 22.935S +16D 05' 58.024"


Utility functions
=================

The following sections list a few examples of using the several utility
functions that come with PyTPM. These are simple interfaces to the
functions in TPM.

For a detailed list of functions defined in PyTPM see the section
on :doc:`functions`. 
  
Get the current *UTC* time as a *Julian date*
---------------------------------------------

.. code-block:: python

    >>> j = tpm.utc_now()
    >>> print j
    2455675.76791
    >>> js = tpm.fmt_j(j)
    >>> print js
     2455675  18H 25M 47.000S

The function ``tpm.utc_now()`` returns the current *UTC* time as a
*Julian day* number; accurate only to a second. The function
``tpm.fmt_j()`` returns a string representation of a *Julian
date*. Note that representing UTC as a Julian date leads to ambiguities
during leap seconds; UTC is not a contiguous time system.

Convert *Gregorian calendar* date into a *Julian date*
------------------------------------------------------

.. code-block:: python

    >>> j = tpm.gcal2j(2000,1,1)
    >>> print tpm.fmt_j(j)
     2451545  00H 00M 00.000S

Function ``tpm.gcal2j()`` converts a *Gregorian calendar* date, given
as ``YYYY``, ``MM``, ``DD``, into the corresponding *Julian date* for
midday, i.e., 12H 00M 00S, of that date. In short, it returns the
Julian day number for the Gregorian calendar date.

Convert a *Julian date* into a date in the *Gregorian calendar*
---------------------------------------------------------------

.. code-block:: python

    >>> j = tpm.gcal2j(2000,1,1)
    >>> d = tpm.j2gcal(j)
    >>> type(d)
        <type 'dict'>
    >>> len(d)
        3
    >>> print d
    {'y': 2000, 'dd': 1, 'm': 1}
    >>> print "{y}/{m}/{dd}".format(**d)
    2000/1/1

The function ``tpm.j2gcal()``, returns the date in the *Gregorian
calendar*, on which, the time corresponding to the given *Julian date*
occurs. The date is returned as a Python dictionary with the key 'y'
for year, 'm' for the month and 'dd' for the day.

Convert decimal degrees into *DMS* string
-----------------------------------------

.. code-block:: python

    >>> d = 12.3456
    >>> dms = tpm.DMS(dd=d)
    >>> print dms
    +12D 20' 44.159"
    >>> type(dms)
        <type 'pytpm.tpm.DMS'>
    >>> dms.dd, dms.mm, dms.ss
        (12.345599999999999, 0.0, 0.0)
    >>> dms.normalize()
    >>> dms.dd, dms.mm, dms.ss
        (12.0, 20.0, 44.159999999997268)
    >>> dms = tpm.DMS(dd=1.2345, mm=-12.34, ss=0.123)
    >>> print dms
    +01D 01' 43.922"
    >>> dms.dd, dms.mm, dms.ss
        (1.2344999999999999, -12.34, 0.123)
    >>> dms.normalize()
    >>> dms.dd, dms.mm, dms.ss
        (1.0, 1.0, 43.922999999999362)
    >>> import math
    >>> dms = tpm.DMS(r=math.pi)
    >>> print dms
    +180D 00' 00.000"
    >>> dms.dd, dms.mm, dms.ss
        (180.0, 0.0, 0.0)
    >>> dms = tpm.DMS(h=24.0)
    >>> dms.dd, dms.mm, dms.ss
        (360.0, 0.0, 0.0)
    >>> dms = tpm.DMS(h=12.5)
    >>> print dms
    +187D 30' 00.000"
    >>> dms.dd, dms.mm, dms.ss
        (187.5, 0.0, 0.0)

Angle in degrees, arc-minutes and arc-seconds can be represented using
the ``tpm.DMS`` class. The angle can be constructed in several ways.
Passing the keywords ``dd``, ``mm``, ``ss`` for degrees, arc-minutes
and arc-seconds respectively, will create a angle with the indicated
value. Passing the keyword ``r`` for angle in radians, will crate a
``DMS`` object with angle converted into degrees. Passing the keyword
``h`` for hours will convert the angle in hours into degrees. The
``normalize()`` method, will normalize the acr-minutes and arc-seconds
of the angle into the proper range.


..  LocalWords:  PyTPM pytpm TPM
