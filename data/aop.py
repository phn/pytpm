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
try:
    from pytpm import tpm, convert
except ImportError:
    sys.path.append("..")
    from pytpm import tpm, convert

# Load HIPPARCOS data and output form running SLALIB aop.
hip_tab = get_hipdata()
tab = np.loadtxt(os.path.join(testdatadir, "slalib_hip_aop.txt"))

# Normalize "alpha" angles to 0 - 360.0
az_sla = np.array([i if i >= 0 else i + 360.0 for i in tab[:, 0]])
zd_sla = tab[:, 1]
ha_sla = np.array([i if i >= 0 else i + 360.0 for i in tab[:, 2]])
dec_sla = tab[:, 3]
ra_sla = np.array([i if i >= 0 else i + 360.0 for i in tab[:, 4]])

# Dummy radial velocity.
rv = np.zeros_like(hip_tab['px'])

# Create array of TPM V6C vectors.
v6l = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], hip_tab['pma'],
                     hip_tab['pmd'], hip_tab['px'], rv, tpm.CJ)

# Time for the observations.
utc = tpm.gcal2j(2010, 1, 1) - 0.5  # midnight
tt = tpm.utc2tdb(utc)

# Convert J2000 RA, DEC to Az, EL and ZD at given UTC.
v6o = convert.proper_motion(v6l, tt, tpm.J2000)
v619 = convert.convertv6(v6o, s1=6, s2=19, utc=utc)
cat19 = convert.v62cat(v619, tpm.CJ)
cat19 = cat2array(cat19)

az = np.degrees(cat19['alpha'])
el = np.degrees(cat19['delta'])
zd = 90.0 - el
# Keep only those objects with ZD < 75.0 degrees.
indx = np.where(zd < 75.0)

# Difference in AZ and ZD, using TPM and SLALIB.
az_diff = np.abs(az[indx] - az_sla[indx]) * 3600.0
zd_diff = np.abs(zd[indx] - zd_sla[indx]) * 3600.0

# Az, El to HA and Dec.
v620 = convert.convertv6(v619, s1=19, s2=20, utc=utc)
cat20 = convert.v62cat(v620, tpm.CJ)
cat20 = cat2array(cat20)

ha = np.degrees(cat20['alpha'])
dec = np.degrees(cat20['delta'])

# Difference in HA and Dec, using TPM and SLALIB.
ha_diff = np.abs(ha[indx] - ha_sla[indx]) * 3600.0
dec_diff = np.abs(dec[indx] - dec_sla[indx]) * 3600.0

# Find RA = LAST - HA.
tstate = tpm.TSTATE()
tpm.tpm_data(tstate, tpm.TPM_INIT)
tstate.utc = utc
tstate.delta_ut = tpm.delta_UT(utc)
tstate.delta_at = tpm.delta_AT(utc)
tstate.lon = tpm.d2r(-111.598333)
tstate.lat = tpm.d2r(31.956389)
tpm.tpm_data(tstate, tpm.TPM_ALL)
last = tpm.r2d(tstate.last)
ra = last - ha
# Have to normalize to 0 - 360.0.
ra = np.array([i if i > 0 else i + 360.0 for i in ra])
ra_diff = np.abs(ra[indx] - ra_sla[indx]) * 3600.0

print("Comparison with SLALIB aop using HIPPARCOS data.")
fs = "{0} {1}\n" + \
    "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
x = stats.describe(az_diff)
print(fs.format("az_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
x = stats.describe(zd_diff)
print(fs.format("zd_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
x = stats.describe(ha_diff)
print(fs.format("ha_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
x = stats.describe(dec_diff)
print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
x = stats.describe(ra_diff)
print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2], x[3] ** 0.5))
