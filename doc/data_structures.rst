=================
 Data Structures
=================

.. currentmodule:: pytpm.tpm

PyTPM wraps many of the C structures in TPM as Python classes, using
Cython *extension types* or *cdef* classes. 

Note that these are only useful in the context of their usage in
PyTPM. Defining these structures make it easy to call the various TPM C
functions from within Python. They are neither complete nor should be
used in general handling of dates, times and vectors. The Python
standard library *dateutil* provides mechanism for handling date and
time. *Numpy* is a vector and matrix library.

.. contents::

Classes for representing angles
===============================

There are two classes for storing angles. ``DMS`` for degrees,
arc-minutes and arc-seconds, and ``HMS`` for hours, minutes and
seconds. Objects of these classes can be initialized by passing scalar
value of the angle in any of the three formats for representing angles:
radians, hours, and degrees. 

``DMS``
-------

.. autoclass:: DMS
   :members:

A ``DMS`` structure stores an angle in decimal degrees, as a degrees
part, ``DMS.dd``, an arc-minutes part, ``DMS.mm`` and an arc-seconds
part, ``DMS.ss``. An object of this type can be initialized by passing
an angle in several ways. If the keyword ``r`` is given then the input
angle is taken to be in radians and all other keywords are ignored. If
the keyword ``h`` is present then the angle is assumed to be in hours
and the rest of the keywords are ignored. If neither of theses are
present then, the values of the keywords ``dd``, ``mm`` and ``ss`` are
assigned to the corresponding attribute of the object.

.. code-block:: python

    >>> dms = tpm.DMS(r=tpm.M_PI)
    >>> dms.dd, dms.mm, dms.ss
    (180.0, 0.0, 0.0)
    >>> dms
        {'mm': 0.0, 'ss': 0.0, 'dd': 180.0}

    >>> dms = tpm.DMS(h=12.0)
    >>> dms
        {'mm': 0.0, 'ss': 0.0, 'dd': 180.0}

    >>> dms = tpm.DMS(dd=180.0)
    >>> dms
        {'mm': 0.0, 'ss': 0.0, 'dd': 180.0}

    >>> dms = tpm.DMS(ss=180.0*3600)
    >>> dms
        {'mm': 0.0, 'ss': 648000.0, 'dd': 0.0}

    >>> dms = tpm.DMS(dd=1.0,mm=20.3,ss=12.45)
    >>> dms
        {'mm': 20.300000000000001, 'ss': 12.449999999999999, 'dd': 1.0}

The components can be assigned to after the creation of the object, by
accessing the ``dd``, ``mm`` and ``ss`` attributes of the ``DMS``
object.

.. code-block:: python

    >>> dms = tpm.DMS()
    >>> dms.dd = 10.23
    >>> dms.mm = 12.3
    >>> dms.ss = 2.3
    >>> dms.dd, dms.mm, dms.ss
        (10.23, 12.300000000000001, 2.2999999999999998)
    >>> print dms
    --> print(dms)
    +10D 26' 08.299"

A ``DMS`` object can be converted into a string by passing it to the
``str()`` or ``unicode()`` functions. It will get converted into a
string representation of the angle, when printed using the ``print``
statement.

.. code-block:: python

    >>> str(dms)
        '+01D 20\' 30.450"'
    >>> unicode(dms)
        u'+01D 20\' 30.450"'
    >>> print dms
    --> print(dms)
    +01D 20' 30.450"

The method ``normalize()`` will normalize the angle contained in the
``DMS`` object. That is, the ``dd`` and ``mm`` components will be
converted into integer values and the ``ss`` will contain the
fractional parts. This method will modify the ``DMS`` and does not
return any value.

.. code-block:: python

    >>> dms = tpm.DMS(ss=180.0*3600)
    >>> dms.dd, dms.mm, dms.ss
        (0.0, 0.0, 648000.0)
    >>> dms.normalize()
    >>> dms.dd, dms.mm, dms.ss
        (180.0, 0.0, 0.0)


There are a few methods available for converting the angle represented
by a ``DMS`` object into other units.

.. code-block:: python

    >>> # The angle 180 degrees = pi radians = 12 hours.
    >>> dms = tpm.DMS(r=tpm.M_PI)
    >>> dms.to_degrees()
        180.0
    >>> dms.to_radians()
        3.1415926535897931
    >>> dms.to_hours()
        12.0

