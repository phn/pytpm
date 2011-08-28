Python interface to the TPM C library
=====================================

.. _Telescope Pointing Machine: http://www.sal.wisc.edu/~jwp/astro/tpm/tpm.html
.. _Jeffrey W Percival: http://www.sal.wisc.edu/~jwp/
.. _Cython: http://www.cython.org/
.. _SWIG: http://www.swig.org/
.. _coords: https://trac6.assembla.com/astrolib
.. _astrolib: https://trac6.assembla.com/astrolib
.. _KPNO WIYN observatory: http://www.noao.edu/wiyn/wiyn.html
.. _WHAM: http://www.astro.wisc.edu/wham/
.. _KPNO: http://www.noao.edu/kpno
.. _Virtualenv: http://pypi.python.org/pypi/virtualenv 
.. _Virtualenvwrapper: 
   http://www.doughellmann.com/projects/virtualenvwrapper/
.. _ipython: http://ipython.scipy.org
.. _Practical Astronomy With Your Calculator: 
  http://www.amazon.com/Practical-Astronomy-Calculator-Peter-Duffett-Smith/dp/0521356997
.. _Distribute: http://packages.python.org/distribute/
.. _numpydoc: http://pypi.python.org/pypi/numpydoc
.. _Sphinx: http://sphinx.pocoo.org/
.. _IERS: http://www.iers.org/
.. _Nose: http://pypi.python.org/pypi/nose
.. _pypi page for the project: http://pypi.python.org/pypi/PyTPM
.. _pip: http://pypi.python.org/pypi/pip
.. _pyslalib: https://github.com/scottransom/pyslalib

PyTPM is a Python interface to the `Telescope Pointing Machine`_ (TPM)
library. TPM is a C library written by `Jeffrey W Percival`_, for performing
coordinate conversions between several astronomical coordinate systems.

TPM was designed with the aim of incorporating it into telescope
control systems. To meet this design goal, TPM offers control over
calculations carried out during coordinate conversions. Some of these
calculations must be performed frequently, for example time related
calculations. Others need to be performed only once per night, for
example nutation and precession matrices. TPM allows the user to select
the exact calculations to be performed. This enables the user to
control the computational load, which is important in telescope control
systems. TPM C library is used by the `KPNO WIYN observatory`_ and the
WHAM_ projects.

PyTPM is not a complete astrometry package. The aim is to provide
access to the TPM C code from Python. TPM machinery can be directly
accessed using the `pytpm.tpm` sub-module. The sub-module
`pytpm.convert` has several convenience functions that can be used for
performing coordinate conversions. The latter is sufficient for most,
but not all, calculations. You should read the `TPM manual`__ before
attempting to use the `pytpm.tpm` module. The manual is present in the
source code repository and is also included with the PyTPM
documentation

__ `Telescope Pointing Machine`_

Python interface to TPM C code is written using Cython_.

Installing PyTPM
================

PyTPM requires the following:

+ Python 2.6, 2.7 or 3.2.
+ GCC.
+ The Distribute_ package.
+ Nose_ for running tests.
+ Cython_, only if the Cython output needs to be regenerated.

To build the documentation Sphinx_ and the numpydoc_ Sphinx extension
is required.

PyTPM was tested on Ubuntu 10.10 and 11.04.

Installation
============

.. important::

    The file `src/tpm/delta_AT.c` must be updated when Delta-AT is
    changed by the IERS_, and PyTPM Cython code must
    re-compiled. Update the file and just run setup.py again. A new
    version of PyTPM will be released when this change occurs.

If you don't have Distribute_, then install it. Then do one of the
following:

+ pip_ or `easy_install`

  Install pip_ and then run `pip install pytpm`. 

  If `easy_install` is available then `easy_install pytpm` will also
  work. Distribute_ comes with easy_install. `pip`_ itself can be
  installed using the command `easy_install pip`.

or 

+ Manual installation.

  Download the distribution from the `pypi page for the project`_. Then
  run `python setup.py install`. Use the `--prefix <dest>` or `--user`
  arguments to change the installation location.


With both these methods, virtualenv_ and virtualenvwrapper_ can be
used. These tools enable easy installation and maintenance of Python
packages.

To run tests, and to build documentation, the manual installation
method has to be followed. Run `python setup.py test` and then run
`python setup.py install`. To build documentation, run `make html` in
the `doc` directory.

Examples
========

