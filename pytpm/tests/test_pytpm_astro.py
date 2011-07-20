# -*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_astro.pxi file.
import unittest
from pytpm import tpm
from test_pytpm_tpm import CheckTSTATE

def default_values(key):
    v = dict(
        t_ind = dict(utc=2451545.6789234, delta_at=32,
                 delta_ut=3.481618662951, lon=-111.598333,
                 lat=31.956389, alt=2093.093, xpole=0.0,
                 ypole=0.0, P=1013.25, T=273.15,
                 wavelength=0.550),
        t_dep = dict(tai=0.0, tdt=0.0, tdb=0.0, obliquity=0.0,
                 nut_lon=0.0, nut_obl=0.0, ut1=0.0, gmst=0.0,
                 gast=0.0, last=0.0, refa=0.000282646376, refap=12,
                 refb=-0.000000324825, refbp=12),
        t_m3 = dict(XX=1.0, XY=0.0, XZ=0.0,
                YX=0.0, YY=1.0, YZ=0.0,
                ZX=0.0, ZY=0.0, ZZ=1.0),
        t_v6 = dict(x=0.0, y=0.0, z=0.0, xdot=0.0, ydot=0.0, zdot=0.0))
    return v.get(key)
    

class TestTPMData(unittest.TestCase, CheckTSTATE):
    """Check tpm_data: calculates dependent state data."""
    # See pytpm/tests/c_tests/tpm_data_test.c, for test values.

    # The proper order is INIT (only once), REFRACTION (if needed),
    # SLOW, FAST, MEDIUM.
    def setdefaults(self, tstate):
        utc = 2451545.6789234; # Just a number.
        tstate.utc = utc
        tstate.delta_at = 32 # from tpm_data_test.c output.
        tstate.delta_ut = 3.481618662951
        tstate.lon = -111.598333
        tstate.lat = 31.956389
        tstate.alt = 2093.093
        # All other parameters are defaults.
        return tstate
        
    def testALL(self):
        """tpm_data(TSTATE, TPM_ALL) => calculate all quantities."""
        
        tstate = tpm.TSTATE()
        tpm.tpm_data(tstate, tpm.TPM_INIT)
        tstate = self.setdefaults(tstate)
        tpm.tpm_data(tstate, tpm.TPM_ALL)
        
        self.check_ind(tstate, default_values('t_ind'))

        self.check_dep_scalars(tstate, dict(
                tai=2451545.679293770343, taip=12,
                tdt=2451545.679666270502, tdtp=12,
                tdb=2451545.679666270036, tdbp=12,
                obliquity=0.409092799999, obliquityp=12,
                nut_lon=-0.000067440875, nut_lonp=12,
                nut_obl=-0.000028061065, nut_oblp=12,
                ut1=2451545.678963696584, ut1p=12,
                gmst=2.889510699245, gmstp=12,
                gast=2.889448823451, gastp=12,
                last=4.388451352684, lastp=12,
                refa=0.000292752467, refap=11,
                refb=-0.000000308573, refbp=11
                ))

        t_m3 = dict(
            XX= 9.999999977258641e-01, XXp=12,
            XY=6.187579351812524e-05, XYp=12,
            XZ=2.682643933803953e-05, XZp=12,
            YX=-6.187654627222567e-05, YXp=12,
            YY=9.999999976919580e-01, YYp=12,
            YZ=2.806023517260188e-05, YZp=12,
            ZX=-2.682470302680538e-05, ZXp=12,
            ZY=-2.806189503626471e-05, ZYp=12,
            ZZ=9.999999992464826e-01, ZZp=12
            )
        self.checkm3(tstate.nm, t_m3)
 
        self.checkm3(tstate.pm.pp, dict(
                XX=9.999999999998971e-01, XXp=12,
                XY=-4.161124735358035e-07, XYp=12,
                XZ=-1.808195760693911e-07, XZp=12,
                YX=4.161124735358035e-07, YXp=12,
                YY=9.999999999999134e-01, YYp=12,
                YZ=-3.762064065129431e-14, YZp=12,
                ZX=1.808195760693911e-07, ZXp=12,
                ZY=-3.762064041063928e-14, ZYp=12,
                ZZ=9.999999999999837e-01, ZZp=12
                ))

        self.checkm3(tstate.pm.vv,dict(
                XX=9.999999999998971e-01, XXp=12,
                XY=-4.161124735358035e-07, XYp=12,
                XZ=-1.808195760693911e-07, XZp=12,
                YX=4.161124735358035e-07, YXp=12,
                YY=9.999999999999134e-01, YYp=12,
                YZ=-3.762064065129431e-14, YZp=12,
                ZX=1.808195760693911e-07, ZXp=12,
                ZY=-3.762064041063928e-14, ZYp=12,
                ZZ=9.999999999999837e-01, ZZp=12
                ))

        t_m3 = default_values('t_m3') 
        t_m3['XX'] = 0.0
        t_m3['YY'] = 0.0
        t_m3['ZZ'] = 0.0
        self.checkm3(tstate.pm.pv, t_m3)
        self.checkm3(tstate.pm.vp, t_m3)  

        self.checkv6(tstate.eb, dict(
                x=-1.959527204776065e-01, xp=12,
                y=8.827521071100740e-01, yp=12,
                z=3.829394946400003e-01, zp=12,
                xdot=-1.716431607228530e-02, xdotp=12,
                ydot=-3.093231817130565e-03, ydotp=12,
                zdot=-1.340979212829042e-03, zdotp=12
                ))
        self.checkv6(tstate.eh, dict(
                xdot=-1.716969479680703e-02, xdotp=12,
                ydot=-3.086441747487442e-03, ydotp=12,
                zdot=-1.337936065008866e-03, zdotp=12,
                x=-1.888170693058779e-01, xp=12,
                y=8.853911600516829e-01, yp=12,
                z=3.838612151173417e-01, zp=12
                ))
        self.checkv6(tstate.obs_m, dict(
                x=2.625603380878096e-06, xp=12,
                y=3.650859582053096e-05, yp=12,
                z=2.181688492029034e-05, zp=12,
                xdot=-2.300183002664428e-04, xdotp=12,
                ydot=1.654231868604970e-05, ydotp=12,
                zdot=0.000000000000000e+00, zdotp=12
                ))
        self.checkv6(tstate.obs_t, dict(
                x=2.625603380878096e-06, xp=12,
                y=3.650859582053096e-05, yp=12,
                z=2.181688492029034e-05, zp=12,
                xdot=-2.300183002664428e-04, xdotp=12,
                ydot=1.654231868604970e-05, ydotp=12,
                zdot=0.000000000000000e+00, zdotp=12
                ))
        self.checkv6(tstate.obs_s, dict(
                x=-1.164921531873317e-05, xp=12,
                y=-3.470047800709317e-05, yp=12,
                z=2.181560079536653e-05, zp=12,
                xdot=2.186226002419965e-04, xdotp=12,
                ydot=-7.339090825315956e-05, ydotp=12,
                zdot=3.765470488651664e-09, zdotp=12
                ))


