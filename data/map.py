from __future__ import print_function
from __future__ import absolute_import
import sys
import math
from scipy import stats
import numpy as np
import os
from read_data import testdatadir
from read_data import get_hipdata, get_sla

# I want to run these without having to install PyTPM.
sys.path.append("..")
from pytpm import tpm, convert


#tab = get_sla("slalib_hip_map.txt")
tab = np.loadtxt(os.path.join(testdatadir, "slalib_hip_map.txt"))
hip_tab = get_hipdata()

rv = np.zeros_like(hip_tab['px'])

v6l = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], hip_tab['pma'],
                     hip_tab['pmd'], hip_tab['px'], rv, tpm.CJ)

utc = tpm.gcal2j(2010, 1, 1) - 0.5  # midnight
tt = tpm.utc2tdb(utc)

v6o = convert.proper_motion(v6l, tt, tpm.J2000)
v6o = convert.convertv6(v6o, s1=6, s2=11, utc=utc)

cat = convert.v62cat(v6o, tpm.CJ)

ra = [math.degrees(j['alpha']) for j in cat]
dec = [math.degrees(j['delta']) for j in cat]
ra = np.array(ra)
dec = np.array(dec)

ra_diff = np.abs(ra - tab[:, 0]) * 3600.0
dec_diff = np.abs(dec - tab[:, 1]) * 3600.0

fs = "{0} {1}\n" + \
    "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
x = stats.describe(ra_diff)
print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
x = stats.describe(dec_diff)
print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
