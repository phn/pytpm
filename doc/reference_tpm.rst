=============
**pytpm.tpm** 
=============

.. contents::

.. automodule:: pytpm.tpm
    :members:
    :undoc-members:

Constants
=========

The following are the various constants defined in ``pytpm.tpm``. Note
that in TPM, and hence in PyTPM, *all Julian Day numbers are in the
UTC time system*.

Constants related to coordinate systems
---------------------------------------

These constants define the galactic coordinate system, relative to the
equatorial system of equinox B1950.0. See `this ADS page`__ for more
information. 

__ http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?
   bibcode=1959ApJ...130..702B&db_key=AST&page_ind=0&
   data_type=GIF&type=SCREEN_VIEW&classic=YES

==============  =======================================================
``GAL_RA``       Equatorial right ascension of the galatic pole, 
                 in degrees (B1950.0).
``GAL_DEC``      Equatorial declination of the galatic pole, in
                 degrees (B1950.0).
``GAL_LON``      Zero of longitude (B1950.0)
==============  =======================================================

Astrometry constants
--------------------

The following are constants that can be used to select FK4 and FK5
precession angles. The first 4 are FK4 angles and the final one is the
"One True FK5" set of angles.

See Aoki et al., 1983, Astornomy and Astrophysics 128, 263.

=======================	 ==================================================
``PRECESS_NEWCOMB``				0; Aoki eqs 9a-c, ES 1961.
``PRECESS_ANDOYER``				1; Aoki eqs 8a-c, Andoyer 1911.
``PRECESS_KINOSHITA``			2; Aoki eqs 10a-c, Kinoshita 1975.
``PRECESS_LIESKE``				3; Aoki eqs 11a-c, Lieske 1967.		 
``PRECESS_FK4``						Same as ``PRECESS_KINOSHITA``.										 
``PRECESS_FK5``						4; ES 1992, Lieske 1979, 1977.
``PRECESS_INERTIAL``			0; Flag to indicate inertial precession frame.
``PRECESS_ROTATING``			1; Flag to indicate non-inertial precess frame.	 
=======================	 ==================================================


Time and date related constants
-------------------------------

==============  =======================================================
``MJD_0``        JD of the modified JD system.
``B1950``        JD of epoch B1950.0.
``J2000``        JD of epoch J2000.0.
``J1984``        JD of 1984.0, the magic FK4/FK5 conversion time.
``CB``           Number of days in a tropical century at epoch 1900.0.
``CJ``           Number of days in a Julian century.
==============  =======================================================

IAU Sytem of Astronomical Constants
-----------------------------------

The following table lists constants from the IAU (1976) System of
Astronomical Constants, obtained from the Astronomical Almanac, 1984
p.K6.

==============  =======================================================
``IAU_K``        Gaussian gravitational constant.
``IAU_DM``       Distance of moon, in meters.
``IAU_AU``       Astronomical unit, in meters.
``IAU_C``        Speed of light, in meters/second.
``IAU_RE``       Radius of Earth, in meters.
``IAU_RM``       Radius if Moon, in meters.
``IAU_F``        Flattening factor of Earth.
``IAU_KAPPA``    Constant of aberration.
``IAU_W``        Rotational velocity of the Earth in radians/second.
==============  =======================================================

Miscellaneous constants
------------------------

==============  =======================================================
``POS``          Index of position vector in a :class:`V6` instance.
``VEL``          Index of velocity vector in a :class:`V6` instance.
``CARTESIAN``    Numerical value 0; indicates type of a :class:`V3` 
                 instance.
``SPHERICAL``    Numerical value 1; indicates type of a :class:`V3` 
                 instance.
``POLAR``        Same as ``SPHERICAL``.
``SUNDAY``       Start of week, numerical value of 0.
``MONDAY``       Numerical value 1.
``TUESDAY``      Numerical value 2.
``WEDNESDAY``    Numerical value 3.
``THURSDAY``     Numerical value 4.
``FRIDAY``       Numerical value 5.
``SATURDAY``     Numerical value 6.
==============  =======================================================

Classes for vectors and matrices
--------------------------------

.. autoclass:: V3
    :members:

.. autoclass:: V6
    :members:

.. autoclass:: M3
    :members:

.. autoclass:: M6
    :members:

Classes for dates, times and angles
-----------------------------------

The class **DMS** is used to represent an angle. It hold has three
data attributes: ``dd``, ``mm`` and ``ss``. These represent, degrees,
arc-minutes and arc-seconds in an angle, respectively. All three are
floating point numbers.

.. autoclass:: DMS
    :members:   

There are three classes that represent time in different
formats. These are **HMS**, **YMD**, and **JD**.

The class **HMS** stores time as hours, minutes and seconds, in
floating point data attributes ``hh``, ``mm`` and ``ss``,
respectively.

.. autoclass:: HMS
    :members:

For a given date, the class **YMD** stores the year and month in the
integer attibutes ``y`` and ``mm``, respectively. It stores the day
part in the floating point attribute ``dd``. **YMD** uses an instance
of :class:`HMS`, ``hms``, to store the hours, minutes and seconds part of
the time.

.. autoclass:: YMD
    :members:

The third class **JD** stores time as a ``Julian Day number``. It has
a floating point attribute ``dd`` that stores the day part of the
``Julian Date`` and an instance of :class:``HMS`` to store the hours,
minutes and seconds, i.e., the fractional part of the ``Julian day
number``.

.. autoclass:: JD
    :members:

