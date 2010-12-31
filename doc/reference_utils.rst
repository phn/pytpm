===============
**pytpm.utils**
===============


.. automodule:: pytpm.utils
..    :members:
..    :undoc-members:

.. contents::

Coordinate conversion
=====================

.. TODO:: Explain how to use with lots of examples. Or in a different
       section?

       Explain epoch, equinox etc., are AND when these are used by
       TPM. Proper motion correction to required epoch must be done
       manually.

       Equinox: The direction of the intersection of the equator and
       ecliptic at this time, was used to define the coordinate
       system.

       Epoch: When did an object occupy the given position in the
       coordinate system indicated by the equinox.

       Timetag: The time of observation.

       Proper motion must be applied to get the position from epoch to
       timetag. This is not carried out by TPM.

       The coordinate system will be in given equinox or catalog
       equinox as required. The coordinates will not have proper
       motions applied to them, i.e., they remain in the epoch
       provided. So when converting to equinox-of-date, the epoch is
       not used at all. In fact epoch is used only for +- T05.

       For merely converting from one equinox to another S02 to S02
       two calls convert function cannot be used, i.e., two states
       must differ. Or we can do S02 to S06 and then perform S06 to
       S02 with a different equinox for the second S02.

The ``convert`` function is provided for performing coordinate
conversions using a single function call. It can be used to set all
the independent parameters of a TPM state and perform coordinate
conversion between any two TPM target states.

.. autofunction:: convert

Functions for manipulating data structures
==========================================

``DMS`` structure
-----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.DMS` structure.

Set the components of :class:`pytpm.tpm.DMS` to scalar values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [2]: dms = tpm.DMS()
   
  In [3]: print utils.fmt_dms(dms)
  ------> print(utils.fmt_dms(dms))
  +00D 00' 00.000"
   
  In [4]: utils.dmsSetDegrees(dms, 2.3)
   
  In [5]: print utils.fmt_dms(dms)
  ------> print(utils.fmt_dms(dms))
  +02D 17' 59.999"
   
  In [6]: utils.dmsSetMinutes(dms, 10.0)
   
  In [7]: print utils.fmt_dms(dms)
  ------> print(utils.fmt_dms(dms))
  +02D 27' 59.999"
   
  In [8]: utils.dmsSetSeconds(dms, 30.0)
   
  In [9]: print utils.fmt_dms(dms)
  ------> print(utils.fmt_dms(dms))
  +02D 28' 29.999"


.. autofunction:: dmsSetDegrees
.. autofunction:: dmsSetMinutes
.. autofunction:: dmsSetSeconds


Retrieve components of :class:`pytpm.tpm.DMS`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [10]: utils.dmsGetDegrees(dms)
  Out[10]: 2.2999999999999998
   
  In [11]: utils.dmsGetMinutes(dms)
  Out[11]: 10.0
   
  In [12]: utils.dmsGetSeconds(dms)
  Out[12]: 30.0
   
  In [13]: dms = tpm.dms2dms(dms) # normalize
   
  In [14]: utils.dmsGetDegrees(dms)
  Out[14]: 2.0
   
  In [15]: utils.dmsGetMinutes(dms)
  Out[15]: 28.0
   
  In [16]: utils.dmsGetSeconds(dms)
  Out[16]: 29.999999999998721

.. autofunction:: dmsGetDegrees
.. autofunction:: dmsGetMinutes
.. autofunction:: dmsGetSeconds



Subtract a scalar from components of :class:`pytpm.tpm.DMS`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [17]: utils.dmsDecDegrees(dms, 1.0)
   
  In [18]: utils.dmsDecMinutes(dms, 0.5)
   
  In [19]: utils.dmsDecSeconds(dms, 0.9)
   
  In [20]: print utils.fmt_dms(dms)
  -------> print(utils.fmt_dms(dms))
  +01D 27' 59.099"

.. autofunction:: dmsDecDegrees
.. autofunction:: dmsDecMinutes
.. autofunction:: dmsDecSeconds


Divide components of :class:`pytpm.tpm.DMS` with scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [21]: utils.dmsDivDegrees(dms, 1.0)
   
  In [22]: utils.dmsDivMinutes(dms, 0.5)
   
  In [23]: utils.dmsDivSeconds(dms, 0.5)
   
  In [24]: print utils.fmt_dms(tpm.dms2dms(dms))
  -------> print(utils.fmt_dms(tpm.dms2dms(dms)))
  +01D 55' 58.199"

.. autofunction:: dmsDivDegrees
.. autofunction:: dmsDivMinutes
.. autofunction:: dmsDivSeconds


Add a scalar to components of :class:`pytpm.tpm.DMS`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [4]: dms = tpm.DMS()
   
  In [5]: utils.dmsIncDegrees(dms, 100)
   
  In [6]: utils.dmsIncMinutes(dms, 100)
   
  In [7]: utils.dmsIncSeconds(dms, 100)
   
  In [8]: dms = tpm.dms2dms(dms)
   
  In [9]: print utils.fmt_dms(dms)
  ------> print(utils.fmt_dms(dms))
  +101D 41' 39.999"
   
  In [10]: dms.dd
  Out[10]: 101.0
   
  In [11]: dms.mm
  Out[11]: 41.0
   
  In [12]: dms.ss
  Out[12]: 39.999999999994316

.. autofunction:: dmsIncDegrees
.. autofunction:: dmsIncMinutes
.. autofunction:: dmsIncSeconds


Multiply components of :class:`pytpm.tpm.DMS` with a scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [13]: utils.dmsMulDegrees(dms, 0.1)
   
  In [14]: utils.dmsMulMinutes(dms, 10)
   
  In [15]: utils.dmsMulSeconds(dms, 20)
   
  In [16]: dms = tpm.dms2dms(dms)
   
  In [17]: print utils.fmt_dms(dms)
  -------> print(utils.fmt_dms(dms))
  +17D 09' 19.999"

.. autofunction:: dmsMulDegrees
.. autofunction:: dmsMulMinutes
.. autofunction:: dmsMulSeconds


``HMS`` structure
-----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.HMS` structure.

