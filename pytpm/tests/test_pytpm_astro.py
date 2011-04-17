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
                refa=0.000292752467, refap=12,
                refb=-0.000000308573, refbp=12
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
        print ut1
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
        
