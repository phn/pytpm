======================
 Astrometry Resources
======================

.. _geo names search facility: http://geonames.nga.mil/ggmagaz/
.. _JPL ephemerides: http://ssd.jpl.nasa.gov/?ephemerides
.. _HORIZONS online ephemerides generator: http://ssd.jpl.nasa.gov/?horizons
.. _The Astronomical Almanac:
  http://www.usno.navy.mil/USNO/astronomical-applications/publications/astro-almanac
.. _SOFA: http://www.iausofa.org/
.. _SOFA Board: http://www.iausofa.org/board.html
.. _IAU Division 1: http://www.iau.org/science/scientific_bodies/divisions/I/
.. _IERS: http://www.iers.org/
.. _USNO Astronomical Applications:
  http://www.usno.navy.mil/USNO/astronomical-applications/
.. _The Explanatory Supplement to the Astronomical Almanac:
  http://www.usno.navy.mil/USNO/astronomical-applications/publications/exp-supp
.. _USNO Astronomy Information Center:
  http://www.usno.navy.mil/USNO/astronomical-applications/astronomical-information-center/astronomical-information-center
.. _USNO Astrometry: http://www.usno.navy.mil/USNO/astrometry
.. _USNO Earth Orientation: http://www.usno.navy.mil/USNO/earth-orientation
.. _Precise Time: http://www.usno.navy.mil/USNO/time

.. currentmodule:: pytpm

This section will given some pointers to resources for obtaining data
related to astrometry. Links to some documents that describe concepts
used in astrometry calculations are also present.

While working with data from the sources mentioned below, it is
helpful, even critical, to subscribe to mailing lists and newsletters,
that announce important updates. This applies to code libraries as
well as data sources.

`The Astronomical Almanac`_ is a collection of information on most of
the topics listed below. `USNO Astronomical Applications`_ division
maintains a large repository of information on astronomical phenomena
and astrometric data.

.. _delta_at_info:

Time scales and calendars
=========================

Information on ``delta_AT = TAI - UTC``, leap seconds in UTC and other similar
information are available from the International Earth Rotation and
Reference Systems Service (IERS). See the section on :ref:`iers_sec`
below.

Information on ``delta_AT`` also maintained in the file
ftp://maia.usno.navy.mil/ser7/tai-utc.dat, which lists ``delta_AT``
values beginning from 1961 Jan. 1.

See files in the directory ftp://hpiers.obspm.fr/eop-pc/eop/eopc04_05
for listings that give ``delta_UT = UT1 - UTC`` values.

The last two resource are the easiest way for obtaining ``delta_AT``
and ``delta_UT``, respectively. 

PyTPM has a function :func:`pytpm.tpm.delta_AT` that gives the value
for ``delta_AT`` for the given ``UTC``. But this file has to be
updated, using values in the ``tai-utc.dat`` file mentioned
above. Notification of changes are notified through the IERS mailing
lists. See :ref:`iers_sec` below.

Geographical and Earth data
===========================

Use the `geo names search facility`_ provided by the `National
Geospatial-Intelligence Survey <http://www.nga.mil/>`_ for finding
longitude and latitudes of places, using place and country
names. Google Maps and Google Earth also give longitude, latitude and
altitude information.

Websites of individual observatories may have information on their
geodetic and geocentric positions.

Use the information in section on :ref:`iers_sec` for data on polar motion
and other Earth orientation parameters.

Ephemerides
===========

Positions and orbital elements of astronomical objects and Earth
satellites, including Earth-Sun ephemerides.

+ `IAU Minor Planet Center
  <http://www.cfa.harvard.edu/iau/Ephemerides/>`_

  Definitive collection of information on minor planets, including
  orbital elements.

+ `The Asteroid Orbital Elements Database
  <ftp://ftp.lowell.edu/pub/elgb/astorb.html>`_

  By Edward Bowell, based on astrometric observations downloaded from
  the Minor Planet Center and "updated daily".

+ `JPL ephemerides`_ and `HORIZONS online ephemerides generator`_

  JPL planetary ephemerides can be downloaded from the `JPL
  ephemerides`_ site.

  HORIZONS is an online system for generating custom ephemerides.
  Output can be generated in the form of osculating elements as well
  as in the form of Cartesian vectors (position, velocity and
  acceleration). Ephemerides for more than 60 satellites are also
  available.

+ `Mars ephemerides generator <http://pds-rings.seti.org/tools/ephem2_mar.html>`_

+ `USNO astrometry service <http://www.usno.navy.mil/USNO/astrometry>`_

  Data on solar system objects observed with the Flagstaff Astrometric
  Scanning Transit Telescope is available at
  http://www.usno.navy.mil/USNO/astrometry/optical-IR-prod/solsys.

+ Earth satellites

  NORAD elements can be obtained from `CelesTrak
  <http://celestrak.com/NORAD/elements/>`_.

  `NASA space flight center
  <http://spaceflight.nasa.gov/realdata/elements/index.html>`_ has
  orbital elements for ISS.


