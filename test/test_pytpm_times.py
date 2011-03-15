# -*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_times.pxi file.
import unittest
from pytpm import tpm

class TestDMSStructure(unittest.TestCase):
    """Test if the methods in the DMS class work."""
    def testCreate(self):
        """Must be able to create an DMS object."""
        dms = tpm.DMS()
        self.assertEqual(type(dms), tpm.DMS)
        
    def testGetFields(self):
        """Must be able to retrieve default values of fields."""
        dms = tpm.DMS()
        self.assertAlmostEqual(dms.dd, 0.0)
        self.assertAlmostEqual(dms.mm, 0.0)
        self.assertAlmostEqual(dms.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to set values to fields at creation."""
        dms = tpm.DMS(dms={'dd':1.0,'mm':1.0,'ss':1.34})
        self.assertAlmostEqual(dms.dd, 1.0)
        self.assertAlmostEqual(dms.mm, 1.0)
        self.assertAlmostEqual(dms.ss, 1.34)
        
    def testSetFieldValues(self):
        """Must be able to set values after creation."""
        dms = tpm.DMS()
        dms.dd = 1.0
        dms.mm = 1.0
        dms.ss = 1.34
        self.assertAlmostEqual(dms.dd, 1.0)
        self.assertAlmostEqual(dms.mm, 1.0)
        self.assertAlmostEqual(dms.ss, 1.34)
        
    def testAddition(self):
        """Must perform addition of two DMS values."""
        dms1 = tpm.DMS()
        dms2 = tpm.DMS()
        dms1.dd = 1.1
        dms1.mm = 1.2
        dms1.ss = 1.3
        dms2.dd = 2.4
        dms2.mm = 2.5
        dms2.ss = 2.6
        dms = dms1 + dms2
        self.assertAlmostEqual(dms.dd, dms1.dd+dms2.dd)
        self.assertAlmostEqual(dms.mm, dms1.mm+dms2.mm)
        self.assertAlmostEqual(dms.ss, dms1.ss+dms2.ss)

    def testSubtraction(self):
        """Must perform subtraction of two DMS values."""
        dms1 = tpm.DMS()
        dms2 = tpm.DMS()
        dms1.dd = 1.1
        dms1.mm = 1.2
        dms1.ss = 1.3
        dms2.dd = 2.4
        dms2.mm = 2.5
        dms2.ss = 2.6
        dms = dms1 - dms2
        self.assertAlmostEqual(dms.dd, dms1.dd-dms2.dd)
        self.assertAlmostEqual(dms.mm, dms1.mm-dms2.mm)
        self.assertAlmostEqual(dms.ss, dms1.ss-dms2.ss)

    def testRepr(self):
        """The __repr__ method must give proper output."""
        dms = tpm.DMS()
        dms.dd = 1.1
        dms.mm = 1.2
        dms.ss = 1.3
        d = eval(repr(dms))
        self.assertAlmostEqual(d['dd'], dms.dd) 
        self.assertAlmostEqual(d['mm'], dms.mm) 
        self.assertAlmostEqual(d['ss'], dms.ss) 
        
    def testUnicodeAndStr(self):
        """Test string representation."""
        dms = tpm.DMS()
        dms.dd = 1.0
        dms.mm = 2.0
        dms.ss = 3.0
        self.assertEqual(str(dms),"+01\xc2\xb0 02' 03.000\"")
        self.assertEqual(dms.__unicode__(),u"+01\u00B0 02' 03.000\"")

        
class TestHMSStructure(unittest.TestCase):
    """Test if the methods in the HMS class work."""
    def testCreate(self):
        """Must be able to create an HMS object."""
        hms = tpm.HMS()
        self.assertEqual(type(hms), tpm.HMS)
        
    def testGetFields(self):
        """Must be able to retrieve default values of fields."""
        hms = tpm.HMS()
        self.assertAlmostEqual(hms.hh, 0.0)
        self.assertAlmostEqual(hms.mm, 0.0)
        self.assertAlmostEqual(hms.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to set values to fields at creation."""
        hms = tpm.HMS(hms={'hh':1.0,'mm':1.0,'ss':1.34})
        self.assertAlmostEqual(hms.hh, 1.0)
        self.assertAlmostEqual(hms.mm, 1.0)
        self.assertAlmostEqual(hms.ss, 1.34)
        
    def testSetFieldValues(self):
        """Must be able to set values after creation."""
        hms = tpm.HMS()
        hms.hh = 1.0
        hms.mm = 1.0
        hms.ss = 1.34
        self.assertAlmostEqual(hms.hh, 1.0)
        self.assertAlmostEqual(hms.mm, 1.0)
        self.assertAlmostEqual(hms.ss, 1.34)
        
    def testAddition(self):
        """Must perform addition of two HMS values."""
        hms1 = tpm.HMS()
        hms2 = tpm.HMS()
        hms1.hh = 1.1
        hms1.mm = 1.2
        hms1.ss = 1.3
        hms2.hh = 2.4
        hms2.mm = 2.5
        hms2.ss = 2.6
        hms = hms1 + hms2
        self.assertAlmostEqual(hms.hh, hms1.hh+hms2.hh)
        self.assertAlmostEqual(hms.mm, hms1.mm+hms2.mm)
        self.assertAlmostEqual(hms.ss, hms1.ss+hms2.ss)

    def testSubtraction(self):
        """Must perform subtraction of two HMS values."""
        hms1 = tpm.HMS()
        hms2 = tpm.HMS()
        hms1.hh = 1.1
        hms1.mm = 1.2
        hms1.ss = 1.3
        hms2.hh = 2.4
        hms2.mm = 2.5
        hms2.ss = 2.6
        hms = hms1 - hms2
        self.assertAlmostEqual(hms.hh, hms1.hh-hms2.hh)
        self.assertAlmostEqual(hms.mm, hms1.mm-hms2.mm)
        self.assertAlmostEqual(hms.ss, hms1.ss-hms2.ss)

    def testRepr(self):
        """The __repr__ method must give proper output."""
        hms = tpm.HMS()
        hms.hh = 1.1
        hms.mm = 1.2
        hms.ss = 1.3
        h = eval(repr(hms))
        self.assertAlmostEqual(h['hh'], hms.hh) 
        self.assertAlmostEqual(h['mm'], hms.mm) 
        self.assertAlmostEqual(h['ss'], hms.ss) 
        
    def testUnicodeAndStr(self):
        """Test string representation."""
        hms = tpm.HMS()
        hms.hh = 1.0
        hms.mm = 2.0
        hms.ss = 3.0
        self.assertEqual(str(hms)," 01H 02M 03.000S")
        self.assertEqual(hms.__unicode__(),u" 01H 02M 03.000S")
        
if __name__ == '__main__':
    unittest.main()
