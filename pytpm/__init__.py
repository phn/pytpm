""""PyTPM: Python interface to the Telescope Pointing Machine C library.

Telescope Pointing Machine, TPM, is a C library written by Jeff
Percival, for performing astrometry calculations, needed for computing
the positions of astronomical objects. It is being used at the WIYN
3.5m telescope at KPNO for calculating pointing directions for the
telescope.

"""

__version__ = "0.7.1"
__docformat__ = "restructuredtext en"

from . import tpm
from . import convert