Set the components of :class:`pytpm.tpm.HMS` to scalar values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [19]: hms = tpm.HMS()
   
  In [20]: utils.hmsSetHours(hms, 12.345)
   
  In [21]: hms = tpm.hms2hms(hms)
   
  In [22]: print utils.fmt_hms(hms)
  -------> print(utils.fmt_hms(hms))
   12H 20M 42.000S
   
  In [23]: utils.hmsSetMinutes(hms, 10)
   
  In [24]: print utils.fmt_hms(hms)
  -------> print(utils.fmt_hms(hms))
   12H 10M 42.000S
   
  In [25]: utils.hmsSetSeconds(hms, 10)
   
  In [26]: print utils.fmt_hms(hms)
  -------> print(utils.fmt_hms(hms))
   12H 10M 09.999S

.. autofunction:: hmsSetHours
.. autofunction:: hmsSetMinutes
.. autofunction:: hmsSetSeconds

Retrieve components of :class:`pytpm.tpm.HMS`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

In [27]: utils.hmsGetHours(hms)
Out[27]: 12.0

In [28]: utils.hmsGetMinutes(hms)
Out[28]: 10.0

In [29]: utils.hmsGetSeconds(hms)
Out[29]: 10.0

.. autofunction:: hmsGetHours
.. autofunction:: hmsGetMinutes
.. autofunction:: hmsGetSeconds

Subtract a scalar from components of :class:`pytpm.tpm.HMS`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [30]: utils.hmsDecHours(hms, 2)
   
  In [31]: utils.hmsGetHours(hms)
  Out[31]: 10.0
   
  In [33]: utils.hmsDecMinutes(hms, 12)
   
  In [34]: utils.hmsGetMinutes(hms)
  Out[34]: -2.0
   
  In [35]: hms = tpm.hms2hms(hms)
   
  In [36]: utils.hmsGetMinutes(hms)
  Out[36]: 58.0
   
  In [37]: utils.hmsSetSeconds(hms, 10.0)
   
  In [38]: hms = tpm.hms2hms(hms)
   
  In [39]: print utils.fmt_hms(hms)
  -------> print(utils.fmt_hms(hms))
   09H 58M 10.000S


.. autofunction:: hmsDecHours
.. autofunction:: hmsDecMinutes
.. autofunction:: hmsDecSeconds

Divide components of :class:`pytpm.tpm.HMS` with scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [40]: hms = tpm.HMS()
   
  In [42]: utils.hmsSetSeconds(hms, 100.12)
   
  In [43]: hms = tpm.hms2hms(hms)
   
  In [44]: hms.hh, hms.mm, hms.ss
  Out[44]: (0.0, 1.0, 40.120000000000005)
   
  In [45]: utils.hmsDivSeconds(hms, 12.34)
   
  In [46]: utils.hmsDivMinutes(hms, 13.4)
   
  In [47]: utils.hmsDivHours(hms, 0.1)
   
  In [48]: hms.hh, hms.mm, hms.ss
  Out[48]: (0.0, 0.074626865671641784, 3.2512155591572127)
   
  In [49]: hms = tpm.hms2hms(hms)
   
  In [50]: print utils.fmt_hms(hms)
  -------> print(utils.fmt_hms(hms))
   00H 00M 07.728S

