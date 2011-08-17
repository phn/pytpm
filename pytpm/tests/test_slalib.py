"""Test PyTPM conversions with results form SLALIB."""
import unittest
import math
import csv
import os

from pytpm import tpm, convert

testdatadir = os.path.abspath(os.path.dirname(__file__))
testdatadir = os.path.join(testdatadir, "data")


def get_ndwfs():
    """Return data in tests/data/ndwfs.txt as a dict.

    The data file was created with ndwfs.py.
    """
    f = open(os.path.join(testdatadir, "ndwfs.txt"), "r")
    s = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                   delimiter=" ", skipinitialspace=True)
    d = dict(racj2=[], deccj2=[], raj2=[], decj2=[], rab1=[], decb1=[],
             glon=[], glat=[], elon2=[], elat2=[])

    for i in s:
        d["racj2"].append(i[0])
        d["deccj2"].append(i[1])
        d["raj2"].append(i[2])
        d["decj2"].append(i[3])
        d["rab1"].append(i[4])
        d["decb1"].append(i[5])
        d["glon"].append(i[6])
        d["glat"].append(i[7])
        d["elon2"].append(i[8])
        d["elat2"].append(i[9])
    f.close()
    return d


def get_hipdata():
    """Return data in tests/data/hip_full.txt.

    The data was created with hip_full.py file.
    """
    f = open(os.path.join(testdatadir, "hip_full.txt"), "r")
    s = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                   delimiter=" ", skipinitialspace=True)
    d = dict(ra_icrs=[], dec_icrs=[], px=[], pma=[], pmd=[],
             raj2=[], decj2=[], rab1=[], decb1=[], glon=[],
             glat=[], elon2=[], elat2=[])

    for i in s:
        d["ra_icrs"].append(i[0])
        d["dec_icrs"].append(i[1])
        d["px"].append(i[2])
        d["pma"].append(i[3])
        d["pmd"].append(i[4])
        d["raj2"].append(i[5])
        d["decj2"].append(i[6])
        d["rab1"].append(i[7])
        d["decb1"].append(i[8])
        d["glon"].append(i[9])
        d["glat"].append(i[10])
        d["elon2"].append(i[11])
        d["elat2"].append(i[12])

    f.close()
    return d


class CommentedFile(object):
    def __init__(self, f, commentstring="#"):
        self.f = f
        self.commentstring = commentstring

    def next(self):
        line = self.f.next()
        while line.startswith(self.commentstring):
            line = self.f.next()
        return line

    def __iter__(self):
        return self


def get_sla(filename):
        f = open(os.path.join(testdatadir, filename), "r")
        tab = csv.reader(CommentedFile(f), quoting=csv.QUOTE_NONNUMERIC,
                         delimiter=" ", skipinitialspace=True)

        l = list(tab)
        f.close()
        return l


