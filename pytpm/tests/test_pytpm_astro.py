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
 
        self.checkm3(tstate.pm['PP'], dict(
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

        self.checkm3(tstate.pm['VV'],dict(
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
        self.checkm3(tstate.pm['PV'], t_m3)
        self.checkm3(tstate.pm['VP'], t_m3)  

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
        
        p = tpm.v62cat(v6, C)

        self.assertAlmostEqual(tpm.r2r(p['ra']), ra)
        self.assertAlmostEqual(p['de'], de)
        self.assertAlmostEqual(p['pmra'], pmra)
        self.assertAlmostEqual(p['pmde'], pmde)
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
        