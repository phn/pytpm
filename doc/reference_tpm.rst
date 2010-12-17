===============
 **pytpm.tpm**
===============


.. automodule:: pytpm.tpm
..    :members:
..    :undoc-members:

.. contents::

Constants
=========

The following are the various constants defined in ``pytpm.tpm``. Note
that in TPM, and hence in PyTPM, *all Julian dates are in the UTC time
system*.

Constants defining the Galactic coordinate system
-------------------------------------------------

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

.. _tpm_fk4_fk5_precess_angles:

Constants for selecting FK4 and FK5 precession angles
-----------------------------------------------------

The following are constants that can be used to select FK4 and FK5
precession angles. The first 4 are FK4 angles and the final one is the
"One True FK5" set of angles.

See Aoki et al., 1983, Astronomy and Astrophysics 128, 263.

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

.. _tpm_states:

TPM state names
---------------

The coordinate systems in TPM are identified with integer constants,
referred to as states:

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

Some of the states have special names:

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

.. _tpm_trans_names:

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

.. _tpm_data_flags:

TPM data flags
--------------

These are the constants used to specify how the TPM data must be
setup. See pages 14 and 15 of the TPM manual. These flags are passed
to the :func:`pytpm.tpm.tpm_data` function to set various properties
of the TPM state.
 
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

TPM defines C structures to represent entities such as vectors and
matrices. These are exposed as classes in PyTPM. Several functions are
provided for manipulating these and are described below.  C macros
provided in TPM, for working with data types, are implemented as
Python functions and are available in :mod:`pytpm.utils`.


Classes for vectors and matrices
--------------------------------

There are two classes, ``V3`` and ``V6``, for representing vectors. 

.. _v3_vector:

``V3`` vectors
~~~~~~~~~~~~~~

``V3`` is used for representing 3D coordinates and 3D velocities of an
astronomical object. This can be either in spherical or in cartesion
coordinates. The type of a vector is indicated using the attribute
``type`` of a ``V3`` instance; ``type == tpm.CARTESIAN`` for the
former type and ``type == tpm.SPHERICAL`` for the latter type.

If the vector is cartesian, then we refer to ``v3[0]`` as ``X``,
``v3[1]`` as ``Y`` and ``v3[2]`` as ``Z``. If the vector is spherical,
then we refer to ``v3[0]`` as ``R``, ``v3[1]`` as ``Alpha`` or ``RA``,
and ``v3[2]`` as ``Delta`` or ``Dec``.

These names are used in functions for manipulating these vectors. For
example, the function that returns the ``R`` value of a position vector
is named ``GetRf``. See section on functions for manipulating
:ref:`v3_func_manip_vec_mat` for more information on these function.

.. autoclass:: V3
    :members:

.. _v6_vector:

``V6`` vectors
~~~~~~~~~~~~~~

The class ``V6`` is used to represent a "six-vector" as opposed to a
"three-vector" represented using ``V3``. A ``V6`` instance uses two
``V3`` instances to store the coordinates and velocities of an
astronomical object. The two element array attribute ``v``, stores the
``V3`` instances. The ``V3`` vector representing position coordinates
is kept in ``v[tpm.POS]`` and the ``V3`` instance representing
velocities is kept in ``v[tpm.VEL]``. By default, ``tpm.POS == 0`` and
``tpm.VEL == 1``; do not change these defaults.

The ``type`` attribute of a ``V6`` instance sets the type of the
coordinate system of both position and velocity vectors; it is set
equal to the ``type`` attribute of ``v[tpm.POS]``.

The naming scheme used for ``V3`` instances, i.e., ``R`` for the first
element of the position vector, is also valid for ``V6``
instances. For example, ``v6[tpm.POS][0]`` is refered to as ``X`` in
the case of cartesian coordinates and as ``R`` in the case of
spherical coordinates. 

For the velocity vector, we use a different naming scheme. For
cartesian velocity vectors, ``XDot`` refers to ``v6[tpm.VEL][0]``,
``YDot`` refers to ``v6[tpm.VEL][1]`` and ``ZDot`` refers to
``v6[tpm.VEL][2]``. For spherical velocity vectors, ``RDot`` refers to
``v6[tpm.VEL][0]``, ``AlphaDot`` and ``PMRA`` refers to
``v6[tpm.VEL][1]``, and ``DeltaDot`` and ``PMDec`` refer to
``v6[tpm.VEL][2]``.

See section on functions for manipulating :ref:`v6_func_manip_vec_mat`
for more information on these function.

.. autoclass:: V6
    :members:

.. _m3_matrix:

``M3`` matrices
~~~~~~~~~~~~~~~

The class ``M3`` represents a matrix. It consists of a 3x3 array
attribute ``m``, each element of which is a floating point
number. This class is used for representing a rotation matrix, "R",
for ``V3`` vectors.

.. autoclass:: M3
    :members:

See section on functions for manipulating :ref:`m3_func_manip_vec_mat`
for more information on these function.

.. _m6_matrix:

``M6`` matrices
~~~~~~~~~~~~~~~

A ``M6`` class consists of a 2x2 array, each element of which is a
``M3`` matrix. This class is used to create a "Q" matrix, that can be
used to rotate, or transform, position and velocity vectors from one
coordinate system to another at the same time; a rotation matrix for
`V6` vectors.

.. autoclass:: M6
    :members:

See section on functions for manipulating :ref:`m6_func_manip_vec_mat`
for more information on these function.

Classes for angles, time and dates
----------------------------------

.. _dms_structure:

``DMS`` structures
~~~~~~~~~~~~~~~~~~

The class ``DMS`` is used to represent an angle. It hold has three
data attributes: ``dd``, ``mm`` and ``ss``. These represent, degrees,
arcminutes and arcseconds in an angle, respectively. All three are
floating point numbers. The :ref:`section on functions for Angles
<d_and_dms_func>` lists some functions for manipulating and formating
angles and ``DMS`` structures.

.. autoclass:: DMS
    :members:   

.. _time_and_date_structure:

Time and date structures
~~~~~~~~~~~~~~~~~~~~~~~~

There are three classes that represent time in different
formats. These are ``HMS``, ``YMD``, and ``JD``.

.. _hms_structure:

``HMS`` structures
++++++++++++++++++

The class ``HMS`` stores time as hours, minutes and seconds, in
floating point data attributes ``hh``, ``mm`` and ``ss``,
respectively. See :ref:`functions for manipulating time and HMS
structures <h_and_hms_func>`.

The section, :ref:`dms_and_hms_func`, describes functions that can be
used to convert between ``DMS`` and ``HMS`` structures.

.. autoclass:: HMS
    :members:

.. _ymd_structure:

``YMD`` structures
++++++++++++++++++

For a given date, the class ``YMD`` stores the year and month in the
integer attibutes ``y`` and ``mm``, respectively. It stores the day
part in the floating point attribute ``dd``. In addition, ``YMD`` uses
an instance of :class:`HMS`, as attribute ``hms``, to store the hours,
minutes and seconds part of the time. 

.. autoclass:: YMD
    :members:

.. _jd_structure:

``JD`` structures
+++++++++++++++++

The third class ``JD`` stores date as a ``Julian date``. It has a
floating point attribute ``dd`` that stores the day part of the
``Julian date``, i.e., the ``Julian Day number``, and an instance of
the :class:``HMS``, in the attribute ``hms``, to store the hours,
minutes and seconds, i.e., the fractional part, of the ``Julian
date``.

.. autoclass:: JD
    :members:

See the section :ref:`date_func`, for more information on functions
that can be used to manipulate dates, including ``YMD`` and ``JD``
structures.

Classes representing TPM states
-------------------------------

TPM state vector
~~~~~~~~~~~~~~~~

The state of the telescope or observer is represented by the class
``TPM_TSTATE``. This state, in effect, defines the coordinate
frame. The following are the properties that define the state of the
telescope. These are divided into two categories: independent and
dependent. 

