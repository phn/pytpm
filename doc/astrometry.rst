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


This section will given some pointers to resources for obtaining
astrometric data and, links to some documents that describe concepts
used in astrometry calculations.

While working with data from the sources mentioned below, it is
helpful, even critical, to subscribe to mailing lists and newsletters,
that announce important updates to the sources. This applies to
computer code libraries as well as data sources.

`The Astronomical Almanac`_ is a collection of information on most of
the topics listed below. USNO Astronomy Department
http://www.usno.navy.mil/astronomy maintains a large repository of
information on astronomical phenomenon and astrometric data.

Time scales and calendars
=========================

Information on ``TAI - UTC``, leap seconds in UTC and other similar
information are available from IERS. See the section on :ref:`iers`
below.

Information on ``TAI - UTC`` is also available in the file
ftp://maia.usno.navy.mil/ser7/tai-utc.dat, which lists ``TAI - UTC``
values beginning from 1961 Jan. 1.

Earth data
==========

Use the `geo names search facility`_ provided by the `National
Geospatial-Intelligence Survey <http://www.nga.mil/>`_ for finding
longitude and latitudes of places. Google Maps/Earth also gives
longitude, latitude and altitude information.

Websites of individual observatories will have information on their
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

  By Edward Bowell based on astrometric observations downloaded from
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


Physical constants and physical properties of astronomical objects.

+ Physical constants and data

  + http://physics.nist.gov/cuu/Constants/index.html
  + http://www.nist.gov/physlab/

+ Data for solar system objects

  `NASA solar system dynamics <http://ssd.jpl.nasa.gov/>`_


Astrometry libraries and applications
=====================================

Examples of software similar to TPM and PyTPM. Some of these can
calculate quantities such as rising and setting time for Sun and Moon,
phases of Moon and others.

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

+ SLALIB_ 
+ SOFA_
+ NOVAS_
+ XEphem_ and PyEphem_
+ Kapteyn_
+ `iraf.images.imcoords.skyctrans`_
+ JSky_
+ JSkyCalc_ and SkyCalc_
+ `Astronomy on the Personal Computer`_

Sky visualization and exploration
=================================

+ http://www.sky-map.org/
+ http://www.google.com/sky
+ http://www.worldwidetelescope.org (Web based but only Win and Mac)
+ `Stellarium with VirGO <http://archive.eso.org/cms/tools-documentation/visual-archive-browser>`_
+ `ALADIN <http://aladin.u-strasbg.fr/aladin.gml>`_
+ XEphem_
+ JSkyCalc_
+ http://skymaps.com/

Catalogs
========

Astrometry catalogs; data can be accessed using the `ViZier service
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
  and USNO-B1 catalogues, supplemented by photometric information from
  the 2MASS final release point source catalogue. The primary aim of
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

  + Tools for Earth Attitude
  + SOFA Time Scales and Calendar Tools

+ `Astronomy on the Personal Computer`_


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
  provided. The `Astrometry Information Center
  <http://www.usno.navy.mil/USNO/astrometry/information>`_ has more
  information on these catalogs.

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
related to Earth orientation.

It was established by the IAU and the International Union of Geodesy
and Geophysics.

IERS has an `email notification service
<http://www.iers.org/IERS/EN/Publications/Subscription/subscription.html>`_
that delivers all their data bulletins and messages:

+ Bulletin A (weekly)

  IERS Bulletin A contains Earth orientation parameters x/y pole,
  UT1-UTC and their errors at daily intervals and predictions for 1
  year into the future.

+ Bulletin B (monthly)

  IERS Bulletin B provides current information on the Earth's
  orientation in the IERS Reference System. This includes Universal
  Time, coordinates of the terrestrial pole, and celestial pole
  offsets.

+ Bulletin C (bi-annual)

  Announcement of leap seconds in UTC and information on ``UTC-TAI``.

+ Bulletin D (irregular)

  Announcements of the value of ``DUT1=UT1-UTC`` to be transmitted
  with time signals with a precision of +/-0.1s.

+ Messages (irregular)

  The IERS Messages contain short and rapid information about the
  IERS and its products for contributors and users.

See `IERS data products page
<http://www.iers.org/IERS/EN/DataProducts/data.html>`_ page for all
data provided by IERS.