class TestTimeFunctions(unittest.TestCase):
    """Test functions that calculate time in various time scales."""
    utc = [tpm.MJD_0, tpm.B1950, tpm.J2000, tpm.J1984,
           2455667.9002314815]
    def testDeltaAT(self):
        """delta_AT(utc): TAI - UTC for the given UTC."""
        dat = [10.0, 10.0, 32.0, 22.0, 34.0]
        for i,j in zip(self.utc, dat):
            self.assertAlmostEqual(tpm.delta_AT(i), j)

    def testDeltaUT(self):
        """delta_UT(utc): UT1 - UTC for the given UTC."""
        dut = [34.384, 13.032937389587, 3.482360655738, 0.392497267760,
               0.967397006595]
        for i,j in zip(self.utc, dut):
            self.assertAlmostEqual(tpm.delta_UT(i), j, 12)

    def testDeltaT(self):
        """delta_T(ut1): TT - UT1 for the given UT1."""
        dt = [7.8, 29.166059415081, 60.705445202903, 53.792092550539,
              65.217663154508]
        ut1 = [x+tpm.delta_UT(x) for x in self.utc]
        for i,j in zip(ut1, dt):
            self.assertAlmostEqual(tpm.delta_T(i), j, 12)

    def testDeltaET(self):
        """delta_ET(utc): ET - UTC for the given UTC."""
        det = [42.184, 42.184, 64.184, 54.184, 66.184]
        for i,j in zip(self.utc, det):
            self.assertAlmostEqual(tpm.delta_ET(i), j, 12)

    def testDeltaTT(self):
        """delta_TT(utc): TT - UTC for the given UTC."""
        dtt = [42.184, 42.184, 64.184, 54.184, 66.184]
        for i,j in zip(self.utc, dtt):
            self.assertAlmostEqual(tpm.delta_TT(i), j, 12)

            
