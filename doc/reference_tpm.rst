**pytpm.tpm** 
=============


.. automodule:: pytpm.tpm
    :members:
    :undoc-members:

Constants
---------

The following are the various constants defined in ``pytpm.tpm``. Note
that in TPM, and hence in PyTPM, *all Julian Day numbers are in the
UTC time system*.

==============  =======================================================
``POS``          Index of position vector in a :class:`V6` instance.
``VEL``          Index of velocity vector in a :class:`V6` instance.
``MJD_0``        JD of the modified JD system.
``B1950``        JD of epoch B1950.0.
``J2000``        JD of epoch J2000.0.
``J1984``        JD of 1984.0, the magic FK4/FK5 conversion time.
``CB``           Number of days in a tropical century at epoch 1900.0.
``CJ``           Number of days in a Julian centruy.
``SUNDAY``       Start of week, numerical value of 0.
``MONDAY``       Numerical value 1.
``TUESDAY``      Numerical value 2.
``WEDNESDAY``    Numerical value 3.
``THURSDAY``     Numerical value 4.
``FRIDAY``       Numerical value 5.
``SATURDAY``     Numerical value 6.
==============  =======================================================


Classes for vectors and matrices
--------------------------------

.. autoclass:: V3
    :members:

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



.. auto

..    :members:
..    :undoc-members:
