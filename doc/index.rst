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

PyTPM is a Python interface to the TPM library, generated using Cython_.
TPM, `Telescope Pointing Machine`_ , is a C library written by `Jeff
Percival`_, for performing coordinate conversions between several
astronomical coordinate systems. It was designed with the aim of
incorporating it into telescope control systems and hence the name. It
is used by the `KPNO WIYN observatory`_ and the WHAM_ project for
calculating directions to astronomical objects. 

In addition to most of the functions, macros, constants and structures
defined in TPM, this module also provides a convenience function,
:func:`pytpm.convert.convert`. This function can be used for the most
common type of coordinate conversion, i.e., converting two angles
between different standard systems. Functions and data structures
provided in the library can be used when more involved conversions are
needed, for example conversions involving different equinoxes and
epochs.

Contents
========

.. toctree::
   :maxdepth: 2

   installation
   intro
   conversions
   data_structures
   functions


Credits
=======

`Jeff Percival`_ wrote the TPM__ C library. See
``src/tpm/TPM_LICENSE.txt`` for TPM license. The version used here was
obtained from the coords_ package (version 0.36) of the astrolib_
library. A few C source files, missing from the above source, were
provided by Jeff Percival.

Send an email to user *prasanthhn*, at the *gmail.com* domain, for
reporting errors, comments, suggestions etc., for the PyTPM library.

__ Telescope Pointing Machine

License
=======

See ``src/tpm/TPM_LICENSE.txt`` for TPM license. Code for the Python
binding itself is released under the BSD license; see LICENSE.txt.

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

