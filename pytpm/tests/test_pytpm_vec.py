# -*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_vec.pxi file.
import unittest
from pytpm import tpm


class TestV3Structure(unittest.TestCase):
    """Test the V3 wrapper for _tpm_vec.V3"""
    def testCreate(self):
        """Must be able to create a V3 object."""
        v3 = tpm.V3()
        self.assertEqual(type(v3), tpm.V3)

        # Must raise Attribute error if any property is accessed
        self.assertRaises(AttributeError, lambda v: v.x, v3)
        self.assertRaises(AttributeError, lambda v: v.getX(), v3)
        
class TestV3CP(unittest.TestCase):
    """Test the V3CP class."""
    def testCreate(self):
        """Must be able to create a V3CP class."""
        v3cp = tpm.V3CP()
        self.assertEqual(type(v3cp), tpm.V3CP)

        # Access default init values.
        self.assertAlmostEqual(v3cp.ctype, tpm.CARTESIAN)
        self.assertAlmostEqual(v3cp.vtype, tpm.POS)
        self.assertAlmostEqual(v3cp.x, 0.0)
        self.assertAlmostEqual(v3cp.y, 0.0)
        self.assertAlmostEqual(v3cp.z, 0.0)

        # ctype and vtype are read only values.
        def f1(x):
            x.ctype = tpm.SPHERICAL
        def f2(x):
            x.vtype = tpm.VEL            
        self.assertRaises(AttributeError, f1, v3cp)
        self.assertRaises(AttributeError, f2, v3cp)
        
        
    def testSetGetInitValues(self):
        """Must be able to set V3CP fields at init and get them back."""
        t = dict(x=-12.34, y=21345.0, z=-0.00001)
        v3cp = tpm.V3CP(**t)
        self.assertAlmostEqual(v3cp.x, t['x'])
        self.assertAlmostEqual(v3cp.y, t['y'])
        self.assertAlmostEqual(v3cp.z, t['z'])

    def testV3C2S(self):
        """V3CP.c2s must return a correct V3SP object."""
        import math
        def verify(t, t_norm):
            v3cp = tpm.V3CP(**t)
            v3sp = v3cp.c2s()
            self.assertEqual(type(v3sp), tpm.V3SP)
            self.assertEqual(v3sp.ctype, tpm.SPHERICAL)
            self.assertEqual(v3sp.vtype, tpm.POS)
            self.assertAlmostEqual(v3sp.r, t_norm['r'])
            self.assertAlmostEqual(v3sp.alpha, t_norm['alpha'])
            self.assertAlmostEqual(v3sp.delta, t_norm['delta'])

        t = dict(x=1.0, y=1.0, z=1.0)
        t_norm = dict(r=math.sqrt(3.0), alpha=math.atan2(1.0,1.0),
                      delta=math.atan2(1.0,math.sqrt(2.0)))
        verify(t, t_norm)
        
        t = dict(x=1123.4556, y=4556.1123, z=9876.1267)
        t_norm = dict(r=10934.26679617, alpha=1.3290371174,
                      delta=1.1272306580)
        verify(t, t_norm)

    def testV3CSubtract(self):
        """Must be able to subtract one V3CP from another."""
        import math
        def verify(t, t_norm):
            v3cp1 = tpm.V3CP(**t)
            v3cp2 = tpm.V3CP(**t_norm)
            v3cp = v3cp2 - v3cp1
            self.assertEqual(type(v3cp), tpm.V3CP)
            self.assertEqual(v3cp.ctype, tpm.CARTESIAN)
            self.assertEqual(v3cp.vtype, tpm.POS)
            self.assertAlmostEqual(v3cp.x, t_norm['x'] - t['x'])
            self.assertAlmostEqual(v3cp.y, t_norm['y'] - t['y'])
            self.assertAlmostEqual(v3cp.z, t_norm['z'] - t['z'])

        t = dict(x=1.0, y=2.0, z=3.0)
        t_norm = dict(x=10.0, y=20.0, z=-0.234)
        verify(t, t_norm)

        t = dict(x=1.0, y=2.0, z=3.0)
        t_norm = dict(x=10.0, y=20.0, z=-0.234)
        verify(t_norm, t)

        # TypeError must be rasied if one of the values is not V3CP.
        self.assertRaises(TypeError, lambda v1: v1 - 1.0, tpm.V3CP(**t))
        