.. autofunction:: hmsDivHours
.. autofunction:: hmsDivMinutes
.. autofunction:: hmsDivSeconds

Add a scalar to components of :class:`pytpm.tpm.HMS`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [51]: utils.hmsIncHours(hms, 1.0)
   
  In [52]: utils.hmsIncMinutes(hms, 1.0)
   
  In [53]: utils.hmsIncSeconds(hms, 1.0)
   
  In [54]: print utils.fmt_hms(hms)
  -------> print(utils.fmt_hms(hms))
   01H 01M 08.728S


.. autofunction:: hmsIncHours
.. autofunction:: hmsIncMinutes
.. autofunction:: hmsIncSeconds

Multiply components of :class:`pytpm.tpm.HMS` with a scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [55]: utils.hmsMulHours(hms, 2.0)
   
  In [56]: utils.hmsMulSeconds(hms, 90.0)
   
  In [57]: hms = tpm.hms2hms(hms)
   
  In [58]: print utils.fmt_hms(hms)
  -------> print(utils.fmt_hms(hms))
   02H 14M 05.594S


.. autofunction:: hmsMulHours
.. autofunction:: hmsMulMinutes
.. autofunction:: hmsMulSeconds

``JD`` structure
----------------

The following are convenience functions for manipulating a
:class:`pytpm.tpm.JD` structure.

Set the components of :class:`pytpm.tpm.JD` to scalar values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [15]: jd = tpm.j2jd(tpm.gcal2j(2000,1,1))
   
  In [16]: print utils.fmt_jd(jd)
  -------> print(utils.fmt_jd(jd))
   2451545  00H 00M 00.000S

  In [19]: utils.jdSetDay(jd, 2451545)
   
  In [20]: utils.jdSetHours(jd, 12)
   
  In [21]: utils.jdSetMinutes(jd, 00)
   
  In [22]: print utils.fmt_jd(jd)
  -------> print(utils.fmt_jd(jd))
   2451545  12H 00M 00.000S

.. autofunction:: jdSetDay 
.. autofunction:: jdSetHours
.. autofunction:: jdSetMinutes
.. autofunction:: jdSetSeconds

Retrieve components of :class:`pytpm.tpm.JD`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [24]: utils.jdGetDay(jd)
  Out[24]: 2451545.0
   
  In [25]: utils.jdGetMinutes(jd)
  Out[25]: 0.0
   
  In [26]: utils.jdGetSeconds(jd)
  Out[26]: 0.0

.. autofunction:: jdGetDay	
.. autofunction:: jdGetHours
.. autofunction:: jdGetMinutes
.. autofunction:: jdGetSeconds

Subtract a scalar from components of :class:`pytpm.tpm.JD`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [33]: utils.jdDecHours(jd, 12)
   
  In [34]: print utils.fmt_jd(jd)
  -------> print(utils.fmt_jd(jd))
   2451542  12H 00M 00.000S
   
  In [36]: jd.hms.hh
  Out[36]: -12.0
   
  In [37]: jd = tpm.jd2j
  tpm.jd2j   tpm.jd2jd  
   
  In [37]: jd = tpm.jd2jd(jd)
   
  In [38]: jd.hms.hh
  Out[38]: 12.0


.. autofunction:: jdDecDay 
.. autofunction:: jdDecHours
.. autofunction:: jdDecMinutes
.. autofunction:: jdDecSeconds

Divide components of :class:`pytpm.tpm.JD` with scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [39]: print utils.fmt_jd(jd)
  -------> print(utils.fmt_jd(jd))
   2451542  12H 00M 00.000S
   
  In [40]: utils.jdDivHours(jd, 0.9)
   
  In [41]: jd.hms.hh
  Out[41]: 13.333333333333332
   
  In [42]: jd = tpm.jd2jd(jd)
   
  In [43]: print utils.fmt_jd(jd)
  -------> print(utils.fmt_jd(jd))
   2451542  13H 19M 59.999S
   
  In [44]: jd.hms.hh
  Out[44]: 13.0


.. autofunction:: jdDivDay 
.. autofunction:: jdDivHours
.. autofunction:: jdDivMinutes
.. autofunction:: jdDivSeconds

