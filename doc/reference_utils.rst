===============
**pytpm.utils**
===============


.. contents::

.. automodule:: pytpm.utils
..    :members:
..    :undoc-members:

Functions for manipulating data structures
==========================================

``DMS`` structure
-----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.DMS` structure.

.. rubric:: Set the components of :class:`pytpm.tpm.DMS` to scalar values

.. autofunction:: dmsSetDegrees
.. autofunction:: dmsSetMinutes
.. autofunction:: dmsSetSeconds

.. rubric:: Retrive components of :class:`pytpm.tpm.DMS`

.. autofunction:: dmsGetDegrees
.. autofunction:: dmsGetMinutes
.. autofunction:: dmsGetSeconds

.. rubric:: Subtract a scalar from components of :class:`pytpm.tpm.DMS`

.. autofunction:: dmsDecDegrees
.. autofunction:: dmsDecMinutes
.. autofunction:: dmsDecSeconds

.. rubric:: Divide components of :class:`pytpm.tpm.DMS` with scalar

.. autofunction:: dmsDivDegrees
.. autofunction:: dmsDivMinutes
.. autofunction:: dmsDivSeconds

.. rubric:: Add a scalar to components of :class:`pytpm.tpm.DMS`

.. autofunction:: dmsIncDegrees
.. autofunction:: dmsIncMinutes
.. autofunction:: dmsIncSeconds

.. rubric:: Multiply components of :class:`pytpm.tpm.DMS` with a scalar

.. autofunction:: dmsMulDegrees
.. autofunction:: dmsMulMinutes
.. autofunction:: dmsMulSeconds


``HMS`` structure
-----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.HMS` structure.

.. rubric:: Set the components of :class:`pytpm.tpm.HMS` to scalar values

.. autofunction:: hmsSetHours
.. autofunction:: hmsSetMinutes
.. autofunction:: hmsSetSeconds

.. rubric:: Retrive components of :class:`pytpm.tpm.HMS`

.. autofunction:: hmsGetHours
.. autofunction:: hmsGetMinutes
.. autofunction:: hmsGetSeconds

.. rubric:: Subtract a scalar from components of :class:`pytpm.tpm.HMS`

.. autofunction:: hmsDecHours
.. autofunction:: hmsDecMinutes
.. autofunction:: hmsDecSeconds

.. rubric:: Divide components of :class:`pytpm.tpm.HMS` with scalar

.. autofunction:: hmsDivHours
.. autofunction:: hmsDivMinutes
.. autofunction:: hmsDivSeconds

.. rubric:: Add a scalar to components of :class:`pytpm.tpm.HMS`

.. autofunction:: hmsIncHours
.. autofunction:: hmsIncMinutes
.. autofunction:: hmsIncSeconds

.. rubric:: Multiply components of :class:`pytpm.tpm.HMS` with a scalar

.. autofunction:: hmsMulHours
.. autofunction:: hmsMulMinutes
.. autofunction:: hmsMulSeconds

