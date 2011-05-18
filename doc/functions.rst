.. _functions:

====================
 Functions in PyTPM
====================

.. currentmodule:: pytpm.tpm 

Most of the functions in TPM can be called from PyTPM, using functions
of the same name. These call the TPM function of the same name, with
the arguments provided and returns the value returned by the TPM
function.

.. contents::

Main TPM functions
------------------

.. autofunction:: tpm_state(s)
.. autofunction:: tpm_data(tstate, action)
.. autofunction:: proper_motion(v6, end, start)
.. autofunction:: tpm(pvec, s1, s2, ep, eq, tstate)


Date and time calculations and conversions
------------------------------------------

The current Julian date can be calculated using the following two
functions. The first function returns a ``JD`` object and the second
returns a scalar. 

.. autofunction:: jd_now
.. autofunction:: utc_now

The following functions convert a Julian date into a Basselian year and
and vice-versa.

.. autofunction:: byear2jd(byear)
.. autofunction:: jd2byear(jd)

The following functions convert a Julian date into a Julian year and
vice-versa.

.. autofunction:: jyear2jd(jyear)
.. autofunction:: jd2jyear(jd)

The functions below convert a Gregorian calendar date and a Julian
calendar date into Julian dates.

.. autofunction:: gcal2j(year, month, day)
.. autofunction:: jcal2j(year, month, day)

The function ``j2dow()`` return the day of the week corresponding to
the given Julian date. 

.. autofunction:: j2dow(j)

The function ``y2doy()`` returns the number or days in the given year.

.. autofunction:: y2doy(j)

The following two functions convert a Julian date into a year with
fractional part.

.. autofunction:: j2y(j)
.. autofunction:: y2j(y) 

Conversion between time scales
------------------------------

.. autofunction:: delta_AT(utc)
.. autofunction:: delta_T(ut1)
.. autofunction:: delta_UT(utc)
.. autofunction:: delta_ET(utc)
.. autofunction:: delta_TT(utc)
.. autofunction:: tdt2tdb(tdt)
.. autofunction:: ut12gmst(ut1)    
.. autofunction:: et2tdt(et)
.. autofunction:: tai2tdt(tai)
.. autofunction:: tdt2et(tdt)
.. autofunction:: ut12et(ut1)
.. autofunction:: utc2et(utc)
.. autofunction:: utc2tdt(utc)
.. autofunction:: utc2ut1(utc)    
.. autofunction:: et2ut1(et)
.. autofunction:: et2utc(et)
.. autofunction:: tai2utc(tai)
.. autofunction:: tdt2tai(tdt)
.. autofunction:: tdt2utc(tdt)
.. autofunction:: ut12utc(ut1)
.. autofunction:: et2tai(et)
.. autofunction:: et2tdb(et)
.. autofunction:: tai2et(tai)
.. autofunction:: tai2tdb(tai)
.. autofunction:: tai2ut1(tai)
.. autofunction:: tdt2ut1(tdt)
.. autofunction:: ut12tai(ut1)
.. autofunction:: ut12tdb(ut1)
.. autofunction:: ut12tdt(ut1)
.. autofunction:: utc2tdb(utc)
.. autofunction:: et2ut(et)
.. autofunction:: ut2et(ut)
.. autofunction:: ut2gmst(ut)


Conversion of angles between different units
--------------------------------------------

The following functions are provided for converting angles between four
different units: degrees, arc-seconds, radians and hours. Many of these
conversions can also be performed by using ``DMS`` and ``HMS`` objects.

.. autofunction:: d2d(d) 
.. autofunction:: h2h(h) 
.. autofunction:: r2r(r) 
.. autofunction:: d2h(d) 
.. autofunction:: h2d(h) 
.. autofunction:: d2r(d) 
.. autofunction:: r2d(r) 
.. autofunction:: h2r(h) 
.. autofunction:: r2h(r) 
.. autofunction:: d2as(d)
.. autofunction:: as2d(arcs) 
.. autofunction:: h2as(h) 
.. autofunction:: as2h(arcs) 
.. autofunction:: r2as(r) 
.. autofunction:: as2r(arcs) 

Formatting angles and dates
---------------------------

Formatted string representations of angles can be generated using the
following functions.

.. autofunction:: fmt_alpha(alpha)
.. autofunction:: fmt_d(d)
.. autofunction:: fmt_delta(delta)
.. autofunction:: fmt_h(h)
.. autofunction:: fmt_j(j)
.. autofunction:: fmt_r(r)
.. autofunction:: fmt_y(y)




..  LocalWords:  autofunction currentmodule pytpm tpm
