============================================
 Coordinate conversions using TPM and PyTPM
============================================

.. _asciitable: http://cxc.harvard.edu/contrib/asciitable/
.. _asciidata: http://www.stecf.org/software/PYTHONtools/astroasciidata/
.. _atpy: http://atpy.github.com/

.. _KPNO: http://www.noao.edu/kpno
.. _coordinates of M100: http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=M100&submit=SIMBAD+search
.. _pyslalib: https://github.com/scottransom/pyslalib

.. currentmodule:: pytpm

Please read the :ref:`TPM manual <tpm_manual>` to learn the details of
using TPM for performing coordinate conversions.

For a detailed list of functions and constants defined in PyTPM, see
the section on :doc:`functions`. For detailed information on the data
structures defined in PyTPM, see the section on :doc:`data_structures`.

See :doc:`comparisons` for a comparison of results obtained using
PyTPM, with those obtained using SLALIB.

.. contents::

In this document several examples of using PyTPM module for performing
coordinate conversions will be presented. 

In the following examples `coordinates of M100`_ is converted between
different systems. TPM can convert both positions and velocities. For
M100 only the position are significant, except for the FK5-FK4
conversion. The section :ref:`convert_pos_vel` has examples of
converting positions and velocities, with data from HIPPARCOS catalog.
Also, the examples here use the convenience function
:func:`convert.convertv6`, instead of directly using the 
underlying TPM functions.

As mentioned before, facilities in TPM that are wrapped by PyTPM are
provided in the module `pytpm.tpm`. The `pytpm.convert`
module contains a few convenience functions for performing coordinate
conversions. We can load both of these modules in the following manner.

.. code-block:: python

    >>> from pytpm import tpm, convert

Function `convert.convertv6`
============================

The :func:`convert.convertv6` function aims to present an easy to use
interface to TPM that allows easy coordinate conversions. It takes a
large set of input, sets up TPM, performs the conversions, and returns
the final coordinates. The source code of this function also serves as
an example of using TPM.

This function takes the following arguments. Not all of these need to
be specified for a given conversion.

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

A :class:`tpm.V6C` object is a 6-D vector that stores positions and
velocities in Cartesian coordinates. 

The function :func:`convert.cat2v6` can be used to create a `V6C`
object from catalog data.  This function will accept scalar or list of
coordinates, and will return a list of `V6C` vectors.

Function :func:`convert.v62cat` can convert `V6C` objects to catalog
coordinates. The coordinates are returned as a dictionary. This
function will also take a list of `V6C` objects and will return a list
of dictionaries.

Coordinate systems in TPM are specified using integers or integer
constants. These are referred to as `states`.The following lists the
states defined in TPM. Note that each of these states are just
integers: ``TPM_S02 == 2``, ``TPM_S13 == 13`` and so on.

.. _tpm_state_names:

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
| TARGET_FK4        |       TPM_S01     |  
+-------------------+-------------------+
| TARGET_FK5        |       TPM_S02     |
+-------------------+-------------------+
| TARGET_ECL        |       TPM_S03     |
+-------------------+-------------------+
| TARGET_GAL        |       TPM_S04     |
+-------------------+-------------------+
| TARGET_APP_HADEC  |       TPM_S17     |
+-------------------+-------------------+
| TARGET_OBS_HADEC  |       TPM_S20     |
+-------------------+-------------------+
| TARGET_APP_AZEL   |       TPM_S18     |
+-------------------+-------------------+
| TARGET_OBS_AZEL   |       TPM_S19     |
+-------------------+-------------------+
| TARGET_OBS_WHAM   |       TPM_S21     |
+-------------------+-------------------+

FK5 equinox and epoch J2000.0, to FK4 equinox and epoch B1950.0
===============================================================

First obtain the `FK5 equinox J2000.0 and epoch J2000.0` RA and Dec
coordinates in radians.

