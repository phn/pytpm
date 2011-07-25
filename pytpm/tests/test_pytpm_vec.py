# -*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_vec.pxi file.
import unittest
from pytpm import tpm

class TestV3Structure(unittest.TestCase):
    """Test the V3 wrapper for _tpm_vec.V3"""
    def testCreate(self):
        """V3.init => create V3 object."""
        v3 = tpm.V3()
        self.assertEqual(type(v3), tpm.V3)

        # Must raise Attribute error if any property is accessed
        self.assertRaises(AttributeError, lambda v: v.x, v3)
        self.assertRaises(AttributeError, lambda v: v.getX(), v3)

        
class TestV3CP(unittest.TestCase):
    """Test the V3CP class."""
    def testCreate(self):
        """V3CP() => create V3CP class."""
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
        """V3CP(**vals) => set V3CP fields at init."""
        t = dict(x=-12.34, y=21345.0, z=-0.00001)
        v3cp = tpm.V3CP(**t)
        self.assertAlmostEqual(v3cp.x, t['x'])
        self.assertAlmostEqual(v3cp.y, t['y'])
        self.assertAlmostEqual(v3cp.z, t['z'])

    def testV3C2S(self):
        """V3CP.c2s() => convert V3CP to V3SP object."""
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
        """V3CP.__sub__ => V3CP - V3CP."""
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

    def testV3CAdd(self):
        """V3CP.__add__ => V3CP + V3CP."""
        import math
        def verify(t, t_norm):
            v3cp1 = tpm.V3CP(**t)
            v3cp2 = tpm.V3CP(**t_norm)
            v3cp = v3cp2 + v3cp1
            self.assertEqual(type(v3cp), tpm.V3CP)
            self.assertEqual(v3cp.ctype, tpm.CARTESIAN)
            self.assertEqual(v3cp.vtype, tpm.POS)
            self.assertAlmostEqual(v3cp.x, t_norm['x'] + t['x'])
            self.assertAlmostEqual(v3cp.y, t_norm['y'] + t['y'])
            self.assertAlmostEqual(v3cp.z, t_norm['z'] + t['z'])

        t = dict(x=1.0, y=2.0, z=3.0)
        t_norm = dict(x=10.0, y=20.0, z=-0.234)
        verify(t, t_norm)

        t = dict(x=1.0, y=2.0, z=3.0)
        t_norm = dict(x=10.0, y=20.0, z=-0.234)
        verify(t_norm, t)

        # TypeError must be rasied if one of the values is not V3CP.
        self.assertRaises(TypeError, lambda v1: v1 + 1.0, tpm.V3CP(**t))

    def testV3CMultiply(self):
        """V3CP.__mul__ => V3CP * x; scale with a scalar."""
        def verify(t, n):
            v3cp1 = tpm.V3CP(**t)
            v3cp = v3cp1 * n
            self.assertEqual(type(v3cp), tpm.V3CP)
            self.assertEqual(v3cp.ctype, tpm.CARTESIAN)
            self.assertEqual(v3cp.vtype, tpm.POS)
            self.assertAlmostEqual(v3cp.x, t['x'] * n)
            self.assertAlmostEqual(v3cp.y, t['y'] * n)
            self.assertAlmostEqual(v3cp.z, t['z'] * n)

        t = dict(x=1.0, y=2.0, z=3.0)
        verify(t, 2.0)

        # This TypeError is raised by Cython. Cython doesn't have a
        # __rmul__ and hence the __mul__ of the right hand V3CP is
        # called. But then the types of self and n in __mul__ become
        # incompatible and TypeError is raised.
        self.assertRaises(TypeError, lambda v1: 3 * v1, tpm.V3CP(**t))

    def testV3Unit(self):
        """V3CP.unit() => return a unit vector."""
        import math
        def verify(t, t_norm):
            v3cp1 = tpm.V3CP(**t)
            v3cp = v3cp1.unit()
            self.assertEqual(type(v3cp), tpm.V3CP)
            self.assertEqual(v3cp.ctype, tpm.CARTESIAN)
            self.assertEqual(v3cp.vtype, tpm.POS)
            self.assertAlmostEqual(v3cp.x, t_norm['x'])
            self.assertAlmostEqual(v3cp.y, t_norm['y'])
            self.assertAlmostEqual(v3cp.z, t_norm['z'])
            r = math.sqrt(v3cp.x**2 + v3cp.y**2 + v3cp.z**2)
            self.assertAlmostEqual(r, 1.0)

        t = dict(x=12.34567, y=34.56712, z=56.71234)
        t_norm = dict(x=0.18275165, y=0.51169344, z= 0.83950680)
        verify(t, t_norm)

    def testV3Mod(self):
        """V3CP.mod() => modulus/length of V3CP."""
        import math
        def verify(t, t_norm):
            v3cp = tpm.V3CP(**t)
            d = v3cp.mod()
            self.assertAlmostEqual(d, t_norm)
        
        t = dict(x=0.18275165, y=0.51169344, z= 0.83950680)
        verify(t, 1.0)

        t = dict(x=12.34567, y=34.56712, z=56.71234)
        verify(t, math.sqrt(t['x']**2+t['y']**2+t['z']**2))

    def testV3CDot(self):
        """V3CP.dot(V3CP) => dot product of two V3CP vectors."""
        def verify(t, t_norm, res):
            v3cp1 = tpm.V3CP(**t)
            v3cp2 = tpm.V3CP(**t_norm)
            d = v3cp1.dot(v3cp2)
            self.assertAlmostEqual(d, res)

        t = dict(x=0.18275165, y=0.51169344, z= 0.83950680)
        t_norm = dict(x=12.34567, y=34.56712, z=56.71234)
        verify(t,t_norm, t['x']*t_norm['x'] + t['y']*t_norm['y'] +
               t['z']*t_norm['z'])

    def testV3CCross(self):
        """V3CP.cross(V3CP) => cross product of two V3CP vectors."""
        def verify(t, t_norm, res):
            v3cp1 = tpm.V3CP(**t)
            v3cp2 = tpm.V3CP(**t_norm)
            v3cp = v3cp1.cross(v3cp2)
            self.assertEqual(v3cp.ctype, tpm.CARTESIAN)
            self.assertEqual(v3cp.vtype, tpm.POS)
            self.assertAlmostEqual(v3cp.x, res['x'])
            self.assertAlmostEqual(v3cp.y, res['y'])
            self.assertAlmostEqual(v3cp.z, res['z'])

        # See pytpm/tests/c_tests/v3cross_test.c.
        t1 = dict(x=1123.4556, y=4556.1123, z=9876.1267)
        t2 = dict(x=2.3456, y=6.7891, z=7.8912)
        res = dict(x=-31096.818397210, y=14300.029956800, z=-3059.564596920)
        verify(t1, t2, res)

    def testStrUnicode(self):
        """V3CP. __str__ => string representation."""
        def verify(t, t_norm, f):
            v3cp = tpm.V3CP(**t)
            s = f(v3cp)
            self.assertEqual(s, t_norm)

        t = dict(x=112.4, y=2234.0, z=322.0)
        t_norm = " 1.124000000000000e+02  2.234000000000000e+03  3.220000000000000e+02"
        verify(t, t_norm, str)