Add a scalar to components of :class:`pytpm.tpm.JD`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [45]: utils.jdIncSeconds(jd, 10)
   
  In [46]: jd.dd, jd.hms.hh, jd.hms.mm, jd.hms.ss
  Out[46]: (2451542.0, 13.0, 19.0, 69.999995529651642)
   
  In [47]: jd = tpm.jd2jd(jd)
   
  In [48]: print utils.fmt_jd(jd)
  -------> print(utils.fmt_jd(jd))
   2451542  13H 20M 09.999S


.. autofunction:: jdIncDay 
.. autofunction:: jdIncHours
.. autofunction:: jdIncMinutes
.. autofunction:: jdIncSeconds

Multiply components of :class:`pytpm.tpm.JD` with a scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [49]: utils.jdMulHours(jd, 23.0)
   
  In [50]: jd.dd, jd.hms.hh, jd.hms.mm, jd.hms.ss
  Out[50]: (2451542.0, 299.0, 20.0, 9.9999815225601196)
   
  In [51]: jd = tpm.jd2jd(jd)
   
  In [52]: print utils.fmt_jd(jd)
  -------> print(utils.fmt_jd(jd))
   2451554  11H 20M 09.999S
   
  In [53]: jd.dd, jd.hms.hh, jd.hms.mm, jd.hms.ss
  Out[53]: (2451554.0, 11.0, 20.0, 9.9999681115150452)

.. autofunction:: jdMulDay 
.. autofunction:: jdMulHours
.. autofunction:: jdMulMinutes
.. autofunction:: jdMulSeconds


``YMD`` structure
-----------------

These are convenience functions for working with
:class:``pytpm.tpm.YMD`` instances.

Set the components of :class:`pytpm.tpm.YMD` to scalar values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [63]: utils.ymdSetYear(ymd, 2010)
   
  In [64]: utils.ymdSetMonth(ymd, 10)
   
  In [65]: utils.ymdSetDay(ymd, 28)
   
  In [66]: utils.ymdSetHours(ymd, 10)
   
  In [67]: utils.ymdSetMinutes(ymd, 15)
   
  In [68]: utils.ymdSetSeconds(ymd, 12345.98)
   
  In [69]: print tpm.fmt_ymd_raw(ymd)
  -------> print(tpm.fmt_ymd_raw(ymd))
  2010 10 28 10 15 12345.98
   
  In [70]: print tpm.fmt_ymd(ymd)
  -------> print(tpm.fmt_ymd(ymd))
  Thu Oct 28 13:40:45.980 2010
   
  In [71]: ymd = tpm.ymd2ymd(ymd)
   
  In [72]: print tpm.fmt_ymd_raw(ymd)
  -------> print(tpm.fmt_ymd_raw(ymd))
  2010 10 28 13 40 45.9800004959106

.. autofunction:: ymdSetYear
.. autofunction:: ymdSetMonth
.. autofunction:: ymdSetDay 
.. autofunction:: ymdSetHours
.. autofunction:: ymdSetMinutes
.. autofunction:: ymdSetSeconds


Retrieve components of :class:`pytpm.tpm.YMD`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [73]: utils.ymdGetHours(ymd)
  Out[73]: 13.0
   
  In [74]: utils.ymdGetSeconds(ymd)
  Out[74]: 45.980000495910645

.. autofunction:: ymdGetYear
.. autofunction:: ymdGetMonth
.. autofunction:: ymdGetDay	
.. autofunction:: ymdGetHours
.. autofunction:: ymdGetMinutes
.. autofunction:: ymdGetSeconds


Subtract a scalar from components of :class:`pytpm.tpm.YMD`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [75]: utils.ymdDecYear(ymd, 1)
   
  In [76]: utils.ymdGetYear(ymd)
  Out[76]: 2009
   
  In [77]: utils.ymdDecMonth(ymd, 23)
   
  In [78]: utils.ymdGetMonth(ymd)
  Out[78]: -13
   
  In [79]: ymd = tpm.ymd2ymd(ymd)
   
  In [80]: utils.ymdGetMonth(ymd)
  Out[80]: 11
   
  In [82]: print tpm.fmt_ymd(ymd)
  -------> print(tpm.fmt_ymd(ymd))
  Fri Nov 28 13:40:45.980 2008

  In [83]: utils.ymdDecHours(ymd, 24.0*12)
   
  In [84]: ymd = tpm.ymd2ymd(ymd)
   
  In [85]: print tpm.fmt_ymd(ymd)
  -------> print(tpm.fmt_ymd(ymd))
  Sun Nov 16 13:40:45.980 2008


