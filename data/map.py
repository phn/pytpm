from __future__ import print_function
from __future__ import absolute_import
import sys
from scipy import stats
import numpy as np
import os
from read_data import testdatadir
from read_data import get_hipdata
from read_data import cat2array

# I want to run these without having to install PyTPM.
sys.path.append("..")
from pytpm import tpm, convert

# Load HIPPAROCS data and output from running SLALIB map.
hip_tab = get_hipdata()
tab = np.loadtxt(os.path.join(testdatadir, "slalib_hip_map.txt"))
rv = np.zeros_like(hip_tab['px'])

# Create V6C array from catalog data.
v6l = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], hip_tab['pma'],
                     hip_tab['pmd'], hip_tab['px'], rv, tpm.CJ)

# UTC and TDB for mid-night of 2010/1/1.
utc = tpm.gcal2j(2010, 1, 1) - 0.5  # midnight
tt = tpm.utc2tdb(utc)

# Apply proper motion from J2000 to date.
v6o = convert.proper_motion(v6l, tt, tpm.J2000)

# Convert from mean equinox J2000 to true equinox and epoch of date.
v6o = convert.convertv6(v6o, s1=6, s2=11, utc=utc)

# Convert to Numpy rec-array.
cat = convert.v62cat(v6o, tpm.CJ)
cat = cat2array(cat)

ra_diff = np.degrees(cat['alpha']) - tab[:, 0]
ra_diff = np.abs(ra_diff) * 3600.0
dec_diff = np.degrees(cat['delta']) - tab[:, 1]
dec_diff = np.abs(dec_diff) * 3600.0

print("Comparison with SLALIB map using HIPPARCOS data.")
fs = "{0} {1}\n" + \
    "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
x = stats.describe(ra_diff)
print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
x = stats.describe(dec_diff)
print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
