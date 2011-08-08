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
    """Print summary of FK5-FK4 comparison with SLALIB fk524 (HIP)."""
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
        # Milli-arcsec / Jul. yr to arcsec per Jul. century.
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


def hipfk425():
    """Print summary of FK4-FK5 comparison with SLALIB fk425 (HIP).

    The input FK4 data is the same generaated for the the FK5-FK4
    conversion test. I read that data into slalib and perform the
    reverse conversion. The result is then compared with that from
    PyTPM.
    """
    sla_tabb = get_sla("slalib_hip_fk524.txt")
    sla_tab = get_sla("slalib_hip_fk524_fk425.txt")

    v6l = []
    for r, d, px, pa, pd, rv in sla_tabb:
        r = tpm.d2r(r)
        d = tpm.d2r(d)
        # Milli-arcsec / Trop. yr to arcsec per Trop. century.
        pma = pa / 1000.0 * 100.0
        pmd = pd / 1000.0 * 100.0
        px /= 1000.0  # mili-arcsec to arc-sec.
        v6 = tpm.cat2v6(r, d, pma, pmd, px, rv, tpm.CB)
        v6l.append(v6)

    v6o = convert.convertv6(v6l, s1=5, s2=6, epoch=tpm.B1950)
    v6o = convert.proper_motion(v6o, tpm.J2000, tpm.B1950)
    cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

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
        # arc-sec/cent. to milli-arcsec/Jul. year.
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


def hipeqecl():
    """Print summary of EQ-ECL comparison with SLALIB eqecl (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_eqecl.txt")

    v6l = []
    for r, d in zip(hip_tab['raj2'], hip_tab['decj2']):
        v6 = tpm.V6S()
        v6.r = 1e9
        v6.alpha = tpm.d2r(r)
        v6.delta = tpm.d2r(d)
        v6l.append(v6.s2c())

    v6o = convert.convertv6(v6l, s1=6, s2=3)
    cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

    l = len(v6o)

    ra_diff = np.zeros((l,), np.float64)
    dec_diff = ra_diff.copy()

    for v, s, i in zip(cat, sla_tab, range(l)):
        ra = math.degrees(tpm.r2r(v['alpha']))
        dec = math.degrees(v['delta'])

        ra_diff[i] = abs(ra - s[0]) * 3600.0
        dec_diff[i] = abs(dec - s[1]) * 3600.0

    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Var: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))


def hipecleq():
    """Print summary of ECL-EQ comparison with SLALIB ecleq (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_ecleq.txt")

    v6l = []
    for r, d in zip(hip_tab['elon2'], hip_tab['elat2']):
        v6 = tpm.V6S()
        v6.r = 1e9
        v6.alpha = tpm.d2r(r)
        v6.delta = tpm.d2r(d)
        v6l.append(v6.s2c())

    v6o = convert.convertv6(v6l, s1=3, s2=6)
    cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

    l = len(v6o)

    ra_diff = np.zeros((l,), np.float64)
    dec_diff = ra_diff.copy()

    for v, s, i in zip(cat, sla_tab, range(l)):
        ra = math.degrees(tpm.r2r(v['alpha']))
        dec = math.degrees(v['delta'])

        ra_diff[i] = abs(ra - s[0]) * 3600.0
        dec_diff[i] = abs(dec - s[1]) * 3600.0

    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Var: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))


def hipeqgal():
    """Print summary of EQ-GAL comparison with SLALIB eqgal (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_eqgal.txt")

    v6l = []
    for r, d in zip(hip_tab['raj2'], hip_tab['decj2']):
        v6 = tpm.V6S()
        v6.r = 1e9
        v6.alpha = tpm.d2r(r)
        v6.delta = tpm.d2r(d)
        v6l.append(v6.s2c())

    v6o = convert.convertv6(v6l, s1=6, s2=4)
    # The galactic coordinates are at epoch J2000. But SLALIB
    # results are for B1950. So apply proper motion here.
    v6o = convert.proper_motion(v6o, tpm.B1950, tpm.J2000)
    cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

    l = len(v6o)

    ra_diff = np.zeros((l,), np.float64)
    dec_diff = ra_diff.copy()

    for v, s, i in zip(cat, sla_tab, range(l)):
        ra = math.degrees(tpm.r2r(v['alpha']))
        dec = math.degrees(v['delta'])

        ra_diff[i] = abs(ra - s[0]) * 3600.0
        dec_diff[i] = abs(dec - s[1]) * 3600.0

    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Var: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))


def hipgaleq():
    """Print summary of GAL-EQ comparison with SLALIB galeq (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_galeq.txt")

    v6l = []
    for r, d in zip(hip_tab['glon'], hip_tab['glat']):
        v6 = tpm.V6S()
        v6.r = 1e9
        v6.alpha = tpm.d2r(r)
        v6.delta = tpm.d2r(d)
        v6l.append(v6.s2c())

    # The actual epoch of galactic data is J2000. But in SLALIB
    # the input is taken to be B1950.0. So use tpm.B1950 as epoch
    # in the conversion.
    v6o = convert.convertv6(v6l, s1=4, s2=6, epoch=tpm.B1950)
    cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

    l = len(v6o)

    ra_diff = np.zeros((l,), np.float64)
    dec_diff = ra_diff.copy()

    for v, s, i in zip(cat, sla_tab, range(l)):
        ra = math.degrees(tpm.r2r(v['alpha']))
        dec = math.degrees(v['delta'])

        ra_diff[i] = abs(ra - s[0]) * 3600.0
        dec_diff[i] = abs(dec - s[1]) * 3600.0

    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Var: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2], x[3]))


if __name__ == "__main__":
    print("**** FK524   ****\n")
    hipfk524()
    print("**** FK425   ****\n")
    hipfk425()
    print("**** EQ-ECL  ****\n")
    hipeqecl()
    print("**** ECL-EQ  ****\n")
    hipecleq()
    print("**** EQ-GAL  ****\n")
    hipeqgal()
    print("**** GAL-EQ  ****\n")
    hipgaleq()
