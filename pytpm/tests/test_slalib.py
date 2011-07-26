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
    f = open(os.path.join(testdatadir,"ndwfs.txt"),"r")
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

def get_sla(filename):
        f = open(os.path.join(testdatadir,filename),"r")
        tab = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC,
                   delimiter=" ", skipinitialspace=True)
        
        l = list(tab)
        f.close()
        return l

class TestSLALIBNDWFS(unittest.TestCase):
    """Test results with SLALIB for NDWFS data set."""
    def setUp(self):
        self.ndwfs_tab = get_ndwfs()
        
    def test_slalib_nwdfs_fk54z(self):
        """convertv6(x,s1=6,s=5) + PM <=> SLALIB FK5-FK4 (fk54z)"""
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
            pma = v['pma']*1000.0/100.0
            pmd = v['pmd']*1000.0/100.0

            ra_diff = abs(ra - s[0])*3600.0
            dec_diff = abs(dec - s[1])*3600.0
            pma_diff = abs(pma - s[2])
            pmd_diff = abs(pmd - s[3])
            self.assertTrue(ra_diff <= 0.0001 )
            self.assertTrue(dec_diff <= 0.0001)
            self.assertTrue(pma_diff <= 1)
            self.assertTrue(pmd_diff <= 1)            

    def test_slalib_nwdfs_fk45z(self):
        """convertv6(x,s1=5,s=6) <=> SLALIB FK4-FK5 (fk45z)"""
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

            ra_diff = abs(ra - s[0])*3600.0
            dec_diff = abs(dec - s[1])*3600.0
            self.assertTrue(ra_diff <= 0.5 )
            self.assertTrue(dec_diff <= 0.5)

    def test_slalib_nwdfs_eqecl(self):
        """convertv6(x,s1=6,s=3) <=> SLALIB eqecl"""
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

            ra_diff = abs(ra - s[0])*3600.0
            dec_diff = abs(dec - s[1])*3600.0
            self.assertTrue(ra_diff <= 0.07 )
            self.assertTrue(dec_diff <= 0.07)

    def test_slalib_nwdfs_ecleq(self):
        """convertv6(x,s1=3,s=6) <=> SLALIB ecleq"""
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

            ra_diff = abs(ra - s[0])*3600.0
            dec_diff = abs(dec - s[1])*3600.0
            self.assertTrue(ra_diff <= 0.07 )
            self.assertTrue(dec_diff <= 0.07)

    def test_slalib_nwdfs_eqgal(self):
        """convertv6(x,s1=6,s=4) <=> SLALIB eqgal"""
        v6l = []        
        for r, d in zip(self.ndwfs_tab['raj2'], self.ndwfs_tab['decj2']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=6, s2=4)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_ndwfs_eqgal.txt")
        
        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0])*3600.0
            dec_diff = abs(dec - s[1])*3600.0
            self.assertTrue(ra_diff <= 0.5 )
            self.assertTrue(dec_diff <= 0.5 )

    def test_slalib_nwdfs_galeq(self):
        """convertv6(x,s1=4,s=6) <=> SLALIB galeq"""
        v6l = []        
        for r, d in zip(self.ndwfs_tab['glon'], self.ndwfs_tab['glat']):
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = tpm.d2r(r)
            v6.delta = tpm.d2r(d)
            v6l.append(v6.s2c())

        v6o = convert.convertv6(v6l, s1=4, s2=6)
        cat = (tpm.v62cat(v, tpm.CJ) for v in v6o)

        tab = get_sla("slalib_ndwfs_galeq.txt")
        
        for v, s in zip(cat, tab):
            ra = math.degrees(tpm.r2r(v['alpha']))
            dec = math.degrees(v['delta'])

            ra_diff = abs(ra - s[0])*3600.0
            dec_diff = abs(dec - s[1])*3600.0
            self.assertTrue(ra_diff <= 0.5 )
            self.assertTrue(dec_diff <= 0.5 )        
