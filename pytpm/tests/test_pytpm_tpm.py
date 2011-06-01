# -*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_vec.pxi file.
import unittest
from pytpm import tpm

   
class CheckTSTATE(object):
    """Perform comparison of TSTATE attributes with provided vals."""
    def checkm3(self, m3, t):
        """Compare M3 with values in t."""
        self.assertAlmostEqual(m3.xx, t['XX'], t.get('XXp', 7))
        self.assertAlmostEqual(m3.xy, t['XY'], t.get('XYp', 7))
        self.assertAlmostEqual(m3.xz, t['XZ'], t.get('XZp', 7))
        self.assertAlmostEqual(m3.yx, t['YX'], t.get('YXp', 7))
        self.assertAlmostEqual(m3.yy, t['YY'], t.get('YYp', 7))
        self.assertAlmostEqual(m3.yz, t['YZ'], t.get('YZp', 7))
        self.assertAlmostEqual(m3.zx, t['ZX'], t.get('ZXp', 7))
        self.assertAlmostEqual(m3.zy, t['ZY'], t.get('ZYp', 7))
        self.assertAlmostEqual(m3.zz, t['ZZ'], t.get('ZZp', 7))

    def checkv6(self, v6c, t):
        """Compare V6 fields with the values in t."""
        self.assertAlmostEqual(v6c.x, t['x'] , t.get('xp', 7))
        self.assertAlmostEqual(v6c.y, t['y'] , t.get('yp', 7))
        self.assertAlmostEqual(v6c.z, t['z'] , t.get('zp', 7))
        self.assertAlmostEqual(v6c.xdot, t['xdot'], t.get('xdotp', 7))
        self.assertAlmostEqual(v6c.ydot, t['ydot'], t.get('ydotp', 7))
        self.assertAlmostEqual(v6c.zdot, t['zdot'], t.get('zdotp', 7))

    def check_ind(self, tstate, t):
        if 'utc' in t:
            self.assertAlmostEqual(tstate.utc, t['utc'],
                                   t.get('utcp',7))
        if 'delta_at' in t:
            self.assertAlmostEqual(tstate.delta_at, t['delta_at'],
                                   t.get('delta_atp', 7))
        if 'delta_ut' in t:
            self.assertAlmostEqual(tstate.delta_ut, t['delta_ut'],
                                   t.get('delta_utp', 7))
        if 'lon' in t:
            self.assertAlmostEqual(tstate.lon, t['lon'],
                                   t.get('lonp', 7))
        if 'lat' in t:
            self.assertAlmostEqual(tstate.lat, t['lat'],
                                   t.get('latp', 7))
        if 'alt' in t:
            self.assertAlmostEqual(tstate.alt, t['alt'],
                                   t.get('altp', 7))
        if 'xpole' in t:
            self.assertAlmostEqual(tstate.xpole, t['xpole'],
                                   t.get('xpolep', 7))
        if 'ypole' in t:
            self.assertAlmostEqual(tstate.ypole, t['ypole'],
                                   t.get('ypolep', 7))
        if 'P' in t:
            self.assertAlmostEqual(tstate.P, t['P'],
                                   t.get('Pp', 7))
        if 'H' in t:
            self.assertAlmostEqual(tstate.H, t['H'],
                                   t.get('Hp', 7))
        if 'T' in t:
            self.assertAlmostEqual(tstate.T, t['T'],
                                   t.get('Tp', 7))
        if 'wavelength' in t:
            self.assertAlmostEqual(tstate.wavelength, t['wavelength'],
                                   t.get('wavelengthp', 7))
            
    def check_dep_scalars(self, tstate, t):
        if 'tai' in  t:
            self.assertAlmostEqual(tstate.tai, t['tai'],
                                   t.get('taip', 7))
        if "tdt" in t:
            self.assertAlmostEqual(tstate.tdt, t['tdt'],
                                   t.get('tdtp', 7))
        if "tdb" in t:
            self.assertAlmostEqual(tstate.tdb, t['tdb'],
                                   t.get('tdbp', 7))
        if "obliquity" in t:
            self.assertAlmostEqual(tstate.obliquity, t['obliquity'],
                                   t.get('obliquityp', 7))
        if "nut_lon" in t:
            self.assertAlmostEqual(tstate.nut_lon, t['nut_lon'],
                                   t.get("nut_lonp", 7))
        if "nut_obl" in t:
            self.assertAlmostEqual(tstate.nut_obl, t['nut_obl'],
                                   t.get('nut_oblp', 7))
        if "ut1" in t:
            self.assertAlmostEqual(tstate.ut1, t['ut1'],
                                   t.get('ut1p', 7))
        if "gmst" in t:
            self.assertAlmostEqual(tstate.gmst, t['gmst'],
                                   t.get('gmstp', 7))
        if "gast" in t:
            self.assertAlmostEqual(tstate.gast, t['gast'],
                                   t.get("gastp", 7))
        if "last" in t:
            self.assertAlmostEqual(tstate.last, t['last'],
                                   t.get("lastp", 7))
        if "refa" in t:
            self.assertAlmostEqual(tstate.refa, t['refa'],
                                   t.get('refap', 12))
        if "refb" in t:
            self.assertAlmostEqual(tstate.refb, t['refb'],
                                   t.get("refbp", 12))