class TestPVECClass(unittest.TestCase):
    """Test facilities of the PVEC class: array of V6 vectors."""
    def checkpvec(self, pvec, i, t):
        """Check values of pvec with those in t"""
        self.assertAlmostEqual(pvec[i].x, t['x'])
        self.assertAlmostEqual(pvec[i].y, t['y'])
        self.assertAlmostEqual(pvec[i].z, t['z'])
        self.assertAlmostEqual(pvec[i].xdot, t['xdot'])
        self.assertAlmostEqual(pvec[i].ydot, t['ydot'])
        self.assertAlmostEqual(pvec[i].zdot, t['zdot'])            

    def testCreate(self):
        """PVEC() => a PVEC object."""
        pvec = tpm.PVEC()
        self.assertEqual(type(pvec), tpm.PVEC)
        
    def testInit(self):
        """PVEC() => pvec with default values for all V6C."""
        pvec = tpm.PVEC()
        # The following also tests getting an item.
        for i in range(tpm.N_TPM_STATES):
            self.checkpvec(pvec, i, dict(x=0.0, y=0.0, z=0.0,
                                      xdot=0.0, ydot=0.0, zdot=0.0))

    def testGetSet(self):
        """PVEC[X] = V6C => assign a V6C to a position in PVEC."""
        pvec = tpm.PVEC()
        t = dict(x=100.0, y=234.156, z=346.5,
                 xdot=-12.3, ydot=0.2, zdot=-9.4)
        pvec[tpm.TPM_S06] = tpm.V6C(**t)
        self.checkpvec(pvec, tpm.TPM_S06, t)

        self.assertRaises(IndexError, lambda x: x[34], pvec)
        self.assertRaises(IndexError, lambda x: x[-4], pvec)

        def f(pvec):
            pvec[tpm.TPM_S03] = tpm.V6S()
        self.assertRaises(TypeError, f, pvec)


class TestTpmState(unittest.TestCase):
    """Test the tpm_state function."""
    def testtpmstate(self):
        """tpm_state(x) => name of state."""
        self.assertEqual(tpm.tpm_state(1).strip(), "Helio. mean FK4")
        self.assertEqual(tpm.tpm_state(tpm.TPM_S20).strip(),
                         "Topo. obs. HA/Dec")

        
class TestTPM(unittest.TestCase):
    """Test the tpm function."""
    def testTPM(self):
        """tpm.tpm() => coordinate conversion."""
        # M100 FK5 J2000 from SIMBAD.
        # See pytpm/tests/c_tests/test_conversion.c.
        results = [
            dict(ra_dd=-175.00, ra_mm=43.0, ra_ss=43.4850,
                 de_dd=15.00, de_mm=49.00, de_ss=20.5700),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=42.3616,
                 de_dd=15.00, de_mm=49.00, de_ss=20.4480),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=43.4850,
                 de_dd=15.00, de_mm=49.00, de_ss=20.5700),
            dict(ra_dd=178.00, ra_mm=46.00, ra_ss=57.2326,
                 de_dd=16.00, de_mm=45.00, de_ss=34.9209),
            dict(ra_dd=-89.00, ra_mm=8.00, ra_ss=10.1024,
                 de_dd=76.00, de_mm=53.00, de_ss=55.9283),
            dict(ra_dd=-175.00, ra_mm=5.00, ra_ss=44.0262,
                 de_dd=16.00, de_mm=5.00, de_ss=58.0246 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=43.4850,
                 de_dd=15.00, de_mm=49.00, de_ss=20.5700 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=43.4852,
                 de_dd=15.00, de_mm=49.00, de_ss=20.5699 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=43.4819,
                 de_dd=15.00, de_mm=49.00, de_ss=20.5712 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=44.9349,
                 de_dd=15.00, de_mm=49.00, de_ss=13.4744 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=44.9350,
                 de_dd=15.00, de_mm=49.00, de_ss=13.4743 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=30.6891,
                 de_dd=15.00, de_mm=49.00, de_ss=19.5611 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=43.4852,
                 de_dd=15.00, de_mm=49.00, de_ss=20.5699 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=43.4819,
                 de_dd=15.00, de_mm=49.00, de_ss=20.5712 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=45.2053,
                 de_dd=15.00, de_mm=49.00, de_ss=13.4529 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=45.2054,
                 de_dd=15.00, de_mm=49.00, de_ss=13.4528 ),
            dict(ra_dd=-175.00, ra_mm=43.00, ra_ss=30.9595,
                 de_dd=15.00, de_mm=49.00, de_ss=19.5396 ),
            dict(ra_dd=-17.00, ra_mm=8.00, ra_ss=52.8721,
                 de_dd=15.00, de_mm=49.00, de_ss=19.5396 ),
            dict(ra_dd=132.00, ra_mm=32.00, ra_ss=57.5676,
                 de_dd=67.00, de_mm=45.00, de_ss=9.6836 ),
            dict(ra_dd=132.00, ra_mm=32.00, ra_ss=57.5676,
                 de_dd=67.00, de_mm=45.00, de_ss=34.3714 ),
            dict(ra_dd=-17.00, ra_mm=9.00, ra_ss=9.5430,
                 de_dd=15.00, de_mm=49.00, de_ss=38.3077 ),
            dict(ra_dd=-17.00, ra_mm=14.00, ra_ss=6.8699,
                 de_dd=-15.00, de_mm=10.00, de_ss=13.0062 )
            ]
        
        ra = tpm.h2r(12+22/60.0+54.899/3600.0)
        de = tpm.d2r(15+49/60.0+20.57/3600.0)
        ep = tpm.J2000
        eq = tpm.J2000
        s1 = tpm.TPM_S06
        s2 = tpm.TPM_S00
        tstate = tpm.TSTATE()
        pvec = tpm.PVEC()
         
        for i in range(tpm.N_TPM_STATES):
            tpm.tpm_data(tstate, tpm.TPM_INIT)
            tstate.utc = tpm.J2000
            tstate.lon = tpm.d2r(-111.598333)
            tstate.lat = tpm.d2r(31.956389)
            tstate.alt = 2093.093
            tstate.delta_ut = tpm.delta_UT(tstate.utc)
            tpm.tpm_data(tstate, tpm.TPM_ALL)
         
            v6 = tpm.V6S()
            v6.r = 1e9
            v6.alpha = ra
            v6.delta = de
            
            pvec[s1] = v6.s2c()
            s2 = i
            tpm.tpm(pvec, s1, s2, ep, eq, tstate)
            v6 = pvec[s2].c2s()
         
            ra1 = v6.alpha
            de1 = v6.delta

            ra_dms = tpm.DMS(r=ra1)
            de_dms = tpm.DMS(r=de1)
            ra_dms.normalize()
            de_dms.normalize()
            self.assertAlmostEqual(ra_dms.dd, results[i]['ra_dd'], 4)
            self.assertAlmostEqual(ra_dms.mm, results[i]['ra_mm'], 4)
            self.assertAlmostEqual(ra_dms.ss, results[i]['ra_ss'], 4)
            self.assertAlmostEqual(de_dms.dd, results[i]['de_dd'], 4)
            self.assertAlmostEqual(de_dms.mm, results[i]['de_mm'], 4)
            self.assertAlmostEqual(de_dms.ss, results[i]['de_ss'], 4)

            