.. _indep_props_state_vector:

.. rubric:: Independent properties of TPM state vector

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
================  =========================================================

.. _dep_props_state_vector:

.. rubric:: Dependent properties of TPM state vector

================  =========================================================
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

The function :func:`pytpm.tpm.tpm_data` is used to initialize a TPM
state and for performing calulations that will set various dependent
properties of the state. The independent properties must be set
manually.

.. TODO:: Examples


Miscellaneous classes
---------------------

These are used internally by TPM for various purposes.

TPM_TARGET
~~~~~~~~~~

The class ``TPM_TARGET`` describes a target, i.e., an object for which
we want to apply coordinate transformations. Following are the
attributes of this class:

.. TODO:: What is offset?

============== ====================================================
 ``name``       Name of the target.
 ``state``      Integer constant identifying the state.
 ``epoch``      Epoch for this state in Julian day number.
 ``equinox``    Equinox for this state in Julian day number.
 ``position``   Spherical coordinates in radians; 2 element array
 ``offset``     Offset in radians; 2 element array
 ``motion``     Proper motion in radians/day; 2 element array
 ``parallax``   Parallax in arcsec.
 ``speed``      Space velocity in AU/day.
============== ====================================================

.. autoclass:: TPM_TARGET
    :members:

TPM_BORESIGHT
~~~~~~~~~~~~~

The "boresight" of a telescope is represented using the class
``TPM_BORESIGHT``:

.. autoclass:: TPM_BORESIGHT
    :members:

TPM_PMCELL
~~~~~~~~~~

``TPM_PMCELL`` is an utility class used by TPM:

.. autoclass:: TPM_PMCELL
    :members:

STAR
~~~~

The class ``STAR`` can be used to represent a "catalog star". It has
three floating point data attributes, ``a``, ``d`` and ``m``,
representing the right ascension, declination and magnitude of a
star, respectively.

.. autoclass:: STAR
    :members:

CONS
~~~~

The class ``CONS`` represens a "line segment" between two stars. It
has four floating point data attributes, ``a1``, ``d1``, ``a2`` and
``d2``, representing the coordinates of the two stars involved.

.. autoclass:: CONS
    :members:


TPM functions
=============

TPM comes with functions and macros, for manipulating vectors and
matrices, calculating date and time, formating angles and several
others purposes.  

All constants and functions defined in TPM are available in
:mod:`pytpm.tpm`. In TPM macros for working with vectors and matrices
are implemented in ``v3.h``, ``v6.h``, ``m3.h`` and ``m6.h``. In
PyTPM, these are implemented as function in ``pytpm.tpm``. The
function names are constructed by adding the character "f" to the end
of the macro name.

Module ``pytpm.tpm`` also contains the function
:func:`pytpm.tpm.convert` for performing coordinate conversions. This
function is not present in TPM. But see :func:`pytpm.utils.convert`
for a more user friendly version of this function.