Constants and fundamental data
==============================

.. _Physical Measurements Laboratory at NIST: http://www.nist.gov/physlab/
.. _Physical Reference Data: http://www.nist.gov/pml/data/index.cfm
.. _CODATA: http://physics.nist.gov/cuu/Constants/index.html

Fundamental physical data, constants and physical properties of
astronomical objects.

+ Physical data and fundamental constants.

  + `CODATA`_ at National Institute of Standards and Technology (NIST).

    Internationally recommended values of the fundamental physical
    data.

  + `Physical Measurements Laboratory at NIST`_, especially the
    `Physical Reference Data`_ section.

+ Data for solar system objects

  `JPL solar system dynamics <http://ssd.jpl.nasa.gov/>`_.

+ IAU Working Group on Numerical Standards for Fundamental Astronomy

  IAU/IERS approved physical and astronomical constants.

  NSFA website: http://maia.usno.navy.mil/NSFA.html.


Astrometry libraries and applications
=====================================

Examples of software similar to TPM and PyTPM. Some of these can be
used to calculate quantities such as rising and setting time for Sun
and Moon, phases of Moon and others.

.. _SLALIB:
 http://www.starlink.rl.ac.uk/star/docs/sun67.htx/sun67.html
.. _NOVAS: http://www.usno.navy.mil/USNO/astronomical-applications/software-products/novas
.. _XEphem: http://www.clearskyinstitute.com/xephem/
.. _PyEphem: http://rhodesmill.org/pyephem/ 
.. _Kapteyn: http://www.astro.rug.nl/software/kapteyn/
.. _iraf.images.imcoords.skyctrans: http://stsdas.stsci.edu/cgi-bin/gethelp.cgi?skyctran
.. _JSky: http://archive.eso.org/cms/tools-documentation/jsky/
.. _JSkyCalc: http://www.dartmouth.edu/~physics/faculty/skycalc/flyer.html
.. _SkyCalc: http://www.dartmouth.edu/~physics/people/faculty/thorstensen.html
.. _Astronomy on the Personal Computer:
  http://www.amazon.com/Astronomy-Personal-Computer-Oliver-Montenbruck/dp/3540672214
.. _Practical Astronomy With Your Calculator: 
  http://www.amazon.com/Practical-Astronomy-Calculator-Peter-Duffett-Smith/dp/0521356997


+ SLALIB_ 
+ SOFA_
+ NOVAS_
+ XEphem_ and PyEphem_
+ Kapteyn_
+ `iraf.images.imcoords.skyctrans`_
+ JSky_
+ JSkyCalc_ and SkyCalc_
+ `Astronomy on the Personal Computer`_
+ `Practical Astronomy With Your Calculator`_

Sky visualization and exploration
=================================

+ http://www.sky-map.org/
+ http://skymaps.com/
+ http://www.google.com/sky
+ http://www.worldwidetelescope.org (Web based but only for Win and Mac)
+ http://skyview.gsfc.nasa.gov/
+ `Stellarium with VirGO <http://archive.eso.org/cms/tools-documentation/visual-archive-browser>`_
+ `ALADIN <http://aladin.u-strasbg.fr/aladin.gml>`_
+ XEphem_
+ JSkyCalc_


Catalogs
========

Astrometry catalogs i.e., catalogs of accurate positions and proper
motion ; data can be accessed using the `ViZier service
<http://cdsarc.u-strasbg.fr/viz-bin/Cat>`_.

.. _Hipparcos:
 http://www.rssd.esa.int/index.php?project=HIPPARCOS&page=Overview
.. _USNO B 1.0: http://www.usno.navy.mil/USNO/astrometry/optical-IR-prod/usno-b1.0
.. _NOMAD: http://www.usno.navy.mil/USNO/astrometry/optical-IR-prod/nomad


+ Hipparcos_
+ `USNO B 1.0`_

  USNO-B1.0 is the latest catalog from the USNO Precision Measuring
  Machine project. It contains over 1,000,000,000 entries and provides
  positions, magnitudes, and proper motions for each object. 

+ `PPMXL Catalog <http://cdsarc.u-strasbg.fr/viz-bin/Cat?cat=I/317&target=brief&>`_

  A new determination of mean positions and proper motions on the ICRS
  system by combining USNO-B1.0 and 2MASS astrometry.

+ NOMAD_ (Naval Observatory Merged Astrometric Dataset)

  NOMAD is a simple merge of data from the Hipparcos, Tycho-2, UCAC-2
  and USNO-B1 catalogs, supplemented by photometric information from
  the 2MASS final release point source catalog. The primary aim of
  NOMAD is to help users retrieve the best currently available
  astrometric data for any star in the sky by providing these data in
  one place.


Documents and papers
====================

These documents explain concepts such as precession, nutation, time
scales and others related to astrometry. The various papers mentioned
in these documents are also important sources of information on
astrometry related concepts.

