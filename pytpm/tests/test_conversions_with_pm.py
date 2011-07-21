"""Conversions with proper motion, using Hipparcos data."""
# See pytpm/tests/c_tests/test_conversions_with_pm.c.
import unittest
from pytpm import tpm, convert
import os
import math

test_dir = os.path.abspath(os.path.dirname(__file__))
hip_data = os.path.join(test_dir, "data/hip_icrs.txt")
c_tests_dir = os.path.join(test_dir, "c_tests")

def get_tstate():
    tstate = tpm.TSTATE()
    tpm.tpm_data(tstate, tpm.TPM_INIT)
    tstate.utc = tpm.J2000
    tstate.lon = tpm.d2r(-111.598333)
    tstate.lat = tpm.d2r(31.956389)
    tstate.alt = 2093.093
    tstate.delta_at = tpm.delta_AT(tstate.utc)
    tstate.delta_ut = tpm.delta_UT(tstate.utc)
    tpm.tpm_data(tstate, tpm.TPM_ALL)

    return tstate
    
class TestICRSEp19912Other(unittest.TestCase):
    """ICRS 1991.25 (~J2000 1991.25) to other states."""
    def testToFK4B1950Ep1950(self):
        """P and V: J2000 (~ICRS) 1991.25 => FK4 B1950 ep 1950.0."""
        # Set s2=TPM_S05 and ep2=B1950 in
        # c_tests/test_conversion_with_pm.c.
        ra = []
        dec = []
        pmra = []
        pmdec = []
        px = []
        f = open(hip_data, "r")
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

        pvec = tpm.PVEC()
        tstate = get_tstate()
        
        for i in xrange(len(ra)):
            v6 = tpm.cat2v6(ra[i], dec[i], pmra[i], pmdec[i], px[i], 0.0,
                            tpm.CJ)
            pvec[s1] = v6
            tpm.tpm(pvec, s1, s2, ep, eq, tstate)
            v6 = pvec[s2]
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

    def testToGalEp1950(self):
        """P and V: J2000 (~ICRS) 1991.25 => Gal ep 1950.0."""
        # Set s2=TPM_S04 and ep2=B1950 in
        # c_tests/test_conversion_with_pm.c.
        ra = []
        dec = []
        pmra = []
        pmdec = []
        px = []
        f = open(hip_data, "r")
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
        s2 = tpm.TPM_S04
        ep2 = tpm.B1950

        f = open(os.path.join(c_tests_dir,
                              "hipicrsep1991_Galep1950.txt"),"r")

        pvec = tpm.PVEC()
        tstate = get_tstate()
        
        for i in xrange(len(ra)):
            v6 = tpm.cat2v6(ra[i], dec[i], pmra[i], pmdec[i], px[i], 0.0,
                            tpm.CJ)
            pvec[s1] = v6
            tpm.tpm(pvec, s1, s2, ep, eq, tstate)
            v6 = pvec[s2]
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
        
    def testToEclJ2000Ep2000(self):
        """P and V: J2000 (~ICRS) 1991.25 => Ecl J2000 ep J2000."""        
        # Set s2=TPM_S03 and ep2=J2000 in
        # c_tests/test_conversion_with_pm.c.
        ra = []
        dec = []
        pmra = []
        pmdec = []
        px = []
        f = open(hip_data, "r")
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
        s2 = tpm.TPM_S03
        ep2 = tpm.J2000

        f = open(os.path.join(c_tests_dir,
                              "hipicrsep1991_EclJ2000ep2000.txt"),"r")

        pvec = tpm.PVEC()
        tstate = get_tstate()
        
        for i in xrange(len(ra)):
            v6 = tpm.cat2v6(ra[i], dec[i], pmra[i], pmdec[i], px[i], 0.0,
                            tpm.CJ)
            pvec[s1] = v6
            tpm.tpm(pvec, s1, s2, ep, eq, tstate)
            v6 = pvec[s2]
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

    def testToObsAzElDateJ2000ep2000(self):
        """P and V: J2000 (~ICRS) 1991.25 => ObsAzEl Date J2000 ep J2000."""
        # Set s2=TPM_S13 and ep2=J2000 in
        # c_tests/test_conversion_with_pm.c.
        ra = []
        dec = []
        pmra = []
        pmdec = []
        px = []
        f = open(hip_data, "r")
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
        s2 = tpm.TPM_S13
        ep2 = tpm.J2000

        f = open(os.path.join(c_tests_dir,
                              "hipicrsep1991_ObsAzElDateJ2000ep2000.txt"),
                 "r")

        pvec = tpm.PVEC()
        tstate = get_tstate()
        
        for i in xrange(len(ra)):
            v6 = tpm.cat2v6(ra[i], dec[i], pmra[i], pmdec[i], px[i], 0.0,
                            tpm.CJ)
            pvec[s1] = v6
            tpm.tpm(pvec, s1, s2, ep, eq, tstate)
            v6 = pvec[s2]
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
        
