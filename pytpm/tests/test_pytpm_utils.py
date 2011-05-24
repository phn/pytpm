# -*- coding: utf-8 -*-
# Test facilities in pytpm_utils.pxi.
import unittest
from pytpm import tpm

class TestNdeltaNalpha(unittest.TestCase):
    """Test ndelta and nalpha."""
    def testNdelta(self):
        delta = [-100, 100, 181, 270]
        delta_out = [-80.0, 80.0, -1.0, -90.0]
        for i,d in enumerate(delta):
            j = tpm.ndelta(d, degrees=True)
            self.assertAlmostEqual(j, delta_out[i], 1)
            k = tpm.ndelta(tpm.d2r(d), degrees=False)
            self.assertAlmostEqual(k, tpm.d2r(delta_out[i]), 1)
    
    def testNalpha(self):
        """tpm.nalpha => angle in [0, 360) or [0, 2π)."""
        alpha = [361, -361, -180]
        alpha_out = [1, 359, 180]
        for i,d in enumerate(alpha):
            j = tpm.nalpha(d, degrees=True)
            self.assertAlmostEqual(j, alpha_out[i], 1)
            k = tpm.nalpha(tpm.d2r(d), degrees=False)
            self.assertAlmostEqual(k, tpm.d2r(alpha_out[i]), 1)
            
        