::

  >>> ra_j2000 = tpm.HMS(hh=12, mm=22, ss=54.899).to_radians()
  >>> dec_j2000 = tpm.DMS(dd=15, mm=49, ss=20.57).to_radians()

Create a :class:`tpm.V6C` vector for the object. Note
that :func:`convert.cat2v6` will accept a list of coordinates as well.

::

  >>> v6 = convert.cat2v6(ra_j2000, dec_j2000)

Now convert to `FK4 equinox B1950.0, but remaining at epoch J2000.0`.

In the following `6` stands for `FK5 equinox J2000.0` coordinates and
`5` stands for `FK4 equinox B1950.0`. The epoch and equinox are
specified using `epoch` and `equinox` keywords. They can be interpreted
in different ways depending on the exact conversion requested. They are
also used only for certain calculations. In the present case, they are
applicable to the input coordinates. Read the :ref:`TPM manual
<tpm_manual>` for more information.

::

  >>> v6_fk4 = convert.convertv6(v6, s1=6, s2=5, epoch=tpm.J2000, 
     ...: equinox=tpm.J2000)

Convert `V6C` to catalog data and print results. Function
:func:`convert.v62cat` will also accept a list of V6C vectors.

::

  >>> d = convert.v62cat(v6_fk4, C=tpm.CB)
  >>> print tpm.HMS(r=d['alpha'])
   12H 20M 22.935S
  >>> print tpm.DMS(r=d['delta'])
  +16D 05' 58.024"

The parameter `C` is the number of days in a century. The velocities in
:class:`tpm.V6C` vectors are stored AU/day. These Cartesian velocities 
must be converted to catalog proper motions. The latter are expressed
in arc-secs/century. 

In the Besselian system a century has approximately 36524.22 days,
where as in the Julian system a century has exactly 36525.0 days. The
former is used in FK4 and the latter is used in FK5. The default value
is set to 36525.0. These two values are provided as the constants
`tpm.CB` and `tpm.CJ`, respectively; see :ref:`tpm_constants`.

Note that the results above *do not agree* with the FK4 values given by
SIMBAD. This is because the results are for the epoch J2000.0, i.e.,
`FK4 equinox B1950.0 epoch J2000.0`. Even though the object doesn't
have proper motion, the FK4 system is rotating with respect to
FK5. This results in a *fictitious proper motion in the FK4 system*. We
must apply proper motion from epoch J2000.0 to epoch B1950.0 to get the
final result, i.e., FK4 equinox B1950.0 epoch B1950.0.

::

  >>> v6_fk4_ep1950 = convert.proper_motion(v6_fk4, tpm.B1950, tpm.J2000)

Finally convert `V6C` to catalog data and print results. The final
result is in `FK4 equinox and epoch B1950.0`. The final results agree
with the values given by SIMBAD.

::

  >>> d = convert.v62cat(v6_fk4_ep1950, C=tpm.CB)
  >>> print tpm.HMS(r=d['alpha'])
   12H 20M 22.943S
  >>> print tpm.DMS(r=d['delta'])
  +16D 05' 58.241"


FK5 equinox and epoch J2000.0, to IAU 1958 Galactic System
==========================================================

The IAU 1958 galactic system is represented using state `4`. The result
below is for the epoch J2000.0, since the input coordinates are at
epoch J2000.0. The epoch of the galactic coordinates given by SIMBAD is
J2000.0. So the result obtained below is what we need, i.e., we don't
need to apply any proper motion corrections.

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


IAU 1958 Galactic, to FK5 equinox and epoch J2000.0
===================================================

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
coordinates. When converting from Galactic to FK5, we pass through the
FK4 system. The lack of proper motion information in the Galactic
system affects the accuracy here. Usually, in catalogs we are
interested in converting FK5 to Galactic, and we do not notice this.

FK5 equinox and epoch J2000.0, to IAU 1980 Ecliptic system
==========================================================

The ecliptic system is indicated using the state `3`. Here the epoch of
the output ecliptic coordinates will be J2000.0, as the input
coordinates are at epoch J2000.0.

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

