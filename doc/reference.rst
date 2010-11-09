Reference
=========

.. currentmodule:: pytpm

The PyTPM library is divided into two parts: :mod:`pytpm.tpm` and
:mod:`pytpm.utils`. The former provides access to all functions in the
TPM library and the latter provides python functions that perform the
same calculations as the C macros defined in TPM.

In addition, a function :func:`tpm.convert` is provided for performing
coordinate conversions. Another function :func:`utils.convert` is also
provided to make it easier in calling :func:`tpm.convert`, by
providing keyword arguments and default values for most of the
arguments needed by :func:`tpm.convert``.

.. toctree::
    :maxdepth: 0

    reference_tpm
    reference_utils

