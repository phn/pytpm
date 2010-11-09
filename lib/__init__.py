"""PyTPM: python interface to the Telescope Pointing Machine C library.

Telescope Pointing Machine, TPM, is a C library written by Jeff
Percival, for performing astrometry calculations, needed for computing
the positions of astronomical objects. It is being used at the WIYN
3.5m telescope at KPNO, for example, for calculating pointing
directions for the telescope.

PyTPM is a python interface to the TPM library, and is mainly a
"wrapper" creating using SWIG.

The PyTPM library has two parts: ``pytpm.tpm`` and ``pytpm.utils``.
The former is the main interface to the C library and allows calling
all the functions defined in the library. The latter contains python
functions that carry out the same calculations as the various C macros
defined in the TPM library. These cannot be wrapped using SWIG and
hence they are provided as functions. These functions were named by
adding an "f" to the name of the corresponding C macro. For example,
``v3SetX`` macro is implemented as the ``v3SetXf`` function in
``pytpm.utils``.

The ``pytpm.tpm`` and ``pytpm.utils`` modules, both, have a function
named ``convert``. The ``convert`` function in the former module can
be used for performing coordinate conversions using TPM. Since it is
written in C, all the arguments must be explicitly provided in the
function call. The ``convert`` function in the latter, is written in
python and calls the former. Since it is written in python, it has
keyword parameters and default values for most of the parameters
required by ``convert``, thereby making it easier to use the function.

For more details, see the docstrings for individual functions, where
available, and the main documentation.

:Author: Prasanth Nair
:Contact: prasanthhn@gmail.com
"""
import tpm
import utils

__version__ = "0.3dev"