+ `The Explanatory Supplement to the Astronomical Almanac`_
+ NOVAS_ Manual
+ :download:`TPM Manual <TPM/tpm.pdf>`
+ SLALIB_ Manual
+ `SOFA Documents <http://www.iausofa.org/cookbooks.html>`_

  + SOFA Manual.
  + SOFA Tools for Earth Attitude.
  + SOFA Time Scales and Calendar Tools.
  
+ `Astronomy on the Personal Computer`_

  This books is essentially a reference manual for the C++ software
  that is distributed with it. It has good explanations of concepts
  such as orbital elements, precession angles and others.

+  `Practical Astronomy With Your Calculator`_

  Step-by-step instructions on performing astrometry calculations
  using a calculator. Great book for understanding basic ideas in
  astrometry.

The SOFA cookbooks, Tools for Earth Attitude and Time Scales and
Calendar Tools, are perhaps the best documents to start
with. `Spherical Astronomy`_ by Robin M. Green and `Fundamentals of
Astrometry`_ by Jean Kovalevsky and P. Kenneth Seidelmann, are two
relevant textbooks.

.. _Spherical Astronomy:
  http://www.amazon.com/Spherical-Astronomy-Robin-M-Green/dp/0521317797
.. _Fundamentals of Astrometry:
  http://www.amazon.com/Fundamentals-Astrometry-Jean-Kovalevsky/dp/0521642167


Organizations
=============

USNO
----

- `USNO Astronomical Applications`_

  Services such as date calculations, setting and rising time and
  others. Information on astronomical concepts behind the above
  calculations are also provided.

- `USNO Astrometry`_ 

  Links to astrometric catalogs such as NOMAD, UCAC, USNO-B1.0 etc.,
  . Observations of planetary satellites and minor planets are also
  provided.

- `USNO Earth Orientation`_

   USNO is the International Earth Rotation and Reference Systems
   Service (IERS) Rapid Service/Prediction Center (RS/PC) for Earth
   Orientation. Most of the information in IERS bulletins are issued
   from USNO.

- `Precise Time`_

   Information on obtaining precise time (UTC).

JPL Solar System Dynamics
-------------------------

`JPL SSD <http://ssd.jpl.nasa.gov/>`_ collects information on orbits,
ephemerides and physical characteristics of solar system objects.

Standards Of Fundamental Astronomy
----------------------------------

SOFA_, or the `SOFA Board`_, is responsible for implementing the
definitive algorithms for standard models used in Astronomy. This
organization works under `IAU Division 1`_.

Implementations of the algorithms in Fortran 77 and ANSI C are made
available by SOFA.

SOFA has an `email service <http://www.iausofa.org/register.html>`_
that sends notifications of software releases and other information.

.. _iers_sec:

International Earth Rotation and Reference Systems Service
----------------------------------------------------------

IERS_ is responsible for defining and determining Earth orientation,
International Terrestrial Reference System/Frame, International
Celestial Reference System/Frame and geophysical fluids data.

IERS also provides information on leap seconds and DUT1, which are
related to Earth orientation. It was established by the IAU and the
International Union of Geodesy and Geophysics.

IERS has an `email notification service
<http://www.iers.org/IERS/EN/Publications/Subscription/subscription.html>`_
that delivers all their data bulletins and messages:

+ Bulletin A (weekly)

  IERS Bulletin A contains Earth orientation parameters x/y pole,
  ``UT1 - UTC`` and their errors at daily intervals and predictions
  for 1 year into the future. 

  But also see files in the directory
  ftp://hpiers.obspm.fr/eop-pc/eop/eopc04_05 for listings that give
  ``UT1 - UTC`` values. These are probably easier to use. For example
  the file ``eopc04_IAU2000.62-now`` in the above directory gives
  ``UT1 - UTC`` values, in addition to many others, for the
  appropriate period.


+ Bulletin B (monthly)

  IERS Bulletin B provides current information on the Earth's
  orientation in the IERS Reference System. This includes Universal
  Time, coordinates of the terrestrial pole, and celestial pole
  offsets.

+ Bulletin C (bi-annual)

  Announcement of leap seconds in UTC and information on ``UTC-TAI``.

+ Bulletin D (irregular)

  Announcements of the value of ``DUT1 = UT1 - UTC`` to be transmitted
  with time signals with a precision of ±0.1s.

+ Messages (irregular)

  The IERS Messages contain short and rapid information about the
  IERS and its products for contributors and users.

See `IERS data products page
<http://www.iers.org/IERS/EN/DataProducts/data.html>`_ page for all
data provided by IERS. The "directory" http://maia.usno.navy.mil/ser7/
contains collection of files that has data from all published
bulletins, for example bulletin B. For information of the contents of
various bulletins see appropriate files in
ftp://hpiers.obspm.fr/iers/bul.

See files in the directory ftp://hpiers.obspm.fr/eop-pc/eop/eopc04_05
for listings that give ``UT1 - UTC`` and other Earth orientation
parameters.
