=============
**pytpm.tpm** 
=============

.. contents::

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

TPM data types
==============

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

In TPM a ``V3`` vector is used to store 3D positions and velocities of
an object. If the vector is cartesian, then we refer to ``v3[0]`` as
``x``, ``v3[1]`` as ``y`` and ``v3[2]`` as ``z``. If the vector is
spherical, then we refer to ``v3[0]`` as ``R``, ``v3[1]`` as ``Alpha``
and ``RA`` and ``v3[2]`` as ``Delta`` and ``Dec``.

These names are used in functions for manipulating these vectors. For
example the function that returns the ``R`` value of a position vector
is named ``GetRf``.

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

The naming scheme used for ``V3`` instances, i.e., ``R`` for the first
element of the position vector, is also valid for ``V6``
instances. For example, ``v6[tpm.POS][0]`` is refered to as ``X`` in
the case of cartesian coordinates and as ``R`` in the case of
spherical coordinates. 

For the velocity vector, we use a different naming scheme. For
cartesian velocity vectors, ``XDot`` refers to ``v6[tpm.VEL][0]``,
``YDOT`` refers to ``v6[tpm.VEL]`` and ``ZDot`` refers to
``v6[tpm.VEL]``. For spherical velocity vectors, ``RDot`` refers to
``v6[tpm.VEL][0]``, ``AlphaDot`` and ``PMRA`` refers to
``v6[tpm.VEL][1]``, and ``DeltaDot`` and ``PMDec`` refer to
``v6[tpm.VEL][2]``.

.. autoclass:: V6
    :members:

The class ``M3`` represents a matrix. It consists of a 3x3 array
attribute ``m``, each element of which is a floating point number.

.. autoclass:: M3
    :members:

``M6`` is a class for representing a rotation matrix that converts
both coordinates and velocities at the same time. It is defined in
REFERENCE. It has a 2x2 array attribute ``m``, each element of which
hold a ``M3`` instance.

.. autoclass:: M6
    :members:


Classes for date, time and angle
--------------------------------

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

Miscellaneous classes
---------------------

The class ``STAR`` can be used to represent a "catalog star". It has
three floating point data attributes, ``a``, ``d`` and ``m``,
representing the right ascension, declination and magnitude of a
star, respectively.

.. autoclass:: STAR
    :members:

The class ``CONS`` represens a "line segment" between two stars. It
has four floating point data attributes, ``a1``, ``d1``, ``a2`` and
``d2``, representing the coordinates of the two stars involved.

.. autoclass:: CONS
    :members:

Classes representing TPM states
-------------------------------

The class ``TPM_TARGET`` describes a target. Following are the
attributes of this class:

.. TODO:: What is offset?

============== ==============================================
 ``name``       Name of the target.
 ``state``      Integer constant identifying the state.
 ``epoch``      Epoch for this state in Julian day number.
 ``equinox``    Equinox for this state in Julian day number.
 ``position``   Spherical coordinates in radians.
 ``offset``     Offset in radians.
 ``motion``     Proper motion in radians/day.
 ``parallax``   Parallax in arcsec.
 ``speed``      Space velocity in AU/day.
============== ==============================================

.. autoclass:: TPM_TARGET
    :members:


The "boresight" of a telescope is represented using the class
``TPM_BORESIGHT``:

.. autoclass:: TPM_BORESIGHT
    :members:

``TPM_PMCELL`` is an utility class used by TPM:

.. autoclass:: TPM_PMCELL
    :members:

The state of the "telescope" is represented by the class
``TPM_TSTATE``. The following are the properties that define the state
of the telescope:

================  =========================================================
``utc``            Coordinated Univeral Time in Julian Day numbers
``delta_at``       UTC + delta_at = TAI, International Atomic Time
``delta_ut``       UTC + delta_ut = UT1, Universal Time
``lon``            East geographic longitude in radians
``lat``            North geographic latitude in radians, negative for South
``alt``            Altitude above the geoid in meters
``xpole``          Polar motion in radians
``ypole``          Polar motion in radians
``T``              Ambient Temperature in Kelvins
``P``              Ambient pressure in millibars
``H``              Ambient humidity (0 - 1)
``wavelength``     Oberving wavelength in microns
``tai``            International Atomic Time
``tdt``            Terrestrial Dynamic Time
``tdb``            Barycentric Dynamic Time
``obliquity``      Obliquity of the ecliptic
``nut_lon``        Nutation in longitude
``nut_obl``        Nutation in the obliquity
``nm``             Nutation matric for *now*
``pm``             Precession matric from J2000 to *now*
``ut1``            Universal Time
``gmst``           Greenwich Mean Sidereal Time
``gast``           Greenwich Apparent Sidereal Time
``last``           Local Apparent Sidereal Time
``eb``             Barycentric Earth state vector
``eh``             Heliocentric Earth state vector
``obs_m``          Geocentric Earth-fixed state vector, mean pole
``obs_t``          Geocentric Earth-fixed state vector, true pole
``obs_s``          Geocentric space-fixed state vector
``refa``           Refraction coefficient
``refb``           Refraction coefficient
================  =========================================================