``JD`` structure
----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.JD` structures.

.. rubric:: Set the components of :class:`pytpm.tpm.JD` to scalar values

.. autofunction:: jdSetDay 
.. autofunction:: jdSetHours
.. autofunction:: jdSetMinutes
.. autofunction:: jdSetSeconds

.. rubric:: Retrive components of :class:`pytpm.tpm.JD`

.. autofunction:: jdGetDay	
.. autofunction:: jdGetHours
.. autofunction:: jdGetMinutes
.. autofunction:: jdGetSeconds

.. rubric:: Subtract a scalar from components of :class:`pytpm.tpm.JD`

.. autofunction:: jdDecDay 
.. autofunction:: jdDecHours
.. autofunction:: jdDecMinutes
.. autofunction:: jdDecSeconds

.. rubric:: Divide components of :class:`pytpm.tpm.JD` with scalar

.. autofunction:: jdDivDay 
.. autofunction:: jdDivHours
.. autofunction:: jdDivMinutes
.. autofunction:: jdDivSeconds

.. rubric:: Add a scalar to components of :class:`pytpm.tpm.JD`

.. autofunction:: jdIncDay 
.. autofunction:: jdIncHours
.. autofunction:: jdIncMinutes
.. autofunction:: jdIncSeconds

.. rubric:: Multiply components of :class:`pytpm.tpm.JD` with a scalar

.. autofunction:: jdMulDay 
.. autofunction:: jdMulHours
.. autofunction:: jdMulMinutes
.. autofunction:: jdMulSeconds


``YMD`` structure
-----------------

These are convenience functions for working with
:class:``pytpm.tpm.YMD`` instances.

.. rubric:: Set the components of :class:`pytpm.tpm.YMD` to scalar values

.. autofunction:: ymdSetDay 
.. autofunction:: ymdSetHours
.. autofunction:: ymdSetMinutes
.. autofunction:: ymdSetMonth
.. autofunction:: ymdSetSeconds
.. autofunction:: ymdSetYear

.. rubric:: Retrive components of :class:`pytpm.tpm.YMD`

.. autofunction:: ymdGetDay	
.. autofunction:: ymdGetHours
.. autofunction:: ymdGetMinutes
.. autofunction:: ymdGetMonth
.. autofunction:: ymdGetSeconds
.. autofunction:: ymdGetYear

.. rubric:: Subtract a scalar from components of :class:`pytpm.tpm.YMD`

.. autofunction:: ymdDecDay 
.. autofunction:: ymdDecHours
.. autofunction:: ymdDecMinutes
.. autofunction:: ymdDecMonth
.. autofunction:: ymdDecSeconds
.. autofunction:: ymdDecYear

.. rubric:: Divide components of :class:`pytpm.tpm.YMD` with scalar

.. autofunction:: ymdDivDay 
.. autofunction:: ymdDivHours
.. autofunction:: ymdDivMinutes
.. autofunction:: ymdDivMonth
.. autofunction:: ymdDivSeconds
.. autofunction:: ymdDivYear

.. rubric:: Add a scalar to components of :class:`pytpm.tpm.YMD`

.. autofunction:: ymdIncDay 
.. autofunction:: ymdIncHours
.. autofunction:: ymdIncMinutes
.. autofunction:: ymdIncMonth
.. autofunction:: ymdIncSeconds
.. autofunction:: ymdIncYear

.. rubric:: Multiply components of :class:`pytpm.tpm.YMD` with a scalar

.. autofunction:: ymdMulDay 
.. autofunction:: ymdMulHours
.. autofunction:: ymdMulMinutes
.. autofunction:: ymdMulMonth
.. autofunction:: ymdMulSeconds
.. autofunction:: ymdMulYear

Functions for generating string representations
-----------------------------------------------

The following functions return string represenation of the quantities
in the appropriate data structures passed to them.

.. autofunction:: fmt_dms
.. autofunction:: fmt_hms
.. autofunction:: fmt_jd

Cooordinate conversion
======================

The ``convert`` function is provided for performing coordinate
conversions using a single function call. It can be used to set all
the independent parameters of a TPM state and perform coordinate
conversion between any two TPM target states.

.. autofunction:: convert

Date conversion
===============

There are 4 functions that can convert between a Julian day number and
a year. The function ``byear2jd`` converts the given year in the in
the Basselian year system into Julian day number.  ``jd2byear``
converts a Julian day number into a year in the Basselian year
system. Functions ``jyear2jd`` and ``jd2jyear`` performs a similar
convertion between a Julian day number and a year in the Julian year
system.

.. autofunction:: byear2jd
.. autofunction:: jd2byear 
.. autofunction:: jyear2jd
.. autofunction:: jd2jyear

Time transformations
====================

.. autofunction:: ut2gmst
.. autofunction:: utc2tai
.. autofunction:: tai2utc
.. autofunction:: tai2tdt
.. autofunction:: tdt2tai
.. autofunction:: tdt2et
.. autofunction:: et2tdt
.. autofunction:: et2tai
.. autofunction:: tai2et

Functions for manipulating angles, time and dates
=================================================

These functions are used for converting angles into different units,
angles into time, assuming 24 hours == 360 degrees and for generating
formatted string representation of various such quantities.

Functions for generating string representations
-----------------------------------------------

.. autofunction:: fmt_r
.. autofunction:: fmt_y

Functions related to angles
---------------------------

.. autofunction:: r2dms
.. autofunction:: d2r
.. autofunction:: r2d
.. autofunction:: d2as
.. autofunction:: as2d
.. autofunction:: r2as
.. autofunction:: as2r

Conversion between angle and time
---------------------------------

.. autofunction:: d2hms
.. autofunction:: dms2h
.. autofunction:: dms2r
.. autofunction:: h2dms
.. autofunction:: hms2d
.. autofunction:: hms2r
.. autofunction:: r2hms
.. autofunction:: d2h
.. autofunction:: h2d
.. autofunction:: h2r
.. autofunction:: r2h
.. autofunction:: as2h
.. autofunction:: h2as

Funtions related to dates
-------------------------

.. autofunction:: j2j
.. autofunction:: j2y
.. autofunction:: j2ymd
.. autofunction:: jd2y
.. autofunction:: y2j
.. autofunction:: y2jd
.. autofunction:: y2y
.. autofunction:: ymd2j
.. autofunction:: ymd_diff

