==============
 Installation
==============

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
.. _Nose: http://pypi.python.org/pypi/nose
.. _pip: http://pypi.python.org/pypi/pip
.. _Sphinx: http://sphinx.pocoo.org/
.. _IERS: http://www.iers.org/
.. _pypi page for the project: http://pypi.python.org/pypi/PyTPM
.. _numpydoc: http://pypi.python.org/pypi/numpydoc

.. contents::

Requirements
============

PyTPM requires the following:

+ Python 2.6, 2.7 or 3.2.
+ GCC.
+ The Distribute_ package.
+ Nose_ for running tests.
+ Cython_, only if the Cython output needs to be regenerated.

To build the documentation Sphinx_ and the numpydoc_ Sphinx extension
is required.

PyTPM was tested on Ubuntu 10.10 and 11.04.

Installation
============

.. important::

   The file :file:`src/tpm/delta_AT.c` must be updated when Delta AT
   (``DAT = TAI - UTC``) is changed by the IERS_, and PyTPM Cython code
   must re-compiled. See
   :ref:`delta_at_info`, for ways to get updated values for this 
   quantity. A new version of PyTPM will be released when this change
   occurs.

If you don't have Distribute_, then install it. Then do one of the
following:

+ pip_ or `easy_install`

  Install pip_ and then run `pip install pytpm`. 

  If `easy_install` is available then `easy_install pytpm` will also
  work. Distribute_ comes with easy_install. `pip`_ itself can be
  installed using the command `easy_install pip`.

or 

+ Manual installation.

  Download the distribution from the `pypi page for the project`_. Then
  run `python setup.py install`. Use the `--prefix <dest>` or `--user`
  arguments to change the installation location.


With both these methods, virtualenv_ and virtualenvwrapper_ can be
used. These tools enable easy installation and maintenance of Python
packages.

To run tests and to build documentation, the manual installation method
has to be followed. Run `python setup.py test` and then run `python
setup.py install`. To build documentation, run `make html` in the `doc`
directory.

Exploring the Cython code
=========================

See the file :file:`devel-notes.rst` in the source code repository.
