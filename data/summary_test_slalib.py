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

from read_data import get_hipdata, get_sla, cat2array

# I want to run these without having to install PyTPM.
try:
    from pytpm import tpm, convert
except ImportError:
    sys.path.append("..")
    from pytpm import tpm, convert


def hipfk524():
    """Print summary of FK5-FK4 comparison with SLALIB fk524 (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_fk524.txt")
    rv = np.zeros((len(hip_tab['px'],)))

    v6l = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], hip_tab['pma'],
                    hip_tab['pmd'], hip_tab['px'], rv, tpm.CJ)

    v6o = convert.convertv6(v6l, s1=6, s2=5, epoch=tpm.J2000)
    v6o = convert.proper_motion(v6o, tpm.B1950, tpm.J2000)
    cat = (tpm.v62cat(v, tpm.CB) for v in v6o)
    d = cat2array(cat)

    ra_diff = np.degrees(d['alpha']) - sla_tab[:, 0]
    ra_diff *= 3600.0
    dec_diff = np.degrees(d['delta']) - sla_tab[:, 1]
    dec_diff *= 3600.0
    px_diff = d['px'] * 1000.0 - sla_tab[:, 2]
    pma_diff = d['pma'] * 1000.0 / 100.0 - sla_tab[:, 3]
    pmd_diff = d['pmd'] * 1000.0 / 100.0 - sla_tab[:, 4]
    rv_diff = d['rv'] - sla_tab[:, 5]

    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
    x = [stats.describe(np.abs(i)) for i in
         [ra_diff, dec_diff, px_diff, pma_diff, pmd_diff, rv_diff]]
    print("Comparison with SLALIB fk524 using HIPPARCOS data.")
    for name, unit, s in zip(
        ["ra_diff", "dec_diff", "px_diff", "pma_diff", "pmd_diff",
         "rv_diff"],
        ["arsec", "arcsec", "milliarcsec", "milli-arsec/trop. yr",
         "milli-arcsec/trop. yr", "km/s"],
        x):
        print(fs.format(name, unit, s[1][0], s[1][1], s[2], s[3] ** 0.5))


def hipfk425():
    """Print summary of FK4-FK5 comparison with SLALIB fk425 (HIP).

    The input FK4 data is the same generated for the the FK5-FK4
    conversion test. I read that data into slalib and perform the
    reverse conversion. The result is then compared with that from
    PyTPM.
    """
    sla_tabb = get_sla("slalib_hip_fk524.txt")
    sla_tab = get_sla("slalib_hip_fk524_fk425.txt")

    r = np.radians(sla_tabb[:, 0])
    d = np.radians(sla_tabb[:, 1])
    px = sla_tabb[:, 2] / 1000.0
    pma = sla_tabb[:, 3] / 1000.0 * 100.0
    pmd = sla_tabb[:, 4] / 1000.0 * 100.0
    rv = sla_tabb[:, 5]

    v6l = convert.cat2v6(r, d, pma, pmd, px, rv, tpm.CB)
    v6o = convert.convertv6(v6l, s1=5, s2=6, epoch=tpm.B1950)
    v6o = convert.proper_motion(v6o, tpm.J2000, tpm.B1950)
    cat = convert.v62cat(v6o, tpm.CJ)
    cat = cat2array(cat)

    r = np.degrees(cat['alpha'])
    d = np.degrees(cat['delta'])
    # arc-sec/cent. to milli-arcsec/Jul. year.
    pma = cat['pma'] * 1000.0 / 100.0
    pmd = cat['pmd'] * 1000.0 / 100.0
    # arc-sec to milli-arcsec
    px = cat['px'] * 1000.0

    ra_diff = np.abs(r - sla_tab[:, 0]) * 3600.0
    dec_diff = np.abs(d - sla_tab[:, 1]) * 3600.0
    px_diff = np.abs(px - sla_tab[:, 2])
    pma_diff = np.abs(pma - sla_tab[:, 3])
    pmd_diff = np.abs(pmd - sla_tab[:, 4])
    rv_diff = np.abs(rv - sla_tab[:, 5])

    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
    x = [stats.describe(np.abs(i)) for i in
         [ra_diff, dec_diff, px_diff, pma_diff, pmd_diff, rv_diff]]
    print("Comparison with SLALIB fk425 using HIPPARCOS data.")
    for name, unit, s in zip(
        ["ra_diff", "dec_diff", "px_diff", "pma_diff", "pmd_diff",
         "rv_diff"],
        ["arsec", "arcsec", "milliarcsec", "milli-arsec/trop. yr",
         "milli-arcsec/trop. yr", "km/s"],
        x):
        print(fs.format(name, unit, s[1][0], s[1][1], s[2], s[3] ** 0.5))


def hipeqecl():
    """Print summary of EQ-ECL comparison with SLALIB eqecl (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_eqecl.txt")

    dummy = np.zeros((len(hip_tab['px']),))
    v6l = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], dummy, dummy,
                         dummy, dummy, tpm.CJ)

    v6o = convert.convertv6(v6l, s1=6, s2=3)
    cat = convert.v62cat(v6o, tpm.CJ)

    cat = cat2array(cat)

    ra_diff = np.degrees(cat['alpha']) - sla_tab[:, 0]
    ra_diff = np.abs(ra_diff * 3600.0)
    dec_diff = np.degrees(cat['delta']) - sla_tab[:, 1]
    dec_diff = np.abs(dec_diff * 3600.0)

    print("Comparison with SLALIB eqecl using HIPPARCOS data.")
    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))