.. autofunction:: ymdDecYear
.. autofunction:: ymdDecMonth
.. autofunction:: ymdDecDay 
.. autofunction:: ymdDecHours
.. autofunction:: ymdDecMinutes
.. autofunction:: ymdDecSeconds


Divide components of :class:`pytpm.tpm.YMD` with scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [95]: utils.ymdDivDay(ymd, 2)
   
  In [96]: print tpm.fmt_ymd_raw(ymd)
  -------> print(tpm.fmt_ymd_raw(ymd))
  2009 1 8 13 40 45.9800004959106
   
  In [97]: utils.ymdDivSeconds(ymd, 100)
   
  In [98]: print tpm.fmt_ymd_raw(ymd)
  -------> print(tpm.fmt_ymd_raw(ymd))
  2009 1 8 13 40 0.459800004959106


.. autofunction:: ymdDivYear
.. autofunction:: ymdDivMonth
.. autofunction:: ymdDivDay 
.. autofunction:: ymdDivHours
.. autofunction:: ymdDivMinutes
.. autofunction:: ymdDivSeconds


Add a scalar to components of :class:`pytpm.tpm.YMD`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [59]: ymd = tpm.jd2ymd(tpm.j2jd(tpm.gcal2j(2000,1,1)))
   
  In [60]: print tpm.fmt_ymd(ymd)
  -------> print(tpm.fmt_ymd(ymd))
  Sat Jan  1 12:00:00.000 2000
   
  In [61]: print tpm.fmt_ymd_raw(ymd)
  -------> print(tpm.fmt_ymd_raw(ymd))
  2000 1 1.5 0 0 0
   
  In [62]: ymd.y, ymd.m, ymd.dd, ymd.hms.hh, ymd.hms.mm, ymd.hms.ss
  Out[62]: (2000, 1, 1.5, 0.0, 0.0, 0.0)

.. autofunction:: ymdIncDay 
.. autofunction:: ymdIncHours
.. autofunction:: ymdIncMinutes
.. autofunction:: ymdIncMonth
.. autofunction:: ymdIncSeconds
.. autofunction:: ymdIncYear

Multiply components of :class:`pytpm.tpm.YMD` with a scalar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: ipython

  In [3]: ymd = tpm.jd2ymd(tpm.j2jd(tpm.gcal2j(2000,1,1)))
   
  In [4]: print tpm.fmt_ymd_raw(ymd)
  ------> print(tpm.fmt_ymd_raw(ymd))
  2000 1 1.5 0 0 0
   
  In [10]: utils.ymdMulDay(ymd, 300)
   
  In [11]: utils.ymdMulMonth(ymd, 300)
   
  In [12]: print tpm.fmt_ymd_raw(ymd)
  -------> print(tpm.fmt_ymd_raw(ymd))
  2000 300 300 12 0 0
   
  In [13]: ymd = tpm.ymd2ymd(ymd)
   
  In [14]: print tpm.fmt_ymd_raw(ymd)
  -------> print(tpm.fmt_ymd_raw(ymd))
  2025 9 26 12 0 0


.. autofunction:: ymdMulYear
.. autofunction:: ymdMulMonth
.. autofunction:: ymdMulDay 
.. autofunction:: ymdMulHours
.. autofunction:: ymdMulMinutes
.. autofunction:: ymdMulSeconds


Functions for generating string representations
-----------------------------------------------

The following functions return string representation of the quantities
in the appropriate data structures passed to them.

.. autofunction:: fmt_dms
.. autofunction:: fmt_hms
.. autofunction:: fmt_jd

Several other string formatting functions are listed in the section
titled :ref:`tpm_func_gen_string`.


Date conversion
===============

There are 4 functions that can convert between a Julian day number and
a year. The function ``byear2jd`` converts the given year in the in
the Basselian year system into Julian day number.  ``jd2byear``
converts a Julian day number into a year in the Basselian year
system. Functions ``jyear2jd`` and ``jd2jyear`` performs a similar
conversion between a Julian day number and a year in the Julian year
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

.. _utils_angle_conv_functions:

Functions related to angles
---------------------------

.. autofunction:: r2dms
.. autofunction:: d2r
.. autofunction:: r2d
.. autofunction:: d2as
.. autofunction:: as2d
.. autofunction:: r2as
.. autofunction:: as2r

.. _utils_conv_angle_time:

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

Functions related to dates
--------------------------

.. autofunction:: j2j
.. autofunction:: j2y
.. autofunction:: j2ymd
.. autofunction:: jd2y
.. autofunction:: y2j
.. autofunction:: y2jd
.. autofunction:: y2y
.. autofunction:: ymd2j
.. autofunction:: ymd_diff

