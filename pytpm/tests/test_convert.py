# Tests for tpm.convert.convert.
import unittest
from pytpm import tpm, convert
import os

test_dir = os.path.abspath(os.path.dirname(__file__))
hip_data = os.path.join(test_dir, "data/hip.txt")
c_tests_dir = os.path.join(test_dir, "c_tests")

class TestConvert(unittest.TestCase):
    """Test tpm.convert.convert."""
    def testConvertInterface(self):
        """Convert properly handles input paramters."""
        self.assertRaises(TypeError, lambda: convert.convert())
        self.assertRaises(TypeError, lambda: convert.convert(ra=0.0))
        self.assertRaises(TypeError, lambda: convert.convert(dec=0.0))
        self.assertRaises(ValueError, lambda: convert.convert(ra=0,
                                                             dec=[0,1]))
        
    def testFK52GAL_simple(self):
        """tpm.convert.convert: FK5 to GAL simple."""
        # See pytpm/tests/c_tests/test_convert.c.
        ra2000 = [359.97907800, 359.97945800]
        de2000 = [-65.57713200, -64.37231300]
        l = [311.30033553, 311.91103451]
        b = [-50.70581628, -51.84847717]
        r = convert.convert(ra2000, de2000,
                            utc = tpm.J2000, epoch=tpm.J2000,
                            equinox = tpm.J2000,
                            s1=tpm.TPM_S06, s2=tpm.TPM_S04)
        for i in range(len(r)):
            if r[i][0] < 0.0: x = r[i][0] + 360.0
            else: x = r[i][0]
            y = r[i][1]
            self.assertAlmostEqual(x, l[i], 8)
            self.assertAlmostEqual(y, b[i], 8)
            
    def testFK52GAL(self):
        """tpm.convert.convert: FK5 to GAL HIPPARCOS."""
        # See pytpm/tests/c_tests/test_convert_hip.c and
        # pytpm/tests/data/hip_readme.txt.
        ra = []
        dec = []
        f = open(hip_data, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(x[2])
            dec.append(x[3])
        f.close()
        r = convert.convert(ra, dec,
                            utc = tpm.J2000, epoch=tpm.J2000,
                            equinox = tpm.J2000,
                            s1=tpm.TPM_S06, s2=tpm.TPM_S04)  

        f = open(os.path.join(c_tests_dir, "hip_fk5j2000_gal.txt"),"r")
        for i,line in enumerate(f):
            c = [float(j) for j in line.split()]
            self.assertAlmostEqual(r[i][0], c[0], 8)
            self.assertAlmostEqual(r[i][1], c[1], 8)

    def testFK52FK4(self):
        """tpm.convert.convert: FK5 to FK4 HIPPARCOS."""
        # See pytpm/tests/c_tests/test_convert_hip.c and
        # pytpm/tests/data/hip_readme.txt.
        ra = []
        dec = []
        f = open(hip_data, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(x[2])
            dec.append(x[3])
        f.close()
        r = convert.convert(ra, dec,
                            utc = tpm.J2000, epoch=tpm.J2000,
                            equinox = tpm.J2000,
                            s1=tpm.TPM_S06, s2=tpm.TPM_S05)

        f = open(os.path.join(c_tests_dir, "hip_fk5j2000_fk4b1950.txt"),"r")
        for i,line in enumerate(f):
            c = [float(j) for j in line.split()]
            self.assertAlmostEqual(r[i][0], c[0], 8)
            self.assertAlmostEqual(r[i][1], c[1], 8)

    def testFK52ECL(self):
        """tpm.convert.convert: FK5 to ECL HIPPARCOS."""
        # See pytpm/tests/c_tests/test_convert_hip.c and
        # pytpm/tests/data/hip_readme.txt.
        ra = []
        dec = []
        f = open(hip_data, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(x[2])
            dec.append(x[3])
        f.close()
        r = convert.convert(ra, dec,
                            utc = tpm.J2000, epoch=tpm.J2000,
                            equinox = tpm.J2000,
                            s1=tpm.TPM_S06, s2=tpm.TPM_S03)

        f = open(os.path.join(c_tests_dir, "hip_fk5j2000_eclj2000.txt"),"r")
        for i,line in enumerate(f):
            c = [float(j) for j in line.split()]
            self.assertAlmostEqual(r[i][0], c[0], 8)
            self.assertAlmostEqual(r[i][1], c[1], 8)

    def testFK42GAL(self):
        """tpm.convert.convert: FK4 to GAL HIPPARCOS."""
        # See pytpm/tests/c_tests/test_convert_hip.c and
        # pytpm/tests/data/hip_readme.txt.
        ra = []
        dec = []
        f = open(hip_data, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(x[4])
            dec.append(x[5])
        f.close()
        r = convert.convert(ra, dec,
                            utc = tpm.J2000, epoch=tpm.J2000,
                            equinox = tpm.J2000,
                            s1=tpm.TPM_S05, s2=tpm.TPM_S04)  

        f = open(os.path.join(c_tests_dir, "hip_fk4b1950_gal.txt"),"r")
        for i,line in enumerate(f):
            c = [float(j) for j in line.split()]
            self.assertAlmostEqual(r[i][0], c[0], 8)
            self.assertAlmostEqual(r[i][1], c[1], 8)

    def testFK42FK5(self):
        """tpm.convert.convert: FK4 to FK5 HIPPARCOS."""
        # See pytpm/tests/c_tests/test_convert_hip.c and
        # pytpm/tests/data/hip_readme.txt.
        ra = []
        dec = []
        f = open(hip_data, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(x[4])
            dec.append(x[5])
        f.close()
        r = convert.convert(ra, dec,
                            utc = tpm.J2000, epoch=tpm.J2000,
                            equinox = tpm.J2000,
                            s1=tpm.TPM_S05, s2=tpm.TPM_S06)

        f = open(os.path.join(c_tests_dir, "hip_fk4b1950_fk5j2000.txt"),"r")
        for i,line in enumerate(f):
            c = [float(j) for j in line.split()]
            self.assertAlmostEqual(r[i][0], c[0], 8)
            self.assertAlmostEqual(r[i][1], c[1], 8)

    def testFK42ECL(self):
        """tpm.convert.convert: FK4 to ECL HIPPARCOS."""
        # See pytpm/tests/c_tests/test_convert_hip.c and
        # pytpm/tests/data/hip_readme.txt.
        ra = []
        dec = []
        f = open(hip_data, "r")
        for i in f:
            x = [float(j) for j in i.split()]
            ra.append(x[4])
            dec.append(x[5])
        f.close()
        r = convert.convert(ra, dec,
                            utc = tpm.J2000, epoch=tpm.J2000,
                            equinox = tpm.J2000,
                            s1=tpm.TPM_S05, s2=tpm.TPM_S03)

        f = open(os.path.join(c_tests_dir, "hip_fk4b1950_eclj2000.txt"),"r")
        for i,line in enumerate(f):
            c = [float(j) for j in line.split()]
            self.assertAlmostEqual(r[i][0], c[0], 8)
            self.assertAlmostEqual(r[i][1], c[1], 8)

    
        
