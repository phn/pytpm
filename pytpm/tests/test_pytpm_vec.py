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
        
        