class TestCatV6(unittest.TestCase):
    """Test cat2v6 and v62cat."""
    def testcat2v6(self):
        """cat2v6 => catalog to Cartesian."""
        # See pytpm/tests/c_tests/cat2v6_v62cat_test.c.
        # Barnard's star from Hipparcos catalog. 
        # ICRS Epoch J1991.25
        import math
        alpha = tpm.d2r(269.45402305)
        delta = tpm.d2r(4.66828815)
        px = 549.01 / 1000.0 # To Arc seconds
        rv = 0.0
        # pmra * cos(de) into pmra
        pma = (-797.84 / 1000.0 ) / math.cos(delta) 
        pma *= 100.0 # To Arcseconds per century.
        pmd = (10326.93 / 1000.0) 
        pmd *= 100.0 # To Arcseconds per century.
        C = tpm.CJ

        v6 = tpm.cat2v6(alpha, delta, pma, pmd, px, rv, C)

        self.assertAlmostEqual(v6.x, -3568.1807935995)
        self.assertAlmostEqual(v6.y, -374439.8219691383)
        self.assertAlmostEqual(v6.z, 30577.3105202634)
        self.assertAlmostEqual(v6.xdot, -0.0039386179)
        self.assertAlmostEqual(v6.ydot, 0.0042290848)
        self.assertAlmostEqual(v6.zdot, 0.0513283878)

    def testv62cat(self):
        """v62cat => Cartesian to catalog; testing cat2v6 <-> v62cat."""
                # See pytpm/tests/c_tests/cat2v6_v62cat_test.c.
        # Barnard's star from Hipparcos catalog. 
        # ICRS Epoch J1991.25
        import math
        alpha = tpm.d2r(269.45402305)
        delta = tpm.d2r(4.66828815)
        px = 549.01 / 1000.0 # To Arc seconds
        rv = 0.0
        # pmra * cos(de) into pmra
        pma = (-797.84 / 1000.0 ) / math.cos(delta) 
        pma *= 100.0 # To Arcseconds per century.
        pmd = (10326.93 / 1000.0) 
        pmd *= 100.0 # To Arcseconds per century.
        C = tpm.CJ

        v6 = tpm.cat2v6(alpha, delta, pma, pmd, px, rv, C)
        
        p = tpm.v62cat(v6, C)

        self.assertAlmostEqual(tpm.r2r(p['alpha']), alpha)
        self.assertAlmostEqual(p['delta'], delta)
        self.assertAlmostEqual(p['pma'], pma)
        self.assertAlmostEqual(p['pmd'], pmd)
        self.assertAlmostEqual(p['px'], px)
        self.assertAlmostEqual(p['rv'], rv)

        