class TestTSTATE(unittest.TestCase, CheckTSTATE):
    """Tests for tpm.TSTATE class that wraps _tpm_tpm.TPM_TSTATE."""
    def testCreate(self):
        """TSTATE.init => creates TSTATE with default values."""
        tstate = tpm.TSTATE()
        # Cant't check for utc and delta_at.
        t = dict(delta_ut=0.0, lon=0.0, lat=0.0, alt=0.0, xpole=0.0,
                 ypole=0.0, P=1013.25, T=273.15, wavelength=0.550)
        self.check_ind(tstate, t)
        
    def testSetGetInitValues(self):
        """TSTATE.init(**vals) => Set values during init."""
        # See pytpm/tests/c_tests/tstate_init_test.c.
        t = dict(utc=0.0, delta_at=0.0, delta_ut=0.0, lon=36.756,
                 lat=-23.4, alt=234.67, P=2026.5, T=300.0,
                 H=0.3, wavelength=0.600)
        tstate = tpm.TSTATE(**t)
        self.check_ind(tstate, t)
        
        t = dict(tai=0.0, tdt=0.0, tdb=0.0, obliquity=0.0,
                 nut_lon=0.0, nut_obl=0.0, ut1=0.0, gmst=0.0,
                 gast=0.0, last=0.0, refa=0.000282646376, refap=12,
                 refb=-0.000000324825, refbp=12)
        self.check_dep_scalars(tstate, t)

        t = dict(XX=1.0, XY=0.0, XZ=0.0,
                 YX=0.0, YY=1.0, YZ=0.0,
                 ZX=0.0, ZY=0.0, ZZ=1.0)
        self.checkm3(tstate.nm, t)
        
        pm = tstate.pm
        self.checkm3(pm.pp, t)
        self.checkm3(pm.vv, t)
        t['XX'] = 0.0
        t['YY'] = 0.0
        t['ZZ'] = 0.0
        self.checkm3(pm.pv, t)
        self.checkm3(pm.vp, t)

        t = dict(x=0.0, y=0.0, z=0.0, xdot=0.0, ydot=0.0, zdot=0.0)
        self.checkv6(tstate.eb, t)

    def testReadOnlyMemberAccess(self):
        """TSTATE.x => can't change read-only members of TSTATE."""
        tstate = tpm.TSTATE()
        def f(tstate, x, v):
            setattr(tstate, x, v)
        for i in ['tai', 'gmst', 'obliquity', 'refa', 'eh']:
            self.assertRaises(AttributeError,f, tstate, i, 0.0)
        
        