Detailed documentation is available at
http://phn.github.com/pytpm. Documentation in HTML format can also be
downloaded from the `pypi page for the project`_. Documentation in ReST
format is available in the `doc` directory of the distribution.
  
PyTPM can be used to convert *positions and velocities* in a given
astronomical coordinate system into another. Examples of doing this are
in the `examples` folder of the source code repository and is also
included with the HTML documentation.

You should read the `TPM manual`__ before attempting to use the
`pytpm.tpm` module.  The manual is also available in the source code
repository and the HTML documentation.

__ `Telescope Pointing Machine`_

.. _coordinates of M100: http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=M100&submit=SIMBAD+search

In the following examples `coordinates of M100`_ is converted between
different systems. 

The following examples use the convenience function
`pytpm.convert.convertv6`, instead of directly using the underlying TPM
functions. The documentation has examples of using the latter.

The `convertv6` function takes the following arguments. Not all of
these need to be specified for a given conversion. 

+------------+----------------------------------------------------+
| Parameter  | Description                                        |
+============+====================================================+
| v6         | one V6C vector or a list of V6C vectors.           |
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

A `V6C` object is a 6-D vector that stores positions and velocities in
Cartesian coordinates. The function `pytpm.convert.v62cat` can be used
to create a `V6C` object from catalog data.  This function will accept
scalar or list of coordinates. Function `pytpm.convert.v62cat` can
convert `V6C` objects to catalog coordinates. The coordinates are
returned as a dictionary. This function will also take a list of `V6C`
objects and will return a list of dictionaries.

Coordinate systems are specified using integers or integer
constants. These are referred to as `states`.The following are some of
the important states.

+---------+------------------------------------------------+
| State   | Description                                    |
+=========+================================================+
|    3    | IAU 1980 Ecliptic system                       |
+---------+------------------------------------------------+
|    4    | IAU 1958 Galactic system                       |
+---------+------------------------------------------------+
|    5    | Heliocentric mean FK4 system, B1950 equinox    |
+---------+------------------------------------------------+
|    6    | Heliocentric mean FK5 system, J2000 equinox    |
+---------+------------------------------------------------+
|   11    | Geocentric apparent FK5, current equinox       |
+---------+------------------------------------------------+
|   16    | Topocentric apparent FK5, current equinox      |
+---------+------------------------------------------------+
|   17    | Topocentric apparent (Hour Angle, Declination) |
+---------+------------------------------------------------+
|   18    | Topocentric apparent (Azimuth, Elevation)      |
+---------+------------------------------------------------+
|   19    | Topocentric observed (Azimuth, Elevation)      |
+---------+------------------------------------------------+
|   20    | Topocentric observed (Hour Angle, Declination) |
+---------+------------------------------------------------+

FK5 equinox and epoch J2000.0, to FK4 equinox and epoch B1950.0
---------------------------------------------------------------

First obtain the FK5 equinox J2000.0 and epoch J2000.0 RA and Dec
coordinates in radians.

::

  >>> ra_j2000 = tpm.HMS(hh=12, mm=22, ss=54.899).to_radians()
  >>> dec_j2000 = tpm.DMS(dd=15, mm=49, ss=20.57).to_radians()

Create a `V6C` vector for the object. Note that `pytpm.convert.cat2v6`
will accept a list of coordinates as well.

::

  >>> v6 = convert.cat2v6(ra_j2000, dec_j2000)

Now convert to FK4 equinox B1950.0 but remaining at epoch J2000.0. In
the following `6` stands for FK5 equinox and epoch J2000.0 coordinates
and `5` stands for FK4 equinox and epoch B1950.0. The epoch and equinox
are specified using `epoch` and `equinox` keywords. But they can be
interpreted in different ways depending on the exact conversion
requested. In this case, they are applicable to the input coordinates.

::

  >>> v6_fk4 = convert.convertv6(v6, s1=6, s2=5, epoch=tpm.J2000, 
     ...: equinox=tpm.J2000)

Convert V6C to catalog data and print results. Function
`pytpm.convert.v62cat` will also accept a list of V6C objects.

::

  >>> d = convert.v62cat(v6_fk4, C=tpm.CB)
  >>> print tpm.HMS(r=d['alpha'])
   12H 20M 22.935S
  >>> print tpm.DMS(r=d['delta'])
  +16D 05' 58.024"

