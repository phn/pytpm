.. PyTPM documentation master file, created by
   sphinx-quickstart on Mon May 16 15:10:00 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Welcome to PyTPM's documentation!
.. =================================

Python interface to the TPM C library
=====================================
.. _Telescope Pointing Machine: http://www.sal.wisc.edu/~jwp/astro/tpm/tpm.html
.. _Jeffrey W. Percival: http://www.sal.wisc.edu/~jwp/
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
.. _Nose: http://pypi.python.org/pypi/nose
.. _pypi page for the project: http://pypi.python.org/pypi/PyTPM
.. _pip: http://pypi.python.org/pypi/pip
.. _pyslalib: https://github.com/scottransom/pyslalib

PyTPM is a Python interface to the `Telescope Pointing Machine`_ (TPM)
library. TPM is a C library written by `Jeffrey W. Percival`_, for
performing coordinate conversions between several astronomical
coordinate systems.

Python interface to TPM C code is written using Cython_.

TPM was designed with the aim of incorporating it into telescope
control systems. To meet this design goal, TPM offers control over
calculations carried out during coordinate conversions. Some of these
calculations must be performed frequently, for example time related
calculations. Others need to be performed only once per night, for
example nutation and precession matrices. In general, the former class
of quantities are easier to calculate than the latter. TPM allows the
user to select the exact calculations to be performed, for a given
coordinate conversion. This enables the user to control the
computational load, which is important in telescope control
systems. TPM C library is used by the `KPNO WIYN observatory`_ and the
WHAM_ projects.

TPM is also useful outside telescope control system. It can be very
useful for converting a large catalog of coordinates. In such cases,
the "star independent" quantities, which tend to be computational
expensive to calculate, can be calculated just once for the entire
catalog. This will make coordinate conversions faster.

PyTPM is not a complete astrometry package. The aim is to provide
access to the TPM C code from Python. TPM machinery can be directly
accessed using the `pytpm.tpm` sub-module. The sub-module
`pytpm.convert` has several convenience functions that can be used for
performing coordinate conversions. The latter is sufficient for most,
but not all, calculations. 

Users must read the :download:`TPM manual <TPM/tpm.pdf>` before
attempting to use the `pytpm.tpm` module.

.. _tpm_manual:

PyTPM has been tested on Python versions 2.6, 2.7 and 3.2. Distribute_
is required for installing PyTPM. Cython is not required, unless the
Cython code is modified and needs to be re-compiled. Nose_ is required
for running tests. Sphinx_ and the numpydoc_ Sphinx extension are
required for building documentation from ReST source.

PyTPM can be downloaded from the `pypi page for the
project`_. Documentation in HTML format can also be downloaded from the
above page. HTML documentation can be viewed at
http://phn.github.com/pytpm/.

PyTPM can also be installed using pip_ or `easy_install`. Use

.. code-block:: sh

  $ pip install pytpm


See :doc:`installation` for detailed instructions on installing PyTPM.

The source code repository for PyTPM is at
https://github.com/phn/pytpm. The repository can be cloned using git,
or a copy can be downloaded using the *Download* button on the above
website.

Important notes
===============

#. The file :file:`src/tpm/delta_AT.c` must be updated when 
   Delta AT (``DAT = TAI - UTC``) is changed by the IERS_, and PyTPM
   Cython code must re-compiled. See
   :ref:`delta_at_info`, for ways to get updated values for this 
   quantity. A new version of PyTPM will be released when this change
   occurs.

#. TPM uses built-in ephemerides for the Earth and Sun, and a built-in
   model for calculating dynamic and rotational time.

Contents
========

Information on installing PyTPM can be found in :doc:`installation`.

For examples of converting positions and velocities
see :doc:`conversions`. Please read the :download:`TPM manual
<TPM/tpm.pdf>` before using the advanced facilities of PyTPM.

For a detailed list of functions and constants defined in PyTPM, see
the section on :doc:`functions`. For detailed information on the data
structures defined in PyTPM, see the section on :doc:`data_structures`.

See :doc:`comparisons` for a comparison of results obtained using
PyTPM, with that obtained using SLALIB (pyslalib_).

The document :doc:`astrometry` presents links to astrometry resources.

.. toctree::
   :maxdepth: 2

   installation
   conversions
   comparisons
   functions
   data_structures
   astrometry

Credits and license
===================

`Jeffrey W. Percival`_ wrote the TPM__ C library. See
`src/tpm/TPM_LICENSE.txt` for TPM license.

The version used here was obtained from the coords_ package (version
0.36) of the astrolib_ library. Some C source files missing from the
above source were provided by Jeff Percival.

Python and Cython code for PyTPM is released under the BSD license; see
`LICENSE.txt`.

Please send email to *prasanthhn*, at the *gmail.com* domain, for
reporting errors, and for comments and suggestions.

__ `Telescope Pointing machine`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


..  LocalWords:  TPM PyTPM ReStructuredText LocalWords Indices SLALIB pyslalib
