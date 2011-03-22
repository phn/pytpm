# -*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_vec.pxi file.
import unittest
from pytpm import tpm

class Checker(object):
    def setup(self, v3, t):
        """Initialize a V3 object."""
        if v3.ctype == tpm.CARTESIAN and v3.vtype == tpm.POS:
            v3.x = t['x']
            v3.y = t['y']
            v3.z = t['z']
        if v3.ctype == tpm.CARTESIAN and v3.vtype == tpm.VEL:
            v3.xdot = t['xdot']
            v3.ydot = t['ydot']
            v3.zdot = t['zdot']
        if v3.ctype == tpm.SPHERICAL and v3.vtype == tpm.POS:
            v3.r = t['r']
            v3.alpha = t['alpha']
            v3.delta = t['delta']
        if v3.ctype == tpm.SPHERICAL and v3.vtype == tpm.VEL:
            v3.rdot = t['rdot']
            v3.alphadot = t['alphadot']
            v3.deltadot = t['deltadot']

        return v3
        
    def cartesian_postest(self, v3, t_norm):
        """Check that Cartesian v3 POS fields have value given in dict."""
        self.assertAlmostEqual(v3.ctype, t_norm['ctype'])
        self.assertAlmostEqual(v3.vtype, t_norm['vtype'])
        self.assertAlmostEqual(v3.x, t_norm['x'])
        self.assertAlmostEqual(v3.y, t_norm['y'])
        self.assertAlmostEqual(v3.z, t_norm['z'])

    def cartesian_veltest(self, v3, t_norm):
        """Check that Cartesian v3 VEL fields have value given in dict."""
        self.assertAlmostEqual(v3.ctype, t_norm['ctype'])
        self.assertAlmostEqual(v3.vtype, t_norm['vtype'])
        self.assertAlmostEqual(v3.xdot, t_norm['xdot'])
        self.assertAlmostEqual(v3.ydot, t_norm['ydot'])
        self.assertAlmostEqual(v3.zdot, t_norm['zdot'])

    def spherical_postest(self, v3, t_norm):
        """Check that spherical v3 POS fields have value given in dict."""
        self.assertAlmostEqual(v3.ctype, t_norm['ctype'])
        self.assertAlmostEqual(v3.vtype, t_norm['vtype'])
        self.assertAlmostEqual(v3.r, t_norm['r'])
        self.assertAlmostEqual(v3.alpha, t_norm['alpha'], 9)
        self.assertAlmostEqual(v3.delta, t_norm['delta'], 9)

    def spherical_veltest(self, v3, t_norm):
        """Check that spherical v3 VEL fields have value given in dict."""
        self.assertAlmostEqual(v3.ctype, t_norm['ctype'])
        self.assertAlmostEqual(v3.vtype, t_norm['vtype'])
        self.assertAlmostEqual(v3.rdot, t_norm['rdot'])
        self.assertAlmostEqual(v3.alphadot, t_norm['alphadot'])
        self.assertAlmostEqual(v3.deltadot, t_norm['deltadot'])

    def cartesian_posraise(self, v3):
        """Given Cartesian v3 POS, other attributes must raise AttributeError"""
        def get_att(s, v3):
            eval(s)
            
        self.assertRaises(AttributeError, get_att, "v3.xdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.ydot", v3)
        self.assertRaises(AttributeError, get_att, "v3.zdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.r", v3)
        self.assertRaises(AttributeError, get_att, "v3.alpha", v3)
        self.assertRaises(AttributeError, get_att, "v3.delta", v3)
        self.assertRaises(AttributeError, get_att, "v3.rdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.alphadot", v3)
        self.assertRaises(AttributeError, get_att, "v3.deltadot", v3)

    def cartesian_velraise(self, v3):
        """Given Cartesian v3 VEL, other attributes must raise AttributeError"""
        def get_att(s, v3):
            eval(s)
            
        self.assertRaises(AttributeError, get_att, "v3.x", v3)
        self.assertRaises(AttributeError, get_att, "v3.y", v3)
        self.assertRaises(AttributeError, get_att, "v3.z", v3)
        self.assertRaises(AttributeError, get_att, "v3.r", v3)
        self.assertRaises(AttributeError, get_att, "v3.alpha", v3)
        self.assertRaises(AttributeError, get_att, "v3.delta", v3)
        self.assertRaises(AttributeError, get_att, "v3.rdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.alphadot", v3)
        self.assertRaises(AttributeError, get_att, "v3.deltadot", v3)

    def spherical_posraise(self, v3):
        """Given spherical v3 POS, other attributes must raise AttributeError"""
        def get_att(s, v3):
            eval(s)

        self.assertRaises(AttributeError, get_att, "v3.x", v3)
        self.assertRaises(AttributeError, get_att, "v3.y", v3)
        self.assertRaises(AttributeError, get_att, "v3.z", v3)
        self.assertRaises(AttributeError, get_att, "v3.xdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.ydot", v3)
        self.assertRaises(AttributeError, get_att, "v3.zdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.rdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.alphadot", v3)
        self.assertRaises(AttributeError, get_att, "v3.deltadot", v3)

    def spherical_velraise(self, v3):
        """Given spherical v3 VEL, other attributes must raise AttributeError"""
        def get_att(s, v3):
            eval(s)

        self.assertRaises(AttributeError, get_att, "v3.x", v3)
        self.assertRaises(AttributeError, get_att, "v3.y", v3)
        self.assertRaises(AttributeError, get_att, "v3.z", v3)
        self.assertRaises(AttributeError, get_att, "v3.xdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.ydot", v3)
        self.assertRaises(AttributeError, get_att, "v3.zdot", v3)
        self.assertRaises(AttributeError, get_att, "v3.r", v3)
        self.assertRaises(AttributeError, get_att, "v3.alpha", v3)
        self.assertRaises(AttributeError, get_att, "v3.delta", v3)
    