.. autoclass:: TPM_TSTATE
    :members:


TPM functions
=============

TPM comes with functions and macros, for manipulating vectors and
matrices, calculating date and time, formating angles and several
others purposes. As mentioned before, most of the macros are defined
as functions in :mod:`pytpm.utils``. Macros for working with vectors
and matrices are implemented as function in :mod:`pytpm.tpm`, with the
character "f" added to the end of the macro name.

Here we will list the functions and macros in :mod:`pytpm.tpm`. See
:mod:`pytpm.utils` for the macros.


Functions for manipulating vectors and matrices
-----------------------------------------------

V3 vector
~~~~~~~~~

See the section on :class:`V3` for information on the fields of a V3
instance. 

To intialize a V3 instance, with all fields set to 0, use the
``v3init`` function. This function takes an integer indicating the
type of the V3 instance and returns a V3 instance. In the case of the
velocity vector in a ``V6`` instance, we use a different naming
scheme. ``RDot

.. autofunction:: v3init  

To get a string representation of the vector, use the ``v3fmt``
function.

.. autofunction:: v3fmt   

For all the functions described below, the first argument must be a V3
instance. The second must be a scalar or another V3 instance,
depending on the type of operation.

The following functions can be used to set the components of a
:class:`V3` instance.  The appropriate field in the V3 instance is set
to the scalar provided.

.. autofunction:: v3SetAlphaf
.. autofunction:: v3SetDecf  
.. autofunction:: v3SetDeltaf
.. autofunction:: v3SetRAf   
.. autofunction:: v3SetRf    
.. autofunction:: v3SetTypef 
.. autofunction:: v3SetXf    
.. autofunction:: v3SetYf    
.. autofunction:: v3SetZf    

These functions return the value of the relevant component of the
vector.

.. autofunction:: v3GetAlphaf
.. autofunction:: v3GetDecf  
.. autofunction:: v3GetDeltaf
.. autofunction:: v3GetRAf   
.. autofunction:: v3GetRf    
.. autofunction:: v3GetTypef 
.. autofunction:: v3GetXf    
.. autofunction:: v3GetYf    
.. autofunction:: v3GetZf    

The following functions can be used to subtract a scalar from a
component of a :class:`V3` instance.

.. autofunction:: v3DecAlphaf       
.. autofunction:: v3DecDecf         
.. autofunction:: v3DecDeltaf       
.. autofunction:: v3DecRAf          
.. autofunction:: v3DecRf           
.. autofunction:: v3DecXf           
.. autofunction:: v3DecYf           
.. autofunction:: v3DecZf

Use the following functions to divide a component of a V3 instance
with a scalar.

.. autofunction:: v3DivAlphaf       
.. autofunction:: v3DivDecf         
.. autofunction:: v3DivDeltaf       
.. autofunction:: v3DivRAf        
.. autofunction:: v3DivRf    
.. autofunction:: v3DivXf    
.. autofunction:: v3DivYf    
.. autofunction:: v3DivZf    

The following functions can be used to add a scalar to a V3 vector.

.. autofunction:: v3IncAlphaf 
.. autofunction:: v3IncDecf   
.. autofunction:: v3IncDeltaf 
.. autofunction:: v3IncRAf    
.. autofunction:: v3IncRf     
.. autofunction:: v3IncXf     
.. autofunction:: v3IncYf     
.. autofunction:: v3IncZf     

Use the following functions to multiply a component of a V3 vector
with a scalar.

.. autofunction:: v3MulAlphaf 
.. autofunction:: v3MulDecf   
.. autofunction:: v3MulDeltaf 
.. autofunction:: v3MulRAf    
.. autofunction:: v3MulRf     
.. autofunction:: v3MulXf    
.. autofunction:: v3MulYf    
.. autofunction:: v3MulZf    


The ``v3alpha`` function returns the "Right Ascension", i.e., value in
``v3[1]``, normalized to the range [0 - 2*pi ). This function takes
only one argument, the V3 instance.

.. autofunction:: v3alpha    

The ``v3delta`` function returns the "Declination", i.e., value in
``v3[2]``, normalized to the range (-pi/2 - pi/2). This function takes
only one argument, the V3 instance.

.. autofunction:: v3delta 

The following functions convert between cartesian and spherical
representations of a V3 vector. Both take a V3 instance as their
argument and returns a new V3 instance.

.. autofunction:: v3c2s   
.. autofunction:: v3s2c   

The function ``v3cross`` returns the cross product and ``v3dot``
returns the dot product of two V3 vectors passed as arguments. Both
return a new V3 instance.

.. autofunction:: v3cross 
.. autofunction:: v3dot   

Function ``v3diff`` returns a V3 instance that stores the difference
between two V3 vectors. Function ``v3sum`` returns the sum of two V3
vectors.

.. autofunction:: v3diff  
.. autofunction:: v3sum   

To cacluate the "modulus" or "length" of a vector use the ``v3mod``
function. This function takes a V3 instance and returns a double.

.. autofunction:: v3mod   

To scale a V3 vector with a scalar use the ``v3scale`` function.

.. autofunction:: v3scale 

The ``v3unit`` function converts the given vector into a unit vector,
i.e., vector of "length" 1.

.. autofunction:: v3unit  

The ``v32v6`` functions sets the given V3 vector as the "position"
vector of a :class:``V6`` vector and returns the V6 vector. The type
of the V6 vector is set to that of the V3 vector.

.. autofunction:: v32v6

V6 vectors
~~~~~~~~~~

A :class:`V6` vector, has a type, indicating whether it is cartesian
or spherical, and a two element array of :class:`V3` vectors. The
first element, or more precisely, ``v6[tpm.POS]`` stores the position
vector and the second, more precisely, ``v6[tpm.VEL]`` stores the
velocity vector.

To initialize a ``V6`` vector, use the ``v6init`` function.

.. autofunction:: v6init        

To get a formatted string representation of the components of a ``V6``
vector use the ``v6fmt`` function.

.. autofunction:: v6fmt         

Use the following functions to set the various components of a ``V6``
instance. These take a ``V6`` instance as the first argument and a
scalar as the second argument.

.. autofunction:: v6SetAlphaDotf
.. autofunction:: v6SetAlphaf   
.. autofunction:: v6SetDecf     
.. autofunction:: v6SetDeltaDotf
.. autofunction:: v6SetDeltaf   
.. autofunction:: v6SetPMDecf   
.. autofunction:: v6SetPMRAf    
.. autofunction:: v6SetPosf     
.. autofunction:: v6SetRAf      
.. autofunction:: v6SetRDotf    
.. autofunction:: v6SetRf       
.. autofunction:: v6SetTypef    
.. autofunction:: v6SetVelf     
.. autofunction:: v6SetXDotf    
.. autofunction:: v6SetXf       
.. autofunction:: v6SetYDotf    
.. autofunction:: v6SetYf       
.. autofunction:: v6SetZDotf    
.. autofunction:: v6SetZf       

These functions retrieve the components of a ``V6`` instance. These
take a ``V6`` instance as their arguments.

.. autofunction:: v6GetAlphaDotf
.. autofunction:: v6GetAlphaf   
.. autofunction:: v6GetDecf     
.. autofunction:: v6GetDeltaDotf
.. autofunction:: v6GetDeltaf   
.. autofunction:: v6GetPMDecf   
.. autofunction:: v6GetPMRAf    
.. autofunction:: v6GetPosf     
.. autofunction:: v6GetRAf      
.. autofunction:: v6GetRDotf    
.. autofunction:: v6GetRf       
.. autofunction:: v6GetTypef    
.. autofunction:: v6GetVelf     
.. autofunction:: v6GetXDotf    
.. autofunction:: v6GetXf       
.. autofunction:: v6GetYDotf    
.. autofunction:: v6GetYf       
.. autofunction:: v6GetZDotf    
.. autofunction:: v6GetZf       

To subtract a scalar from a component of a ``V6`` vector, use the
following function. These take a ``V6`` instance as the first argument
and a scalar as the second argument. These return a new ``V6``
instance.

.. autofunction:: v6DecAlphaDotf      
.. autofunction:: v6DecAlphaf         
.. autofunction:: v6DecDecf           
.. autofunction:: v6DecDeltaDotf      
.. autofunction:: v6DecDeltaf         
.. autofunction:: v6DecPMDecf         
.. autofunction:: v6DecPMRAf          
.. autofunction:: v6DecRAf            
.. autofunction:: v6DecRDotf          
.. autofunction:: v6DecRf             
.. autofunction:: v6DecXDotf          
.. autofunction:: v6DecXf             
.. autofunction:: v6DecYDotf          
.. autofunction:: v6DecYf             
.. autofunction:: v6DecZDotf          
.. autofunction:: v6DecZf             

The following function can be used to divide a component with a
scalar. These take a ``V6`` instance as the first argument and a
scalar as the second argument. These return a new ``V6`` instance.

.. autofunction:: v6DivAlphaDotf      
.. autofunction:: v6DivAlphaf         
.. autofunction:: v6DivDecf           
.. autofunction:: v6DivDeltaDotf      
.. autofunction:: v6DivDeltaf         
.. autofunction:: v6DivPMDecf         
.. autofunction:: v6DivPMRAf          
.. autofunction:: v6DivRAf            
.. autofunction:: v6DivRDotf          
.. autofunction:: v6DivRf             
.. autofunction:: v6DivXDotf          
.. autofunction:: v6DivXf             
.. autofunction:: v6DivYDotf    
.. autofunction:: v6DivYf       
.. autofunction:: v6DivZDotf    
.. autofunction:: v6DivZf       

The following functions add a scalar to a component of a ``V6``
instance. These take a ``V6`` instance as the first argument and a
scalar as the second argument. These return a new ``V6`` instance.

.. autofunction:: v6IncAlphaDotf
.. autofunction:: v6IncAlphaf   
.. autofunction:: v6IncDecf     
.. autofunction:: v6IncDeltaDotf
.. autofunction:: v6IncDeltaf   
.. autofunction:: v6IncPMDecf   
.. autofunction:: v6IncPMRAf    
.. autofunction:: v6IncRAf      
.. autofunction:: v6IncRDotf    
.. autofunction:: v6IncRf       
.. autofunction:: v6IncXDotf    
.. autofunction:: v6IncXf       
.. autofunction:: v6IncYDotf    
.. autofunction:: v6IncYf       
.. autofunction:: v6IncZDotf    
.. autofunction:: v6IncZf       

Use these functions to multiply a component of a ``V6`` vector with a
scalar. These take a ``V6`` instance as the first argument and a
scalar as the second argument. These return a new ``V6`` instance.

.. autofunction:: v6MulAlphaDotf
.. autofunction:: v6MulAlphaf   
.. autofunction:: v6MulDecf     
.. autofunction:: v6MulDeltaDotf
.. autofunction:: v6MulDeltaf   
.. autofunction:: v6MulPMDecf   
.. autofunction:: v6MulPMRAf    
.. autofunction:: v6MulRAf      
.. autofunction:: v6MulRDotf    
.. autofunction:: v6MulRf       
.. autofunction:: v6MulXDotf    
.. autofunction:: v6MulXf       
.. autofunction:: v6MulYDotf    
.. autofunction:: v6MulYf       
.. autofunction:: v6MulZDotf    
.. autofunction:: v6MulZf       

To get the "RA" and "Dec" values in the position vector of a ``V6``
vector, normalized to [0 - 2pi) and (-pi/2 and pi/2), respectively,
use the functions ``v6alpha`` and ``v6delta``. 

.. autofunction:: v6alpha       
.. autofunction:: v6delta       

Use the following two functions to convert between cartesian and
spherical representations of a ``V6`` vector.

.. autofunction:: v6c2s         
.. autofunction:: v6s2c         

The cross product and dot product of two ``V6`` vector use ``v6cross``
and ``v6dot`` respectively.

.. autofunction:: v6cross       
.. autofunction:: v6dot         

To find the sum and difference of two ``V6`` vectors use ``v6sum`` and
``v6diff`` functions, respectively.

.. autofunction:: v6sum         
.. autofunction:: v6diff        

The  modulus or length of the position vector in a ``V6`` vector can
be calculated using the ``v6mod`` function.

.. autofunction:: v6mod         

The ``v6unit`` vector converts the position vector in a ``V6`` vector
into a unit vector.

.. autofunction:: v6unit        

A ``V6`` vector can be scaled , i.e., all components multiplied, with
a scalar using the ``v6scale`` function.

.. autofunction:: v6scale       


The ``v62v3`` function applies space motion to the position vector in
a ``V6`` vector. The veolcity components and multiplied with the time
interval provided and then the result is added to the corresponding
position component. The resulting ``V3`` position vector is returned.

.. autofunction:: v62v3