The parameter `C` is the number of days in a century. The velocities in
AU/day must be converted into "/century. In the Besselian system, a
century has approximately 36524.22 days, where as in the Julian system
a century has 36525.0 days. The former is used in FK4 and the latter is
used in FK5. The default value is set to 36525.0.

Note that the results above *do not agree* with the FK4 values given by
SIMBAD. This is because the results are for the epoch J2000.0. Even
though the object doesn't have proper motion, the FK4 system is
rotating with respect to FK5. This results in a fictitious proper
motion in the FK4 system. We must apply proper motion from epoch
J2000.0 to epoch B1950.0 to get the final result.

::

  >>> v6_fk4_ep1950 = convert.proper_motion(v6_fk4, tpm.B1950, tpm.J2000)

Finally convert V6C to catalog data and print results. The final result
is in FK4 equinox and epoch B1950.0. The final results agree with the
values given by SIMBAD.

::

  >>> d = convert.v62cat(v6_fk4_ep1950, C=tpm.CB)
  >>> print tpm.HMS(r=d['alpha'])
   12H 20M 22.943S
  >>> print tpm.DMS(r=d['delta'])
  +16D 05' 58.241"


FK5 equinox and epoch J2000 to IAU 1958 Galactic System
-------------------------------------------------------

The IAU 1958 galactic system is represented using state `4`. The result
below is for the epoch J2000.0. The epoch of the Galactic coordinates
given by SIMBAD is J2000.0. So the result obtained below is what we
need, i.e., we don't need to apply any proper motion corrections.

::

  >>> ra_j2000 = tpm.HMS(hh=12, mm=22, ss=54.899).to_radians()
  >>> dec_j2000 = tpm.DMS(dd=15, mm=49, ss=20.57).to_radians()
  >>> v6 = convert.cat2v6(ra_j2000, dec_j2000)

  >>> v6_gal = convert.convertv6(v6, s1=6, s2=4, epoch=tpm.J2000, 
     ...: equinox=tpm.J2000)

  >>> d = convert.v62cat(v6_gal)
  >>> print tpm.r2d(d['alpha'])
  271.136139562
  >>> print tpm.r2d(d['delta'])
  76.8988689751


IAU 1958 Galactic to FK5 equinox and epoch J2000.0
--------------------------------------------------

Here we set the starting state to galactic i.e., `4` and the end state
to FK5 equinox. Since the input coordinates are at epoch J2000.0, the
final results will also be at epoch J2000.0, i.e., FK5 equinox and
epoch J2000.0.

::

  >>> gal_lon = tpm.d2r(271.1361)
  >>> gal_lat = tpm.d2r(76.8989)
  >>> v6 = convert.cat2v6(gal_lon, gal_lat)

  >>> v6_fk5 = convert.convertv6(v6, s1=4, s2=6, epoch=tpm.J2000)

  >>> d = convert.v62cat(v6_fk5)
  >>> print tpm.HMS(r=d['alpha'])
   12H 22M 54.900S
  >>> print tpm.DMS(r=d['delta'])
  +15D 49' 20.683"

The results are consistent with the accuracy of the input galactic
coordinates. 

FK5 equinox and epoch J2000 to IAU 1980 Ecliptic system
-------------------------------------------------------

The ecliptic system is indicated using the state `3`. Here the epoch of
the output ecliptic coordinates will be J2000.0.

::

  >>> ra_j2000 = tpm.HMS(hh=12, mm=22, ss=54.899).to_radians()
  >>> dec_j2000 = tpm.DMS(dd=15, mm=49, ss=20.57).to_radians()
  >>> v6 = convert.cat2v6(ra_j2000, dec_j2000)

  >>> v6_ecl = convert.convertv6(v6, s1=6, s2=3, epoch=tpm.J2000, 
     ...: equinox=tpm.J2000)

  >>> d = convert.v62cat(v6_ecl)
  >>> print tpm.r2d(d['alpha'])
  178.78256462
  >>> print tpm.r2d(d['delta'])
  16.7597002513

The results agree with the results form the SLALIB (pyslalib_) routine
`sla_eqecl`.


IAU 1980 Ecliptic system to FK5 equinox and epoch J2000.0
---------------------------------------------------------

The starting state is set to `3` for ecliptic and the end state is set
to `6` for FK5 equinox and epoch J2000.0.

