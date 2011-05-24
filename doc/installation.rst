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

The source code for PyTPM can be found at
http://github.com/phn/pytpm. Either clone the repository or click on
the **Download** button in the above page. Use versions >= 0.4; 0.4 is
a complete rewrite of PyTPM using Cython instead of SWIG_ and is a much
more complete and "pythonic" implementation.

The documentation is available at http://phn.github.com/pytpm/ and the
reStructuredText source for the documentation is available with the
source code.

The package can be installed by running the command

.. code-block:: sh

  $ python setup.py install

in the main source code directory.

This will install the library in the default python *site-packages*
directory, which usually requires root access. 

For Python versions >= 2.6, we can install the package without needing
root access using:

.. code-block:: sh

  $ python setup.py install --user


If that doesn't work then, then the package can be installed in the
*PYTHONPATH* directory. The following assumes that the Python version
is 2.6 and the shell is bash.

.. code-block:: sh

  $ mkdir ~/lib
  $ export PYTHONPATH=${HOME}/lib/python2.6/site-packages
  $ python setup.py install --prefix=${HOME}

Even better, run ``python setup.py install`` inside a virtual
environment created using `virtualenv`_ and `virtualenvwrapper`_.

To run the tests execute:

.. code-block:: sh

  $ python setup.py test


Source files
============

The files for the project are arranged as follows.

The base module directory is ``pytpm`` and contains the test suite in
``pytpm/tests``. The C code for TPM is under ``src/tpm`` and the Cython
input files and Cython generate C files are under ``src/``. The C code
used in testing are available under
``pytpm/tests/c_tests``. Documentation source in restructuredtext
format is in ``doc/``. File ``setup.py`` is used for installing the
software. The file ``setup-devel.py`` is used for convenience while
developing the package and is not useful otherwise.

The declarations of functions, macros, structures and constants in TPM,
for use from within Cython, are in the ``.pxd`` files. The main
Cython code is in ``src/pytpm.pyx``, which has been split into several
``.pxi`` files. Modifying any of the Cython files in ``src/`` and
running ``setup.py`` will re-generate the Cython C file and then
re-build the extension, if Cython is installed. 

The package is divided into two modules: ``pytpm.tpm`` and
``pytpm.convert``. The former is the interface to TPM. The latter
defines a function, also called ``convert``, that can be used to
perform the most common type of coordinate conversion, i.e., convert
two angles from one coordinate system into another. Cython code for the
``pytpm.tpm`` module is in ``pytpm.pyx`` (split into .pxi files) and
the code for ``pytpm.convert`` is in ``convert.pyx``.

If none of the Cython input files and Cython generated C files have
been modified, then running ``setup.py`` will use the existing Cython
generated C files; in this case Cython need not be installed.

With this layout, ``python setup.py test`` will build the module, place
the extension module in ``pytpm`` and runs the tests in
``pytpm/tests``. This it very convenient while developing the module.