class TestV3SP(unittest.TestCase):
    """Test the V3CP class."""
    def testCreate(self):
        """Must be able to create a V3CP class."""
        v3sp = tpm.V3SP()
        self.assertEqual(type(v3sp), tpm.V3SP)

        # Access default init values.
        self.assertAlmostEqual(v3sp.ctype, tpm.SPHERICAL)
        self.assertAlmostEqual(v3sp.vtype, tpm.POS)
        self.assertAlmostEqual(v3sp.r, 0.0)
        self.assertAlmostEqual(v3sp.alpha, 0.0)
        self.assertAlmostEqual(v3sp.delta, 0.0)

        # ctype and vtype are read only values.
        def f1(x):
            x.ctype = tpm.SPHERICAL
        def f2(x):
            x.vtype = tpm.VEL            
        self.assertRaises(AttributeError, f1, v3sp)
        self.assertRaises(AttributeError, f2, v3sp)
        
        
    def testSetGetInitValues(self):
        """Must be able to set V3SP fields at init and get them back."""
        t = dict(r=2.0, alpha=-0.12, delta=2*3.14)
        v3sp = tpm.V3SP(**t)
        self.assertAlmostEqual(v3sp.r, t['r'])
        self.assertAlmostEqual(v3sp.alpha, t['alpha'])
        self.assertAlmostEqual(v3sp.delta, t['delta'])

        
    def testV3S2C(self):
        """V3SP.s2c must return a correct V3CP object."""
        import math
        def verify(t, t_norm, n=7):
            v3sp = tpm.V3SP(**t)
            v3cp = v3sp.s2c()
            self.assertEqual(type(v3cp), tpm.V3CP)
            self.assertEqual(v3cp.ctype, tpm.CARTESIAN)
            self.assertEqual(v3cp.vtype, tpm.POS)
            self.assertAlmostEqual(v3cp.x, t_norm['x'], n)
            self.assertAlmostEqual(v3cp.y, t_norm['y'], n)
            self.assertAlmostEqual(v3cp.z, t_norm['z'], n)

        t_norm = dict(x=1.0, y=1.0, z=1.0)
        t = dict(r=math.sqrt(3.0), alpha=math.atan2(1.0,1.0),
                      delta=math.atan2(1.0,math.sqrt(2.0)))
        verify(t, t_norm)
        
        t_norm = dict(x=1123.4556, y=4556.1123, z=9876.1267)
        t = dict(r=10934.26679617, alpha=1.3290371174,
                      delta=1.1272306580)
        verify(t, t_norm, n=4)

    def testV3SSubtract(self):
        """Must be able to subtract one V3SP from another."""
        import math
        def verify(t, t_norm, res):
            v3sp1 = tpm.V3SP(**t)
            v3sp2 = tpm.V3SP(**t_norm)
            v3sp = v3sp2 - v3sp1
            self.assertEqual(type(v3sp), tpm.V3SP)
            self.assertEqual(v3sp.ctype, tpm.SPHERICAL)
            self.assertEqual(v3sp.vtype, tpm.POS)
            self.assertAlmostEqual(v3sp.r, res['r'])
            self.assertAlmostEqual(v3sp.alpha, res['alpha'])
            self.assertAlmostEqual(v3sp.delta, res['delta'])

        # see pytpm/tests/c_tests/v3diff_test.c
        t = dict(r=1.0, alpha=2.0, delta=3.0)
        t_norm = dict(r=10.0, alpha=0.2, delta=-0.234)
        res = dict(r=9.86298456, alpha=0.30111131, delta=-0.25206013)
        # t_norm - t
        verify(t, t_norm, res)

        t = dict(r=-1.0, alpha=2.0, delta=3.0)
        t_norm = dict(r=1.0, alpha=-2.0, delta=-0.234)
        res = dict(r=1.78703389, alpha=-1.56677510, delta=-0.05080452)
        # t_norm - t 
        verify(t, t_norm, res)

        # TypeError must be rasied if one of the values is not V3SP.
        self.assertRaises(TypeError, lambda v1: v1 - 1.0, tpm.V3SP(**t))