Two ``DMS`` objects can be added to and subtracted from each other.

.. code-block:: python

    >>> dms = tpm.DMS(dd=12.0)
    >>> dms = dms + tpm.DMS(dd=10.0)
    >>> dms.dd, dms.mm, dms.ss
        (22.0, 0.0, 0.0)
    >>> dms = dms - tpm.DMS(dd=10.0)
    >>> dms.dd, dms.mm, dms.ss
        (12.0, 0.0, 0.0)

A ``DMS`` object can be converted into an ``HMS`` object, discussed
below, using the ``to_hms()`` method. This method will return a new
``HMS`` object.

.. code-block:: python

    >>> dms = tpm.DMS(dd=180.0)
    >>> hms = dms.to_hms()
    >>> hms.hh, hms.mm, hms.ss
        (12.0, 0.0, 0.0)

``HMS``
-------

.. autoclass:: HMS
   :members:

An ``HMS`` object can be used to represent an angle in hours, minutes
and seconds format. It can also be used to store time in the same
units.

Like the ``DMS`` class, it will accept several keywords, that can be
used to initialize it with an angle or a time. If the keyword ``r`` is
present then the angle is assumed to be in radians and all other
keywords are ignored. If the keyword ``d`` is present then the angle is
assumed to be in degrees. If neither of the above are present, then the
keywords ``hh``, ``mm`` and ``ss`` will be used to initialize the
corresponding attributes.

.. code-block: python
     
    >>> hms = tpm.HMS(r=tpm.M_PI/2.0)
    >>> hms.hh, hms.mm, hms.ss
        (6.0, 0.0, 0.0)
    >>> hms = tpm.HMS(d=45.0)
    >>> hms.hh, hms.mm, hms.ss
        (3.0, 0.0, 0.0)
    >>> hms = tpm.HMS(hh=5.0,mm=12.0,ss=1)
    >>> hms.hh, hms.mm, hms.ss
        (5.0, 12.0, 1.0)
    >>> hms = tpm.HMS(ss=12.0)
    >>> hms.hh, hms.mm, hms.ss
        (0.0, 0.0, 12.0)
    >>> hms
        {'mm': 0.0, 'ss': 12.0, 'hh': 0.0}

The components can be assigned to after the creation of the object, by
accessing the ``dd``, ``mm`` and ``ss`` attributes of the ``DMS``
object.

.. code-block:: python

    >>> hms = tpm.HMS()
    >>> hms.hh = 12.0
    >>> hms.mm = 0.34
    >>> hms.ss = 1.05
    >>> hms.hh, hms.mm, hms.ss
        (12.0, 0.34000000000000002, 1.05)
    >>> print hms
    --> print(hms)
     12H 00M 21.450S

An ``HMS`` object can be converted into a string by passing it to the
``str()`` or the ``unicode()`` functions. It will get converted into a
string representation of the angle, when printed using the ``print``
statement.

.. code-block:: python

    >>> hms = tpm.HMS(hh=12.34, mm=54.34, ss=0.34)
    >>> str(hms)
        ' 13H 14M 44.740S'
    >>> unicode(hms)
        u' 13H 14M 44.740S'
    >>> print hms
    --> print(hms)
     13H 14M 44.740S

The method ``normalize()`` will normalize the angle contained in the
``HMS`` object. That is the ``hh`` and ``mm`` components will be
converted into integer values and the ``ss`` component will contain the
fractional parts. This method will modify the ``HMS`` object and does
not return any value.

.. code-block:: python

    >>> hms = tpm.HMS(hh=12.34, mm=54.34, ss=0.34)
    >>> hms.normalize()
    >>> hms.hh, hms.mm, hms.ss
        (13.0, 14.0, 44.740000000000748)

There are a few methods available for converting the angle represented
by an ``HMS`` object into other units.

.. code-block:: python

   >>> hms = tpm.HMS(r=tpm.M_PI)
   >>> hms.to_radians()
       3.1415926535897931
   >>> hms.to_degrees()
       180.0
   >>> hms.to_hours()
       12.0

Two ``HMS`` objects can be added to and subtracted from each other.