class TestV3SP(unittest.TestCase):
    """Test the V3CP class."""
    def testCreate(self):
        """V3CP() => create V3CP class."""
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
        """V3SP(**vals) => set fields at init."""
        t = dict(r=2.0, alpha=-0.12, delta=2*3.14)
        v3sp = tpm.V3SP(**t)
        self.assertAlmostEqual(v3sp.r, t['r'])
        self.assertAlmostEqual(v3sp.alpha, t['alpha'])
        self.assertAlmostEqual(v3sp.delta, t['delta'])

    def testV3S2C(self):
        """V3SP.s2c() => convert V3CP into a V3CP object."""
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
        """V3SP.__sub__ => V3SP - V3SP."""
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
        # t_norm + t
        verify(t, t_norm, res)

        t = dict(r=-1.0, alpha=2.0, delta=3.0)
        t_norm = dict(r=1.0, alpha=-2.0, delta=-0.234)
        res = dict(r=1.78703389, alpha=-1.56677510, delta=-0.05080452)
        # t_norm + t 
        verify(t, t_norm, res)

        # TypeError must be rasied if one of the values is not V3SP.
        self.assertRaises(TypeError, lambda v1: v1 - 1.0, tpm.V3SP(**t))

    def testV3SAdd(self):
        """V3SP.__add__ => V3SP + V3SP."""
        def verify(t, t_norm, res):
            v3sp1 = tpm.V3SP(**t)
            v3sp2 = tpm.V3SP(**t_norm)
            v3sp = v3sp2 + v3sp1
            self.assertEqual(type(v3sp), tpm.V3SP)
            self.assertEqual(v3sp.ctype, tpm.SPHERICAL)
            self.assertEqual(v3sp.vtype, tpm.POS)
            self.assertAlmostEqual(v3sp.r, res['r'])
            self.assertAlmostEqual(v3sp.alpha, res['alpha'])
            self.assertAlmostEqual(v3sp.delta, res['delta'])

        # see pytpm/tests/c_tests/v3sum_test.c
        t = dict(r=1.0, alpha=2.0, delta=3.0)
        t_norm = dict(r=10.0, alpha=0.2, delta=-0.234)
        res = dict(r=10.23335408, alpha=0.10342998, delta=-0.21443228)
        # t_norm + t
        verify(t, t_norm, res)

        t = dict(r=-1.0, alpha=2.0, delta=3.0)
        t_norm = dict(r=1.0, alpha=-2.0, delta=-0.234)
        res = dict(r=0.89805895, alpha=3.12239595, delta=-0.42830498)
        # t_norm + t 
        verify(t, t_norm, res)

        # TypeError must be rasied if one of the values is not V3SP.
        self.assertRaises(TypeError, lambda v1: v1 + 1.0, tpm.V3SP(**t))

    def testV3SMultiply(self):
        """V3SP.__mul__ => V3SP * x; scale with a scalar."""
        def verify(t, n):
            v3sp1 = tpm.V3SP(**t)
            v3sp = v3sp1 * n
            self.assertEqual(type(v3sp), tpm.V3SP)
            self.assertEqual(v3sp.ctype, tpm.SPHERICAL)
            self.assertEqual(v3sp.vtype, tpm.POS)
            self.assertAlmostEqual(v3sp.r, t['r'] * n)
            self.assertAlmostEqual(v3sp.alpha, t['alpha'])
            self.assertAlmostEqual(v3sp.delta, t['delta'])

        t = dict(r=1345678.12345, alpha=-2.345, delta=0.234)
        verify(t, 2.0)

        # This TypeError is raised by Cython. Cython doesn't have a
        # __rmul__ and hence the __mul__ of the right hand V3CP is
        # called. But then the types of self and n in __mul__ become
        # incompatible and TypeError is raised.
        self.assertRaises(TypeError, lambda v1: 3 * v1, tpm.V3SP(**t))

    def testV3SMod(self):
        """V3SP.mod() => return the magnitude of R."""
        def verify(t, t_norm):
            v3sp = tpm.V3SP(**t)
            d = v3sp.mod()
            self.assertAlmostEqual(d, t_norm)

        t = dict(r=12345.678, alpha=0.23, delta=-1.2)
        verify(t, t['r'])

        t = dict(r=-12345.678, alpha=0.23, delta=-1.2)
        verify(t, -t['r'])
            
    def testV3SDot(self):
        """V3SP.dot(V3SP) => dot product of two V3SP vectors."""
        import math
        def verify(t, t_norm, res):
            v3sp1 = tpm.V3SP(**t)
            v3sp2 = tpm.V3SP(**t_norm)
            d = v3sp1.dot(v3sp2)
            self.assertAlmostEqual(d, res)

        t1 = dict(r=1.67000000, alpha=-1.2340000000, delta=4.3450000000)
        t2 = dict(r=178.50000000, alpha=-0.2340000000, delta=-5.4320000000)
        res = -247.35416601
        verify(t1, t2, res)

    def testV3SCross(self):
        """V3SP.cross(V3SP) => cross product of two V3SP vectors."""
        def verify(t, t_norm, res):
            v3sp1 = tpm.V3SP(**t)
            v3sp2 = tpm.V3SP(**t_norm)
            v3sp = v3sp1.cross(v3sp2)
            self.assertEqual(v3sp.ctype, tpm.SPHERICAL)
            self.assertEqual(v3sp.vtype, tpm.POS)
            self.assertAlmostEqual(v3sp.r, res['r'])
            self.assertAlmostEqual(v3sp.alpha, res['alpha'])
            self.assertAlmostEqual(v3sp.delta, res['delta'])

        # See pytpm/tests/c_tests/v3cross_test.c.
        t1 = dict(r=123.456, alpha=0.1123, delta=-6.1267)
        t2 = dict(r=2.3456, alpha=-0.7891, delta=1.8912)
        res = dict(r=289.283397536, alpha=-1.498240701, delta=0.246708418)
        verify(t1, t2, res)

    def testNAlpha(self):
        """V3SP.nalpha => normalized alpha i.e., RA."""
        def verify(t, t_norm):
            v3sp = tpm.V3SP(**t)
            a = v3sp.nalpha
            self.assertAlmostEqual(a, t_norm)

        # See pytpm/tests/c_tests/v3alpha_test.c.
        t = dict(r=-1.0, alpha=-2.0, delta=3.0)
        t_norm = 1.14159265
        verify(t, t_norm)

        t = dict(r=10.0, alpha=0.2, delta=-0.234)
        t_norm = 0.20
        verify(t, t_norm)

        t = dict(r=-1.0, alpha=2.0, delta=3.0)
        t_norm = 5.14159265
        verify(t, t_norm)

        t = dict(r=1.0, alpha=-2.0, delta=-0.234)
        t_norm = 4.28318531
        verify(t, t_norm)

    def testNDelta(self):
        """V3SP.ndelta => normalized delta i.e., DEC."""
        def verify(t, t_norm):
            v3sp = tpm.V3SP(**t)
            a = v3sp.ndelta
            self.assertAlmostEqual(a, t_norm)

        # See pytpm/tests/c_tests/v3delta_test.c.
        t = dict(r=-1.0, alpha=-2.0, delta=3.0)
        t_norm = -0.14159265
        verify(t, t_norm)

        t = dict(r=10.0, alpha=0.2, delta=-0.234)
        t_norm = -0.234000
        verify(t, t_norm)

        t = dict(r=-1.0, alpha=2.0, delta=3.0)
        t_norm = -0.14159265
        verify(t, t_norm)

        t = dict(r=1.0, alpha=-2.0, delta=-0.234)
        t_norm = -0.23400
        verify(t, t_norm)

    def testStrUnicode(self):
        """V3SP.__str__ => string representation of V3SP."""
        def verify(t, t_norm, f):
            v3sp = tpm.V3SP(**t)
            s = f(v3sp)
            self.assertEqual(s, t_norm)

        t = dict(r=1.0, alpha=2.0, delta=3.0)
        t_norm = " 1.000000000000000e+00  2.000000000000000e+00  3.000000000000000e+00"
        verify(t, t_norm, str)

