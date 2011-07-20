Python interface to the TPM C library
=====================================

.. _Telescope Pointing Machine: http://www.sal.wisc.edu/~jwp/astro/tpm/tpm.html
.. _Jeff Percival: http://www.sal.wisc.edu/~jwp/
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

PyTPM is a Python interface to the TPM library, generated using
Cython_.  TPM, `Telescope Pointing Machine`_ , is a C library written
by `Jeff Percival`_, for performing coordinate conversions between
several astronomical coordinate systems. It was designed with the aim
of incorporating it into telescope control systems and hence the
name. It is used by the `KPNO WIYN observatory`_ and the WHAM_ project
for calculating directions to astronomical objects. The TPM C source
code used here was copied from the astrolib_ project, and additional C
source files were provided by Jeff Percival.

In addition to most of the functions, macros, constants and structures
defined in TPM, this module also provides a few convenience function in
the module ``pytpm.convert``. The functions in this module provides a
simple interface to performing coordinate conversions.

Installing PyTPM
================

Requirements
------------

+ A recent version of Python and gcc.
+ The Distribute_ package.
+ Cython_, only if the Cython output needs to be regenerated.

This library was tested using Python 2.6/2.7, gcc 4.4 and Cython 0.14 on
Ubuntu 10.10 and Ubuntu 11.04.

To build the documentation Sphinx_ and the numpydoc_ Sphinx extension are
required. 

Installation
------------

.. important::

    The file `src/tpm/delta_AT.c` must be updated when Delta-AT
    is changed by the IERS_, and PyTPM Cython code must
    re-compiled. Update the file and just run setup.py again.

If you don't have Distribute_, then install it by following the
instructions 
`here <http://pypi.python.org/pypi/distribute#distribute-setup-py>`_.

#. Install pip/easy_install and then run `pip install pytpm` or
   `easy_install pytpm`.

or 

#. Download the distribution by clicking the *Download* button in the
   `Github repository page <https://github.com/phn/pytpm>`_ or from the
   `pypi page <http://pypi.python.org/pypi/PyTPM>`_. Then run `python
   setup.py install`. Use the `--prefix <dest>` or `--user` arguments
   to change the install location.

Examples
========

For detailed information on the constants, data structures and
functions in PyTPM, see the reference section in the documentation.

::

    >>> import pytpm

    >>> from pytpm import tpm, convert

  
Convert astronomical coordinates between different systems
----------------------------------------------------------

PyTPM can be used to convert positions and velocities in a given
astronomical coordinate system into another. Examples of doing this are
in the ``examples`` folder of the source code and documentation. You
should read the TPM manual before attempting to use these advanced
features.

For the most common coordinate conversion, i.e., converting two angles
in one system into those in another system, a convenience function is
provided with PyTPM: ``pytpm.convert.convert``.  

The signature of this function is::

    def convert(ra, de,
            s1=tpm.TPM_S06, s2=tpm.TARGET_OBS_AZEL,
            epoch=tpm.J2000, equinox=tpm.J2000,
            utc=tpm.utc_now(),
            delta_at=tpm.delta_AT(tpm.utc_now()),
            delta_ut=tpm.delta_UT(tpm.utc_now()),
            lon=-111.598333,
            lat=31.956389,
            alt=2093.093,
            xpole=0.0, ypole=0.0,
            T=273.15, P=1013.25, H=0.0,
            wavelength=0.550):

The arguments to this function are given in the table below; all
arguments, except for the input angles, have defaults. Also note that
not all values are needed for many types of coordinate conversions.

+------------+----------------------------------------------------+
| Parameter  | Description                                        |
+============+====================================================+
| x          | input RA like angle in degrees (RA, longitude, Az) |
+------------+----------------------------------------------------+
| y          | input DE like angle in degrees (DE, latitude, El)  |
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
|            | defaults to the current UTC                        |
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
(*TSTATE* in PyTPM). There are 21 states, plus a "null" state, defined
in TPM. These are given below. The states can be identified using
integers or the special integer constants.

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


So to convert RA and DE from FK5 (equinox and epoch J2000) to Galactic
coordinates, we execute::

    >>> ra = 359.97907800
    >>> de = -65.57713200
    >>> from pytpm import tpm, convert
    >>> l,b = convert.convert(ra, de, s1=tpm.TPM_S06, s2=tpm.TPM_S04)
    >>> l
        -48.699664474942672
    >>> b
        -50.705816281924577

The following code converts the `coordinates of M100`_ between
different systems.

.. _coordinates of M100: http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=M100&submit=SIMBAD+search

>>> from pytpm import tpm, convert

>>> # FK5 epoch=J2000, equinox=J2000 to Galactic coordinates epoch=J2000
>>> ra2000 = tpm.HMS(hh=12,mm=22,ss=54.899).to_degrees()
>>> de2000 = tpm.DMS(dd=15,mm=49,ss=20.57).to_degrees()
>>> l,b = convert.convert(ra2000, de2000, s1=tpm.TPM_S06, s2=tpm.TPM_S04)
>>> l,b
    (-88.863860438221522, 76.898868975136054)
>>> l+360.0,b
    (271.13613956177846, 76.898868975136054)

>>> # FK4 epoch=B1950, equinox=B1950 to Galactic coordinates epoch=B1950
>>> ra1950 = tpm.HMS(hh=12,mm=20,ss=22.94).to_degrees()
>>> de1950 = tpm.DMS(dd=16, mm=5, ss=58.2).to_degrees()
>>> l,b = convert.convert(ra1950, de1950, s1=tpm.TPM_S05, s2=tpm.TPM_S04)
>>> l+360.0,b
    (271.13611058008075, 76.898921112825732)

>>> # FK4 epoch=B1950 equinox=B1950 to FK5 epoch=J2000, equinox=J2000
>>> ra,de = convert.convert(ra1950, de1950, s1=tpm.TPM_S05,
   ....: s2=tpm.TPM_S06, epoch=tpm.B1950, equinox=tpm.B1950)
>>> print tpm.HMS(d=ra+360.0), tpm.DMS(dd=de)
 12H 22M 54.895S +15D 49' 20.528"

>>> # FK5 epoch=J2000, equinox=J2000 to FK4 epoch=B1950, equinox=B1950
>>> ra,de = convert.convert(ra2000, de2000, s1=tpm.TPM_S06, 
   ....: s2=tpm.TPM_S05, epoch=tpm.J2000, equinox=tpm.J2000)
>>> print tpm.HMS(d=ra+360.0), tpm.DMS(dd=de)
 12H 20M 22.935S +16D 05' 58.024"


Credits
=======

`Jeff Percival`_ wrote the TPM__ C library. See
``src/tpm/TPM_LICENSE.txt`` for TPM license. The version used here was
obtained from the coords_ package of the astrolib_ library. Send email
to user prasanthhn, at the gmail.com domain, for reporting errors,
comments, suggestions etc., for the PyTPM library.

__ Telescope Pointing Machine

License
=======

See ``src/tpm/TPM_LICENSE.txt`` for TPM license. Code for the Python
binding itself is released under the BSD license; see LICENSE.txt.