.. code-block:: python

    >>> hms = tpm.HMS(r=tpm.M_PI)
    >>> hms = hms + tpm.HMS(hh=2.0)
    >>> hms
        {'mm': 0.0, 'ss': 0.0, 'hh': 14.0}
    >>> hms = hms - tpm.HMS(hh=8.0)
    >>> hms
        {'mm': 0.0, 'ss': 0.0, 'hh': 6.0}

An ``HMS`` object can be converted into a ``DMS`` object using the
``to_dms()`` method. This method will return a new ``DMS`` object.

.. code-block:: python

    >>> hms = tpm.HMS(d=180.0)
    >>> hms
        {'mm': 0.0, 'ss': 0.0, 'hh': 12.0}
    >>> dms = hms.to_dms()
    >>> dms
        {'mm': 0.0, 'ss': 0.0, 'dd': 180.0}


Classes for storing time and date-time
======================================

The class ``YMD`` can be used to store a Gregorian calendar date and
time, where as the class ``JD`` can be used to store a Julian date. As
noted before the ``HMS`` structure can be used to store time in hours,
minutes and seconds.

``YMD``
-------

.. autoclass:: YMD
   :members:

The ``YMD`` class stores year, month, day, hours, minutes and seconds
of a date, in the attributes ``y``, ``m``, ``dd``, ``hh``, ``mm`` and
``ss`` respectively. The first two are integers and the rest are
floating point numbers.

A ``YMD`` object can be initialized by passing date and time in several
ways. If the keyword ``j`` is present then the value is taken to be a
Julian date and the rest of the keywords are ignored. If the keyword
``year`` is present then the value is taken to be years, which can have
a fractional part, and the rest of the keywords are ignored. If the
keyword ``ydd`` is present, the the value must be a tuple of 2
elements, the first being the year, which can have a fractional part
and the second begin the day of the year, which can also have a
fractional part. The rest of the keywords, again gets ignored. If none
of the above are present, then the values from the keywords ``y``,
``m``, ``dd``, ``hh``, ``mm`` and ``ss`` are used to initialize the
object. Here, ``y`` and ``m`` must be integers.

.. code-block:: python

    >>> ymd = tpm.YMD(j=2451545.0)
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2000, 1, 1.5, 0.0, 0.0, 0.0)
    >>> ymd
        {'mm': 0.0, 'dd': 1.5, 'm': 1, 'ss': 0.0, 'hh': 0.0, 'y': 2000}
    >>> ymd = tpm.YMD(year=2000.0)
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2000, 1, 0.0, 0.0, 0.0, 0.0)
    >>> ymd = tpm.YMD(year=2000.5)
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2000, 1, 183.0, 0.0, 0.0, 0.0)
    >>> ymd = tpm.YMD(ydd=(2000,183.0))
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2000, 1, 183.0, 0.0, 0.0, 0.0)
    >>> ymd = tpm.YMD(y=2010,m=4,dd=14)
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2010, 4, 14.0, 0.0, 0.0, 0.0)
    >>> ymd = tpm.YMD(y=2010,m=4,dd=14, hh=12.0, mm=10, ss=20.9)
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2010, 4, 14.0, 12.0, 10.0, 20.899999999999999)
    >>> ymd = tpm.YMD(y=2010)
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2010, 1, 0.0, 0.0, 0.0, 0.0)


The individual components can also be assigned to and modified after
creating the object.

.. code-block:: python

    >>> ymd = tpm.YMD()
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2000, 1, 0.0, 0.0, 0.0, 0.0)
    >>> ymd.y=2010
    >>> ymd.dd = 12
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2010, 1, 12.0, 0.0, 0.0, 0.0)

A ``YMD`` can be converted into a string using the ``str()`` and
``unicode()`` functions and by using the ``print`` statement. The
method ``raw_str()`` that will return a "raw" string representation of
the date and time.

.. code-block:: python

    >>> ymd = tpm.YMD(j=2451545.5)
    >>> str(ymd)
        'Sun Jan  2 00:00:00.000 2000'
    >>> unicode(ymd)
        u'Sun Jan  2 00:00:00.000 2000'
    >>> print ymd
    --> print(ymd)
    Sun Jan  2 00:00:00.000 2000
    >>> ymd.raw_str()
        '2000 1 2 0 0 0'
    >>> ymd = tpm.YMD(j=2451545.5+0.25)
    >>> print ymd
    --> print(ymd)
    Sun Jan  2 06:00:00.000 2000
    >>> ymd.raw_str()
        '2000 1 2.25 0 0 0'