class TestV6C(unittest.TestCase):
    """Test V6 cartesian vector."""
    def testCreate(self):
        """V6C() => creat a V6C class."""
        v6c = tpm.V6C()
        self.assertEqual(type(v6c), tpm.V6C)

        # Access default init values.
        self.assertAlmostEqual(v6c.ctype, tpm.CARTESIAN)
        self.assertAlmostEqual(v6c.x, 0.0)
        self.assertAlmostEqual(v6c.y, 0.0)
        self.assertAlmostEqual(v6c.z, 0.0)
        self.assertAlmostEqual(v6c.xdot, 0.0)
        self.assertAlmostEqual(v6c.ydot, 0.0)
        self.assertAlmostEqual(v6c.zdot, 0.0)

        # ctype is read only.
        def f(x):
            x.ctype = tpm.SPHERICAL
        self.assertRaises(AttributeError, f, v6c)

    def checkv6(self, v6c, t):
        """Compare V6 fields with the values in t."""
        self.assertAlmostEqual(v6c.x, t['x'])
        self.assertAlmostEqual(v6c.y, t['y'])
        self.assertAlmostEqual(v6c.z, t['z'])
        self.assertAlmostEqual(v6c.xdot, t['xdot'])
        self.assertAlmostEqual(v6c.ydot, t['ydot'])
        self.assertAlmostEqual(v6c.zdot, t['zdot'])
        
    def testSetGetInitValues(self):
        """V6C(**vals) => set fields at init."""
        t = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        v6c = tpm.V6C(**t)
        self.checkv6(v6c, t)

    def testV6Sub(self):
        """V6C.__sub__ => V6C - V6C."""
        t1 = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        t2 = dict(x=23.5, y=12.3, z=1234.5, xdot=-1.23, ydot=-123.4, zdot=100.0)
        tdiff = dict(x=t1['x']-t2['x'], y=t1['y']-t2['y'], z=t1['z']-t2['z'],
                     xdot=t1['xdot']-t2['xdot'], ydot=t1['ydot']-t2['ydot'],
                     zdot=t1['zdot']-t2['zdot'])
        v6c1 = tpm.V6C(**t1)
        v6c2 = tpm.V6C(**t2)
        v6cdiff = v6c1 - v6c2
        self.checkv6(v6cdiff, tdiff)

    def testV6Add(self):
        """V6C.__add__ => V3C + V3C."""
        t1 = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        t2 = dict(x=23.5, y=12.3, z=1234.5, xdot=-1.23, ydot=-123.4, zdot=100.0)
        tsum = dict(x=t1['x']+t2['x'], y=t1['y']+t2['y'], z=t1['z']+t2['z'],
                     xdot=t1['xdot']+t2['xdot'], ydot=t1['ydot']+t2['ydot'],
                     zdot=t1['zdot']+t2['zdot'])
        v6c1 = tpm.V6C(**t1)
        v6c2 = tpm.V6C(**t2)
        v6csum = v6c1 + v6c2
        self.checkv6(v6csum, tsum)

    def testV6Mod(self):
        """V6C.mod() => modulus/length of a V6C vector."""
        t = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        v6c = tpm.V6C(**t)
        tm = (t['x']**2 + t['y']**2 + t['z']**2)**(0.5)
        self.assertAlmostEqual(v6c.mod(), tm)

    def testV6Unit(self):
        """V6C.unit() =>  unit POS vector and scaled VEL vector."""
        t = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        v6c = tpm.V6C(**t)
        v6c = v6c.unit()
        tm = (t['x']**2 + t['y']**2 + t['z']**2)**(0.5)
        t1 = t.copy()
        for key in t1:
            t1[key] *= 1/tm
        self.checkv6(v6c, t1)
        
    def testV6Scale(self):
        """V6C.scale() => scale with a scalar."""
        t = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        v6c = tpm.V6C(**t)
        v6c = v6c.scale(1.234)
        t1 = t.copy()
        for key in t1:
            t1[key] *= 1.234
        self.checkv6(v6c, t1)
        
    def testV62V3(self):
        """V6C.v62v3() => apply space motion and return resulting V3CP."""
        t = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        v6c = tpm.V6C(**t)
        dt = 1200.345
        v3cp = v6c.v62v3(dt)
        self.assertEqual(v3cp.ctype, tpm.CARTESIAN)
        self.assertEqual(v3cp.vtype, tpm.POS)
        self.assertAlmostEqual(v3cp.x, t['x']+t['xdot']*dt)
        self.assertAlmostEqual(v3cp.y, t['y']+t['ydot']*dt)
        self.assertAlmostEqual(v3cp.z, t['z']+t['zdot']*dt)

    def testV6Dot(self):
        """V6C.dot(V6C) => dot product of two V6C vector withs."""
        t = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        v6c = tpm.V6C(**t)
        t1 = dict(x=100.34, y=-0.230, z=0.0, xdot=-1234.5, ydot=-43.5, zdot=123.9)
        v6c1 = tpm.V6C(**t1)
        x = t['x']*t1['x']+ t['y']*t1['y']+t['z']*t1['z']
        self.assertEqual(v6c.dot(v6c1), x)
        self.assertEqual(v6c1.dot(v6c), x)

    def testV6Cross(self):
        """V6C.cross(V6C) => cross product V6C vectors."""
        t1 = dict(x=-12.34, y=21345.0, z=0.01, xdot=1.23, ydot=3.21, zdot=0.0)
        v6c = tpm.V6C(**t1)
        t2 = dict(x=100.34, y=-0.230, z=0.0, xdot=-1234.5, ydot=-43.5, zdot=123.9)
        v6c1 = tpm.V6C(**t2)
        t = dict(x=t1['y']*t2['z']-t1['z']*t2['y'],
                 y=t1['z']*t2['x']-t1['x']*t2['z'],
                 z=t1['x']*t2['y']-t1['y']*t2['x'],
                 xdot=0.0, ydot=0.0, zdot=0.0)

        self.checkv6(v6c.cross(v6c1), t)
        self.checkv6(v6c1.cross(v6c), dict(x=-t['x'], y=-t['y'],
                                           z=-t['z'], xdot=0.0,
                                           ydot=0.0, zdot=0.0))

    def testV6C2S(self):
        """V6C.c2s() => V6C to V6S i.e., Cartesian to spherical."""
        t = dict(x=1123.4556, y=4556.1123, z=9876.1267, xdot=2.3456,
                 ydot=6.7891, zdot=7.8912)
        tn = dict(r=10934.26679617, alpha=1.32903712, delta=1.12723066,
                  rdot=10.19744374, alphadot=-0.00013894, deltadot=
                  -0.00028117)
        v6c = tpm.V6C(**t)
        v6s = v6c.c2s()
        self.assertEqual(v6s.ctype, tpm.SPHERICAL)
        self.assertAlmostEqual(v6s.r, tn['r'])
        self.assertAlmostEqual(v6s.alpha, tn['alpha'])
        self.assertAlmostEqual(v6s.delta, tn['delta'])
        self.assertAlmostEqual(v6s.rdot, tn['rdot'])
        self.assertAlmostEqual(v6s.alphadot, tn['alphadot'])
        self.assertAlmostEqual(v6s.deltadot, tn['deltadot'])

    def testV6GetPOS(self):
        """V6C.pos => POS components of V6C, as V3CP."""
        t = dict(x=1123.4556, y=4556.1123, z=9876.1267, xdot=2.3456,
                 ydot=6.7891, zdot=7.8912)
        v6c = tpm.V6C(**t)
        v6pos = v6c.pos
        self.assertEqual(v6pos.vtype, tpm.POS)
        self.assertEqual(v6pos.ctype, tpm.CARTESIAN)
        self.assertAlmostEqual(v6pos.x, t['x'])
        self.assertAlmostEqual(v6pos.y, t['y'])
        self.assertAlmostEqual(v6pos.z, t['z'])

    def testV6SetPOS(self):
        """V6C.pos = V3CP => set POS components of V6C, using V3CP."""
        t = dict(x=1123.4556, y=4556.1123, z=9876.1267)
        v3cp = tpm.V3CP(**t)
        v6cp = tpm.V6C()
        v6cp.pos = v3cp
        self.assertAlmostEqual(v6cp.x, t['x'])
        self.assertAlmostEqual(v6cp.x, v3cp.x)
        self.assertAlmostEqual(v6cp.y, t['y'])
        self.assertAlmostEqual(v6cp.y, v3cp.y)
        self.assertAlmostEqual(v6cp.z, t['z'])
        self.assertAlmostEqual(v6cp.z, v3cp.z)

        