.. ============
..  Astrometry
.. ============
..  
..  
.. .. TODO::
..   
..   Explain time, dates and calendars: Gregorian and Julian calendars,
..   Gregorian and Julian years,  y in TPM is Greogrian year, Julian day
..   numbers. 
..  
..   print(tpm.fmt_ymd(tpm.y2ymd(2000.0)))
..   Fri Dec 31 00:00:00.000 1999
..  
..   UTC, UT, UT1 etc.,
..  
..  
.. Refs: SLALIB, TPM, NOVAS, SOFA
..  
.. Coordinate systems:
..  
.. 6 celestial systems
..  
.. RH  
..  
..   galactic, equatorial, ecliptic, supergalactic
..  
..   geographic longitude and latitude (east +ve)
..  
.. LH 
..  
..   local equatorial, horizon (north to east)
..  
.. FK5 J2000 and ICRS distinction is important only if accuracies better
.. than 50 mas is required.
..  
.. ICRS: decouples Earth orientation and rotation from coordinate systems
..  
.. 26000 year component: luni-solar precession 
..  
.. 0.5"/y secular rotation of ecliptic (Earth-Moon orbit) mainly due to
.. planets: planetary precession
..  
.. luni-solar + planetary = general precession 11"/18.6y and smaller
.. component: nutation
..  
.. nutation: some factors: non-rigidity of Earth, planets
..  
.. main effect of precession-nutation: 50"/year change in ecliptic
.. longitudes. 
..  
.. coordinates related by general precession: Mean coordinates
..  
.. mean FK4|FK5 equator and equinox of epoch xxxx.
..  
.. FK4 defined by the Bessel-Newcomb precession model
.. FK5 defined by Fricke model and newer Simon et al model
..  
.. Nutation models: IAU 1980 and newer SF2001; latter includes correction
.. for 23 mas difference between J2000 and ICRS resulting in 1 mas
.. precession in the current era.
..  
.. Epoch
..  
.. Is a moment in time and hence can be specified in many different
.. calendar systems and time scales.
..  
.. Besselian epoch: Year starts when the ecliptic longitude of the **mean
.. Sun** is 280 deg. One year is a tropical year of lenght 365.2422... .
.. Julian epoch: Julian epoch 2000 is 2000/1/1 12:00:00 TT. One year is
.. 365.25 days exactly.
..  
.. Stars have proper motion. So in addition to the epoch of the mean
.. equator and equinox we must also specify when did the star have the
.. mentioned position i.e., epoch of the coordinates.
..  
.. α and δ, equinox (i.e. epoch of the equator and equinox), epoch of the
.. coordinates and proper motion
..  
.. Aberration
..  
.. finite speed of light and Earth's motion: annual abberation/stellar abberation
..  
.. max of 20.5" for star 90 deg from Earth's motion
..  
.. the contribution due to eccentricity of Earth's orbit: E-terms of
.. aberration; amplitude 0.3" and is approximately constant for a given
.. star. Star positions after IAU 1976 use Earth's actual barycentric
.. velocity and not a formulation based on circular velocity and
.. corrections for eccentricity.
..  
.. diurnal aberration: due to rotation of Earth for an observer on the
.. Earth's surface; max amplitude about 0.3".
..  
.. planetary aberration: this is not aberration but is caused by motion
.. of both Earth and the solar system body leading to displacement from
.. the ephemeris position. 
..  
..  
.. Mean places: FK4 and FK5 systems
..  
.. FK4 rotates at 0.5" per century and have E-terms of aberration added
.. to the positions.
..  
.. QSO will have non-zero proper motions in FK4 system.
..  
.. After reading section 4.11 of SLALIB: can apply proper motion to given
.. coordinates to get coordinates for equinox and epoch B1950,
.. current-epoch-of-obs, do FK4-FK5 to get coordiantes for equinox and
.. epoch J2000, current-epoch-of-obs. Or do not apply proper motion and
.. use coordiantes for equinox and epoch B1950, given-epoch-of-obs, in
.. FK4-FK5 to get  coordinates in equinox and epoch of J2000,
.. given-epoch-of-obs. Then apply the proper motions in FK5 system, which
.. will be different form the given proper motions, to get coordinates in
.. equinox and epoch J2000, current-epoch-of-obs.
..  
.. Mean geocentric place to apparent geocentric place
..  
.. light deflection: 1.74" at solar limb; 0.02" at 20 degrees
..  
.. aberration: 20.5" w.r.t solar system barycenter
..  
.. precession-nutation: J2000 to current(true) equinox and epoch; a
.. rotation matrix.
..  
.. Apparent geocentric to apparent topocentric
..  
.. h-δ : α-δ to local equatorial
..  
..   apply h = θ - α where θ is the sidereal time (Earth roation angle)
..   of-course, α must be the apparent RA at the time of observation and
..   θ must be the local apparent sidereal time
..  
..   From civil time obtain UTC; then find UT using UT1 - UTC; Greenwich
..   Mean Sidereal Time is a function of UT; add east longitude to get
..   Local Mean Sidereal Time; now the mean equinox is not what we need
..   we need the true equinox; add equation of the equinoxes
..  
..   equation of equinoxes: effect of nutation on sidereal time
..  
..   Also the observer's longitude should be corrected for polar motion;
..   but this is of not much use if the telescope's location is not known
..   to a few meters; the corrections are less than 0.3".
..  
.. az-elv: local equatorial to horizon
..  
..   diurnal aberration: 0.2"
..  
.. refraction: changes only the az
..  
..  
.. The ICRF (reaization of ICRS) is based on 608 extra-galactic radio
.. sources. The Hipparcos data is alligned to ICRF to within 0.5 mas and
.. 0.5 mas/year at epoch 1991.25. The Hipparcos (ICRS) and FK5 agree to
.. 32 mas and 1 mas/year.
..  
.. Time scales
..  
.. + TAI: International Atomic Time
.. + UTC: Coordinated Universal Time 
.. + TT Terrestrial Time (synonymous to Terrestrial Dynamic Time (TDT))
.. + TDB: Barycentric Dynamic Time
.. + TCG: Geocentric Coordinate Time
.. + TCB: Barycentric Coordinate Time
..  
.. + UT: Universal Time 
.. + GMST: Greenwich Mean Sidereal Time
.. + GAST: Greenwich Apparent Sidereal Time
.. + LAST: Local Apparent Sidereal Time
..  
.. Obsolete: 
..  
..   + GMT (if specified this may be UTC or UT)
..   + ET Ephemeris Time (close to TT/TDT)
..  
..  
.. + TAI
..  
..   Kept by a changing population of Atomic clocks, giving a weighted
..   average. Unit is SI seconds.
..  
..   UTC and TAI have the same unit but differ in epoch: DAT = TAI - UTC.
..  
..   DAT must be kept up-to-date with published quantities.
..  
.. + UT(UT1)
..  
..   Unit i.e., 1 UT second is not the same as one SI second. UT reflects
..   Earth's rotation and it is irregular. UT is defined through its
..   relationship with the Earth rotation angle i.e., sidereal time.
..  
..   Length of the day is slightly longer that 86400 SI seconds.
..  
..   To point a telescope we need UT1.
..  
.. + UTC 
..  
..   UTC is tied to Earth's rotation like UT but is kept to within 1
..   second of TAI by adding leap seconds.
..  
..   Unit is SI second.
..  
..   Since unit is UTC will get ahead of Earth's rotation and hence must
..   be "stopped" for a brief interval, DAT, so that Earth catches up.
..  
..   UT1 and UTC are related through DUT = UT1 - UTC. DUT is available
..   from publications.
..  
.. + GMST
..  
..   linked to UT1 but instead of the Sun the reference is with
..   stars. Sidereal second changes along with UT1; but the former is
..   shorter than the latter.
..  
..   UT1 - GMST is available in functioanl format. 
..  
.. + GAST
..  
..   Refer to the apparent position of the equinox rather than the mean
..   i.e., applying corrections for nutation effects. This correction is
..   available as the equation of the equinoxes.
..  
.. + LAST is GMST + East longitude (with polar motion correction) +
..   equation of equinoxes.
..  
.. + TT (TDT)
..  
..   Time scale for geocentric ephemerides for solar system objects.
..  
..   TT = TAI + 32.184 s
..  
..   DTT = TT - UTC
..  
.. + TDB
..   
..   Time used for describing movement of solar system objects, pulsat
..   timings etc., where we want a time scale that is not affected by the
..   presence of solar system objects and motion of Earth. It is a
..   *coordinate* time.
..  
..   This is kept close to TT; relativistic effects manifest as
..   quasi-periodic changes about 2 milli-secs in magnitude. Can affect
..   long term monitoring of pulsar timings.
..  
..   ``sla_RCC`` implements TDB in a way that is most consistent with the
..   IAU 1976 definition; provides TDB - TT accurate to a few µs.
..  
..   Difference between TT and TDB are not import for most purposes.
..  
..   Time scale used by JPL solar system ephemerides is numerically equal
..   to TDB.
..  
.. For calculating topocentric solar-system phenomena such as
.. occultaions, dynamic time and UT are required. DT = ET - UT is needed
.. here. ``sla_DT``.
..  
.. Julian day number and Julian date
..  
.. Julian day number: noon (Greenwich?) 
.. Julian date: includes fractional part of day
.. MJD = JD - 2400000.5
..  
.. In effect Julian date is based on UT.