The method ``normalize()`` will normalize the components of a ``YMD``
object. 

.. code-block:: python

    >>> ymd = tpm.YMD(j=2451545.5+0.25)
    >>> ymd
        {'mm': 0.0, 'dd': 2.25, 'm': 1, 'ss': 0.0, 'hh': 0.0, 'y': 2000}
    >>> ymd.normalize()
    >>> ymd
        {'mm': 0.0, 'dd': 2.0, 'm': 1, 'ss': 0.0, 'hh': 6.0, 'y': 2000}


The date and time in a ``YMD`` object can be converted into a scalar
Julian date and a year, with fractional part, using the methods
``to_j()`` and ``to_year`` respectively. The method ``to_jd()`` returns
a ``JD`` object, which is described in the next section. The method
``doy`` returns the time stored in the ``YMD`` as the day of the year,
including fractional part.

.. code-block:: python

    >>> ymd = tpm.YMD(y=2010,m=1, dd=1, hh=12.0, mm=0.0,ss=0.0)
    >>> ymd.to_j()
        2455198.0
    >>> ymd.to_year()
        2010.004109589041
    >>> ymd.doy()
        1.5
    >>> jd = ymd.to_jd()
    >>> jd.dd, jd.hh, jd.mm, jd.ss
        (2455198.0, 0.0, 0.0, 0.0)


``JD``
------

.. autoclass:: JD
   :members:

The ``JD`` class stores date and time in the form of a Julian date. It
stores a Julian date, ``dd``, as well as three attributes, ``hh``,
``mm`` and ``ss`` for the fraction of a day in hours, minutes and
seconds respectively. The value of the Julian date is the sum of ``dd``
with the fraction of the day calculated from ``hh``, ``mm`` and ``ss``.

A ``JD`` object can be initialized by passing date and time in several
formats. If the keyword ``j`` is present then the value is taken to be
a Julian date and all the other keywords are ignored. If the keyword
``year`` is present the value is assumed to be a year with fractional
parts. If neither are present, then the values given by the keywords
``dd``, ``hh``, ``mm`` and ``ss`` are used.

.. code-block:: python

    >>> jd = tpm.JD(j=2451545.0)
    >>> jd
    {'mm': 0.0, 'ss': 0.0, 'dd': 2451545.0, 'hh': 0.0}
    >>> jd.dd, jd.hh, jd.mm, jd.ss
        (2451545.0, 0.0, 0.0, 0.0)
    >>> jd = tpm.JD(year=2000.0+1.5/366)
    >>> jd.dd, jd.hh, jd.mm, jd.ss
        (2451545.5, -12.0, 0.0, 0.0)
    >>> jd = tpm.JD(dd=2451544.0, hh=24.0, mm=0.0, ss=0.0)
    >>> jd.dd, jd.hh, jd.mm, jd.ss
        (2451544.0, 24.0, 0.0, 0.0)

The individual components can also be assigned to and modified after
creating the object.

.. code-block:: python

    >>> jd = tpm.JD()
    >>> jd.dd = 2451545.0
    >>> jd.hh = 12.0
    >>> jd.mm = 45.0
    >>> jd.ss = 12.3
    >>> jd.dd, jd.hh, jd.mm, jd.ss
        (2451545.0, 12.0, 45.0, 12.300000000000001)


A ``JD`` object can be converted into a string using the ``str()`` and
``unicode()`` functions and by using the ``print`` statement.

.. code-block:: python

    >>> jd = tpm.JD(j=2451545.0)
    >>> str(jd)
        ' 2451545  00H 00M 00.000S'
    >>> unicode(jd)
        u' 2451545  00H 00M 00.000S'
    >>> print jd
    --> print(jd)
     2451545  00H 00M 00.000S
    >>> jd = tpm.JD(year=2000.0+23.25/366)
    >>> print jd
    --> print(jd)
     2451566  18H 00M 00.000S