As mentioned before, all the other macros in TPM are defined as
functions in :mod:`pytpm.utils``.

.. _tpm_convert_func:

The ``convert`` function
------------------------


This function takes as input the ``X`` and ``Y`` coordinates, i.e.,
``RA`` and ``DEC`` or latitude and longitude, and all the
:ref:`independent variables of the TPM state vector
<indep_props_state_vector>`. It initializes the state vector, sets the
independent properties and caclulates all the :ref:`dependent
properties <dep_props_state_vector>`. It then call the TPM state
machine and performs the coordinate conversion requested. The
resultant values are returned.

This is a direct interface to the C function, ``convert``, and hence
all arguments must be provided in the proper order. Function
:func:`pytpm.utils.convert` on the other hand, is a Python function
that accepts keyword arguments and has default values for the
parameters. The default values are for KPNO observatory. This function
call ``pytpm.tpm.convert`` and takes care of providing all the
required arguments in the proper order.

For more details on how to use TPM to perform coordinate conversions
see the explanation and examples given in :func:``pytpm.utils.convert``.

The arguments expected by ``pytpm.tpm.convert`` are:

``x0``        The X coordinate; RA or longitude in radians
``y0``        The Y coordinate; DEC or latitude in radians
``s1``        Initial :ref:`TPM state <tpm_states>`; integer
``s2``        Final :ref:`TPM state <tpm_states>`; integer
``epoch``     Epoch of coordinate position; Julian date
``equinox``   Equinox of coordinate system; Julian date
``timetag``   Time of observation; Julian date


double x0, double y0, int s1, int s2, 
             double epoch, double equinox, double timetag,
             double lon, double lat, double alt,
             double T, double P, double H, 
             double W,

.. autofunction:: convert


.. _func_manip_vec_mat:

Functions for manipulating vectors and matrices
-----------------------------------------------

The following sections describe various functions that can be used for
manipulating :class:`V3` and :class:`V6` vectors and :class:`M3` and
:class:`M6` matrices.

.. _v3_func_manip_vec_mat:

V3 vectors
~~~~~~~~~~

See the section on :class:`V3` for information on the fields of a V3
instance. 

Initialize
++++++++++

To intialize a V3 instance, with all fields set to 0, use the
``v3init`` function. This function takes an integer indicating the
type of the V3 instance and returns a V3 instance.

.. autofunction:: v3init  

Formatted string representation
+++++++++++++++++++++++++++++++

To get a string representation of the vector, use the ``v3fmt``
function.

.. autofunction:: v3fmt   

For all the functions described below, the first argument must be a V3
instance. The second must be a scalar or another V3 instance,
depending on the type of operation.

Set the field values
++++++++++++++++++++

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

Retrieve the field values
+++++++++++++++++++++++++

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

Subtract a scalar from the field values
+++++++++++++++++++++++++++++++++++++++

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

Divide fields with  a scalar
++++++++++++++++++++++++++++

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

Add a scalar to field values
++++++++++++++++++++++++++++

The following functions can be used to add a scalar to a V3 vector.

.. autofunction:: v3IncAlphaf 
.. autofunction:: v3IncDecf   
.. autofunction:: v3IncDeltaf 
.. autofunction:: v3IncRAf    
.. autofunction:: v3IncRf     
.. autofunction:: v3IncXf     
.. autofunction:: v3IncYf     
.. autofunction:: v3IncZf     

Multiply fields with a scalar
+++++++++++++++++++++++++++++

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

Return normalized right ascension
+++++++++++++++++++++++++++++++++

The ``v3alpha`` function returns the "Right Ascension", i.e., value in
``v3[1]``, normalized to the range [0 - 2*pi ). This function takes
only one argument, the V3 instance.

.. autofunction:: v3alpha    

Return normalized declination
+++++++++++++++++++++++++++++

The ``v3delta`` function returns the "Declination", i.e., value in
``v3[2]``, normalized to the range (-pi/2 - pi/2). This function takes
only one argument, the V3 instance.

.. autofunction:: v3delta 

Convert between cartesian and spherical
+++++++++++++++++++++++++++++++++++++++

The following functions convert between cartesian and spherical
representations of a V3 vector. Both take a V3 instance as their
argument and returns a new V3 instance.

.. autofunction:: v3c2s   
.. autofunction:: v3s2c   

Cross product and dot product
+++++++++++++++++++++++++++++

The function ``v3cross`` returns the cross product and ``v3dot``
returns the dot product of two V3 vectors passed as arguments. Both
return a new V3 instance.

.. autofunction:: v3cross 
.. autofunction:: v3dot   

Sum and difference of two vectors
+++++++++++++++++++++++++++++++++

Function ``v3diff`` returns a V3 instance that stores the difference
between two V3 vectors. Function ``v3sum`` returns the sum of two V3
vectors.

.. autofunction:: v3diff  
.. autofunction:: v3sum   

Modulus
+++++++

To cacluate the "modulus" or "length" of a vector use the ``v3mod``
function. This function takes a V3 instance and returns a double.

.. autofunction:: v3mod   

Scale fields with a scalar
++++++++++++++++++++++++++

To scale a V3 vector with a scalar use the ``v3scale`` function.

.. autofunction:: v3scale 

Unit vector
+++++++++++

The ``v3unit`` function converts the given vector into a unit vector,
i.e., vector of "length" 1.

.. autofunction:: v3unit  

Return position vector as a ``V6`` vector
+++++++++++++++++++++++++++++++++++++++++

The ``v32v6`` functions sets the given V3 vector as the "position"
vector of a :class:``V6`` vector and returns the V6 vector. The type
of the V6 vector is set to that of the V3 vector.

.. autofunction:: v32v6

.. _v6_func_manip_vec_mat:

V6 vectors
~~~~~~~~~~

A :class:`V6` vector, has a type, indicating whether it is cartesian
or spherical, and a two element array of :class:`V3` vectors. The
first element, or more precisely, ``v6[tpm.POS]`` stores the position
vector and the second, more precisely, ``v6[tpm.VEL]`` stores the
velocity vector.

Initialize
++++++++++

To initialize a ``V6`` vector, use the ``v6init`` function.

.. autofunction:: v6init        

Formatted string representation
+++++++++++++++++++++++++++++++

To get a formatted string representation of the components of a ``V6``
vector use the ``v6fmt`` function.

.. autofunction:: v6fmt         

Set field values
++++++++++++++++

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

Get field values
++++++++++++++++

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

Subtract scalars from field values
++++++++++++++++++++++++++++++++++

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

Divide field values with a scalar
+++++++++++++++++++++++++++++++++

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

Add a scalar to field values
++++++++++++++++++++++++++++

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

Multiply field values with a scalar
+++++++++++++++++++++++++++++++++++

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

Retrive normalized RA and Dec
+++++++++++++++++++++++++++++

To get the "RA" and "Dec" values in the position vector of a ``V6``
vector, normalized to [0 - 2pi) and (-pi/2 and pi/2), respectively,
use the functions ``v6alpha`` and ``v6delta``. 

.. autofunction:: v6alpha       
.. autofunction:: v6delta       

Convert cartesian to spherical and vice-versa
+++++++++++++++++++++++++++++++++++++++++++++

Use the following two functions to convert between cartesian and
spherical representations of a ``V6`` vector.

.. autofunction:: v6c2s         
.. autofunction:: v6s2c         

Cross product and dot product
+++++++++++++++++++++++++++++

The cross product and dot product of two ``V6`` vector use ``v6cross``
and ``v6dot`` respectively.

.. autofunction:: v6cross       
.. autofunction:: v6dot         

Sum and difference
++++++++++++++++++

To find the sum and difference of two ``V6`` vectors use ``v6sum`` and
``v6diff`` functions, respectively.

.. autofunction:: v6sum         
.. autofunction:: v6diff        

Modulus
+++++++

The  modulus or length of the position vector in a ``V6`` vector can
be calculated using the ``v6mod`` function.

.. autofunction:: v6mod         

Unit vector
+++++++++++

The ``v6unit`` vector converts the position vector in a ``V6`` vector
into a unit vector.

.. autofunction:: v6unit        

Scale field values with a scalar
++++++++++++++++++++++++++++++++

A ``V6`` vector can be scaled , i.e., all components multiplied, with
a scalar using the ``v6scale`` function.

.. autofunction:: v6scale       

Apply proper motion to position vector
++++++++++++++++++++++++++++++++++++++

The ``v62v3`` function applies space motion to the position vector in
a ``V6`` vector. The veolcity components and multiplied with the time
interval provided and then the result is added to the corresponding
position component. The resulting ``V3`` position vector is returned.

.. autofunction:: v62v3

.. _m3_func_manip_vec_mat:

M3 matrices
~~~~~~~~~~~

Scaled identity matrix and null matrix
++++++++++++++++++++++++++++++++++++++

Function ``m3I`` returns an identity ``M3`` matrix, scaled with the
given scalar. To construct a null matrix, use the function ``m3O``.
 
.. autofunction:: m3I     
.. autofunction:: m3O     

Formatted string representation
+++++++++++++++++++++++++++++++

Use the function ``m3fmt`` to get a formatted string containing the
elements of a matix.

.. autofunction:: m3fmt    

Set values
++++++++++

Use the following functions to set the various elements of a ``M3``
matrix.

.. autofunction:: m3SetXXf 
.. autofunction:: m3SetXYf 
.. autofunction:: m3SetXZf 
.. autofunction:: m3SetYXf 
.. autofunction:: m3SetYYf 
.. autofunction:: m3SetYZf 
.. autofunction:: m3SetZXf 
.. autofunction:: m3SetZYf 
.. autofunction:: m3SetZZf 

Retrive values
++++++++++++++

The following functions return the value of a particular component of
a matrix.

.. autofunction:: m3GetXXf
.. autofunction:: m3GetXYf
.. autofunction:: m3GetXZf
.. autofunction:: m3GetYXf
.. autofunction:: m3GetYYf
.. autofunction:: m3GetYZf
.. autofunction:: m3GetZXf
.. autofunction:: m3GetZYf
.. autofunction:: m3GetZZf

Subtract a scalar from a component
++++++++++++++++++++++++++++++++++

The following functions can be used to subtract a scalar from a
component of a matrix. These take a ``M3`` instance as their first
argument, a scalar as their second argument and returns a new ``M3``
instance.


.. autofunction:: m3DecXXf       
.. autofunction:: m3DecXYf       
.. autofunction:: m3DecXZf       
.. autofunction:: m3DecYXf       
.. autofunction:: m3DecYYf       
.. autofunction:: m3DecYZf       
.. autofunction:: m3DecZXf       
.. autofunction:: m3DecZYf       
.. autofunction:: m3DecZZf       

Divide a component with a scalar
++++++++++++++++++++++++++++++++

Use the following functions to divide a component with a scalar. These
take a ``M3`` instance as their first argument, a scalar as their
second argument and returns a new ``M3`` instance.

.. autofunction:: m3DivXXf       
.. autofunction:: m3DivXYf       
.. autofunction:: m3DivXZf        
.. autofunction:: m3DivYXf        
.. autofunction:: m3DivYYf        
.. autofunction:: m3DivYZf        
.. autofunction:: m3DivZXf       
.. autofunction:: m3DivZYf
.. autofunction:: m3DivZZf

Add a scalar to a component
+++++++++++++++++++++++++++

Use the following functions to add a scalar to a component of a
matrix. These take a ``M3`` instance as their first argument, a scalar
as their second argument and returns a new ``M3`` instance.

.. autofunction:: m3IncXXf
.. autofunction:: m3IncXYf
.. autofunction:: m3IncXZf
.. autofunction:: m3IncYXf
.. autofunction:: m3IncYYf
.. autofunction:: m3IncYZf
.. autofunction:: m3IncZXf
.. autofunction:: m3IncZYf
.. autofunction:: m3IncZZf

Multiply a component with a scalar
++++++++++++++++++++++++++++++++++

The following functions return a matrix with the component set to the
value obtained by multiplying the corresponding value in the input
matirx with a scalar.

.. autofunction:: m3MulXXf
.. autofunction:: m3MulXYf
.. autofunction:: m3MulXZf
.. autofunction:: m3MulYXf
.. autofunction:: m3MulYYf
.. autofunction:: m3MulYZf
.. autofunction:: m3MulZXf
.. autofunction:: m3MulZYf
.. autofunction:: m3MulZZf

Rotation matrices
+++++++++++++++++

The main use of ``M3`` matrices in TPM is for creating rotation
matrices. The following functions return rotation matrix about the
axis indicated. These functions take an angle, the rotation angle, as
their input.

.. autofunction:: m3Rx    
.. autofunction:: m3Ry     
.. autofunction:: m3Rz     

The following functions return the time derivative of the
corresponding rotation matrices. These functions take a rotation angle
and the time derivative of the rotation angle as inputs.

.. autofunction:: m3RxDot  
.. autofunction:: m3RyDot  
.. autofunction:: m3RzDot  

Sum and difference of matrices
++++++++++++++++++++++++++++++

The functions return the sum and difference of two matrices.

.. autofunction:: m3sum    
.. autofunction:: m3diff   

Inverse of an orthogonal matrix
+++++++++++++++++++++++++++++++

The functions return the inverse of a matrix, assuming that it is
orthogonal. 

.. autofunction:: m3inv    

Scale a matrix with a scalar
++++++++++++++++++++++++++++

The function ``m3scale`` return a ``M3`` martix with components set to
those obtained by multiplying the corresponding components of the
input matrix with a scalar.

.. autofunction:: m3scale  

Product of two ``M3`` matrices
++++++++++++++++++++++++++++++

The function ``m3v3`` returns a ``M3`` matrix that is the product of
two input matrices.

.. autofunction:: m3m3     

Product of a ``M3`` matrix with a ``V3`` matrix
+++++++++++++++++++++++++++++++++++++++++++++++

The function ``m3v3`` returns a ``V3`` vector that is the product of a
``M3`` matrix with a ``V3`` vector.

.. autofunction:: m3v3     

Product of a ``M3`` matrix with a ``V6`` matrix
+++++++++++++++++++++++++++++++++++++++++++++++

The function ``m3v6`` returns a ``V6`` vector, obtained by multiplying
the velocity and position components of the input ``V6`` vecctor with
the input ``M3`` matrix.

.. autofunction:: m3v6     

.. _m6_func_manip_vec_mat:

M6 matrices
~~~~~~~~~~~

Scaled iDentity matrix and null matrix
++++++++++++++++++++++++++++++++++++++

Function ``m6I`` returns an identity ``M6`` matrix, scaled with the
given scalar. To construct a null matrix, use the function ``m6O``.

.. autofunction:: m6I      
.. autofunction:: m6O      

Formatted string representation
+++++++++++++++++++++++++++++++

Use the function ``m6fmt`` to get a formatted string containing the
elements of a matix.

.. autofunction:: m6fmt   

Set values
++++++++++

Use the following functions to set the various elements of a ``M6``
matrix.

.. autofunction:: m6SetPPf 
.. autofunction:: m6SetPVf
.. autofunction:: m6SetVPf
.. autofunction:: m6SetVVf

Retrive values
++++++++++++++

The following functions return the value of a particular component of
a matrix.

.. autofunction:: m6GetPPf 
.. autofunction:: m6GetPVf 
.. autofunction:: m6GetVPf 
.. autofunction:: m6GetVVf 

The 6x6 rotation matrix
+++++++++++++++++++++++

The "Q" matrix is a 6x6 matrix that can be used to rotate position and
velocity vectors at the same time. The following functions return the
rotation matrices for the specified axis. They take as input the
rotation angle and the rate of change of the rotation angle.

The 6x6 matrix actual is composed of a 2x2 array, with each element of
the array being a ``M3`` matrix.

.. autofunction:: m6Qx     
.. autofunction:: m6Qy     
.. autofunction:: m6Qz     

Sum and difference of matrices
++++++++++++++++++++++++++++++

The functions return the sum and difference of two matrices.

.. autofunction:: m6sum   
.. autofunction:: m6diff  

Inverse of an orthogonal matrix
+++++++++++++++++++++++++++++++

The functions return the inverse of a matrix, assuming that the
component ``M3`` matrices are orthogonal.

.. autofunction:: m6inv   

Scale a matrix with a scalar
++++++++++++++++++++++++++++

The function ``m6scale`` return a ``M6`` martix with each of the
``M3`` matrix component in the ``M6`` matrix scaled with the given
constant.

.. autofunction:: m6scale 

Product of two ``M6`` matrices
++++++++++++++++++++++++++++++

Function ``m6m6`` returns a ``M6`` matrix obtained by taking the
product of two ``M6`` matrices. The matrix is obtained by following
the same procedures used in regular matrix multiplication, but the
multiplications and additions are between ``M3``.

.. autofunction:: m6m6    

Product of a ``M6`` matrix with a ``V3`` matrix
+++++++++++++++++++++++++++++++++++++++++++++++

The function ``m6v3`` returns a ``V3`` vector that is the product of
the "PP" component, i.e., m6[0][0], of the ``M6`` matrix and a ``V3``
vector.

.. autofunction:: m6v3    

Product of a ``M6`` matrix with a ``V6`` vector
+++++++++++++++++++++++++++++++++++++++++++++++

The function ``m6v6`` returns a ``V6`` obtained by taking the product
of the given ``M6`` matrix and the given ``V6`` vector.

.. autofunction:: m6v6    

Functions related to angles, time and dates
-------------------------------------------

This section will discuss the functions that deal with calculation of
dates and time. Macros in TPM that deal with dates and time are
provided as functions, with the same name as that of the macros, in
:mod:`pytpm.utils`. Code samples shown below were copied from
`ipython` shell.

Angles
~~~~~~

.. _d_and_dms_func:

Function ``d2dms`` returns a :class:`DMS` with the given scalar set as
the value of the "degrees" part of the DMS structure. 

.. autofunction:: d2dms

.. sourcecode:: ipython

  In [2]: dms = tpm.d2dms(23.456)

  In [3]: dms.dd
  Out[3]: 23.456
   
  In [4]: dms.mm
  Out[4]: 0.0
   
  In [5]: dms.ss
  Out[5]: 0.0

The function ``dms2dms`` is used to normalize a :class:`DMS`
structure.

.. autofunction:: dms2dms

.. sourcecode:: ipython

  In [6]: dms = tpm.dms2dms(dms)
   
  In [7]: dms.dd
  Out[7]: 23.0
   
  In [8]: dms.mm
  Out[8]: 27.0
   
  In [9]: dms.ss
  Out[9]: 21.599999999998261

Functions ``dms_diff`` and ``dms_sum`` return a :class:`DMS` structure,
that correponds to the difference and sum between the given DMS
structures, repectively.

.. autofunction:: dms_sum
.. autofunction:: dms_diff

.. sourcecode:: ipython

  In [10]: dms1 = tpm.d2dms(23.4567)
   
  In [11]: dms2 = tpm.d2dms(13.1985)
   
  In [12]: dms = tpm.dms_diff(dms1, dms2)
   
  In [13]: dms.dd
  Out[13]: 10.258200000000002
   
  In [14]: dms.mm
  Out[14]: 0.0
   
  In [15]: dms.ss
  Out[15]: 0.0
   
  In [16]: dms = tpm.dms2dms(dms)
   
  In [17]: dms.dd
  Out[17]: 10.0
   
  In [18]: dms.mm
  Out[18]: 15.0
   
  In [19]: dms.ss
  Out[19]: 29.52000000000794

  In [20]: dms = tpm.dms_sum(dms1, dms2)
   
  In [21]: dms = tpm.dms2dms(dms)
   
  In [22]: dms.dd
  Out[22]: 36.0
   
  In [23]: dms.mm
  Out[23]: 39.0
   
  In [24]: dms.ss
  Out[24]: 18.720000000002415

To convert a :class:`DMS` to a scalar degree value, use the function
``dms2d``. 

.. autofunction:: dms2d

.. sourcecode:: ipython

  In [28]: print tpm.dms2d(dms)
  -------> print(tpm.dms2d(dms))
  36.6552

The function ``d2d`` can be used to normalize a scalar angle in
degrees to the range [0, 360].

.. autofunction:: d2d

.. sourcecode:: ipython
   
  In [29]: tpm.d2d(45.1234)
  Out[29]: 45.123399999999997
   
  In [30]: tpm.d2d(361.0)
  Out[30]: 1.0
   
  In [31]: tpm.d2d(-361.0)
  Out[31]: 359.0
   
  In [32]: tpm.d2d(-720.0)
  Out[32]: 0.0
   
  In [33]: tpm.d2d(-721.0)
  Out[33]: 359.0


The function ``fmt_d`` gives a formatted string representation of a
scalar angle in degrees. To format a :class:`DMS` structure use the
function :func:`pytpm.utils.fmt_dms`. To format an angle in radians
use the function :func:`pytpm.utils.fmt_r`.

.. autofunction:: fmt_d

.. sourcecode:: ipython

  In [26]: print tpm.fmt_d(23.4567)
  -------> print(tpm.fmt_d(23.4567))
  +23D 27' 24.120"
   
  In [27]: utils.fmt_dms(dms)
  Out[27]: '+36D 39\' 18.720"'

The function ``r2r`` can be used to normalize an angle in radians to
the range [0, 2π). 

.. autofunction:: r2r

.. sourcecode:: ipython

  In [34]: tpm.r2r(1.34)
  Out[34]: 1.3400000000000001
   
  In [35]: tpm.r2r(3.456)
  Out[35]: 3.456
   
  In [36]: tpm.r2r(2*3.456)
  Out[36]: 0.62881469282041369
   
  In [37]: tpm.r2r(2*tpm.M_PI)
  Out[37]: 0.0
   
  In [38]: tpm.r2r(-2*tpm.M_PI)
  Out[38]: 0.0
   
  In [39]: tpm.r2r(-2*tpm.M_PI+tpm.M_PI)
  Out[39]: 3.1415926535897931
   
  In [40]: tpm.r2r(-tpm.M_PI)
  Out[40]: 3.1415926535897931

The function ``fmt_delta`` converts an angle in radians into an angle
in degrees in the range [-90, 90]. This is useful, for example, in
normalizing a angle representing a declination coordinate.

.. autofunction:: fmt_delta

.. sourcecode:: ipython

  In [41]: tpm.fmt_delta(tpm.M_PI)
  Out[41]: '+00D 00\' 00.000"'
   
  In [42]: tpm.fmt_delta(-tpm.M_PI)
  Out[42]: '+00D 00\' 00.000"'
   
  In [43]: tpm.fmt_delta(-2*tpm.M_PI)
  Out[43]: '+00D 00\' 00.000"'
   
  In [44]: tpm.fmt_delta(tpm.M_PI/2)
  Out[44]: '+90D 00\' 00.000"'
   
  In [45]: tpm.fmt_delta(tpm.M_PI/4)
  Out[45]: '+45D 00\' 00.000"'
   
  In [46]: tpm.fmt_delta(-tpm.M_PI/4)
  Out[46]: '-45D 00\' 00.000"'

  In [48]: tpm.fmt_delta(utils.d2r(-91.0))
  Out[48]: '-89D 00\' 00.000"'
   
  In [49]: tpm.fmt_delta(utils.d2r(91.0))
  Out[49]: '+89D 00\' 00.000"'

`Some functions are provided <utils_angle_conv_functions>`_ in
:mod:`pytpm.utils` for converting angles between various units.

.. _h_and_hms_func:

The following are some functions for working with time. 

Functions ``h2hms`` and ``hms2h`` convert between scalar hours and
time stored in :class:`HMS` structure.

.. autofunction:: h2hms
.. autofunction:: hms2h

.. sourcecode:: ipython

  In [52]: hms = tpm.h2hms(12.5)
   
  In [53]: hms.hh
  Out[53]: 12.5
   
  In [54]: hms.mm
  Out[54]: 0.0
   
  In [55]: hms.ss
  Out[55]: 0.0
   
  In [56]: h = tpm.hms2h(hms)
   
  In [57]: h
  Out[57]: 12.5

Use the function ``hms2hms`` to normalize a :class:`HMS` structure and
the function ``h2h`` to normalize a scalar time in hours to the range
[0, 24.0).

.. autofunction:: hms2hms
.. autofunction:: h2h

.. sourcecode:: ipython

  In [58]: tpm.h2h(24.1)
  Out[58]: 0.10000000000000142
   
  In [59]: tpm.h2h(24)
  Out[59]: 0.0
   
  In [60]: hms = tpm.hms2hms(hms)
   
  In [61]: hms.hh
  Out[61]: 12.0
   
  In [62]: hms.mm
  Out[62]: 30.0
   
  In [63]: hms.ss
  Out[63]: 0.0


The functions ``hms_diff`` and ``hms_sum`` return a :class:`HMS`
structure containing the difference and sum of two ``HMS`` structures.

.. autofunction:: hms_diff
.. autofunction:: hms_sum

.. sourcecode:: ipython

  In [64]: hms1 = tpm.h2hms(12.345678)
   
  In [65]: hms2 = tpm.h2hms(9.7654321)
   
  In [66]: hms = tpm.hms_diff(hms1, hms2)
   
  In [67]: print hms.hh, hms.mm, hms.ss
  -------> print(hms.hh, hms.mm, hms.ss)
  (2.5802458999999995, 0.0, 0.0)
   
  In [68]: hms = tpm.hms2hms(hms)
   
  In [69]: print hms.hh, hms.mm, hms.ss
  -------> print(hms.hh, hms.mm, hms.ss)
  (2.0, 34.0, 48.885239999998333)
   
  In [70]: hms = tpm.hms2hms(tpm.hms_sum(hms1, hms2))
   
  In [71]: print hms.hh, hms.mm, hms.ss
  -------> print(hms.hh, hms.mm, hms.ss)
  (22.0, 6.0, 39.996359999991569)


The function ``fmt_h`` returns a formatted string representation of a
scalar time in hours. The function :func:`pytpm.utils.fmt_hms`` can be
used to format a :class:`HMS` structure.

