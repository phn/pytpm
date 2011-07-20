===============================
 Installation and source files
===============================

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

.. contents::

Requirements
============

+ A recent version of Python and gcc.
+ The Distribute_ package.
+ Cython_, only if the Cython output needs to be regenerated.

This library was tested using Python 2.6, gcc 4.4 and Cython 0.14 on
Ubuntu 10.10 and Ubuntu 11.04.

Installation
============

.. important::

    The file :file:`src/tpm/delta_AT.c` must be updated when Delta-AT
    is changed by the IERS_, and PyTPM Cython code must
    re-compiled. Update the file and just run setup.py again. See 
    :ref:`delta_at_info`, for ways to get updated values for this 
    quantity.


If you don't have Distribute_, then install it by following the
instructions `here
<http://pypi.python.org/pypi/distribute#distribute-setup-py>`_.

If you don't have Distribute_, then install it by following the
instructions 
`here
<http://pypi.python.org/pypi/distribute#distribute-setup-py>`_. Then do
one of the following:


#. Install pip/easy_install and then run `pip install pytpm` or
   `easy_install pytpm`.

or 

#. Download the distribution by clicking the *Download* button in the
   `Github repository page <https://github.com/phn/pytpm>`_ or from the
   `pypi page <http://pypi.python.org/pypi/PyTPM>`_. Then run `python
   setup.py install`. Use the `--prefix <dest>` or `--user` arguments
   to change the install location.