The method ``normalize()`` will normalize the components of a ``JD``
object. 

.. code-block:: python

    >>> jd = tpm.JD(year=2000.0+1.5/366)
    >>> jd.dd, jd.hh, jd.mm, jd.ss
        (2451545.5, -12.0, 0.0, 0.0)
    >>> jd.normalize()
    >>> jd.dd, jd.hh, jd.mm, jd.ss
        (2451545.0, 0.0, 0.0, 0.0)

The date and time stored in a ``JD`` object can be converted into a
scalar Julian date, a year with a fractional part and a ``YMD`` object,
using the methods ``to_j()``, ``to_year()`` and ``to_ymd()``
respectively. 

.. code-block:: python

    >>> # Midday Jan 1 of 2000
    >>> jd = tpm.JD(year=2000.0+1.5/366)
    >>> jd.to_j()
    2451545.0

    >>> jd.to_year()
        2000.0040983606557
    >>> 1.5/366
        0.0040983606557377051

    >>> print jd.to_ymd()
    --> print(jd.to_ymd())
    Sat Jan  1 12:00:00.000 2000
    >>> ymd = jd.to_ymd()
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2000, 1, 2.0, -12.0, 0.0, 0.0)
    >>> ymd.normalize()
    >>> ymd.y, ymd.m, ymd.dd, ymd.hh, ymd.mm, ymd.ss
        (2000, 1, 1.0, 12.0, 0.0, 0.0)


Classes for representing vectors
================================

TPM stores and manipulates positions of objects using full length
vectors. All calculations are carried out using Cartesian vectors with
units of AU for length and AU/day for velocities. In addition to
vectors with three components TPM uses, "6-vectors" that store the
three position components and the three velocity components. TPM uses
spherical vectors while handling user input coordinates, for example
positions and proper motions from catalog. Here the units are radians
and radians/day.

In PyTPM, these data structures are provided as Python classes; Cython
extension types. These are not meant to provide a complete
implementation of vectors, but only have those features needed for
their use in PyTPM. Just like the classes for angles and dates
described above, they should only be used within the context of PyTPM.

There are four vector classes: ``V3CP``, ``V3SP``, ``V6C`` and
``V6S``. For the general use of PyTPM, only ``V6C`` and ``V6S`` are
required.

Classes ``V3CP`` and ``V3SP`` are used for representing a position
vector in Cartesian and spherical coordinates, respectively. Both of
these are derived from the class ``V3``, which by itself is not very
useful.

The class ``V6C`` is used for representing a Cartesian 6-vector, and
the class ``V6S`` is used for representing a spherical 6-vector. Both
of these are derived from the class ``V6``, which by itself is not very
useful.

There is no class for representing a velocity vector on its own, since
I didn't find any need for it. In fact, the ``V3CP`` and ``V3SP`` are
also not needed, but I have them implemented anyway.


``V3CP`` and ``V3SP``
---------------------

.. autoclass:: V3CP
   :members:

.. autoclass:: V3SP
   :members:

As mentioned above, these are used for representing a position vector
in Cartesian and spherical coordinates respectively.

An instance of the ``V3CP`` class has the attributes ``x``, ``y`` and
``z`` which stores the three components. The ``V3SP`` class stores the
components in ``r``, ``alpha`` and ``delta``; ``alpha`` is the RA like
angle and ``delta`` is the DE like angle. It also has attributes
``nalpha`` and ``ndelta`` that store the angles ``alpha`` and ``delta``
respectively, scaled to [0 - 2π] and [-π/2 - π/2], respectively.

The values for these components can be supplied at creation time, and
can be modified later on.

.. code-block:: python

  >>> v3cp = tpm.V3CP(x=1.0)
  >>> v3cp.x, v3cp.y, v3cp.z
      (1.0, 0.0, 0.0)
  >>> v3cp.y=1
  >>> v3cp.x, v3cp.y, v3cp.z
      (1.0, 1.0, 0.0)
  >>> v3sp = tpm.V3SP(r=10.0)
  >>> v3sp.r, v3sp.alpha, v3sp.delta
      (10.0, 0.0, 0.0)
  >>> v3sp.delta = 2.3
  >>> v3sp.r, v3sp.alpha, v3sp.delta
      (10.0, 0.0, 2.2999999999999998)

