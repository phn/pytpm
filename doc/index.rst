.. PyTPM documentation master file, created by
   sphinx-quickstart on Mon May 16 15:10:00 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Welcome to PyTPM's documentation!
.. =================================

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
.. _IERS: http://www.iers.org/

PyTPM is a Python interface to the `Telescope Pointing Machine`_ (TPM)
C library, generated using Cython_.  TPM is a C library written by
`Jeff Percival`_, for performing coordinate conversions between several
astronomical coordinate systems. It was designed with the aim of
incorporating it into telescope control systems. It is used by the
`KPNO WIYN observatory`_ and the WHAM_ project for calculating
directions to astronomical objects. 

The TPM C source code used here was copied from the astrolib_ project,
and additional C source files were provided by Jeff Percival.

In addition to most of the functions, macros, constants and structures
defined in TPM, this module also provides a few convenience function in
the module ``pytpm.convert``. The functions in this module provides a
simple interface for performing coordinate conversions.

.. _tpm_manual:

Proper usage of PyTPM, and TPM, requires familiarity with concepts in
astrometry. Before any non-trivial use of this module please read
the :download:`TPM manual <TPM/tpm.pdf>`. A trivial use case would be
converting *FK5 epoch and equinox J2000* coordinates to *FK4 epoch and
equinox B1950* coordinates, *Galactic* coordinates or *Ecliptic epoch
and equinox J2000* coordinates. The :func:`pytpm.convert.convert`
function can be used for this. A non trivial use case would be
converting *Hipparcos ICRS epoch 1991.25* coordinates of an object
*with proper motion*, into *FK5 epoch and equinox J2000* coordinates;
as provided by the Vizier catalog service, for example.


Contents
========

.. toctree::
   :maxdepth: 2

   installation
   intro
   conversions
   data_structures
   functions
   astrometry

Important notes
===============

#. As of now there is a ~0.2 arc-seconds difference between the
   declination given by PyTPM and that given by Vizier/Simbad, for the
   FK5 J2000 to FK4 B1950 conversion, . This is most likely due to
   difference in the model used for the FK5-FK4 conversion.

#. The file :file:`src/tpm/delta_AT.c` must be updated when Delta-AT is
   changed by the IERS_, and PyTPM Cython code must re-compiled. See
   :ref:`delta_at_info`, for ways to get updated values for this 
   quantity.

#. TPM uses built-in ephemerides for the Earth and Sun, and a built-in
   model for calculating dynamic and rotational time.

Credits and license
===================

`Jeff Percival`_ wrote the TPM__ C library. See
:file:`src/tpm/TPM_LICENSE.txt` for TPM license.  Code for the
Python binding itself is released under the BSD license;
see :file:`LICENSE.txt`. The version used here was obtained from the
coords_ package (version 0.36) of the astrolib_ library. Some C source
files, missing from the above source, were provided by Jeff Percival.

Send email to user *prasanthhn*, at the *gmail.com* domain, for
reporting errors, comments, suggestions etc., for the PyTPM library.

__ `Telescope Pointing machine`_

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

