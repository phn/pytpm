"""Summarize test results.

In the automated tests, I only test if the difference between SLALIB
and PyTPM is within some limit. But that can be contaminated by a few
bad data points. So use this script to get some details of the
comparison. In here I repeat the code used in the test_slalib.py
file. But then use Numpy and Scipy for obtaining statistics.
"""
from __future__ import print_function
from __future__ import absolute_import
import sys
import math
from scipy import stats
import numpy as np

from read_data import get_hipdata, get_sla

# I want to run these without having to install PyTPM.
sys.path.append("..")
from pytpm import tpm, convert


def hipfk524():
    """Print summary of FK5-FK4 comparison with SLALIB fk524."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_fk524.txt")

    v6l = []
    for r, d, pa, pd, px in zip(hip_tab['raj2'],
                                hip_tab['decj2'],
                                hip_tab['pma'],
                                hip_tab['pmd'],
                                hip_tab['px']):
        r = tpm.d2r(r)
        d = tpm.d2r(d)
        # Milli-arcsec / Jul. yr to milli-arcsec per Jul. century.
        pma = pa / math.cos(d) / 1000.0 * 100.0
        pmd = pd / 1000.0 * 100.0
        px /= 1000.0  # mili-arcsec to arc-sec.
        v6 = tpm.cat2v6(r, d, pma, pmd, px, 0.0, tpm.CJ)
        v6l.append(v6)

    v6o = convert.convertv6(v6l, s1=6, s2=5)
    v6o = convert.proper_motion(v6o, tpm.B1950, tpm.J2000)
    cat = (tpm.v62cat(v, tpm.CB) for v in v6o)

    l = len(v6o)

    ra_diff = np.zeros((l,), np.float64)
    dec_diff = ra_diff.copy()
    px_diff = ra_diff.copy()
    pma_diff = ra_diff.copy()
    pmd_diff = ra_diff.copy()
    rv_diff = ra_diff.copy()

    for v, s, i in zip(cat, sla_tab, range(l)):
        ra = math.degrees(tpm.r2r(v['alpha']))
        dec = math.degrees(v['delta'])
        # arc-sec/cent. to milli-arcsec/trop. year.
        pma = v['pma'] * 1000.0 / 100.0
        pmd = v['pmd'] * 1000.0 / 100.0
        px = v['px'] * 1e3  # arc-sec to milli-arcsec

        ra_diff[i] = abs(ra - s[0]) * 3600.0
        dec_diff[i] = abs(dec - s[1]) * 3600.0
        px_diff[i] = abs(px - s[2])
        pma_diff[i] = abs(pma - s[3])
        pmd_diff[i] = abs(pmd - s[4])
        rv_diff[i] = abs(v['rv'] - s[5])

    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Var: {5:.4f}\n"
    x = [stats.describe(i) for i in
         [ra_diff, dec_diff, px_diff, pma_diff, pmd_diff, rv_diff]]
    print("Comparison with SLALIB fk524 using HIPPARCOS data.")
    for name, unit, s in zip(
        ["ra_diff", "dec_diff", "px_diff", "pma_diff", "pmd_diff",
         "rv_diff"],
        ["arsec", "arcsec", "milliarcsec", "milli-arsec/trop. yr",
         "milli-arcsec/trop. yr", "km/s"],
        x):
        print(fs.format(name, unit, s[1][0], s[1][1], s[2], s[3]))
