=================
 Data Structures
=================

.. currentmodule:: pytpm.tpm

PyTPM wraps many of the C structures in TPM as Python classes, using
Cython *extension types* or *cdef* classes. 

Note that these are only useful in the context of their usage in
PyTPM. Defining these structures make it easy to call the various TPM C
functions from within Python. They are neither complete nor should be
used in general handling of dates, times and vectors. 


.. contents::

Classes for representing angles
===============================

There are two classes for storing angles. ``DMS`` for degrees,
arc-minutes and arc-seconds, and ``HMS`` for hours, minutes and
seconds. Objects of these classes can be initialized by passing scalar
value of the angle in any of the three formats for representing angles:
radians, hours, and degrees. 

.. autoclass:: DMS
   :members:

.. autoclass:: HMS
   :members:

Classes for storing time and date-time
======================================

The class ``YMD`` can be used to store a Gregorian calendar date and
time, where as the class ``JD`` can be used to store a Julian date. As
noted before the ``HMS`` structure can be used to store time in hours,
minutes and seconds.

.. autoclass:: YMD
   :members:

.. autoclass:: JD
   :members:

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