.. autofunction:: fmt_h

.. sourcecode:: ipython

  In [74]: tpm.fmt_h(12.3456)
  Out[74]: ' 12H 20M 44.159S'
   
  In [75]: tpm.fmt_h(24.3456)
  Out[75]: ' 24H 20M 44.160S'


.. _dms_and_hms_func:

Converting between angles and time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions ``dms2hms`` and ``hms2dms`` can convert between angles in a
:class:`DMS` structure to time in a :class:`HMS` structure, assuming
24 hours = 360.0 degrees. The function ``fmt_alpha`` converts a scalar
angle in radians into time between [0, 24) hours and returns a
formatted string representing this time.

.. autofunction:: hms2dms
.. autofunction:: dms2hms
.. autofunction:: fmt_alpha

.. sourcecode:: ipython

  In [77]: tpm.fmt_alpha(tpm.M_PI)
  Out[77]: ' 12H 00M 00.000S'
   
  In [78]: tpm.fmt_alpha(2*tpm.M_PI)
  Out[78]: ' 00H 00M 00.000S'
   
  In [79]: dms = tpm.d2dms(23.45678)
   
  In [80]: utils.fmt_dms(tpm.dms2dms(dms))
  Out[80]: '+23D 27\' 24.407"'
   
  In [81]: hms = tpm.dms2hms(dms)
   
  In [82]: utils.fmt_hms(hms)
  Out[82]: ' 01H 33M 49.627S'

