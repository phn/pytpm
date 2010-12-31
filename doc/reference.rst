Reference
=========


.. currentmodule:: pytpm

TPM library defines a set a data structures for representing vectors
and matrices, and functions and macros for manipulating these data
structures. Declarations for all these are available in the C header
files in the TPM library source code: :file:`v3.h`, :file:`v6.h`,
:file:`m3.h`, :file:`m6.h` and :file:`vec.h`.  Further data
structures, constants, functions and macros are provided for
performing calculations related to time and date. These are declared
in the header file :file:`times.h`.  Constants, functions and macros
related to astrometry are declared in the header file :file:`astro.h`.
Structures used in representing TPM states are declared in
:file:`tpm.h`. Finally, declarations for some routines for numerical
integration are provided in :file:`misc.h`.

Documentation for the TPM C library, in PDF format, is included with
the source code and is also available at :download:`this url
<TPM/tpm.pdf>`.

The items in the TPM library that were wrapped with *SWIG* and made
available through PyTPM, are present in the :mod:`pytpm.tpm`
module. This includes all functions and constants implemented in the
TPM library, except the numerical integration routines defined in
:file:`misc.h`.

The macros for manipulating vectors and matrices, declared in
:file:`v3.h`, :file:`v6.h`, :file:`m3.h`, and :file:`m6.h`, have been
re-written as C function, in :file:`v3Functions.c`,
:file:`v6Functions.c`, :file:`m3Functions.c`, :file:`m6Functions.c`
and corresponding headers. They were then wrapped with *SWIG* and are
present in :mod:`pytpm.tpm`.  The names of these functions were
constructed by adding an "f" to end of the C macro name.

All other macros defined in TPM are provided as functions in the
:mod:`pytpm.utils`.  Their names are the same as the corresponding C
macro.

Interface to the numerical integration routines defined in
:file:`misc.h` are not provided in PyTPM.

In addition, a function :func:`pytpm.tpm.convert` is provided for performing
coordinate conversions. This function is an interface to a C function
defined in :file:`convert.c`, and hence requires all arguments to be
supplied when invoking it. Another function, :func:`pytpm.utils.convert`, is
provided to make it easier to call :func:`pytpm.tpm.convert`. This is
achieved by providing keyword arguments and default values for most of
the arguments needed by :func:`pytpm.tpm.convert`.

Modules
-------

.. toctree::
    :maxdepth: 1

    reference_tpm
    reference_utils