class TestV3Structure(unittest.TestCase, Checker):
    """Test various features of the tpm.V3 class."""
    def testCreate(self):
        """Must be able to create an V3 object."""
        v3 = tpm.V3()
        self.assertEqual(type(v3), tpm.V3)

    def testGetDefaultFields(self):
        """Must be able to retrieve default values of V3 fields."""
        v3 = tpm.V3()
        self.assertAlmostEqual(v3.x, 0.0)
        self.assertAlmostEqual(v3.y, 0.0)
        self.assertAlmostEqual(v3.z, 0.0)

        # Default only has x, y, z; others must raise exception.
        self.cartesian_posraise(v3)

    def testSetFieldValuesAtInit(self):
        """V3 fields must be properly set using initilization values."""      
        # Appropriate attributes must be set and others must
        # result in AttributeError exception.
        t=dict(x=1.0,y=2.0,z=3.0, ctype=tpm.CARTESIAN, vtype=tpm.POS)
        v3 = tpm.V3(**t)
        self.cartesian_postest(v3, t)
        self.cartesian_posraise(v3)

        t=dict(xdot=12.0,ydot=23.0,zdot=65.0, ctype=tpm.CARTESIAN, vtype=tpm.VEL)
        v3 = tpm.V3(**t)
        self.cartesian_veltest(v3, t)
        self.cartesian_velraise(v3)

        t=dict(r=12.0,alpha=23.0,delta=65.0, ctype=tpm.SPHERICAL,
               vtype=tpm.POS)
        v3 = tpm.V3(**t)
        self.spherical_postest(v3, t)
        self.spherical_posraise(v3)

        t=dict(rdot=12.0,alphadot=23.0,deltadot=65.0, ctype=tpm.SPHERICAL,
               vtype=tpm.VEL)
        v3 = tpm.V3(**t)
        self.spherical_veltest(v3, t)
        self.spherical_velraise(v3)

    def testSetFieldValues(self):
        """Must be able to set V3 fields after creation."""
        v3 = tpm.V3()
        t = dict(x=1.0, y=-1.0, z=200.0, ctype=tpm.CARTESIAN, vtype=tpm.POS)
        v3.x = t['x']
        v3.y = t['y']
        v3.z = t['z']
        self.cartesian_postest(v3, t)

        # Must raise AttributeError for invalid property.
        def f(x):
            x.b = 0.0
        self.assertRaises(AttributeError,  f, v3)

        v3 = tpm.V3(ctype=tpm.SPHERICAL, vtype=tpm.VEL)
        t = dict(rdot=1.0, alphadot=-1.0, deltadot=200.0,
                 ctype=tpm.SPHERICAL, vtype=tpm.VEL)
        v3.rdot = t['rdot']
        v3.alphadot = t['alphadot']
        v3.deltadot = t['deltadot']
        self.spherical_veltest(v3, t)

    def testDeleteAttribute(self):
        """Must raise TypeError when deleting V3 attributes."""
        v3 = tpm.V3()
        def f(x):
            del x.x
        self.assertRaises(TypeError, f, v3)

        v3 = tpm.V3(ctype=tpm.SPHERICAL, vtype=tpm.VEL)
        def f(x):
            del x.rdot
        self.assertRaises(TypeError, f, v3)

    def testV3C2S(self):
        """Must properly convert V3 Cartesian POS into Spherical"""
        # See pytpm/tests/c_tests/v3c2s_test.c.
        v3 = tpm.V3(ctype=tpm.CARTESIAN, vtype=tpm.POS)
        t = dict(ctype = tpm.CARTESIAN, vtype=tpm.POS, x=1123.4556,
                 y=4556.1123, z=9876.1267)
        t_norm = dict(ctype=tpm.SPHERICAL, vtype=tpm.POS,
                      r=10934.26679617, alpha=1.3290371174, delta=1.1272306580)
        v3 = self.setup(v3, t)
        v3_s = v3.c2s()
        self.spherical_postest(v3_s, t_norm)

        # Must raise exception on CARTESIAN VEL to SPHERICAL convertion.
        v3 = tpm.V3(ctype=tpm.CARTESIAN, vtype=tpm.VEL)
        def f(x):
            x.c2s()
        self.assertRaises(NotImplementedError, f, v3)

        # Must return the same V3 if SPHERICAL POS.
        v3 = tpm.V3(ctype=tpm.SPHERICAL, vtype=tpm.POS)
        t = dict(ctype=tpm.SPHERICAL, vtype=tpm.POS,
                      r=10934.26679617, alpha=1.3290371174, delta=1.1272306580)
        v3 = self.setup(v3, t)
        v3_s = v3.c2s()
        self.spherical_postest(v3_s, t)

        





if __name__ == '__main__':
    unittest.main()
