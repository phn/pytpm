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

        