The results agree with the results from the SLALIB (pyslalib_) routine
`sla_eqecl`.

See :doc:`comparisons` for a more detailed comparison between PyTPM and
SLALIB.

IAU 1980 Ecliptic system, to FK5 equinox and epoch J2000.0
==========================================================

The starting state is set to `3` for ecliptic and the end state is set
to `6` for FK5 equinox J2000.0.

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


FK5 equinox and epoch J2000.0, to Geocentric apparent
=====================================================

Geocentric apparent RA & Dec. for midnight of 2010/1/1 can be
calculated as shown below. The state identification number for
geocentric apparent position is `11`, as shown in the :ref:`table above
<tpm_state_names>`.

Obtain UTC and TDB time for the time of observation.

::

  >>> utc = tpm.gcal2j(2010, 1, 1) - 0.5  # midnight
  >>> tdb = tpm.utc2tdb(utc)

Obtain coordinates and :class:`V6C` vector.

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


See :doc:`comparisons` for a more detailed comparison between PyTPM and
SLALIB.

FK5 equinox and epoch J2000.0, to topocentric observed
======================================================

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
underlying TPM machinery provided in `pytpm.tpm`.

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
  
See :doc:`comparisons` for a more detailed comparison between PyTPM and
SLALIB.

.. _convert_pos_vel:

Converting positions and velocities
===================================

Converting position and velocities involve the exact same procedures as
in the above sections. The only difference is that we provide
velocities in addition to positions and the output will have both the
converted positions as well as the converted velocities.

All these files mentioned below are available in the :file:`examples/`
directory of the documentation source code (:file:`_downloads` in the
HTML distribution).

The examples shown here are available in
the :download:`examples/conversions.py` file. 

The file :download:`examples/hip_full.txt` contains data from the
HIPPARCOS catalog. This file was generated using
the :download:`examples/hip_full.py` script. We will convert this data
between different coordinate systems.

The `get_hipdata` function below is one way of reading in the data
in :file:`hip_full.txt`. With table reading packages such as
asciitable_, asciidata_ and atpy_, or the `numpy.loadtxt` function,
this function is not needed. The calculations are much easier to
perform with Numpy. PyTPM does not need Numpy or table reading
software. Hence I want to have examples that don't use these, even
though the calculations are harder.

.. code-block:: python

  import csv
  import math
  from pytpm import tpm, convert
   
  def get_hipdata():
      """Return data in hip_full.txt.
   
      The data was created with hip_full.py file. Assumes that the file
      hip_full.txt is in the current directory.
   
      A dictionary is returned. All positions are in radians. Proper
      motions are in arc-sec per Julian century. Parallax is in
      arc-sec. The keys are:
   
        ra_icrs: ICRS RA
        dec_icrs: ICRS Dec
        raj2: RA J2000
        decj2: Dec J2000
        rab1: RA B1950
        decb1: Dec B1950
        glon: Galactic longitude (epoch J2000)
        glat: Galactic latitude (epoch J2000)
        elon2: Ecliptic longitude (epoch J2000)
        elat2: Ecliptic latitude (epoch J2000)
        pma: proper motion in RA (without cos(dec) factor)
        pmd: proper motion in Dec
        px: parallax.
   
      """
      f = open("hip_full.txt", "r")
      s = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                     delimiter=" ", skipinitialspace=True)
      d = dict(ra_icrs=[], dec_icrs=[], px=[], pma=[], pmd=[],
               raj2=[], decj2=[], rab1=[], decb1=[], glon=[],
               glat=[], elon2=[], elat2=[])
   
      for i in s:
          d["ra_icrs"].append(math.radians(i[0]))
          d["dec_icrs"].append(math.radians(i[1]))
          d["raj2"].append(math.radians(i[5]))
          d["decj2"].append(math.radians(i[6]))
          d["rab1"].append(math.radians(i[7]))
          d["decb1"].append(math.radians(i[8]))
          d["glon"].append(math.radians(i[9]))
          d["glat"].append(math.radians(i[10]))
          d["elon2"].append(math.radians(i[11]))
          d["elat2"].append(math.radians(i[12]))
   
          # milli-arc-sec/jul yr to arc-sec per Jul. cent.
          # And take out cos in RA proper motion.
          d["pma"].append(i[3] / math.cos(d["decj2"][-1]) / 1000.0 * 100.0)
          d["pmd"].append(i[4] / 1000.0 * 100.0)
   
          # milli-arsec to arc-sec
          d["px"].append(i[2] / 1000.0)
   
      f.close()
      return d