class TestProperMotion(unittest.TestCase):
    """Test function proper_motion."""
    def testpm(self):
        """Proper motion => apply PM to position."""
        import math
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
        
        v6 = tpm.proper_motion(v6, tpm.J2000, tpm.jyear2jd(1991.25))
        v6 = v6.c2s()
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

        
class TestAberrate(unittest.TestCase):
    """Test aberrate function."""
    def testaberrate(self):
        """tpm.aberrate => aberrate function."""
        v61 = tpm.V6C(x=1.0,y=2.0,z=3.0)
        v62 = tpm.V6C(xdot=-0.5,ydot=-0.6,zdot=-0.00345)

        v6 = tpm.aberrate(v61, v62, 1)
        self.assertAlmostEqual(v6.x, 0.989194995, 8)
        self.assertAlmostEqual(v6.y, 1.987033994, 8)
        self.assertAlmostEqual(v6.z, 2.999925445, 8)
        self.assertAlmostEqual(v6.xdot, 0.0)
        self.assertAlmostEqual(v6.ydot, 0.0)
        self.assertAlmostEqual(v6.zdot, 0.0)

        v6 = tpm.aberrate(v61, v62, -1)
        self.assertAlmostEqual(v6.x, 1.010805005, 8)
        self.assertAlmostEqual(v6.y, 2.012966006, 8)
        self.assertAlmostEqual(v6.z, 3.000074555, 8)
        self.assertAlmostEqual(v6.xdot, 0.0)
        self.assertAlmostEqual(v6.ydot, 0.0)
        self.assertAlmostEqual(v6.zdot, 0.0)


class TestAzel2hadec(unittest.TestCase):
    """Test the azel2hadec function."""
    az = [0,90,133.30805555555557]
    el = [90, -45.0, 59.086111111111116]
    lat = 43.07833
    # From pytpm/tests/c_tests/azel2hadec_test.c
    ha_c = [0.000000000, 233.854836313, 336.682858247]
    dec_c = [43.078330000, 331.121606194, 19.182450965]
    def testazel2hadec(self):
        """tpm.azel2hadec => (AZ,EL) to (HA,DEC)"""
        v6 = tpm.V6S(r=1e9)
        for i,j,k,l in zip(self.az,self.el,self.ha_c,self.dec_c):
            v6.alpha = tpm.d2r(i)
            v6.delta = tpm.d2r(j)
            v61 = tpm.azel2hadec(v6.s2c(), tpm.d2r(self.lat))
            v6 = v61.c2s()
            self.assertAlmostEqual(tpm.r2d(tpm.r2r(v6.alpha)), k, 8)
            self.assertAlmostEqual(tpm.r2d(tpm.r2r(v6.delta)), l, 8)
            

class TestAzel2hadec(unittest.TestCase):
    """Test the hadec2azel function."""
    az = [0,90,133.30805555555557]
    el = [90, -45.0, 59.086111111111116]
    lat = 43.07833
    # From pytpm/tests/c_tests/azel2hadec_test.c
    ha_c = [0.000000000, 233.854836313, 336.682858247]
    dec_c = [43.078330000, 331.121606194, 19.182450965]
    def testHadec2azel(self):
        """tpm.hadec2azel => (HA,DEC) to (AZ,EL)"""
        v6 = tpm.V6S(r=1e9)
        for i,j,k,l in zip(self.az,self.el,self.ha_c,self.dec_c):
            j = tpm.r2d(tpm.r2r(tpm.d2r(j)))
            v6.alpha = tpm.d2r(k)
            v6.delta = tpm.d2r(l)
            v61 = tpm.hadec2azel(v6.s2c(), tpm.d2r(self.lat))
            v6 = v61.c2s()
            self.assertAlmostEqual(tpm.r2d(tpm.r2r(v6.alpha)),
                                   i, 8)
            self.assertAlmostEqual(tpm.r2d(tpm.r2r(v6.delta)), j, 8)


