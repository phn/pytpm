# Tests for tpm.convert.convert.
import unittest
from pytpm import tpm, convert
import os
import math

test_dir = os.path.abspath(os.path.dirname(__file__))
hip_data = os.path.join(test_dir, "data/hip.txt")
c_tests_dir = os.path.join(test_dir, "c_tests")
hip_data_icrs = os.path.join(test_dir, "data/hip_icrs.txt")

class TestConvertV6(unittest.TestCase):
    """ICRS 1991.25 (~J2000 1991.25) to other states."""
    def testConvertv6(self):
        """ConvertV6: J2000 (~ICRS) 1991.25 => FK4 B1950 ep 1950.0."""
        # Set s2=TPM_S05 and ep2=B1950 in
        # c_tests/test_conversion_with_pm.c.
        ra = []
        dec = []
        pmra = []
        pmdec = []
        px = []
        f = open(hip_data_icrs, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(tpm.d2r(x[0]))
            dec.append(tpm.d2r(x[1]))
            # Milli-arcsec/year to arcsec/century.
            pmra.append( ((x[2]/1000.0) / math.cos(tpm.d2r(x[1]))) * 100.0 )
            pmdec.append( (x[3]/1000.0) * 100.0)
            px.append(x[4])
        f.close()
        
        s1 = tpm.TPM_S06
        ep = tpm.y2j(1991.25)
        eq = tpm.J2000
        s2 = tpm.TPM_S05
        ep2 = tpm.B1950

        f = open(os.path.join(c_tests_dir,
                              "hipicrsep1991_fk4B1950ep1950.txt"),"r")

        v6_l = []
        for i in range(len(ra)):
            v6 = tpm.cat2v6(ra[i], dec[i], pmra[i], pmdec[i], px[i], 0.0,
                            tpm.CJ)
            v6_l.append(v6)
            
        v6_out = convert.convertv6(v6_l, epoch=ep, equinox=eq, s1=s1, s2=s2)
        
        for v in v6_out:
            tpm.proper_motion(v, ep2, ep)
            d = tpm.v62cat(v, tpm.CJ)
            x = [float(j) for j in f.readline().strip().split()]
            self.assertAlmostEqual(tpm.r2d(tpm.r2r(d['alpha'])), x[0], 8)
            self.assertAlmostEqual(tpm.r2d(d['delta']), x[1], 8)
            self.assertAlmostEqual(d['pma'], x[2], 4)
            self.assertAlmostEqual(d['pmd'], x[3], 4)            
            self.assertAlmostEqual(d['px'], x[4], 8)
            self.assertAlmostEqual(d['rv'], x[5], 2)
            
        f.close()

    def testConvertv6Single(self):
        """ConvertV6(single): J2000 (~ICRS) 1991.25 => FK4 B1950 ep 1950.0."""
        # Set s2=TPM_S05 and ep2=B1950 in
        # c_tests/test_conversion_with_pm.c.
        ra = []
        dec = []
        pmra = []
        pmdec = []
        px = []
        f = open(hip_data_icrs, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(tpm.d2r(x[0]))
            dec.append(tpm.d2r(x[1]))
            # Milli-arcsec/year to arcsec/century.
            pmra.append( ((x[2]/1000.0) / math.cos(tpm.d2r(x[1]))) * 100.0 )
            pmdec.append( (x[3]/1000.0) * 100.0)
            px.append(x[4])
        f.close()
        
        s1 = tpm.TPM_S06
        ep = tpm.y2j(1991.25)
        eq = tpm.J2000
        s2 = tpm.TPM_S05
        ep2 = tpm.B1950

        f = open(os.path.join(c_tests_dir,
                              "hipicrsep1991_fk4B1950ep1950.txt"),"r")

        for i in range(len(ra)):
            v6 = tpm.cat2v6(ra[i], dec[i], pmra[i], pmdec[i], px[i], 0.0,
                            tpm.CJ)

            v6 = convert.convertv6(v6, epoch=ep, equinox=eq, s1=s1, s2=s2)
        
            tpm.proper_motion(v6, ep2, ep)
            d = tpm.v62cat(v6, tpm.CJ)
            x = [float(j) for j in f.readline().strip().split()]
            self.assertAlmostEqual(tpm.r2d(tpm.r2r(d['alpha'])), x[0], 8)
            self.assertAlmostEqual(tpm.r2d(d['delta']), x[1], 8)
            self.assertAlmostEqual(d['pma'], x[2], 4)
            self.assertAlmostEqual(d['pmd'], x[3], 4)            
            self.assertAlmostEqual(d['px'], x[4], 8)
            self.assertAlmostEqual(d['rv'], x[5], 2)
            
        f.close()

class TestCPrecessV6(unittest.TestCase):
    """Test convert.precessv6."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 1)
        self.assertAlmostEqual(v61.alpha, v62.alpha, 5)
        self.assertAlmostEqual(v61.delta, v62.delta, 5)
        self.assertAlmostEqual(v61.rdot, v62.rdot, 5)
        self.assertAlmostEqual(v61.alphadot, v62.alphadot, 5)
        self.assertAlmostEqual(v61.deltadot, v62.deltadot, 5)

    def testPrecessV6(self):
        """convert.precessv6 => precess V6 in inertial frame."""
        v6 = tpm.V6S(r=1e9, alpha=tpm.d2r(34.1592),
                     delta=tpm.d2r(12.9638), rdot=-0.123,
                     alphadot=0.382, deltadot=1.0)

        v6 = v6.s2c()
        v6 = [v6, v6]
        v6 = convert.precessv6(v6, tpm.J2000, tpm.J1984, tpm.PRECESS_FK5)
        
        for v in v6:
            v = v.c2s()
            self.verify(v,tpm.V6S(r=1e9, alpha=0.5924126644,
                               delta=0.2249726697,rdot=-0.1229999560,
                               alphadot=0.3809705204,
                               deltadot=1.0003321415))

class TestCPrecess(unittest.TestCase):
    """Test convert.precess."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 1)
        self.assertAlmostEqual(v61.alpha, v62.alpha, 5)
        self.assertAlmostEqual(v61.delta, v62.delta, 5)
        self.assertAlmostEqual(v61.rdot, v62.rdot, 5)
        self.assertAlmostEqual(v61.alphadot, v62.alphadot, 5)
        self.assertAlmostEqual(v61.deltadot, v62.deltadot, 5)

    def testPrecess(self):
        """convert.precess => precess in inertial frame."""
        alpha = [34.1592]*2
        delta = [12.9638]*2
        
        a,d = convert.precess(alpha, delta, tpm.J2000,
                              tpm.J1984, tpm.PRECESS_FK5)

        for i,j in zip(a,d):
            self.assertAlmostEqual(tpm.d2r(i),0.5924126644,5)
            self.assertAlmostEqual(tpm.d2r(j),0.2249726697,5)
            

class TestCProperMotion(unittest.TestCase):
    """Test convert.proper_motion."""
    def testProperMotion(self):
        """Convert.proper_motion: multiple V6C values."""
        ra = tpm.d2r(269.45402305)
        de = tpm.d2r(4.66828815)
        px = 549.01 / 1000.0 # To Arc seconds
        rv = 0.0
        # pmra * cos(de) into pmra
        pmra = (-797.84 / 1000.0 ) / math.cos(de) 
        pmra *= 100.0 # To Arcseconds per century.
        pmde = (10326.93 / 1000.0) 
        pmde *= 100.0 # To Arcseconds per century.
        C = tpm.CJ

        v6 = tpm.cat2v6(ra, de, pmra, pmde, px, rv, C)

        v6_out = convert.proper_motion([v6, v6],
                                       tpm.J2000, tpm.jyear2jd(1991.25))

        for i in v6_out:
            v6 = i.c2s()
            hms = tpm.HMS(r=v6.alpha)
            dms = tpm.DMS(r=v6.delta)
            hms.normalize()
            dms.normalize() 
     
            self.assertAlmostEqual(hms.hh, -7.0)
            self.assertAlmostEqual(hms.mm, 57.0)
            self.assertAlmostEqual(hms.ss, 48.4986, 3)
            self.assertAlmostEqual(dms.dd, 4.0)
            self.assertAlmostEqual(dms.mm, 41.0)
            self.assertAlmostEqual(dms.ss, 36.1980, 3)
                        