First read in the data and create :class:`tpm.V6C` vectors. Since we
don't have radial velocities, we will set it to 0.0.

.. code-block:: python

  hip_tab = get_hipdata()
  # Dummy radial velocities.
  rv = [0.0 for i in range(len(hip_tab['px']))]
  # Create V6C vectors.
  v6 = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], hip_tab['pma'],
                  hip_tab['pmd'], hip_tab['px'], rv, tpm.CJ)


Subsequent steps are identical to those for converting positions. For
example for the FK5 to FK4 conversions we can do:

.. code-block:: python

  # Convert from FK5 equinox and epoch J2000.0 to FK4 equinox B1950, but
  # at the given epoch i.e., J2000.0.
  v6o = convert.convertv6(v6, s1=6, s2=5, epoch=tpm.J2000)
   
  # Apply proper motion from J2000.0 to B1950.0. Objects with zero
  # velocity in FK5 will have a fictitious proper motion in FK4.
  v6o = convert.proper_motion(v6o, tpm.B1950, tpm.J2000)
   
  # Convert V6C vectors into a list of dictionaries, each of which
  # contain the 6-D Fk4 B1950.0 coordinates.
  cat = convert.v62cat(v6o, tpm.CB)


The variable `cat` will be a list of dictionaries, each containing the
FK4 coordinates of the corresponding entry in the `hip_full.txt` file.

We can print out the first of these and compare the result with the
FK4 data in `hip_full.txt`.

.. code-block:: python

  >>> print tpm.HMS(r=hip_tab['rab1'][0])  # HIPPAROCS FK4 from Vizier.
   23H 57M 26.475S
  >>> print tpm.HMS(r=c['alpha'])  # PyTPM output.
   23H 57M 26.474S
  >>> print tpm.DMS(r=hip_tab['decb1'][0])
  +00D 48' 38.264"
  >>> print tpm.DMS(r=c['delta'])
  +00D 48' 38.257"

Similarly FK5 to ecliptic conversion can be performed in the following
manner.

.. code-block:: python

   # FK5 equinox and epoch J2000.0, to IAU 1980 ecliptic J2000.0
   v6o = convert.convertv6(v6, s1=6, s2=3)
   # Convert V6C vectors into a list of dictionaries, each of which
   # contain the 6-D Fk4 B1950.0 coordinates.
   cat = convert.v62cat(v6o, tpm.CJ)

We can compare the result with that in the HIPPARCOS catalog returned
by Vizier.

.. code-block:: python

  >>> print tpm.HMS(r=hip_tab['elon2'][0])  # Ecliptic data from Vizier cat.
   00H 01M 44.172S
  >>> print tpm.HMS(r=c['alpha'])  # PyTPM conversion of FK5.
   00H 01M 44.172S
  >>> print tpm.DMS(r=hip_tab['elat2'][0])
  +00D 59' 55.604"
  >>> print tpm.DMS(r=c['delta'])
  +00D 59' 55.604"

All other conversions can be performed in the same manner.


PyTPM and TPM
=============

All the facilities of TPM can be used form within Python, using
functions and classes.

The following are C and Python code that perform equivalent
conversions. The code takes the FK5 J2000.0 equinox and epoch
coordinates of M100 through all coordinate systems defined in
TPM. 

These, and the source code for the `convert` module, should allow
translation of TPM C code to PyTPM Python code.