class TestEvp(unittest.TestCase):
    """Test evp function."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.x, v62.x, 8)
        self.assertAlmostEqual(v61.y, v62.y, 8)
        self.assertAlmostEqual(v61.z, v62.z, 8)
        self.assertAlmostEqual(v61.xdot, v62.xdot, 8) 
        self.assertAlmostEqual(v61.ydot, v62.ydot, 8) 
        self.assertAlmostEqual(v61.zdot, v62.zdot, 8) 

    def testEvp(self):
        """tpm.evp => Barycentric and Heliocentric V6C."""
        # See pytpm/tests/c_tests/evp_test.c
        tdt = [tpm.J2000, tpm.J1984]
        v6b_c = [tpm.V6C(x=-0.184273673, y=0.884790492, z=0.383823230,
                       xdot=-0.017202342, ydot=-0.002904995, zdot=-0.001259484),
                 tpm.V6C(x=-0.167332100, y=0.896946944, z=0.388718633,
                        xdot=-0.017240508, ydot=-0.002790623, zdot=-0.001209123)]
        v6h_c = [tpm.V6C(x=-0.177134378, y=0.887424942, z=0.384742891,
                         xdot=-0.017207714, ydot=-0.002898199, zdot=-0.001256438),
                 tpm.V6C(x=-0.170373080, y=0.888493845, z=0.385246878,
                         xdot=-0.017232243, ydot=-0.002792198, zdot=-0.001210002)]
        for i,t in enumerate(tdt):
            v6b, v6h = tpm.evp(tpm.tdt2tdb(t))
            self.verify(v6b, v6b_c[i])
            self.verify(v6h, v6h_c[i])

            
class TestEcl2equ(unittest.TestCase):
    """Test ecl2equ function."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.x, v62.x, 8)
        self.assertAlmostEqual(v61.y, v62.y, 8)
        self.assertAlmostEqual(v61.z, v62.z, 8)
        self.assertAlmostEqual(v61.xdot, v62.xdot, 8) 
        self.assertAlmostEqual(v61.ydot, v62.ydot, 8) 
        self.assertAlmostEqual(v61.zdot, v62.zdot, 8) 

    def testEcl2equ(self):
        """tpm.ecl2equ => Ecliptic to FK5 equatorial."""
        v6 = tpm.V6S(r=1.0,alpha=tpm.M_PI/4.0,delta=tpm.M_PI/4.0)
        v6 = v6.s2c()
        v6.xdot = -0.034
        v6.ydot = -0.12
        v6.zdot = -0.9

        v6 = tpm.ecl2equ(v6, tpm.d2r(23.7))

        self.verify(v6, tpm.V6C(x=0.5, y=0.173611298, z=0.848445117,
                                xdot=-0.034000000, ydot=0.251873488,
                                zdot=-0.872330067))

        
class TestEqu2ecl(unittest.TestCase):
    """Test equ2ecl function."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.x, v62.x, 5)
        self.assertAlmostEqual(v61.y, v62.y, 5)
        self.assertAlmostEqual(v61.z, v62.z, 5)
        self.assertAlmostEqual(v61.xdot, v62.xdot, 5) 
        self.assertAlmostEqual(v61.ydot, v62.ydot, 5) 
        self.assertAlmostEqual(v61.zdot, v62.zdot, 5) 

    def testEcl2equ(self):
        """tpm.equ2ecl => FK5 Equatorial to Ecliptic."""
        v6 = tpm.V6C(x=0.5, y=0.173611298, z=0.848445117,
                xdot=-0.034000000, ydot=0.251873488,
                zdot=-0.872330067)
        
        v6 = tpm.equ2ecl(v6, tpm.d2r(23.7))

        self.verify(v6, tpm.V6C(x=0.5, y=0.499999997, z=0.707106774,
                                 xdot=-0.0340, ydot=-0.120, zdot=-0.9))

        
class TestEllab(unittest.TestCase):
    """Test ellab function."""
    def testEllab(self):
        """tpm.ellab => apply elliptic aberration."""
        # pytpm/tests/c_tests/ellab_test.c
        v6 = tpm.V6S(r=1e9, alpha=tpm.h2r(20), delta=tpm.d2r(40.0))
        v6 = v6.s2c()
        v6 = tpm.ellab(tpm.J2000, v6, -1)
        v6 = v6.c2s()
        self.assertAlmostEqual(v6.r, 1e9,5)
        self.assertAlmostEqual(tpm.r2h(tpm.r2r(v6.alpha)), 20.000007838,8)
        self.assertAlmostEqual(tpm.r2d(tpm.r2r(v6.delta)), 39.999987574,8)
    

class TestEqu2gal(unittest.TestCase):
    """Test equ2gal function."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 2)
        self.assertAlmostEqual(tpm.r2r(v61.alpha), tpm.r2r(v62.alpha), 2)
        self.assertAlmostEqual(tpm.r2r(v61.delta), tpm.r2r(v62.delta), 2)
    
    def testEqu2gal(self):
        """tpm.equ2gal => convert FK4 equatorial to Galactic."""
        v6 = tpm.V6S(r=1e9,alpha=tpm.d2r(192.25), delta=tpm.d2r(27.4))
        v6 = v6.s2c()
        v6 = tpm.equ2gal(v6)
        v6 = v6.c2s()
        self.verify(v6, tpm.V6S(r=1e9, alpha=tpm.d2r(120.866),
                                delta=tpm.d2r(90.0)))

        