class TestV6S(unittest.TestCase):
    """Test V6 spherical vector."""
    def testCreate(self):
        """V6S() => create a V6S class."""
        v6s = tpm.V6S()
        self.assertEqual(type(v6s), tpm.V6S)

        # Access default init values.
        self.assertAlmostEqual(v6s.ctype, tpm.SPHERICAL)
        self.assertAlmostEqual(v6s.r, 0.0)
        self.assertAlmostEqual(v6s.alpha, 0.0)
        self.assertAlmostEqual(v6s.delta, 0.0)
        self.assertAlmostEqual(v6s.rdot, 0.0)
        self.assertAlmostEqual(v6s.alphadot, 0.0)
        self.assertAlmostEqual(v6s.deltadot, 0.0)

        # ctype is read only.
        def f(x):
            x.ctype = tpm.CARTESIAN
        self.assertRaises(AttributeError, f, v6s)

    def checkv6(self, v6s, t):
        """Compare V6 fields with the values in t."""
        self.assertAlmostEqual(v6s.r, t['r'])
        self.assertAlmostEqual(v6s.alpha, t['alpha'])
        self.assertAlmostEqual(v6s.delta, t['delta'])
        self.assertAlmostEqual(v6s.rdot, t['rdot'])
        self.assertAlmostEqual(v6s.alphadot, t['alphadot'])
        self.assertAlmostEqual(v6s.deltadot, t['deltadot'])
        
    def testSetGetInitValues(self):
        """V6S(**vals) => set V6S fields at init."""
        t = dict(r=1234.56, alpha=2.345, delta=-6.456,
                 rdot=-123.89, alphadot=0.123, deltadot=-0.54)
        v6s = tpm.V6S(**t)
        self.checkv6(v6s, t)

    def testV6S2C(self):
        """V6S.s2c() => V6C to V6C i.e., spherical to Cartesian."""
        tn = dict(x=1123.4556, y=4556.1123, z=9876.1267, xdot=2.3456,
                 ydot=6.7891, zdot=7.8912)
        t = dict(r=10934.26679617, alpha=1.32903712, delta=1.12723066,
                  rdot=10.19744374, alphadot=-0.00013894, deltadot=
                  -0.00028117)
        v6s = tpm.V6S(**t)
        v6c = v6s.s2c()
        self.assertEqual(v6c.ctype, tpm.CARTESIAN)
        self.assertAlmostEqual(v6c.x, tn['x'], 4)
        self.assertAlmostEqual(v6c.y, tn['y'], 4)
        self.assertAlmostEqual(v6c.z, tn['z'], 4)
        self.assertAlmostEqual(v6c.xdot, tn['xdot'], 4)
        self.assertAlmostEqual(v6c.ydot, tn['ydot'], 4)
        self.assertAlmostEqual(v6c.zdot, tn['zdot'], 4)

    def testNAlpha(self):
        """V6S.nalpha => properly normalized alpha i.e., RA."""
        def verify(t, t_norm):
            v6s = tpm.V6S(**t)
            a = v6s.nalpha
            self.assertAlmostEqual(a, t_norm)

        # The velocity components get default value i.e., 0.
        # See pytpm/tests/c_tests/v3alpha_test.c.
        t = dict(r=-1.0, alpha=-2.0, delta=3.0)
        t_norm = 1.14159265
        verify(t, t_norm)

        t = dict(r=10.0, alpha=0.2, delta=-0.234)
        t_norm = 0.20
        verify(t, t_norm)

        t = dict(r=-1.0, alpha=2.0, delta=3.0)
        t_norm = 5.14159265
        verify(t, t_norm)

        t = dict(r=1.0, alpha=-2.0, delta=-0.234)
        t_norm = 4.28318531
        verify(t, t_norm)

    def testNDelta(self):
        """V6S.ndelta => properly normalized delta i.e., DEC."""
        def verify(t, t_norm):
            v6s = tpm.V6S(**t)
            a = v6s.ndelta
            self.assertAlmostEqual(a, t_norm)

        # The velocity components get default value i.e., 0.
        # See pytpm/tests/c_tests/v3delta_test.c.
        t = dict(r=-1.0, alpha=-2.0, delta=3.0)
        t_norm = -0.14159265
        verify(t, t_norm)

        t = dict(r=10.0, alpha=0.2, delta=-0.234)
        t_norm = -0.234000
        verify(t, t_norm)

        t = dict(r=-1.0, alpha=2.0, delta=3.0)
        t_norm = -0.14159265
        verify(t, t_norm)

        t = dict(r=1.0, alpha=-2.0, delta=-0.234)
        t_norm = -0.23400
        verify(t, t_norm)
