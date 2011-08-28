=================================
 Comparison of PyTPM with SLALIB
=================================

.. _pypi page for the project: http://pypi.python.org/pypi/PyTPM

Automated tests that compare output from TPM C code and Python code are
present in :file:`pytpm/tests`. Most of these simply test if the output
from Python code matches that from the C code.  Automated tests that
compare PyTPM and SLALIB are present in the file
:file:`pytpm/tests/test_slalib.py`. 

All these tests are run when the `python setup.py test` command is
used.

These tests do not use Numpy, as PyTPM itself doesn't use Numpy. Most
of the work done in these tests involves reading in data and then
converting it into appropriate units. The actual conversion process
itself is very simple.

In the automated tests, I only test if the difference between SLALIB
and PyTPM is within some limit. But that can be contaminated by a few
bad data points. In order to check the distribution in difference
between PyTPM and SLALIB, I use several scripts that are present in the
folder :file:`data/` of the source code repository. These scripts are
also present in the :file:`data/` directory of source code distribution
available on the `pypi page for the project`_.  These scripts use Numpy
and Scipy.


Data
====

Both the automated tests and the scripts use the same data, present
in :file:`pytpm/tests/data`. The input data is from the HIPPARCOS
catalog and the NDWFS catalog.

The :file:`hip_full.txt` was created using
the :file:`data/hip_full.py`. This file contains data from the
HIPPARCOS catalog downloaded from Vizier.  Note that **TPM does not
handle the HIPPARCOS coordinate frame**; data in other coordinate
systems are used.

The file :file:`ndwfs.txt` was created
using :file:`data/ndwfs.py`. This catalog was used as a data set that
doesn't have proper motions.

All text files that start with `slalib_` contain results obtained by
running appropriate functions in SLALIB, on the data in one of the
above two data files.

The files starting with `slalib_ndwfs_` were created using the
script :file:`data/slalib_convert_ndwfs.py`. These contain results from
SLALIB, using data in :file:`pytpm/tests/data/ndwfs.txt` as input.

The files starting with `slalib_hip_` were created using the
script :file:`data/slalib_convert_hip.py`. These contain results from
SLALIB, using data in :file:`pytpm/tests/data/hip_full.txt` as input.

Within automated tests and test scripts, the data
in :file:`hip_full.txt` or :file:`ndwfs.txt` are read and a conversion
is performed using PyTPM. This result is compared with the data in one
of the `slalib_` files, which contain results from SLALIB.

Scripts
=======

The script :file:`data/summary_test_slalib.py`, has several functions
that print summary of the difference between PyTPM and SLALIB, for
different types of coordinate conversions.

The script :file:`data/map.py` compares the results for FK5 to
geocentric apparent conversion. The SLALIB function used is `sla_map`. 

The script :file:`data/aop.py` compares the results for FK5 to
topocentric apparent. The SLALIB function used is `sla_aop`.

Comparisons
===========

Comparison of PyTPM and SLALIB for various coordinate transformations
are given below. For many conversions, SLALIB does not return
velocities, and hence the comparison of velocity output from PyTPM could
not be tested.

For each comparison the minimum, maximum, mean and variance or
std. deviation of the absolute difference between PyTPM and SLALIB
results are included. The units are arc-secs for positions and
milli-arcsec / year for proper motions.

FK5 to FK4
----------

Using function `hipfk524` in `summary_test_slalib.py`.

::

  **** FK524   ****
   
  Comparison with SLALIB fk524 using HIPPARCOS data.
  ra_diff arsec
  Min:  0.0000 Max: 0.0002 
  Mean: 0.0000 Var: 0.0000
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000
   
  px_diff milliarcsec
  Min:  0.0000 Max: 8.3406 
  Mean: 0.0767 Var: 0.1608
   
  pma_diff milli-arsec/trop. yr
  Min:  0.0000 Max: 0.0001 
  Mean: 0.0000 Var: 0.0000
   
  pmd_diff milli-arcsec/trop. yr
  Min:  0.0000 Max: 0.0001 
  Mean: 0.0000 Var: 0.0000
   
  rv_diff km/s
  Min:  0.0000 Max: 0.0397 
  Mean: 0.0001 Var: 0.0000
   
FK4 to FK5
----------

Using function `hipfk425` in `summary_test_slalib.py`.

::

  **** FK425   ****
   
  Comparison with SLALIB fk425 using HIPPARCOS data.
  ra_diff arsec
  Min:  0.0000 Max: 0.0001 
  Mean: 0.0000 Var: 0.0000
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000
   
  px_diff milliarcsec
  Min:  0.0000 Max: 8.3406 
  Mean: 0.0767 Var: 0.1608
   
  pma_diff milli-arsec/trop. yr
  Min:  0.0000 Max: 0.0001 
  Mean: 0.0000 Var: 0.0000
   
  pmd_diff milli-arcsec/trop. yr
  Min:  0.0000 Max: 0.0001 
  Mean: 0.0000 Var: 0.0000
   
  rv_diff km/s
  Min:  0.0000 Max: 0.0008 
  Mean: 0.0000 Var: 0.0000
   
FK5 to Ecliptic
---------------

Using function `hipeqecl` in `summary_test_slalib.py`.

::

  **** EQ-ECL  ****
   
  ra_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000
  
Ecliptic to FK5
---------------

Using function `hipecleq` in `summary_test_slalib.py`.

::

  **** ECL-EQ  ****
   
  ra_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000

FK5 to Galactic
---------------

Using function `hipeqgal` in `summary_test_slalib.py`.

::

  **** EQ-GAL  ****
   
  ra_diff arcsec
  Min:  0.0000 Max: 0.0001 
  Mean: 0.0000 Var: 0.0000
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000
  
Galactic to FK5
---------------

Using function `hipgaleq` in `summary_test_slalib.py`.

::

  **** GAL-EQ  ****
   
  ra_diff arcsec
  Min:  0.0000 Max: 0.0001 
  Mean: 0.0000 Var: 0.0000
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0000 
  Mean: 0.0000 Var: 0.0000

Fk5 to geocentric apparent
--------------------------

Using the script `map.py`.

::
   
  >>> %run map.py
  ra_diff arcsec
  Min:  0.0004 Max: 0.3282 
  Mean: 0.0602 Std: 0.0281
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0268 
  Mean: 0.0163 Std: 0.0081
   
FK5 to topocentric observed
---------------------------

Using the script `aop.py`.

::

  >>> %run aop.py
  az_diff arcsec
  Min:  0.0001 Max: 0.2410 
  Mean: 0.0211 Std: 0.0245
   
  zd_diff arcsec
  Min:  0.0001 Max: 0.0356 
  Mean: 0.0189 Std: 0.0091
   
  ha_diff arcsec
  Min:  0.0002 Max: 0.2783 
  Mean: 0.0263 Std: 0.0327
   
  dec_diff arcsec
  Min:  0.0000 Max: 0.0316 
  Mean: 0.0166 Std: 0.0077
   
  ra_diff arcsec
  Min:  0.0018 Max: 0.3285 
  Mean: 0.0586 Std: 0.0341


..  LocalWords:  PyTPM SLALIB LocalWords Scipy