class TestGal2equ(unittest.TestCase):
    """Test gal2equ function."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 2)
        self.assertAlmostEqual(tpm.r2r(v61.alpha), v62.alpha, 2)
        self.assertAlmostEqual(tpm.r2r(v61.delta), v62.delta, 2)
    
    def testEqu2gal(self):
        """tpm.equ2gal => convert Galactic to FK4 equatorial."""
        v6 = tpm.V6S(r=1e9,alpha=tpm.d2r(120.0), delta=tpm.d2r(90.0))
        v6 = v6.s2c()
        v6 = tpm.gal2equ(v6)
        self.verify(v6.c2s(), tpm.V6S(r=1e9, alpha=tpm.d2r(192.25),
                                      delta=tpm.d2r(27.4))) 
                               

class TestEterms(unittest.TestCase):
    """Test eterms."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.x, v62.x, 9)
        self.assertAlmostEqual(v61.y, v62.y, 9)
        self.assertAlmostEqual(v61.z, v62.z, 9)
        self.assertAlmostEqual(v61.xdot, v62.xdot, 9) 
        self.assertAlmostEqual(v61.ydot, v62.ydot, 9) 
        self.assertAlmostEqual(v61.zdot, v62.zdot, 9) 

    def testEterms(self):
        """tpm.eterms => return e-terms of aberration."""
        ep = [tpm.J2000, tpm.J1984]
        v6c = [tpm.V6C(x=-0.0000016181, y=-0.0000003411,
                       z=-0.0000001479),
               tpm.V6C(x=-0.0000016206, y=-0.0000003341,
                       z=-0.0000001449)]
        for i,e in enumerate(ep):
            v6 = tpm.eterms(e)
            self.verify(v6, v6c[i])
            
            
class TestFk425(unittest.TestCase):
    """Test fk425."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 5)
        self.assertAlmostEqual(v61.alpha, v62.alpha, 5)
        self.assertAlmostEqual(v61.delta, v62.delta, 5)

    def testFk425(self):
        """tpm.fk425 => B1950 FK4 to J2000 FK5."""
        v6 = tpm.V6S(r=1e9, alpha=tpm.d2r(23.15678), delta=
                     tpm.d2r(54.3892))
        v6 = v6.s2c()
        v6 = tpm.fk425(v6)
        v6 = v6.c2s()
        # Why does R change?
        self.verify(v6, tpm.V6S(r=1000000000.0008671284,
                                alpha=tpm.d2r(23.9534903408),
                                delta=tpm.d2r(54.6442824316)))

        
class TestFk524(unittest.TestCase):
    """Test fk524."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 1)
        self.assertAlmostEqual(v61.alpha, v62.alpha, 5)
        self.assertAlmostEqual(v61.delta, v62.delta, 5)

    def testFk524(self):
        """tpm.fk524 => J2000 FK5 to B1950 FK4."""
        v6 = tpm.V6S(r=1e9,
                                alpha=tpm.d2r(23.9534903408),
                                delta=tpm.d2r(54.6442824316))
        v6 = v6.s2c()
        v6 = tpm.fk524(v6)
        v6 = v6.c2s()
        # Why does R change?
        self.verify(v6, tpm.V6S(r=1e9, alpha=tpm.d2r(23.15678), delta=
                     tpm.d2r(54.3892)))


class TestGeod2geoc(unittest.TestCase):
    """Test geod2geoc."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.x, v62.x, 5)
        self.assertAlmostEqual(v61.y, v62.y, 5)
        self.assertAlmostEqual(v61.z, v62.z, 5)
        self.assertAlmostEqual(v61.xdot, v62.xdot, 5) 
        self.assertAlmostEqual(v61.ydot, v62.ydot, 5) 
        self.assertAlmostEqual(v61.zdot, v62.zdot, 5) 

    def testGeod2geoc(self):
        """tpm.geod2geoc => Geodetic to geocentric."""
        v6 = tpm.geod2geoc(tpm.d2r(30.567), tpm.d2r(46.713), 1500.0)
        self.verify(v6,tpm.V6C(x=3773051.892626300,y=2228444.491846553,
                              z=4621039.023174386,xdot=-162.500738326,
                              ydot=275.135288555,zdot=0.0))

        
class TestLdeflect(unittest.TestCase):
    """Test ldeflect."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 5)
        self.assertAlmostEqual(v61.alpha, v62.alpha, 5)
        self.assertAlmostEqual(v61.delta, v62.delta, 5)
        self.assertAlmostEqual(v61.rdot, v62.rdot, 5)
        self.assertAlmostEqual(v61.alphadot, v62.alphadot, 5)
        self.assertAlmostEqual(v61.deltadot, v62.deltadot, 5)
                
    def testLdelfect(self):
        """tpm.ldeflect => apply GR light deflection."""
        v6h = tpm.evp(tpm.J2000)[1]
        v6 = tpm.V6S(r=1, alpha=tpm.d2r(34.56), delta=tpm.d2r(46.19))
        v6 = v6.s2c()

        v6 = tpm.ldeflect(v6, v6h, 1)

        self.verify(v6.c2s(), tpm.V6S(r=1.0, alpha=0.6031857970,
                                delta=0.8061675815))