These code fragments can be found
in :download:`examples/conversion_example.c`
and :download:`examples/conversion_example.py`, respectively. 

Note that the conversions themselves are not accurate, since we do not
apply any proper motions. They are meant to compare C and Python code.

C code
------

.. code-block:: c

  #include "tpm/astro.h"
  #include <stdio.h>
  #include <math.h>
   
  /* Take a coordinate through all states. */
  /* Coordinates for M100 from SIMBAD. */
   
  int main(){
    double ra = (12+22/60.0+54.899/3600.0) * (2*M_PI/24.0);
    double de = (15+49/60.0+20.57/3600.0) * (2*M_PI/360.0);
    double ra1, ra1_d, de1, de1_d;
    double ep = J2000;
    double eq = J2000;
    V6 v6;
    V6 pvec[N_TPM_STATES];
    TPM_TSTATE tstate;
    int s1 = TPM_S06; /* Heliocentric mean J2000 FK5 ~~ ICRS */
    int s2 = TPM_S00; /* Assign required states. */
   
    for(int i=TPM_S00; i < N_TPM_STATES; i ++){
      tpm_data(&tstate, TPM_INIT);
      tstate.utc = J2000;
      tstate.lon = d2r(-111.598333);
      tstate.lat = d2r(31.956389);
      tstate.alt = 2093.093;
      tstate.delta_ut = delta_UT(tstate.utc);
      tpm_data(&tstate, TPM_ALL);
       
      v6 = v6init(SPHERICAL);
      v6SetR(v6, 1e9);
      v6SetAlpha(v6, ra);
      v6SetDelta(v6, de);
       
      pvec[s1] = v6s2c(v6);
      s2 = i;
      tpm(pvec, s1, s2, ep, eq, &tstate);
      v6 = v6c2s(pvec[s2]);
       
      ra1 = v6GetAlpha(v6);
      de1 = v6GetDelta(v6);
      ra1_d = r2d(ra1);
      if (ra1_d < 0.0) ra1_d += 360.0;
      de1_d = r2d(de1);
      if (de1_d < 0.0) de1_d += 360.0;
   
      printf("%02d-%02d %-17s %s %s %8.4f %8.4f\n", s1, s2, 
        tpm_state(s2), fmt_alpha(ra1), fmt_delta(de1), ra1_d, de1_d);
    }
    return 0;
  }


.. _pytpm-full-conversion:

PyTPM code
----------

.. code-block:: python

  # Take coordinates of M100 through all states.
  from pytpm import tpm
   
  ra = tpm.h2r(12+22/60.0+54.899/3600.0)
  de = tpm.d2r(15+49/60.0+20.57/3600.0)
  ep = tpm.J2000
  eq = tpm.J2000
  s1 = tpm.TPM_S06
  s2 = tpm.TPM_S00
  tstate = tpm.TSTATE()
  pvec = tpm.PVEC()
   
  for i in range(tpm.N_TPM_STATES):
      tpm.tpm_data(tstate, tpm.TPM_INIT)
      tstate.utc = tpm.J2000
      tstate.lon = tpm.d2r(-111.598333)
      tstate.lat = tpm.d2r(31.956389)
      tstate.alt = 2093.093
      tstate.delta_ut = tpm.delta_UT(tstate.utc)
      tpm.tpm_data(tstate, tpm.TPM_ALL)
   
      v6 = tpm.V6S()
      v6.r = 1e9
      v6.alpha = ra
      v6.delta = de
      
   
      pvec[s1] = v6.s2c()
      s2 = i
      tpm.tpm(pvec, s1, s2, ep, eq, tstate)
      v6 = pvec[s2].c2s()
   
      ra1 = v6.alpha
      de1 = v6.delta
      ra1_d = tpm.r2d(ra1)
      if ra1_d < 0.0 : ra1_d += 360.0
      de1_d = tpm.r2d(de1)
      if de1_d < 0.0 : de1_d += 360.0
   
      s = "{0:02d}-{1:02d} {2:<17s} {3:s} {4:s} {5:8.4f} {6:8.4f}"
      print s.format(s1, s2, tpm.tpm_state(s2),
                     tpm.fmt_alpha(ra1), tpm.fmt_delta(de1), ra1_d,
                     de1_d)

      