`Several functions are provided <utils_conv_angle_time>`_ in
:mod:`pytpm.utils` for converting between angles and time.

.. _date_func:

Dates
~~~~~

The function ``utc_now`` returns the current ``UTC`` date as a Julian
day number. This is accurate to the nearest second. The function
``jd_now`` returns the same, but the returned value is a :class:`JD
<pytpm.tpm.JD>` structure.

.. autofunction:: utc_now
.. autofunction:: jd_now

.. sourcecode:: python

  In [88]: tpm.utc_now()
  Out[88]: 2455530.1067824075

  In [98]: jd = tpm.jd_now()
   
  In [99]: jd.dd
  Out[99]: 2455530.1088657407
   
  In [100]: jd.hms.hh
  Out[100]: 0.0
   
  In [101]: jd.hms.mm
  Out[101]: 0.0
   
  In [102]: jd.hms.ss
  Out[102]: 0.0

The ``j2jd`` function converts a scalar Julian day number into a
:class:``JD`` structure. The ``dd`` member of the structure is set to
the supplied scalar. To convert a :class:``JD`` structure into a
scalar Julian day number, use the function ``jd2j``. To normalize the
components of a :class:`JD`` structure use the function ``jd2jd``.

.. autofunction:: j2jd
.. autofunction:: jd2j
.. autofunction:: jd2jd

.. sourcecode:: ipython

  In [103]: jd = tpm.jd2jd(jd)
   
  In [104]: jd.dd
  Out[104]: 2455530.0
   
  In [105]: jd.hms.hh
  Out[105]: 2.0
   
  In [106]: jd.hms.mm
  Out[106]: 36.0
   
  In [107]: jd.hms.ss
  Out[107]: 45.99999725818634

  In [108]: j = tpm.utc_now()
   
  In [109]: jd = tpm.j2jd(j)
   
  In [110]: jd = tpm.jd2jd(jd)
   
  In [111]: print jd.dd, jd.hms.hh, jd.hms.mm, jd.hms.ss
  --------> print(jd.dd, jd.hms.hh, jd.hms.mm, jd.hms.ss)
  (2455530.0, 3.0, 32.0, 23.000002205371857)


To find the sum and difference of dates represented by two :class:`JD`
instances use the ``jd_diff`` and ``jd_sum`` functions.

.. autofunction:: jd_diff
.. autofunction:: jd_sum

.. sourcecode:: ipython

  In [112]: jd = tpm.utc_now()
   
  In [113]: jd1 = tpm.utc_now()
   
  In [114]: jd1 = tpm.jd_now()
   
  In [115]: jd2 = tpm.jd_now()
   
  In [116]: jd = tpm.jd_diff(jd2, jd1)
   
  In [117]: jd = tpm.jd2jd(jd)
   
  In [118]: print jd.dd, jd.hms.hh, jd.hms.mm, jd.hms.ss
  --------> print(jd.dd, jd.hms.hh, jd.hms.mm, jd.hms.ss)
  (0.0, 0.0, 0.0, 6.000007688999176)


The ``gcal2j`` functions calculates the Julian day number for mid-day
of the given *proleptic Gregorian calendar* date. In a proleptic
Gregorian calendar all dates are expressed as Gregorian dates and no
conversion to Julian calendar takes place. The ``jcal2j`` function
calculates the Julian day number for mid-day of the given *proleptic
Julian calendar* date. In a proleptic Julian calendar, all dates are
expressed as Julian dates and no conversion to Gregorian calendar is
performed. The functions ``j2gcal`` and ``j2jcal`` perform the reverse
conversion, i.e., returns the calendar date on which the given Julian
day number occurs.

Functions ``gcal2j`` and ``jcal2j`` take as input an integer year, an
integer month and an integer day, and returns a scalar Julian day
number. Functions ``j2gcal`` and ``j2jcal`` take as input a scalar
Julian day number and returns a list of the format [year, month, day],
where all three are integers.

In all these function, BC years are represented using negative
numbers, with ``1 BC = 0``. So we have, ``10 BC = -9``, ``4713 BC =
-4712`` and so on.

.. autofunction:: gcal2j
.. autofunction:: jcal2j
.. autofunction:: j2gcal
.. autofunction:: j2jcal

.. sourcecode:: ipython

  In [129]: j = tpm.gcal2j(1987,10,11)
   
  In [130]: j
  Out[130]: 2447080.0
   
  In [131]: gcal = tpm.j2gcal(j)
   
  In [132]: gcal
  Out[132]: [1987, 10, 11]
   
  In [133]: jcal = tpm.j2jcal(0)
   
  In [134]: jcal
  Out[134]: [-4712, 1, 1]

The function ``jd2ymd`` converts a Julian day number in a :class:`JD`
structure into a Gregorian calendar date and time stored in a
:class:`YMD`. This is more useful than :func:`j2gcal`, since it will
also convert the fractional part of the Julian day number into hours,
minutes and second of the corresponding *proleptic Gregorian* calendar
date. For the reverse conversion use ``ymd2jd``. To normalize a
:class:`YMD` structure, use the function ``ymd2ymd``.

.. autofunction:: jd2ymd
.. autofunction:: ymd2jd
.. autofunction:: ymd2ymd

.. sourcecode:: ipython

  In [139]: ymd = tpm.jd2ymd(tpm.jd_now())
   
  In [140]: ymd = tpm.ymd2ymd(ymd)
   
  In [141]: ymd.y
  Out[141]: 2010
   
  In [142]: ymd.m
  Out[142]: 11
   
  In [143]: ymd.dd
  Out[143]: 29.0
   
  In [144]: ymd.hms.hh
  Out[144]: 16.0
   
  In [145]: ymd.hms.mm
  Out[145]: 58.0
   
  In [146]: ymd.hms.ss
  Out[146]: 1.0000151395797729


There are three functions that convert dates between a scalar year and
a :class:`YMD` structure. Functions ``y2ymd`` and ``ymd2y`` convert a
scalar year, including fractional part, into a :class:`YMD` structure
and a :class:`YMD` structure into scalar year, preserving the
fractional part, respectively. The function ``ydd2ymd`` takes as input
a year and a day, the latter can have fractional part, and returns a
:class:`YMD` structure.

.. autofunction:: y2ymd
.. autofunction:: ymd2y
.. autofunction:: ydd2ymd

.. sourcecode:: ipython

  In [153]: ymd = tpm.y2ymd(2000.12345)
   
  In [154]: ymd = tpm.ymd2ymd(ymd)
   
  In [155]: print ymd.y, ymd.m, ymd.dd, ymd.hms.hh, ymd.hms.mm, ymd.hms.ss
  --------> print(ymd.y, ymd.m, ymd.dd, ymd.hms.hh, ymd.hms.mm, ymd.hms.ss)
  (2000, 2, 14.0, 4.0, 23.0, 5.280020534992218)
   
  In [162]: ymd = tpm.ydd2ymd(2000,366)
   
  In [163]: ymd = tpm.ymd2ymd(ymd)
   
  In [164]: print ymd.y, ymd.m, ymd.dd, ymd.hms.hh, ymd.hms.mm, ymd.hms.ss
  --------> print(ymd.y, ymd.m, ymd.dd, ymd.hms.hh, ymd.hms.mm, ymd.hms.ss)
  (2000, 12, 31.0, 0.0, 0.0, 0.0)

The function ``j2dow`` returns the day of the week corresponding to
the given Julian day number; sunday is day 0. The function ``y2doy``
calculates the number of days in the given *proleptic Gregorian* year.

.. autofunction:: j2dow
.. autofunction:: y2doy

.. sourcecode:: ipython

  In [165]: j = tpm.utc_now()
   
  In [166]: tpm.j2dow(j)
  Out[166]: 1
   
  In [167]: tpm.y2doy(2000)
  Out[167]: 366
   
  In [168]: tpm.y2doy(1900)
  Out[168]: 365

Several functions are provided for generating formatted string
representations of dates. Function ``fmt_j`` formats a scalar year,
whereas ``fmt_ymd`` and ``fmt_ymd_raw`` generate slightly different
string representations of data in a :class:`YMD` structure.

The function :func:`pytpm.utils.fmt_jd` will format a :class:`JD`
structure and :func:`pytpm.utils.fmt_y` will format a scalar year.


.. autofunction:: fmt_j
.. autofunction:: fmt_ymd
.. autofunction:: fmt_ymd_raw

.. sourcecode:: ipython

  In [169]: j = tpm.utc_now()
   
  In [170]: print tpm.fmt_j(j)
  --------> print(tpm.fmt_j(j))
   2455530  05H 40M 58.999S
   
  In [174]: ymd = tpm.y2ymd(2000.12345)
   
  In [175]: ymd = tpm.ymd2ymd(ymd)
   
  In [176]: print tpm.fmt_ymd(ymd)
  --------> print(tpm.fmt_ymd(ymd))
  Mon Feb 14 04:23:05.280 2000
   
  In [177]: print tpm.fmt_ymd_raw(ymd)
  --------> print(tpm.fmt_ymd_raw(ymd))
  2000 2 14 4 23 5.28002053499222


Functions for working with TPM state machine
--------------------------------------------

tpm_state
~~~~~~~~~

The ``tpm_state`` function accepts an integer argument, between 0 and
``N_TPM_STATES``, and returns the name of the corresponding state. See
:ref:`tpm_states` for more information on state names.

.. autofunction:: tpm_state

.. sourcecode:: ipython

  In [2]: tpm.tpm_state(10)
  Out[2]: 'S09 + Precession'
  In [3]: tpm.tpm_state(tpm.TPM_S10)
  Out[3]: 'S09 + Precession'
  In [5]: for i in range(tpm.N_TPM_STATES):
     ....:      print "S{0:02d} {1:s}".format(i, tpm.tpm_state(i))
     ....: 
  S00 null
  S01 Helio. mean FK4
  S02 Helio. mean FK5
  S03 IAU 1980 Ecliptic
  S04 IAU 1958 Galactic
  S05 Helio. mean FK4
  S06 Helio. mean FK5
  S07 Geoc. mean FK5
  S08 S07 + Light Defl.
  S09 S08 + Aberration
  S10 S09 + Precession
  S11 Geoc. app. FK5
  S12 Topo. mean FK5
  S13 S12 + Light Defl.
  S14 S13 + Aberration
  S15 S14 + Precession
  S16 Topo. app. FK5
  S17 Topo. app. HA/Dec
  S18 Topo. app. Az/El
  S19 Topo. obs. Az/El
  S20 Topo. obs. HA/Dec
  S21 Topo. obs. WHAM


tpm_data
~~~~~~~~

Function, ``tpm_data`` is used for computing the :ref:`dependent
properties <dep_props_state_vector>` of a TPM state. It takes two
arguments: the :class:`pytpm.tpm.TPM_STATE` instance and a :ref:`TPM
data flag <tpm_data_flag>`. More than one data flag can be passed at a
time by combining the flags with the "&" operator.

If data flag is ``TPM_INIT``, then both independent and dependent
properties are set to default values. In this case. ``utc`` is set to
current time, ``delta_at`` is set to ``utc + delta_AT(utc)``, ``T`` is
set to 273.15, ``P`` is set to 1013.25, ``wavelength`` is set to
0.550, ``refa`` is set to 58.3 arcseconds converted into radians and
``refb`` is set to -0.067 arcseconds converted into radians. All other
scalar values are set to 0 and vectors and matrices are set to null
values of identity matrices.

For the data flag ``TPM_FAST``, the quantities that change on a short
time scales are calculated. The dynamical times, ``tai``, ``tdt`` and
``tdb``, and the rotational times, ``ut1``, ``gmst``, ``gast`` and
``last`` are calculated. Value of ``tai = utc + delta_at``. The value
of ``delta_at`` must be set manually.
  
If the data flag is ``TPM_MEDIUM`` then the quantities that change on
a "medium" time scales are computed. These are the observer's
Earth-fixed and space state vectors: ``obs_m``, ``obs_t`` and
``obs_s``.

If data flag is ``TPM_SLOW`` then the "slowly" changing quantities are
calculated.  ``obliquity``, nutation in longitude, ``nut_lon``, nutation
in obliquity, ``nut_obl``, the nutation matrix, ``nm``, the precession
matrix, ``pm``, the barycentric Earth vector, ``eb`` and the
heliocentric Earth vector, ``eh``.

If data flag is ``TPM_REFRACTION`` then the refraction coefficients
are computed by calling :func:`pytpm.tpm.refco`.

If the flag ``TPM_ALL`` is provided then all the above calculations,
except those corresponding to ``TPM_INIT``, are carried out.

.. autofunction:: tpm_data

In the example, below we initialize a TPM state vector and then print
its contents; only a portion of the output is shown. The module
``fmt_tpm.py`` can be downloaded from :download:`this url
<code/fmt_tpm.py>`.

.. sourcecode:: ipython

  In [1]: from pytpm import tpm, utils

  In [2]: tstate = tpm.TPM_TSTATE()
   
  In [3]: tpm.tpm_data(tstate, tpm.TPM_INIT)
   
  In [4]: import fmt_tpm
   
  In [5]: fmt_tpm.print_state(tstate)
   
  *************** Independent properties **********************
   
  UTC (Julian date)      : 2455541.10182870
  Delta AT (s)           :     34.00000000
  Delta UT (s)           :      0.00000000
  Latitude (rad)         :      0.00000000
  Longitude (rad)        :      0.00000000
  Polar motion x (rad)   :      0.00000000
  Polar motion y (rad)   :      0.00000000
  Altitude (meters)      :      0.00000000
  Humidity (0-1)         :      0.00000000
  Pressure (milli-bars)  :   1013.25000000
  Temperature (Kelvin)   :    273.15000000
  Wavelength (microns)   :      0.55000000
   
  *************** Dependent properties ************************
   
  UT1 (s)                :      0.00000000
  GAST (Julian date)     :      0.00000000
  GMST (Julian date)     :      0.00000000
  LAST (Julian date)     :      0.00000000
  TAI (Julian date)      :      0.00000000
  TDB (Julian date)      :      0.00000000
  TDT (Julian date)      :      0.00000000
  Obliquity (rad)        :      0.00000000
  Nutation in longitude  :      0.00000000
  Nutation in obliquity  :      0.00000000
  Refraction coeff. A    :      0.00028265
  Refraction coeff. B    :     -0.00000032
  .
  .
  .
  .



tpm
~~~

The is the function that performs the conversion of a given state
vector from one coordinate system into another. It takes as arguments
an array of ``V6`` vectors, the starting state number, the end state
number, epoch of the coordinates in the ``V6`` vector, the equinox of
the coordinates in the ``V6`` vector and the state data. 

Currently, there is no way of creating an array of ``V6`` vectors from
within PyTPM and hence this has to be called indirectly using the
:func:`pytpm.tpm.convert` or :func:`pytpm.utils.convert` functions.

.. autofunction:: tpm


Functions for astrometry calculations
-------------------------------------

The following lists all functions used for performing astrometry
calculations, such as applying aberration corrections and finding the
location of objects as viewed by different observers.

.. _time_scales:

Time scales
~~~~~~~~~~~

Function ``delta_AT`` returns the difference between the International
Atomic Time, TAI, and the Coordinated Universal Time, UTC, at the time
given by the input UTC.

.. attention::

  The values in the source file, ``delta_AT.c`` must be updated, and
  ``pytpm`` rebuild, whenever new values for ``TAI - UTC`` are
  published. This information is available at
  http://maia.usno.navy.mil/, specifically in the file
  http://maia.usno.navy.mil/ser7/tai-utc.dat available at the former
  URL. 

.. autofunction:: delta_AT

.. sourcecode:: ipython

  In [2]: tpm.delta_AT(tpm.utc_now())
  Out[2]: 34.0

The function ``tdt2tdb`` converts Terrestrial Dynamic Time, TDT, to
Barycentric Dynamic Time, TDB.

.. autofunction:: tdt2tdb

Function ``ut12gmst`` return the Greenwich Mean Sidereal Time, as an
angle in radians, normalized to the range [0, 2π).

NOTE: CURRENTLY THERE IS NO FUNCTION TO CONVERT UTC TO UT1. TPM STATE
ENDS UP USING UTC INSTEAD OF UT1. CURRENTLY UT1 - UTC = -0.2.

.. autofunction:: ut12gmst

.. sourcecode:: ipython

  In [4]: x = tpm.ut12gmst(tpm.utc_now())
  In [5]: print(tpm.fmt_h(utils.r2h(x)))
  15H 54M 19.166S


Proper motion
~~~~~~~~~~~~~

TPM never applies proper motion to output coordinates. Proper motion
must be applied by the user. The function ``proper_motion`` takes a
``V6`` vector, ``v6``, an end time, ``t``, and a start time, ``t0``
and applies proper motion for the interval ``t - t0``. The time
difference is assumed to be in days; use Julian dates for ``t`` and
``t0``. Velocities in ``V6`` vectors are in radians/day.

.. autofunction:: proper_motion


Ephemerides
~~~~~~~~~~~

Function ``solar_perigee`` calculates the mean longitude of the
perigee of the solar orbit for the given Terrestrial Dynamic Time (TDT) in
radians. The rate of change of this quantity, for a given TDT is
returned by ``solar_perigee_dot``.

.. autofunction:: solar_perigee
.. autofunction:: solar_perigee_dot

For a given Barycentric Dynamic Time (TDB), the function ``evp``
return the barycentric and heliocentric state vectors for the Earth.

.. autofunction:: evp

Precession and nutation
~~~~~~~~~~~~~~~~~~~~~~~

Functions ``eccentricity`` and ``eccentricity_dot`` return the
eccentricity of the Earth's orbit for the given TDT.  Functions
``obliquity`` and ``obliquity_do`` return the mean obliquity of the
ecliptic for the epoch J2000 at the given TDT. All these functions
return values in radians and radians per Julian centruy as
appropriate.

.. TODO:: Check units of eccentricity_dot and obliquity_dot.

.. autofunction:: eccentricity
.. autofunction:: eccentricity_dot
.. autofunction:: obliquity
.. autofunction:: obliquity_dot

Function ``eterms`` returns the ecliptic E-terms of aberrations, as
a :class:`V6 <pytpm.tpm.V6>` vector.

.. autofunction:: eterms

Function ``ellab`` adds to or removes from a :class:`V6
<pytpm.tpm.V6>` vector, the E-terms of aberration for the given
TDT. It removes E-terms if the ``flag`` is negative and adds the
E-terms if the ``flag`` is positive.

.. autofunction:: ellab

The following 6 functions calculate the rotation angles for precessing
equatorial coordinates, inluding velocities, between equator and
equinox of two epochs. The first and second parameters are the initial
and target epochs of the equator and equinox, as Julian dates. The
``flag`` indicates which version of these angles should be used. These
flags defined are defined as constants in TPM and decribed earlier in
:ref:`tpm_fk4_fk5_precess_angles`.


.. autofunction:: zee
.. autofunction:: zeedot
.. autofunction:: theta
.. autofunction:: thetadot
.. autofunction:: zeta
.. autofunction:: zetadot


The functions ``precess_m`` calculates the precession matrix, using
the above six functions, for precessing equatorial coordinates between
equator and equinox at two different epochs. The first two parameters
are the initial and final epochs, the parameter ``pflag`` selects the
appropriate precession angles as described in the section
:ref:`tpm_fk4_fk5_precess_angles`. The last parameter, ``sflag``
indicates whether the precession involves transition from or to a
non-inertial frame. FK4-FK5 and FK5-FK4 precessions invlove the non-inertial FK4
reference frame. All these are described in the section
:ref:`tpm_fk4_fk5_precess_angles`. 

.. autofunction:: precess_m
.. autofunction:: precess

Given a :class:`V6 <pytpm.tpm.V6>` vector, the functions ``fk425`` and
`fk542` converts it from FK4 system to FK5 system and vice-versa,
respectively.

.. autofunction:: fk425
.. autofunction:: fk524

Function ``nutations`` returns the nutation in longitude and nutation
in obliquity for the given TDT.

.. autofunction:: nutations

Aberration and light deflection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Function ``aberrate`` adds or substracts aberration, given as a
:class:`V6 <pytpm.tpm.V6>` vector, from another :class:`V6
<pytpm.tpm.V6>` vector. The latter is given as the first argument to
the function and the latter is given as the second. If argument
``flag`` is positive then aberation is added to the state vector, else
it is subtracted from the state vector.

.. autofunction:: aberrate

Function ``ldeflect`` takes a :class:`V6 <pytpm.tpm.V6>` state vector
as its first argument, and a :class:`V6 <pytpm.tpm.V6>` state vector
representing the heliocentric coordinates of Earth, and applies the
correction for gravitational deflection of light. If the third
argument, ``flag`` is positive then the change is added to the state
vector, else the change is subtracted from the state vector.
 
.. autofunction:: ldeflect

Locations on Earth
~~~~~~~~~~~~~~~~~~

Given longitude, latitude and altitude, in that order, ``geod2geoc``
returns the geocentric state vector as a :class:`V6 <pytpm.tpm.V6>`
instance. 

.. autofunction:: geod2geoc


Tranform between local, equatorial, ecliptic and galactic systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following functions rotate a :class:`V6 <pytpm.tpm.V6>` vector
from one coordinate system to the other.

Given a latitude, in radians, as the second argument, ``azel2hadec``
converts the :class:`V6 <pytpm.tpm.V6>` vector from the local
*azimuth-elevation* system into local equatorial, i.e., *hour
angle-declination* system. Function ``hadec2azel`` performs the
opposite conversion.

.. autofunction:: azel2hadec
.. autofunction:: hadec2azel

Given a :class:`V6 <pytpm.tpm.V6>` vector and the obliquity of the
ecliptic, as second argument, ``ecl2equ`` rotates the ecliptic
coordinates into equatorial coordinates. Function ``equ2ecl`` performs
the opposite conversion.

.. autofunction:: ecl2equ
.. autofunction:: equ2ecl

Functions ``equ2gal`` and ``gal2equ`` converts equatorial coordiantes
to galactic and vice-versa, respectively. Both accept a :class:`V6
<pytpm.tpm.V6>` vector as their only argument.

.. autofunction:: equ2gal
.. autofunction:: gal2equ

Refraction
~~~~~~~~~~

Given latitude, altitude, ambient temperature in Kelvins, ambient
pressure in milli-bars, relative humidity (0-1), wavelength of
observation in micrometers and the required fractional accuracy, in
that order, ``refco`` calculates the refraction coefficients, ``A``
and ``B``. 

.. autofunction:: refco

Functions ``atm`` and ``refraction`` are use to perform the full
refraction calculations. The former defines a model atmosphere.

.. autofunction:: refraction
.. autofunction:: atm

Given a zenith angle, refraction coefficient A, refraction coefficient
B, and a flag the function ``refract`` will return the zenith distance
after applying refraction, if ``flag`` is positive and the zenith
distance after removing refraction, if ``flag`` is not positive.

.. autofunction:: refract

.. _tpm_func_gen_string:

Functions for generating string representations
-----------------------------------------------

This section collects together links to all functions that return
string representations of data passed to them.

* :func:`pytpm.tpm.fmt_alpha`          
* :func:`pytpm.tpm.fmt_d`         
* :func:`pytpm.tpm.fmt_delta`
* :func:`pytpm.tpm.fmt_h` 
* :func:`pytpm.tpm.fmt_j`  
* :func:`pytpm.tpm.fmt_ymd` 
* :func:`pytpm.tpm.fmt_ymd_raw`
* :func:`pytpm.tpm.v3fmt`
* :func:`pytpm.tpm.v6fmt`
* :func:`pytpm.tpm.m3fmt`
* :func:`pytpm.tpm.m6fmt`

Similar functions in :mod:`pytpm.utils` are:

* :func:`pytpm.utils.fmt_dms`
* :func:`pytpm.utils.fmt_hms` 
* :func:`pytpm.utils.fmt_jd` 
* :func:`pytpm.utils.fmt_r`
* :func:`pytpm.utils.fmt_y`