class TestPrecess(unittest.TestCase):
    """Test precess."""
    def verify(self, v61, v62):
        self.assertAlmostEqual(v61.r, v62.r, 1)
        self.assertAlmostEqual(v61.alpha, v62.alpha, 5)
        self.assertAlmostEqual(v61.delta, v62.delta, 5)
        self.assertAlmostEqual(v61.rdot, v62.rdot, 5)
        self.assertAlmostEqual(v61.alphadot, v62.alphadot, 5)
        self.assertAlmostEqual(v61.deltadot, v62.deltadot, 5)

    def testPrecess(self):
        """tpm.precess => precess V6 in inertial frame."""
        v6 = tpm.V6S(r=1e9, alpha=tpm.d2r(34.1592),
                     delta=tpm.d2r(12.9638), rdot=-0.123,
                     alphadot=0.382, deltadot=1.0)

        v6 = v6.s2c()
        v6 = tpm.precess(tpm.J2000, tpm.J1984, v6, tpm.PRECESS_FK5)
        v6 = v6.c2s()

        self.verify(v6,tpm.V6S(r=1e9, alpha=0.5924126644,
                               delta=0.2249726697,rdot=-0.1229999560,
                               alphadot=0.3809705204,
                               deltadot=1.0003321415))

        
class TestEEDot(unittest.TestCase):
    """Test eccentricity and eccentricity_dot."""
    ep = [tpm.J2000, tpm.J1984]
    e_c = [0.0167091134, 0.0167158397]
    edot_c = [-0.0000420560, -0.0000420157]
    def testEccentricity(self):
        """tpm.eccentricity => Earth's eccentricity."""
        for i,j in enumerate(self.ep):
            self.assertAlmostEqual(self.e_c[i], tpm.eccentricity(j), 8)
            self.assertAlmostEqual(self.edot_c[i],
                                   tpm.eccentricity_dot(j), 8)
            

class TestOODot(unittest.TestCase):
    """Test obliquity and obliquity_dot."""
    ep = [tpm.J2000, tpm.J1984]
    e_c = [0.4090928042, 0.4091291217]
    edot_c = [-0.0002269655, -0.0002269633]
    def testObliquity(self):
        """tpm.obliquity => Earth's obliquity."""
        for i,j in enumerate(self.ep):
            self.assertAlmostEqual(self.e_c[i], tpm.obliquity(j), 8)
            self.assertAlmostEqual(self.edot_c[i],
                                   tpm.obliquity_dot(j), 8)
            

class TestRefract(unittest.TestCase):
    """Test refco and refract."""
    def testRefract(self):
        """tpm.refco, tom.refract => refraction."""
        refa, refb = tpm.refco(tpm.M_PI/3.0)
        z = tpm.refract(tpm.M_PI/6.0, refa, refb, 1)
        self.assertAlmostEqual(refa, 0.0002927535)
        self.assertAlmostEqual(refb, -0.0000003077)
        self.assertAlmostEqual(z, -0.000168896)


class TestSolarPerigee(unittest.TestCase):
    """Test solar perigee."""
    def testSolarPerigee(self):
        """tpm.solar_perigee, tpm.solar_perigee_dot => orbit."""
        sp = tpm.solar_perigee(tpm.J2000)
        spd = tpm.solar_perigee_dot(tpm.J2000)

        self.assertAlmostEqual(sp, 4.9382428903, 8)
        self.assertAlmostEqual(spd, 0.0300213018, 8)
    
    
class TestPrecessionAngles(unittest.TestCase):
    """Test theta, zee and zeta."""
    def testPrecessionAngles(self):
        """tpm.theta, thetadot, zee, zeedot, theta and thetadot."""
        self.assertAlmostEqual(tpm.theta(tpm.J1984, tpm.J2000,
                                         tpm.PRECESS_FK5),
                               0.0015549329, 8)

        self.assertAlmostEqual(tpm.thetadot(tpm.J1984, tpm.J2000,
                                         tpm.PRECESS_FK5),
                               0.0000002660, 9)

        self.assertAlmostEqual(tpm.zee(tpm.J1984, tpm.J2000,
                                         tpm.PRECESS_FK5),
                               0.0017890537, 8)

        self.assertAlmostEqual(tpm.zeedot(tpm.J1984, tpm.J2000,
                                         tpm.PRECESS_FK5),
                               0.0000003061, 9)
        
        self.assertAlmostEqual(tpm.zeta(tpm.J1984, tpm.J2000,
                                         tpm.PRECESS_FK5),
                               0.0017889553, 8)

        self.assertAlmostEqual(tpm.zetadot(tpm.J1984, tpm.J2000,
                                         tpm.PRECESS_FK5),
                               0.0000003061, 9)


class TestNutations(unittest.TestCase):
    """Test nutations."""
    def testNutations(self):
        """tpm.nutations => nutation in longitude and obliquity."""
        delta_phi, delta_eps = tpm.nutations(tpm.J2000)
        self.assertAlmostEqual(delta_phi, -0.0000675025, 9)
        self.assertAlmostEqual(delta_eps, -0.0000279922, 9)
