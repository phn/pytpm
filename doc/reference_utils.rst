===============
**pytpm.utils**
===============


.. contents::

.. automodule:: pytpm.utils
..    :members:
..    :undoc-members:

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
a year. The function ``byear2jd`` converts the given year in the
Julian year system, into one in the Basselian year system.
``jd2byear`` converts a Julian day number into a year in the Basselian
year system. Functions ``jyear2jd`` and ``jd2jyear`` performs a
similar convertion between a Julian day number and a year in the
Julian year system.

.. autofunction:: byear2jd
.. autofunction:: jd2byear 
.. autofunction:: jyear2jd
.. autofunction:: jd2jyear


Functions for manipulating data structures
==========================================

``DMS`` structure
-----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.DMS` structure.

.. autofunction:: dmsDecDegrees
.. autofunction:: dmsDecMinutes
.. autofunction:: dmsDecSeconds
.. autofunction:: dmsDivDegrees
.. autofunction:: dmsDivMinutes
.. autofunction:: dmsDivSeconds
.. autofunction:: dmsGetDegrees
.. autofunction:: dmsGetMinutes
.. autofunction:: dmsGetSeconds
.. autofunction:: dmsIncDegrees
.. autofunction:: dmsIncMinutes
.. autofunction:: dmsIncSeconds
.. autofunction:: dmsMulDegrees
.. autofunction:: dmsMulMinutes
.. autofunction:: dmsMulSeconds
.. autofunction:: dmsSetDegrees
.. autofunction:: dmsSetMinutes
.. autofunction:: dmsSetSeconds

``HMS`` structure
-----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.HMS` structure.

.. autofunction:: hmsDecHours
.. autofunction:: hmsDecMinutes
.. autofunction:: hmsDecSeconds
.. autofunction:: hmsDivHours
.. autofunction:: hmsDivMinutes
.. autofunction:: hmsDivSeconds
.. autofunction:: hmsGetHours
.. autofunction:: hmsGetMinutes
.. autofunction:: hmsGetSeconds
.. autofunction:: hmsIncHours
.. autofunction:: hmsIncMinutes
.. autofunction:: hmsIncSeconds
.. autofunction:: hmsMulHours
.. autofunction:: hmsMulMinutes
.. autofunction:: hmsMulSeconds
.. autofunction:: hmsSetHours
.. autofunction:: hmsSetMinutes
.. autofunction:: hmsSetSeconds

``JD`` structure
----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.JD` structures.

.. autofunction:: jdDecDay 
.. autofunction:: jdDecHours
.. autofunction:: jdDecMinutes
.. autofunction:: jdDecSeconds
.. autofunction:: jdDivDay 
.. autofunction:: jdDivHours
.. autofunction:: jdDivMinutes
.. autofunction:: jdDivSeconds
.. autofunction:: jdGetDay	
.. autofunction:: jdGetHours
.. autofunction:: jdGetMinutes
.. autofunction:: jdGetSeconds
.. autofunction:: jdIncDay 
.. autofunction:: jdIncHours
.. autofunction:: jdIncMinutes
.. autofunction:: jdIncSeconds
.. autofunction:: jdMulDay 
.. autofunction:: jdMulHours
.. autofunction:: jdMulMinutes
.. autofunction:: jdMulSeconds
.. autofunction:: jdSetDay 
.. autofunction:: jdSetHours
.. autofunction:: jdSetMinutes
.. autofunction:: jdSetSeconds

``YMD`` structure
-----------------

These are convenience functions for working with
:class:``pytpm.tpm.YMD`` instances.

.. autofunction:: ymdDecDay 
.. autofunction:: ymdDecHours
.. autofunction:: ymdDecMinutes
.. autofunction:: ymdDecMonth
.. autofunction:: ymdDecSeconds
.. autofunction:: ymdDecYear
.. autofunction:: ymdDivDay 
.. autofunction:: ymdDivHours
.. autofunction:: ymdDivMinutes
.. autofunction:: ymdDivMonth
.. autofunction:: ymdDivSeconds
.. autofunction:: ymdDivYear
.. autofunction:: ymdGetDay	
.. autofunction:: ymdGetHours
.. autofunction:: ymdGetMinutes
.. autofunction:: ymdGetMonth
.. autofunction:: ymdGetSeconds
.. autofunction:: ymdGetYear
.. autofunction:: ymdIncDay 
.. autofunction:: ymdIncHours
.. autofunction:: ymdIncMinutes
.. autofunction:: ymdIncMonth
.. autofunction:: ymdIncSeconds
.. autofunction:: ymdIncYear
.. autofunction:: ymdMulDay 
.. autofunction:: ymdMulHours
.. autofunction:: ymdMulMinutes
.. autofunction:: ymdMulMonth
.. autofunction:: ymdMulSeconds
.. autofunction:: ymdMulYear
.. autofunction:: ymdSetDay 
.. autofunction:: ymdSetHours
.. autofunction:: ymdSetMinutes
.. autofunction:: ymdSetMonth
.. autofunction:: ymdSetSeconds
.. autofunction:: ymdSetYear

Functions for manipulating angles, dates and time
=================================================

These functions are used for converting angles into different units,
angles into time, assuming 24 hours == 360 degrees and for generating
formatted string representation of various such quantities.


Functions related to angles
---------------------------

.. autofunction:: fmt_dms
.. autofunction:: fmt_r
.. autofunction:: r2dms
.. autofunction:: d2r
.. autofunction:: r2d
.. autofunction:: d2as
.. autofunction:: as2d
.. autofunction:: r2as
.. autofunction:: as2r

Date and time related funtions
------------------------------

.. autofunction:: j2j
.. autofunction:: j2y
.. autofunction:: j2ymd
.. autofunction:: jd2y
.. autofunction:: fmt_hms
.. autofunction:: fmt_jd
.. autofunction:: fmt_y
.. autofunction:: y2j
.. autofunction:: y2jd
.. autofunction:: y2y
.. autofunction:: ymd2j
.. autofunction:: ymd_diff

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