Both these types can be can be converted into a string representation
by passing it to ``str()`` or ``unicode()``. These will be converted
into strings if they are used with the ``print`` statement.

.. code-block:: python

  >>> print v3sp
  --> print(v3sp)
   1.000000000000000e+01  0.000000000000000e+00  2.300000000000000e+00
  >>> print v3cp
  --> print(v3cp)
   1.000000000000000e+00  1.000000000000000e+00  0.000000000000000e+00

Two ``V3CP`` vectors can be added together, subtracted from each
other. The method ``unit()`` returns the unit vector, where as
``mod()`` returns the length of the vector. The method ``cross()``
returns the cross product between two ``V3CP`` vectors, and the method
``dot`` returns the dot product between two ``V3CP`` vectors. A
``V3CP`` method can also be multiplied with a scalar; all components
will get multiplied with the scalar and a new ``V3CP`` vector will be
returned.

.. code-block:: python

  >>> v3cp = tpm.V3CP(x=1.0,y=1.0,z=1.0)
  >>> v3cp1 = tpm.V3CP(x=1.0,y=1.0,z=1.0)
  >>> v = v3cp + v3cp1
  >>> v.x, v.y, v.z
      (2.0, 2.0, 2.0)
  >>> v = v3cp - v3cp1
  >>> v.x, v.y, v.z
      (0.0, 0.0, 0.0)
  >>> v3cp = tpm.V3CP(x=1.0,y=1.0,z=1.0)
  >>> v3cp.mod()
      1.7320508075688772
  >>> v = v3cp.unit()
  >>> v.x, v.y, v.z
      (0.57735026918962584, 0.57735026918962584, 0.57735026918962584)
  >>> v3cp = tpm.V3CP(x=1.0,y=1.0,z=1.0)
  >>> v3cp1 = tpm.V3CP(x=1.0,y=1.0,z=1.0)
  >>> v = v3cp.cross(v3cp1)
  >>> v.x, v.y, v.z
      (0.0, 0.0, 0.0)
  >>> v3cp.dot(v3cp1)
      3.0
  >>> v = v3cp * 3
  >>> v.x, v.y, v.z
      (3.0, 3.0, 3.0)
 

The method ``c2s()`` will convert the Cartesian components into
spherical and return the results as a ``V3SP`` object.

.. code-block:: python

  >>> v3cp = tpm.V3CP(x=1.0,y=1.0,z=1.0)
  >>> v3sp = v3cp.c2s()
  >>> v3sp.r, v3sp.alpha, v3sp.delta
      (1.7320508075688772, 0.78539816339744828, 0.61547970867038726)


A ``V3SP`` object, has most of methods as a ``V3CP`` object. Most
operations are done by first converting into Cartesian and then
converting the result back into spherical. It has the ``s2c()`` method
that will convert the vector into Cartesian coordinates and returns the
results as a ``V3CP`` object.


``V6C``
-------

.. autoclass:: V6C
   :members:

This class is used for representing a Cartesian 6-vector and has 6
important attributes: ``x``, ``y``, ``z``, ``xdot``, ``ydot`` and
``zdot``. Each of these stand for the position and velocity
components. These can be assigned values at creation time by passing
keyword arguments. Their values can be modified after creation.

.. code-block:: python

  >>> v6c = tpm.V6C(x=1.0)
  >>> v6c.x
      1.0
  >>> v6c.y
      0.0
  >>> v6c.z=100.0
  >>> v6c.ydot=-10.94
  >>> v6c.x, v6c.y, v6c.z, v6c.xdot, v6c.ydot, v6c.zdot
      (1.0, 0.0, 100.0, 0.0, -10.94, 0.0)

We can add and subtract two ``V6C`` vectors: the corresponding
coordinate components are added and subtracted.

.. code-block:: python

  >>> v6c1 = tpm.V6C(x=10,y=9,z=8,xdot=-1.0,ydot=3.0,zdot=-12.345)
  >>> v6c2 = tpm.V6C(x=10,y=7,z=3,xdot=-6.0,ydot=-3.0,zdot=1)
  >>> v6c = v6c1 + v6c2  
  >>> v6c.x, v6c.y, v6c.z, v6c.xdot, v6c.ydot, v6c.zdot
      (20.0, 16.0, 11.0, -7.0, 0.0, -11.345000000000001)
  >>> v6c = v6c1 - v6c2  
  >>> v6c.x, v6c.y, v6c.z, v6c.xdot, v6c.ydot, v6c.zdot
      (0.0, 2.0, 5.0, 5.0, 6.0, -13.345000000000001)