class TestSLALIBNDWFS(unittest.TestCase):
    """Test results with SLALIB for NDWFS data set."""
    def setUp(self):
        self.ndwfs_tab = get_ndwfs()

    def test_slalib_nwdfs_fk54z(self):
        """convertv6(x,s1=6,s=5) + PM <=> SLALIB FK5-FK4 (fk54z) NDWFS"""
        v6l = []
        for r, d in zip(self.ndwfs_tab['raj2'], self.ndwfs_tab['decj2']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=6, s2=5)
        v6o = convert.proper_motion(v6o, tpm.B1950, tpm.J2000)
        cat = (tpm.v62cat(v, tpm.CB) for v in v6o)

        tab = get_sla("slalib_ndwfs_fk54z.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])
            # arcsec/cent to milli-arcsec/year.
            pma = v['pma'] * 1000.0 / 100.0
            pmd = v['pmd'] * 1000.0 / 100.0

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            pma_diff = abs(pma - s[2])
            pmd_diff = abs(pmd - s[3])
            self.assertTrue(ra_diff <= 0.0001 )
            self.assertTrue(dec_diff <= 0.0001)
            self.assertTrue(pma_diff <= 1)
            self.assertTrue(pmd_diff <= 1)

    def test_slalib_nwdfs_fk45z(self):
        """convertv6(x,s1=5,s=6) <=> SLALIB FK4-FK5 (fk45z) NDWFS"""
        v6l = []
        for r, d in zip(self.ndwfs_tab['rab1'], self.ndwfs_tab['decb1']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=5, s2=6)
        v6o = convert.proper_motion(v6o, tpm.J2000, tpm.B1950)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_ndwfs_fk45z.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.5 )
            self.assertTrue(dec_diff <= 0.5)

    def test_slalib_nwdfs_eqecl(self):
        """convertv6(x,s1=6,s=3) <=> SLALIB eqecl NDWFS"""
        v6l = []
        for r, d in zip(self.ndwfs_tab['raj2'], self.ndwfs_tab['decj2']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=6, s2=3)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_ndwfs_eqecl.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001 )
            self.assertTrue(dec_diff <= 0.001)

    def test_slalib_nwdfs_ecleq(self):
        """convertv6(x,s1=3,s=6) <=> SLALIB ecleq NDWFS"""
        v6l = []
        for r, d in zip(self.ndwfs_tab['elon2'], self.ndwfs_tab['elat2']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=3, s2=6)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_ndwfs_ecleq.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001 )
            self.assertTrue(dec_diff <= 0.001)

    def test_slalib_nwdfs_eqgal(self):
        """convertv6(x,s1=6,s=4) + PM <=> SLALIB eqgal NDWFS"""
        v6l = []
        for r, d in zip(self.ndwfs_tab['raj2'], self.ndwfs_tab['decj2']):
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

        tab = get_sla("slalib_ndwfs_eqgal.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001 )
            self.assertTrue(dec_diff <= 0.001 )

    def test_slalib_nwdfs_galeq(self):
        """convertv6(x,s1=4,s=6) + PM <=> SLALIB galeq NDWFS"""
        v6l = []
        for r, d in zip(self.ndwfs_tab['glon'], self.ndwfs_tab['glat']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        # The epoch of galactic data is J2000. But in SLALIB
        # the input is taken to be B1950.0. I can't apply proper_motion
        # from J2000 to B1950 before input to SLALIB since, I don't
        # have galactic velocities. In essence, the SLALIB input has a
        # proper_motion for the period B1950 to J2000, which is also
        # present in the output. By setting
        # epoch=tpm.B1950 PyTPM will return FK5 values at eq. J2000
        # but at epoch B1950, which should match the results from
        # SLALIB. The velocities for this conversion show up during
        # FK4-FK5 frame conversion.
        v6o = convert.convertv6(v6l, s1=4, s2=6, epoch=tpm.B1950)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_ndwfs_galeq.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001 )
            self.assertTrue(dec_diff <= 0.001 )


class TestSLALIBHIPFK54(unittest.TestCase):
    """Test PyTPM with SLALIB for HIPPARCOS FK5-FK4 data.

    This does not involve the HIPPARCOS frame.
    """
    def setUp(self):
        self.hip_tab = get_hipdata()

    def test_slalib_hip_fk524(self):
        """convertv6(x,s1=6,s2=5) + PM <=> SLALIB FK5-FK4 (fk524) HIP"""
        v6l = []
        for r, d, pa, pd, px in zip(self.hip_tab['raj2'],
                                    self.hip_tab['decj2'],
                                    self.hip_tab['pma'],
                                    self.hip_tab['pmd'],
                                    self.hip_tab['px']):
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

        tab = get_sla("slalib_hip_fk524.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])
            # arc-sec/cent. to milli-arcsec/trop. year.
            pma = v['pma'] * 1000.0 / 100.0
            pmd = v['pmd'] * 1000.0 / 100.0
            px = v['px'] * 1e3  # arc-sec to milli-arcsec

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            px_diff = abs(px - s[2])
            pma_diff = abs(pma - s[3])
            pmd_diff = abs(pmd - s[4])
            rv_diff = abs(v['rv'] - s[5])

            self.assertTrue(ra_diff <= 0.001)
            self.assertTrue(dec_diff <= 0.001)
            self.assertTrue(pma_diff <= 0.001)
            self.assertTrue(pmd_diff <= 0.001)
            self.assertTrue(px_diff <= 9)
            self.assertTrue(rv_diff <= 0.04)

    def test_slalib_hip_fk425(self):
        """convertv6(v6,s1=5,s2=6) + PM <=> SLALIB FK4-FK5 (fk425) HIP."""
        sla_tabb = get_sla("slalib_hip_fk524.txt")
        tab = get_sla("slalib_hip_fk524_fk425.txt")

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

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])
            # arc-sec/cent. to milli-arcsec/Jul. year.
            pma = v['pma'] * 1000.0 / 100.0
            pmd = v['pmd'] * 1000.0 / 100.0
            px = v['px'] * 1e3  # arc-sec to milli-arcsec

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            px_diff = abs(px - s[2])
            pma_diff = abs(pma - s[3])
            pmd_diff = abs(pmd - s[4])
            rv_diff = abs(v['rv'] - s[5])

            self.assertTrue(ra_diff <= 0.001)
            self.assertTrue(dec_diff <= 0.001)
            self.assertTrue(pma_diff <= 0.001)
            self.assertTrue(pmd_diff <= 0.001)
            self.assertTrue(px_diff <= 9)
            self.assertTrue(rv_diff <= 0.04)

    def test_slalib_hip_eqecl(self):
        """convertv6(x,s1=6,s=3) <=> SLALIB eqecl HIP"""
        v6l = []
        for r, d in zip(self.hip_tab['raj2'], self.hip_tab['decj2']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=6, s2=3)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_hip_eqecl.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001 )
            self.assertTrue(dec_diff <= 0.001)

    def test_slalib_hip_ecleq(self):
        """convertv6(x,s1=3,s=6) <=> SLALIB ecleq HIP"""
        v6l = []
        for r, d in zip(self.hip_tab['elon2'], self.hip_tab['elat2']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=3, s2=6)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_hip_ecleq.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001)
            self.assertTrue(dec_diff <= 0.001)

    def test_slalib_hip_eqgal(self):
        """convertv6(x,s1=6,s=4) + PM <=> SLALIB eqgal HIP"""
        v6l = []
        for r, d in zip(self.hip_tab['raj2'], self.hip_tab['decj2']):
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

        tab = get_sla("slalib_hip_eqgal.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001 )
            self.assertTrue(dec_diff <= 0.001 )

    def test_slalib_hip_galeq(self):
        """convertv6(x,s1=4,s=6) + PM <=> SLALIB galeq HIP"""
        v6l = []
        for r, d in zip(self.hip_tab['glon'], self.hip_tab['glat']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        # The epoch of galactic data is J2000. But in SLALIB
        # the input is taken to be B1950.0. I can't apply proper_motion
        # from J2000 to B1950 before input to SLALIB since, I don't
        # have galactic velocities. In essence, the SLALIB input has a
        # proper_motion for the period B1950 to J2000, which is also
        # present in the output. By setting
        # epoch=tpm.B1950 PyTPM will return FK5 values at eq. J2000
        # but at epoch B1950, which should match the results from
        # SLALIB. The velocities for this conversion show up during
        # FK4-FK5 frame conversion.
        v6o = convert.convertv6(v6l, s1=4, s2=6, epoch=tpm.B1950)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_hip_galeq.txt")

        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.001 )
            self.assertTrue(dec_diff <= 0.001 )

    def test_slalib_hip_fk52appradec(self):
        """convert(x, s1=6, s2=11) + PM => SLALIB sla_map HIP."""
        tab = get_sla("slalib_hip_map.txt")

        v6l = []
        for r, d, pa, pd, px in zip(self.hip_tab['raj2'],
                                    self.hip_tab['decj2'],
                                    self.hip_tab['pma'],
                                    self.hip_tab['pmd'],
                                    self.hip_tab['px']):
            r = tpm.d2r(r)
            d = tpm.d2r(d)
            # Milli-arcsec / Jul. yr to arcsec per Jul. century.
            pma = pa / math.cos(d) / 1000.0 * 100.0
            pmd = pd / 1000.0 * 100.0
            px /= 1000.0  # mili-arcsec to arc-sec.
            v6 = tpm.cat2v6(r, d, pma, pmd, px, 0.0, tpm.CJ)
            v6l.append(v6)

        utc = tpm.gcal2j(2010, 1, 1) - 0.5  # midnight
        tt = tpm.utc2tdb(utc)

        v6o = convert.proper_motion(v6l, tt, tpm.J2000)
        v6o = convert.convertv6(v6o, s1=6, s2=11, epoch=tt,
                                equinox=tpm.J2000,
                                utc=utc, delta_at=tpm.delta_AT(utc))

        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        l = len(v6o)

        for v, s, i in zip(cat, tab, range(l)):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0]) * 3600.0
            dec_diff = abs(dec - s[1]) * 3600.0
            self.assertTrue(ra_diff <= 0.33)
            self.assertTrue(dec_diff <= 0.03)

    def test_slalib_hip_fk52obs(self):
        """convert(x, s1=6, s2=19) (+ s2=20) + PM => SLALIB sla_aop HIP."""
        tab = get_sla("slalib_hip_aop.txt")
        az_sla = []
        zd_sla = []
        ha_sla = []
        dec_sla = []
        ra_sla = []
        for i in tab:
            # Convert longitude values to 0 - 360
            az_sla.append(i[0] if i[0] >= 0 else i[0] + 360.0)
            zd_sla.append(i[1])
            ha_sla.append(i[2] if i[2] >= 0 else i[2] + 360.0)
            dec_sla.append(i[3])
            ra_sla.append(i[4] if i[4] >= 0 else i[4] + 360.0)

        v6l = []
        for r, d, pa, pd, px in zip(self.hip_tab['raj2'],
                                    self.hip_tab['decj2'],
                                    self.hip_tab['pma'],
                                    self.hip_tab['pmd'],
                                    self.hip_tab['px']):
            r = tpm.d2r(r)
            d = tpm.d2r(d)
            # Milli-arcsec / Jul. yr to arcsec per Jul. century.
            pma = pa / math.cos(d) / 1000.0 * 100.0
            pmd = pd / 1000.0 * 100.0
            px /= 1000.0  # mili-arcsec to arc-sec.
            v6 = tpm.cat2v6(r, d, pma, pmd, px, 0.0, tpm.CJ)
            v6l.append(v6)

        utc = tpm.gcal2j(2010, 1, 1) - 0.5  # midnight
        tt = tpm.utc2tdb(utc)

        # Convert to Az-EL.
        v6o = convert.proper_motion(v6l, tt, tpm.J2000)
        v6o = convert.convertv6(v6o, s1=6, s2=19, utc=utc)

        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        az = []
        zd = []
        for i in cat:
            az.append(tpm.r2d(i['alpha']))
            zd.append(90.0 - tpm.r2d(i['delta']))

        # Convert Az-El to HA-Dec.
        v6o = convert.convertv6(v6o, s1=19, s2=20, utc=utc)

        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        # Find LAST.
        tstate = tpm.TSTATE()
        tpm.tpm_data(tstate, tpm.TPM_INIT)
        tstate.utc = utc
        tstate.delta_ut = tpm.delta_UT(utc)
        tstate.delta_at = tpm.delta_AT(utc)
        tstate.lon = tpm.d2r(-111.598333)
        tstate.lat = tpm.d2r(31.956389)
        tpm.tpm_data(tstate, tpm.TPM_ALL)
        last = tpm.r2d(tstate.last)

        ha = []
        dec = []
        ra = []
        for i in cat:
            ha.append(tpm.r2d(i['alpha']))
            dec.append(tpm.r2d(i['delta']))
            # RA = LAST - HA and convert to 0 - 360.
            x = last - tpm.r2d(i['alpha'])
            ra.append(x if x >= 0  else x + 360.0)

        for i in range(len(az)):
            # Test only the coordinates with ZD < 75.0.
            if zd[i] < 75.0:
                self.assertTrue(abs(az[i] - az_sla[i]) * 3600.0 <= 0.25)
                self.assertTrue(abs(zd[i] - zd_sla[i]) * 3600.0 <= 0.04)
                self.assertTrue(abs(ha[i] - ha_sla[i]) * 3600.0 <= 0.28)
                self.assertTrue(abs(dec[i] - dec_sla[i]) * 3600.0 <= 0.04)
                self.assertTrue(abs(ra[i] - ra_sla[i]) * 3600.0 <= 0.33)
