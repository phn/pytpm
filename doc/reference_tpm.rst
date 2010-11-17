=============
**pytpm.tpm** 
=============

.. TODO:: 
  Inlcude examples of macros and functions for V3 etc., and
  provide links to reference_utils for their signatures and other
  details.

.. automodule:: pytpm.tpm
..    :members:
..    :undoc-members:

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

IAU System of Astronomical Constants
------------------------------------

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

TPM state names
---------------

The targets or states in TPM are identified with integer constants:

=================  ==================================================
``N_TPM_STATES``    Number of TPM states.
 ``TPM_S00``        Null                                           
 ``TPM_S01``        Heliocentric mean FK4 system, any equinox      
 ``TPM_S02``        Heliocentric mean FK5 system, any equinox      
 ``TPM_S03``        IAU 1980 Ecliptic system                       
 ``TPM_S04``        IAU 1958 Galactic system                       
 ``TPM_S05``        Heliocentric mean FK4 system, B1950 equinox    
 ``TPM_S06``        Heliocentric mean FK5 system, J2000 equinox    
 ``TPM_S07``        Geocentric mean FK5 system, J2000 equinox      
 ``TPM_S08``        TPM_S07 + light deflection                     
 ``TPM_S09``        TPM_S08 + Aberration                           
 ``TPM_S10``        TPM_S09 + precession                           
 ``TPM_S11``        Geocentric apparent FK5, current equinox       
 ``TPM_S12``        Topocentric mean FK5, J2000 equinox            
 ``TPM_S13``        TPM_S12 + light definition                     
 ``TPM_S14``        TPM_S13 + aberration                           
 ``TPM_S15``        TPM_S14 + precession                           
 ``TPM_S16``        Topocentric apparent FK5, current equinox      
 ``TPM_S17``        Topocentric apparent FK5, current equnix       
 ``TPM_S18``        Topocentric apparent (Hour Angle, Declination) 
 ``TPM_S19``        Topecentric observed (Azimuth, Elevation)      
 ``TPM_S20``        Topocentric observed (Hour Angle, Declination) 
 ``TPM_S21``        Topocentric observed WHAM (longitude, latitude)
=================  ==================================================

Some of the targets have special names:

========================   ===============
 ``TARGET_FK4``              ``TPM_S01``      
 ``TARGET_FK5``              ``TPM_S02``    
 ``TARGET_ECL``              ``TPM_S03``    
 ``TARGET_GAL``              ``TPM_S04``    
 ``TARGET_APP_HADEC``        ``TPM_S17``    
 ``TARGET_OBS_HADEC``        ``TPM_S20``    
 ``TARGET_APP_AZEL``         ``TPM_S18``    
 ``TARGET_OBS_AZEL``         ``TPM_S19``    
 ``TARGET_OBS_WHAM``         ``TPM_S21``    
 ``TARGET_HADEC``            ``TPM_S17``
 ``TARGET_TOP_AZEL``         ``TPM_S18``
========================   ===============

TPM transition names
--------------------

The transitions between different states that can be performed in TPM
are also coded as integer constants:

===============  ==========================================================
``N_TPM_TRANS``   Number of TPM transitions.
``TPM_T00``       Null transition.
``TPM_T01``       FK4 precession to B1950.
``TPM_T02``       FK5 precession to J2000.
``TPM_T03``       IAU 1980 ecliptic to FK5 equatorial.
``TPM_T04``       IAU 1958 galactic to FK4 B1950.
``TPM_T05``       IAU FK4 B1950 to FK5 J2000.
``TPM_T06``       Heliocentric parallax.
``TPM_T07``       Geocentric parallax.
``TPM_T08``       Light deflection.
``TPM_T09``       Aberration.
``TPM_T10``       Precession from FK5 J2000 to date, i.e., given epoch.
``TPM_T11``       Nutation.
``TPM_T12``       Earth's rotation.
``TPM_T13``       HA-Dec to Az-El.
``TPM_T14``       Refraction.
``TPM_T15``       WHAM coordinate system.
===============  ==========================================================

TPM data flags
--------------

These are the constants used to specify how the TPM data must be
setup. See pages 14 and 15 of the TPM manual.
 
=====================  ===================================================
 ``TPM_INIT``           Initialize.
 ``TPM_FAST``           Setup all calculations that are "fast".
 ``TPM_SLOW``	          Setup all calculation that are "slow".
 ``TPM_MEDIUM``         Setup all calculations that take "medium" amount.
                        of time.
 ``TPM_REFRACTION``     Setup refraction calculations.
 ``TPM_ALL``	          Setup all calculations.
=====================  ===================================================

Miscellaneous constants
-----------------------

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

TPM data types and functions for manipulating them
==================================================

TPM defines C structures to represent entities such as vectors,
matrices and other. These are exposed as classes in PyTPM. Several
functions are provided for manipulating these and are described
below. As mentioned before, several C macros are provided in TPM for
working with data types, in addition to functions, and implementations
of these macros as python functions are available in
:mod:`pytpm.utils`.


Classes for vectors and matrices
--------------------------------

There are two classes, ``V3`` and ``V6``, for representing vectors. 

``V3`` is used for representing 3D coordinates and 3D velocities of an
astronomical object. This can be either spherical or cartesion
coordinates, indicated using the attribute ``type`` of a ``V3``
instance; ``type == tpm.CARTESION`` for the former and ``type ==
tpm.SPHERICAL`` for the latter.

.. TODO:: Link to section on v3 macros in reference_utils.

.. autoclass:: V3
    :members:

The class ``V6`` is used to represent a "six-vector" as opposed to a
"three-vector" represented using ``V3``. A ``V6`` instance uses two
``V3`` instances to store the coordinates and velocities of an
astronomical object. The two element array attribute ``v``, stores the
``V3`` instance representing coordinates in ``v[tpm.POS]`` and the
``V3`` instance representing velocities in ``v[tpm.VEL]``, where
``tpm.POS == 0`` and ``tpm.VEL == 1``. The ``type`` attribute sets the
type of the coordinate system; it is set equal to the ``type``
attribute of ``v[tpm.POS]``.


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