The length of the position component in a ``V6C`` vector can be
calculated using the ``mod()`` method.

.. code-block:: python

  >>> v6c = tpm.V6C(x=3.0,y=3.0,z=3.0)
  >>> v6c.mod()
      5.196152422706632
  >>> v6c.mod()**2
      27.0

The method ``unit()`` will return another ``V6C`` vector, containing
the unit vector of the position component and with the velocity
components scaled with reciprocal of length of the position component. 

.. code-block:: python

  >>> v6c = tpm.V6C(x=3.0,y=3.0,z=3.0,xdot=1.0,ydot=1.0,zdot=1.0)
  >>> v6cu = v6c.unit()
  >>> v6cu.x, v6cu.y, v6cu.z, v6cu.xdot, v6cu.ydot, v6cu.zdot
  (0.57735026918962573,
   0.57735026918962573,
   0.57735026918962573,
   0.19245008972987526,
   0.19245008972987526,
   0.19245008972987526)
  >>> 1.0/v6c.mod()
      0.19245008972987526
  >>> 3.0/v6c.mod()
      0.57735026918962573


The method ``scale()`` will multiply all components with the given number
and return a new ``V6C`` vector with the components set to the results.

.. code-block:: python

  >>> v6c = tpm.V6C(x=3.0,y=3.0,z=3.0,xdot=1.0,ydot=1.0,zdot=1.0)
  >>> v6c = v6c.scale(10.0)
  >>> v6c.x, v6c.y, v6c.z, v6c.xdot, v6c.ydot, v6c.zdot
      (30.0, 30.0, 30.0, 10.0, 10.0, 10.0)

The method ``v62v3()``, multiply the velocity components with the given
scalar, adds them to the corresponding position component and returns
the result as a ``V3CP`` vector. That is, it applies space motion to
the given ``V6C`` position component.

.. code-block:: python

  >>> v6c = tpm.V6C(x=3.0,y=3.0,z=3.0,xdot=1.0,ydot=1.0,zdot=1.0)
  >>> v3cp = v6c.v62v3(2.0)
  >>> v3cp.x, v3cp.y, v3cp.z
      (5.0, 5.0, 5.0)

The methods ``dot()`` and ``cross()`` perform scalar and vector product
between the two vectors. In the latter case, the velocity components of
the resulting vector is set to 0.0

.. code-block:: python

  >>> v6c1 = tpm.V6C(x=10,y=9,z=8,xdot=-1.0,ydot=3.0,zdot=-12.345)
  >>> v6c2 = tpm.V6C(x=10,y=7,z=3,xdot=-6.0,ydot=-3.0,zdot=1)
  >>> v6c1.dot(v6c2)
      187.0
  >>> v6c = v6c1.cross(v6c2)
  >>> v6c.x, v6c.y, v6c.z, v6c.xdot, v6c.ydot, v6c.zdot
      (-29.0, 50.0, -20.0, 0.0, 0.0, 0.0)


The method ``c2s()`` converts the 6-vector into spherical coordinates
and returns the result as a ``V6S`` vector. This is the method that
will be used often, while using the PyTPM library. All calculations in
PyTPM are done in Cartesian coordinates but the final result is most
often needed in spherical coordinates, for example RA and DE.

.. code-block:: python

  >>> v6c = tpm.V6C(x=1.0,y=1.0,z=1.0,xdot=1,ydot=1,zdot=1.0)
  >>> v6s = v6c.c2s()
  >>> v6s.r, v6s.alpha, v6s.delta, v6s.rdot, v6s.alphadot, v6s.deltadot
  (1.7320508075688772,
   0.78539816339744828,
   0.61547970867038726,
   1.7320508075688774,
   0.0,
   -8.739772475095232e-18)


``V6S``
-------

.. autoclass:: V6S
   :members:

The ``V6S`` class holds a 6-vector in spherical coordinates. The
components are stored in the attributes ``r``, ``alpha``, ``delta``,
``rdot``, ``alphadot``, and ``deltadot``. Here ``alpha`` is the
RA like angle and ``delta`` is the DE like angle. These properties can
be set at creation time and can be modified later on. The angles are in
radians.

.. code-block:: python

  >>> v6s = tpm.V6S(r=1e9,alpha=2.3, delta=3.5)
  >>> v6s.r, v6s.alpha, v6s.delta, v6s.rdot, v6s.alphadot, v6s.deltadot
      (1000000000.0, 2.2999999999999998, 3.5, 0.0, 0.0, 0.0)
  >>> v6s.r = 1.0
  >>> v6s.r, v6s.alpha, v6s.delta, v6s.rdot, v6s.alphadot, v6s.deltadot
      (1.0, 2.2999999999999998, 3.5, 0.0, 0.0, 0.0)

The attributes ``nalpha`` and ``ndelta`` gives normalized values of
``alpha`` and ``delta`` respectively. The first gives a value between
0 and 2π, while the latter gives a value between -π/2 and π/2.

.. code-block:: python

  >>> tpm.M_PI
      3.1415926535897931
  >>> v6s.alpha = tpm.M_PI*3
  >>> v6s.nalpha
      3.1415926535897931
  >>> v6s.delta = -tpm.M_PI
  >>> v6s.ndelta
      0.0

Since a ``V6S`` vector is only used for converting catalog data into
Cartesian coordinates, and vice-versa, this vector has only one method:
``s2c``. The method converts the vector into Cartesian coordinates and
returns a ``V6C`` vector.

.. code-block:: python

  >>> tpm.M_PI
      3.1415926535897931
  >>> v6s = tpm.V6S(r=1.0,alpha=tpm.M_PI/4.0,delta=tpm.M_PI/3.0)
  >>> v6c = v6s.s2c()
  >>> v6c.x, v6c.y, v6c.z
      (0.35355339059327384, 0.35355339059327379, 0.8660254037844386)
  >>> v6c.xdot, v6c.ydot, v6c.zdot
      (0.0, 0.0, 0.0)


``TSTATE``
----------

.. autoclass:: TSTATE
   :members:

A ``TSTATE`` object is used to store the "state data" in PyTPM. This is
equivalent to the ``TPM_TSTATE`` structure in TPM. The reason I
implemented this class was so that I can call the ``tpm_data()`` and
``tpm()`` functions from within Python. This object does not have any
useful methods, but only has attributes corresponding to the 32
parameters that define a state. Of these the independent parameters are
read-write, where as the dependent parameters are read only. The latter
can be calculated, as in TPM, by passing the object to ``tpm_data()``
along with the type of calculation.

.. code-block:: python

  >>> tstate = tpm.TSTATE()
  >>> for i in dir(tstate):
     .....:     if not i.startswith("_"): print i
     .....:     
     .....:     
  H
  P
  T
  alt
  delta_at
  delta_ut
  eb
  eh
  gast
  gmst
  last
  lat
  lon
  nm
  nut_lon
  nut_obl
  obliquity
  obs_m
  obs_s
  obs_t
  pm
  refa
  refb
  tai
  tdb
  tdt
  ut1
  utc
  wavelength
  xpole
  ypole


``PVEC``
--------

.. autoclass:: PVEC
   :members:

TPM needs an array of ``V6`` structures, where it will store the
initial, intermediate and final results, while performing coordinate
transformations. In PyTPM, I have decided to implement a class that can
be treated as an array of ``V6CP`` object. This is much more flexible
and robust than dealing with a simple list of ``V6CP`` objects. This
object can be passed, along with other information, to ``tpm()`` when
performing coordinate transformations.

An index location corresponds to the appropriate TPM state. For
example, the index location 6, i.e., pvec[6], corresponds to the state
``TPM_S06``, and pvec[4] corresponds to ``TPM_S04``.

So while performing FK5 epoch and equinox J2000 to Galactic conversion,
we would insert our input ``V6CP`` vector at index location 6 and
retrieve the result from index location 4.

A full example is shown :ref:`here <pytpm-full-conversion>`.


..  LocalWords:  PyTPM TPM cdef LocalWords DMS