::

  >>> ecl_lon = tpm.d2r(178.78256462)
  >>> ecl_lat = tpm.d2r(16.7597002513)
  >>> v6 = convert.cat2v6(ecl_lon, ecl_lat)

  >>> v6_fk5 = convert.convertv6(v6, s1=3, s2=6, epoch=tpm.J2000)

  >>> d = convert.v62cat(v6_fk5)
  >>> print tpm.HMS(r=d['alpha'])
   12H 22M 54.898S
  >>> print tpm.DMS(r=d['delta'])
  +15D 49' 20.570"


FK5 equinox and epoch J2000 to Geocentric apparent
--------------------------------------------------

Geocentric apparent RA & Dec. for midnight of 2010/1/1 is calculated as
shown below. The state identification number for geocentric apparent
position is `11`.

Obtain UTC and TDB time for the time of observation.

::

  >>> utc = tpm.gcal2j(2010, 1, 1) - 0.5  # midnight
  >>> tdb = tpm.utc2tdb(utc)

Obtain coordinates and `V6C` vector.

::

  >>> ra_j2000 = tpm.HMS(hh=12, mm=22, ss=54.899).to_radians()
  >>> dec_j2000 = tpm.DMS(dd=15, mm=49, ss=20.57).to_radians()
  >>> v6 = convert.cat2v6(ra_j2000, dec_j2000)

Apply proper motion from epoch J2000.0 to epoch of observation. In this
example, this is not needed since proper motion is zero. But we do this
for completeness. The result is FK5 J2000 current epoch.

::

  >>> v6 = convert.proper_motion(v6, tt, tpm.J2000)

Convert coordinates from FK5 equinox J2000, current epoch to FK5
equinox and epoch of date.

::

  >>> v6_gc = convert.convertv6(v6, s1=6, s2=11, utc=utc)
  >>> d = convert.v62cat(v6_gc)
  >>> print tpm.r2d(d['alpha'])
  185.860038856
  >>> print tpm.r2d(d['delta'])
  15.7631353482

The result from SLALIB (pyslalib_) for the equivalent conversion, using
the `sla_map` function is given below.

::

  >>> utc = slalib.sla_caldj(2010, 1, 1)[0]  # midnight
  >>> tt = slalib.sla_dtt(utc) / 86400.0 + utc

  >>> r, d = slalib.sla_map(ra_j2000, dec_j2000, 0, 0, 0, 0.0, 2000.0,
     ...: tt)

  >>> tpm.r2d(r)
  185.86002229414245
  >>> tpm.r2d(d)
  15.763142468669891

The difference is about 0.06 arc-sec in RA and about 0.03 arc-sec
in Dec.::

  >>> (tpm.r2d(r) - 185.860038856) * 3600.0
  -0.059622687126648088
  >>> (tpm.r2d(d) - 15.7631353482) * 3600.0
  0.025633691604554087


FK5 equinox and epoch J2000 to topocentric observed
---------------------------------------------------

Topocentric observed azimuth and elevation (and zenith distance) for an
observer at the default location (KPNO) is calculated for 2010/1/1
mid-day. The final state i.e., apparent topocentric Az & El, is `19`.

For midnight 2010/1/1 this object is below the horizon and hence the
refraction calculations are not reliable. So we use mid-day for the
following example.

::

  >>> utc = tpm.gcal2j(2010, 1, 1)  # mid-day
  >>> tt = tpm.utc2tdb(utc)

  >>> ra_j2000 = tpm.HMS(hh=12, mm=22, ss=54.899).to_radians()
  >>> dec_j2000 = tpm.DMS(dd=15, mm=49, ss=20.57).to_radians()
  >>> v6 = convert.cat2v6(ra_j2000, dec_j2000)

  >>> v6 = convert.proper_motion(v6, tt, tpm.J2000)

  >>> v6_app = convert.convertv6(v6, s1=6, s2=19, utc=utc)

  >>> d = convert.v62cat(v6_app)
  >>> print tpm.r2d(d['alpha']), 90 - tpm.r2d(d['delta'])
  133.49820871 22.0162437585

To calculate the observed hour angle and declination the `v6_app`
vector obtained above can be used as input. We don't need to go back to
the FK5 equinox and epoch J2000.0 values. The input state is now `19`
and the output, i.e., topocentric observed HA & Dec, is `20`.

::

  >>> v6_hadec = convert.convertv6(v6_app, s1=19, s2=20, utc=utc)

  >>> d = convert.v62cat(v6_hadec)
  >>> print tpm.r2d(d['alpha'])
  343.586827647
  >>> print tpm.r2d(d['delta'])
  15.7683070508

