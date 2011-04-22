# Some tests for tpm.convert.convert.
import unittest
from pytpm import tpm, convert

class TestConvert(unittest.TestCase):
    """Test tpm.convert.convert."""
    def testFK52GAL(self):
        """tpm.convert.convert: FK5 to GAL."""
        # See pytpm/tests/c_tests/test_convert.c.
        ra2000 = [359.97907800, 359.97945800]
        de2000 = [-65.57713200, -64.37231300]
        l = [311.30033553, 311.91103451]
        b = [-50.70581628, -51.84847717]
        r = convert.convert(ra2000, de2000, s1=tpm.TPM_S06, s2=tpm.TPM_S04)
        for i in range(len(r)):
            if r[i][0] < 0.0: x = r[i][0] + 360.0
            else: x = r[i][0]
            y = r[i][1]
            self.assertAlmostEqual(x, l[i], 8)
            self.assertAlmostEqual(y, b[i], 8)
            