We create a state structure, :class:`tpm.TSTATE`, and initialize it by 
calling
:func:`tpm.tpm_data()` with `TPM_INIT`. Then we assign values to 
independent parameters of the state data structure. We then calculate
all dependent state properties by calling `tpm_data()` and passing
`TPM_ALL`. We then create an array of :class:`tpm.V6C` vectors, `pvec`
(:class:`tpm.PVEC`), create a `V6C` vector for our object, and assign
it to the desired location in the array, based on the starting
state. We then call :func:`tpm.tpm()` with the state structure and the
array of `V6C` vectors, along with the starting and ending state
numbers. Finally we retrieve the appropriate `V6C` vector from the
array, which will give us the final coordinates.

         
The result from running the above code is given below::

 06-00 null               12H 22M 54.898S +15D 49' 20.570" 185.7287  15.8224
 06-01 Helio. mean FK4    12H 22M 54.824S +15D 49' 20.447" 185.7284  15.8223
 06-02 Helio. mean FK5    12H 22M 54.898S +15D 49' 20.570" 185.7287  15.8224
 06-03 IAU 1980 Ecliptic  11H 55M 07.815S +16D 45' 34.920" 178.7826  16.7597
 06-04 IAU 1958 Galactic  18H 04M 32.673S +76D 53' 55.928" 271.1361  76.8989
 06-05 Helio. mean FK4    12H 20M 22.935S +16D 05' 58.024" 185.0956  16.0995
 06-06 Helio. mean FK5    12H 22M 54.898S +15D 49' 20.570" 185.7287  15.8224
 06-07 Geoc. mean FK5     12H 22M 54.899S +15D 49' 20.569" 185.7287  15.8224
 06-08 S07 + Light Defl.  12H 22M 54.898S +15D 49' 20.571" 185.7287  15.8224
 06-09 S08 + Aberration   12H 22M 54.995S +15D 49' 13.474" 185.7291  15.8204
 06-10 S09 + Precession   12H 22M 54.995S +15D 49' 13.474" 185.7291  15.8204
 06-11 Geoc. app. FK5     12H 22M 54.045S +15D 49' 19.561" 185.7252  15.8221
 06-12 Topo. mean FK5     12H 22M 54.899S +15D 49' 20.569" 185.7287  15.8224
 06-13 S12 + Light Defl.  12H 22M 54.898S +15D 49' 20.571" 185.7287  15.8224
 06-14 S13 + Aberration   12H 22M 55.013S +15D 49' 13.452" 185.7292  15.8204
 06-15 S14 + Precession   12H 22M 55.013S +15D 49' 13.452" 185.7292  15.8204
 06-16 Topo. app. FK5     12H 22M 54.063S +15D 49' 19.539" 185.7253  15.8221
 06-17 Topo. app. HA/Dec  22H 52M 35.524S +15D 49' 19.539" 343.1480  15.8221
 06-18 Topo. app. Az/El   08H 50M 11.837S +67D 45' 09.683" 132.5493  67.7527
 06-19 Topo. obs. Az/El   08H 50M 11.837S +67D 45' 34.371" 132.5493  67.7595
 06-20 Topo. obs. HA/Dec  22H 52M 36.636S +15D 49' 38.307" 343.1527  15.8273
 06-21 Topo. obs. WHAM    22H 52M 56.457S -14D 49' 46.993" 343.2352 345.1703


..  LocalWords:  PyTPM TPM LocalWords

..  LocalWords:  TPM FK currentmodule PyTPM SLALIB pytpm kpno func convertv TPM
..  LocalWords:  docstring LocalWords tpm pyslalib kpno SLALIB