To calculate the observed RA we need to find the LAST, since TPM only
provides apparent RA. The observed RA can be found by subtracting hour
angle from LAST. This is one situation where we need to access the
underlying TPM machinery provided in `pytpm.tpm`. Please consult the
TPM manual and the PyTPM documentation for more information.

::

  >>> tstate = tpm.TSTATE()
  >>> tpm.tpm_data(tstate, tpm.TPM_INIT)
  >>> tstate.utc = utc
  >>> tstate.delta_ut = tpm.delta_UT(utc)
  >>> tstate.delta_at = tpm.delta_AT(utc)
  >>> tstate.lon = tpm.d2r(-111.598333)
  >>> tstate.lat = tpm.d2r(31.956389)
  >>> tpm.tpm_data(tstate, tpm.TPM_ALL)
  >>> last = tpm.r2d(tpm.r2r(tstate.last))
  >>> last - tpm.r2d(d['alpha']) + 360.0
  185.85569737491355  

The same calculation with SLALIB, using `sla_aop` produces results that
agree with PyTPM.

::

  >>> dut = tpm.delta_UT(tpm.gcal2j(2010, 1, 1))  # DUT for mid-day.
  >>> utc = slalib.sla_caldj(2010, 1, 1)[0] + 0.5  # mid-day.
  >>> tt = slalib.sla_dtt(utc) / 86400.0 + utc

  >>> r, d = slalib.sla_map(ra_j2000, dec_j2000, 0, 0, 0, 0.0, 2000.0,
     ...: tt)

  >>> lon = tpm.d2r(-111.598333)
  >>> lat = tpm.d2r(31.956389)

  >>> az, zd, ha, dec, ra = slalib.sla_aop(r, d, utc, dut, lon, lat,
     ...: 2093.093, 0, 0, 273.15, 1013.25, 0, 0.550, 0.0065)

  >>> tpm.r2d(tpm.r2r(az)), tpm.r2d(tpm.r2r(zd))
  133.498195532 22.0162383595

The hour angle, declination and right ascension are::

  >>> print tpm.r2d(tpm.r2r(ha))
  343.586827289
  >>> print tpm.r2d(tpm.r2r(dec))
  15.7683143606
  >>> print tpm.r2d(tpm.r2r(ra))
  185.855680678

Consult the appropriate section of the PyTPM documentation for a
detailed comparison between PyTPM and SLALIB.

Converting positions and velocities
-----------------------------------

Converting positions and velocities follow exactly the same procedure
as the examples shown above. The `convert.cat2v6` function will take
proper motions, radial velocity and parallax in addition to
position. The returned dictionary will have appropriate fields for
final proper motions, radial velocity and parallax.

See the file `doc/examples/conversions.py` for a full example. The file
is also included with the HTML documentation and with the source
distribution. 

For example if `tab` is a table that contains full 6-D coordinates with
keys `ra`, `dec`, `pma`, `pmd`, `px` and `rv`, then a full `V6C` vector
can be constructed as::

  >>> v6 = convert.cat2v6(tab['ra'], tab['dec'], tab['pma'],
     ...: tab['pmd'], tab['px'], rv, tpm.CJ)

See docstring of the `convert.convertv6` function for the required units
for each of these.

To convert this from, say FK5 to Ecliptic, at the same epoch, we can
use::

  >>> v6o = convert.convertv6(v6, s1=6, s2=3)
  >>> cat = convert.v62cat(v6o)

The variable `cat` will contain a dictionary, or a list of
dictionaries, with the relevant catalog quantities. See the docstring
of this `convert.v62cat` for units of output quantities.


Credits and license
===================

`Jeffrey W Percival`_ wrote the TPM__ C library. See
`src/tpm/TPM_LICENSE.txt` for TPM license.

The version used here was obtained from the coords_ package (version
0.36) of the astrolib_ library. Some C source files missing from the
above source were provided by Jeff Percival.

Python and Cython code for PyTPM is released under the BSD license; see
`LICENSE.txt`.

Please send email to *prasanthhn*, at the *gmail.com* domain, for
reporting errors, and for comments and suggestions.

__ `Telescope Pointing Machine`_

..  LocalWords:  pyslalib SLALIB sla caldj utc tstate TPM PyTPM pytpm tpm WIYN
..  LocalWords:  numpydoc GCC virtualenvwrapper virtualenv LocalWords ReST
..  LocalWords:  docstring
