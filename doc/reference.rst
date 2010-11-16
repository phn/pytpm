Reference
=========

.. currentmodule:: pytpm

TPM library defines a set a data structures for representing vectors
and matrices, and functions and macros for manipulating these data
structures. Declarations for all these are available in the C header
files available in the TPM library source code: :file:`v3.h`,
:file:`v6.h`, :file:`m3.h`, :file:`m6.h` and :file:`vec.h`. Further
data structures, constants, functions and macros are provided for
performing calculations related to time and date. These are declared
in the header file :file:`times.h`. Constants, functions and macros
related to astrometry are declared in the header file
:file:`astro.h`. Finally, declarations for some routines for numerical
integration are provided in :file:`misc.h`.

The items in the TPM library that were wrapped with *swig* are present
in the **pytpm.tpm** module. All the macros and a few functions that
were not wrapped with *swig* are provided in the
:mod:`pytpm.utils`. Interface to the numerical integration routines
are not provided in PyTPM.

In addition, a function :func:`tpm.convert` is provided for performing
coordinate conversions. This function is an interface to a C function
defined in :file:`convert.c`, and hence requires all arguments to be
supplied when invoking it. Another function, :func:`utils.convert`, is
provided to make it easier to call :func:`tpm.convert`, by providing
keyword arguments and default values for most of the arguments needed
by :func:`tpm.convert``.

.. toctree::
    :maxdepth: 0

    reference_tpm
    reference_utils