def hipecleq():
    """Print summary of ECL-EQ comparison with SLALIB ecleq (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_ecleq.txt")

    dummy = np.zeros((len(hip_tab['px']),))
    v6l = convert.cat2v6(hip_tab['elon2'], hip_tab['elat2'], dummy, dummy,
                         dummy, dummy, tpm.CJ)

    v6o = convert.convertv6(v6l, s1=3, s2=6)
    cat = convert.v62cat(v6o, tpm.CJ)

    cat = cat2array(cat)

    ra_diff = np.degrees(cat['alpha']) - sla_tab[:, 0]
    ra_diff = np.abs(ra_diff * 3600.0)
    dec_diff = np.degrees(cat['delta']) - sla_tab[:, 1]
    dec_diff = np.abs(dec_diff * 3600.0)

    print("Comparison with SLALIB ecleq using HIPPARCOS data.")
    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))


def hipeqgal():
    """Print summary of EQ-GAL comparison with SLALIB eqgal (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_eqgal.txt")

    dummy = np.zeros((len(hip_tab['px']),))
    v6l = convert.cat2v6(hip_tab['raj2'], hip_tab['decj2'], dummy, dummy,
                         dummy, dummy, tpm.CJ)

    v6o = convert.convertv6(v6l, s1=6, s2=4)
    # The galactic coordinates are at epoch J2000. But SLALIB
    # results are for B1950. So apply proper motion here.
    v6o = convert.proper_motion(v6o, tpm.B1950, tpm.J2000)
    cat = convert.v62cat(v6o, tpm.CJ)

    cat = cat2array(cat)

    ra_diff = np.degrees(cat['alpha']) - sla_tab[:, 0]
    ra_diff = np.abs(ra_diff * 3600.0)
    dec_diff = np.degrees(cat['delta']) - sla_tab[:, 1]
    dec_diff = np.abs(dec_diff * 3600.0)

    print("Comparison with SLALIB eqgal using HIPPARCOS data.")
    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))


def hipgaleq():
    """Print summary of GAL-EQ comparison with SLALIB galeq (HIP)."""
    hip_tab = get_hipdata()
    sla_tab = get_sla("slalib_hip_galeq.txt")

    dummy = np.zeros((len(hip_tab['px']),))
    v6l = convert.cat2v6(hip_tab['glon'], hip_tab['glat'], dummy, dummy,
                         dummy, dummy, tpm.CJ)

    # The actual epoch of galactic data is J2000. But in SLALIB
    # the input is taken to be B1950.0. So use tpm.B1950 as epoch
    # in the conversion.
    v6o = convert.convertv6(v6l, s1=4, s2=6, epoch=tpm.B1950)
    cat = convert.v62cat(v6o, tpm.CJ)

    cat = cat2array(cat)

    ra_diff = np.degrees(cat['alpha']) - sla_tab[:, 0]
    ra_diff = np.abs(ra_diff * 3600.0)
    dec_diff = np.degrees(cat['delta']) - sla_tab[:, 1]
    dec_diff = np.abs(dec_diff * 3600.0)

    print("Comparison with SLALIB galeq using HIPPARCOS data.")
    fs = "{0} {1}\n" + \
        "Min:  {2:.4f} Max: {3:.4f} \nMean: {4:.4f} Std: {5:.4f}\n"
    x = stats.describe(ra_diff)
    print(fs.format("ra_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))
    x = stats.describe(dec_diff)
    print(fs.format("dec_diff", "arcsec", x[1][0], x[1][1], x[2],
                    x[3] ** 0.5))


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
