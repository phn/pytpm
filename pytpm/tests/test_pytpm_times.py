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
        t={'dd':1.0,'mm':1.0,'ss':1.34}
        dms = tpm.DMS(**t)
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

    def testAdditionNonHMS(self):
        """Must raise exception if addition involves non DMS value."""
        dms = tpm.DMS() # All zeros.
        def add_dms(dms,x):
            return dms + x
        self.assertRaises(TypeError,add_dms, dms, 1)

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

    def testSubtractionNonDMS(self):
        """Must raise exception if subtraction involves non DMS value."""
        dms = tpm.DMS() # All zeros.
        def sub_dms(dms,x):
            return dms - x
        self.assertRaises(TypeError,sub_dms, dms, 1)

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

    def testToHMS(self):
        """Must return a tpm.HMS object with appropriate field values."""
        t = {'dd': 180.0, 'mm':450.0, 'ss':0.0 }
        t_hms = {'hh': 12.0, 'mm':30.0, 'ss': 0.0}
        dms = tpm.DMS(**t)
        hms = dms.to_hms()
        self.assertEqual(type(hms), tpm.HMS)
        self.assertEqual(hms.hh, t_hms['hh'])
        self.assertEqual(hms.mm, t_hms['mm']) 
        self.assertEqual(hms.ss, t_hms['ss'])

    def testNormalize(self):
        """Must properly normalize degrees, arc-minutes and arc-seconds."""
        def verify(t,t_norm):
            dms = tpm.DMS(**t)
            dms.normalize()
            self.assertAlmostEqual(dms.dd, t_norm['dd'])
            self.assertAlmostEqual(dms.mm, t_norm['mm'])
            self.assertAlmostEqual(dms.ss, t_norm['ss'])

        # See tests/c_tests/dms2dms_test.c
        # Note:
        # angle = (dms.dd) + (dms.mm/60.0) + (dms.ss/3600.0)
        # i.e., each must have its own sign. But in string
        # representation only the degrees will have sign. Normalization
        # removes negative sign from mm and ss and incorporates the
        # necessary change into the degrees part and range is (-360.0, 360.0).
        # That is string -12D 14' 43" => -(12+14/60.0+43/3600.0) and
        # dms.hh = -12 dms.mm=14 dms.ss=43 => (-12)+(14/60.0)+(43/3600.0).
        # So -12.425 = "-12D 14' 43\"" = (dms.dd=-13, dms.mm=45, dms.ss=18)
        # = (dms.dd=-12, dms.mm=-14, dms.ss=-43) to three decimal places.
        # Also -360.0 = 0.0 = 360.0
        t = {'dd': 180.0, 'mm':450.0, 'ss':0.0 }
        t_norm = {'dd': 187.0, 'mm': 30.0, 'ss':0.0}
        verify(t,t_norm)
        
        t = {'dd':12.245, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': 12.0, 'mm': 14.0, 'ss': 42.0}
        verify(t,t_norm)
        
        t = {'dd':-12.245, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': -13.0, 'mm': 45.0, 'ss': 18.0}
        verify(t,t_norm)

        t = {'dd':361.1230, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': 1.0, 'mm': 7.0, 'ss': 22.8}
        verify(t,t_norm)

        t = {'dd':-361.1230, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': 358.0, 'mm': 52.0, 'ss': 37.2}
        verify(t,t_norm)
        
        t = {'dd':-358.0, 'mm':-1.0, 'ss':-1.0}
        t_norm = {'dd': -359.0, 'mm': 58.0, 'ss': 59.0}
        verify(t,t_norm)

        t = {'dd':-358.0, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': -358.0, 'mm': 0.0, 'ss': 0.0}
        verify(t,t_norm)

        t = {'dd':-710.0, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': 10.0, 'mm': 0.0, 'ss': 0.0}
        verify(t,t_norm)

        t = {'dd':710.0, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': 350.0, 'mm': 0.0, 'ss': 0.0}
        verify(t,t_norm)

        t = {'dd':-730.0, 'mm':0.0, 'ss':0.0}
        t_norm = {'dd': 350.0, 'mm': 0.0, 'ss': 0.0}
        verify(t,t_norm)

    def testToDegrees(self):
        """Must given decimal degrees of angle in DMS."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.DMS(**t).to_degrees(), t_norm)

        t = dict(dd=12.0, mm=10.0, ss=100.0)
        verify(t, t['dd']+(t['mm']/60.0)+(t['ss']/3600.0))
        
        t = dict(dd=-2.0, mm=-0.0, ss=-0.3)
        verify(t, t['dd']+(t['mm']/60.0)+(t['ss']/3600.0))


    def testToHours(self):
        """Must convert DMS into hours."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.DMS(**t).to_hours(), t_norm)

        def d(t):
            return (t['dd']+t['mm']/60.0+t['ss']/3600.0)/15.0
        
        t = dict(dd=12.0, mm=10.0, ss=100.0)
        verify(t, d(t))
            
        t = dict(dd=-2.0, mm=-0.0, ss=-0.3)
        verify(t, d(t))

    def testToRadians(self):
        """Must convert DMS into radians."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.DMS(**t).to_radians(), t_norm)

        def r(t):
            import math
            return (t['dd']+t['mm']/60.0+t['ss']/3600.0)*(math.pi/180.0)        

        t = dict(dd=12.0, mm=10.0, ss=100.0)
        verify(t, r(t))
            
        t = dict(dd=-2.0, mm=-0.0, ss=-0.3)
        verify(t, r(t))

        
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
        t = {'hh':1.0,'mm':1.0,'ss':1.34}
        hms = tpm.HMS(**t)
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
        
    def testAdditionNonHMS(self):
        """Must raise exception if addition involves non HMS value."""
        hms = tpm.HMS() # All zeros.
        def add_hms(hms,x):
            return hms + x
        self.assertRaises(TypeError, add_hms, hms, 1)

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

    def testSubtractNonHMS(self):
        """Must raise exception if subtraction involves non HMS value."""
        hms = tpm.HMS() # All zeros.
        def sub_hms(hms,x):
            return hms - x
        self.assertRaises(TypeError,sub_hms, hms, 1)

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

    def testToDMS(self):
        """Must return a tpm.DMS object with appropriate field values."""
        t = {'hh': 12.0, 'mm':30.0, 'ss': 0.0}
        t_dms = {'dd': 180.0, 'mm':450.0, 'ss':0.0 }
        hms = tpm.HMS(**t)
        dms = hms.to_dms()
        self.assertEqual(type(dms), tpm.DMS)
        self.assertEqual(dms.dd, t_dms['dd'])
        self.assertEqual(dms.mm, t_dms['mm']) 
        self.assertEqual(dms.ss, t_dms['ss'])

    def testNormalize(self):
        """Must properly normalize degrees, arc-minutes and arc-seconds."""
        # See tests/c_tests/hms2hms_test.c
        # Note:
        # h = (hms.dd) + (hms.mm/60.0) + (hms.ss/3600.0) i.e., each
        # must have its own
        # sign. But in string representation only the hours will have
        # sign. Normalization removes negative sign from mm and ss,
        # normalizes them into the range 0-60 and incorporates the
        # necessary change into the hours part. 
        def verify(t,t_norm):
            hms = tpm.HMS(**t)
            hms.normalize()
            self.assertAlmostEqual(hms.hh, t_norm['hh'])
            self.assertAlmostEqual(hms.mm, t_norm['mm'])
            self.assertAlmostEqual(hms.ss, t_norm['ss'])

        t = dict(hh=25.0, mm=0.0, ss=0.0)
        t_norm = dict(hh=25.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(hh=23.345, mm=0.0, ss=0.0)
        t_norm = dict(hh=23.0, mm=20.0, ss=42.0)
        verify(t, t_norm)

        t = dict(hh=6.0, mm=128.0, ss=2000.0)
        t_norm = dict(hh=8.0, mm=41.0, ss=20.0)
        verify(t, t_norm)

        t = dict(hh=-12.456, mm=0.0, ss=0.0)
        t_norm = dict(hh=-13.0, mm=32.0, ss=38.4)
        verify(t, t_norm)

        t = dict(hh=-25.0, mm=0.0, ss=0.0)
        t_norm = dict(hh=-25.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(hh=-1.0, mm=-1.0, ss=-1.0)
        t_norm = dict(hh=-2.0, mm=58.0, ss=59.0)
        verify(t, t_norm)

    def testToHours(self):
        """Must convert HMS into decimal hours."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.HMS(**t).to_hours(), t_norm)
                                   

        t = dict(hh=24.0, mm=0.0, ss=0.0)
        verify(t, t['hh']+(t['mm']/60.0)+(t['ss']/3600.0))

        t = dict(hh=-2.23456, mm=123456.78, ss=0.0)
        verify(t, t['hh']+(t['mm']/60.0)+(t['ss']/3600.0))

    def testToDegrees(self):
        """Must convert HMS into degrees."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.HMS(**t).to_degrees(), t_norm)

        def d(t):
            return (t['hh']+t['mm']/60.0+t['ss']/3600.0)*15.0 

        t = dict(hh=12.0, mm=10.0, ss=100.0)
        verify(t, d(t))
            
        t = dict(hh=-2.0, mm=-0.0, ss=-0.3)
        verify(t, d(t))
        
    def testToRadians(self):
        """Must convert HMS into radians."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.HMS(**t).to_radians(), t_norm)

        def r(t):
            import math
            return (t['hh']+t['mm']/60.0+t['ss']/3600.0)*15.0*(math.pi/180.0)        

        t = dict(hh=12.0, mm=10.0, ss=100.0)
        verify(t, r(t))
            
        t = dict(hh=-2.0, mm=-0.0, ss=-0.3)
        verify(t, r(t))

        
class TestYMDStructure(unittest.TestCase):
    def testCreate(self):
        """Must be able to create a YMD object."""
        ymd = tpm.YMD()
        self.assertEqual(type(ymd), tpm.YMD)

    def testGetFields(self):
        """Must be able to retrieve field values."""
        ymd = tpm.YMD()
        self.assertAlmostEqual(ymd.y, 2000)
        self.assertAlmostEqual(ymd.m, 1)
        self.assertAlmostEqual(ymd.dd, 0.0)
        self.assertAlmostEqual(ymd.hh, 0.0)
        self.assertAlmostEqual(ymd.mm, 0.0)
        self.assertAlmostEqual(ymd.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to initialize field values."""
        t = dict(y=2000, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        ymd = tpm.YMD(**t)
        self.assertAlmostEqual(ymd.y, t['y'])
        self.assertAlmostEqual(ymd.m, t['m'])
        self.assertAlmostEqual(ymd.dd, t['dd'])
        self.assertAlmostEqual(ymd.hh, t['hh'])
        self.assertAlmostEqual(ymd.mm, t['mm'])
        self.assertAlmostEqual(ymd.ss, t['ss'])

    def testSetFieldValues(self):
        """Must be able to set field values."""
        t = dict(y=2010, m=11, dd=19.34, hh=29.3, mm=1.345, ss=10.8)
        ymd = tpm.YMD()
        ymd.y = t['y']
        ymd.m = t['m']
        ymd.dd = t['dd']
        ymd.hh = t['hh']
        ymd.mm = t['mm']
        ymd.ss = t['ss']
        self.assertAlmostEqual(ymd.y, t['y'])
        self.assertAlmostEqual(ymd.m, t['m'])
        self.assertAlmostEqual(ymd.dd, t['dd'])
        self.assertAlmostEqual(ymd.hh, t['hh'])
        self.assertAlmostEqual(ymd.mm, t['mm'])
        self.assertAlmostEqual(ymd.ss, t['ss'])

    def testNonIntegerYearMonth(self):
        """Must raise exception for non-integer year and month."""
        ymd = tpm.YMD()
        def non_int(ymd,y,m):
            ymd.y = y
            ymd.m = m
        self.assertRaises(AssertionError, non_int, ymd, 1.0, 1.0)

    def testSubtract(self):
        """Must be able to subtract two YMD values."""
        t1 = dict(y=2000, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        t2 = dict(y=2010, m=11, dd=19.34, hh=29.3, mm=1.345, ss=10.8)
        ymd1 = tpm.YMD()
        ymd2 = tpm.YMD()
        ymd1.y = t1['y']
        ymd1.m = t1['m']
        ymd1.dd = t1['dd']
        ymd1.hh = t1['hh']
        ymd1.mm = t1['mm']
        ymd1.ss = t1['ss']
        ymd2.y = t2['y']
        ymd2.m = t2['m']
        ymd2.dd = t2['dd']
        ymd2.hh = t2['hh']
        ymd2.mm = t2['mm']
        ymd2.ss = t2['ss']
        ymd = ymd1 - ymd2
        self.assertAlmostEqual(ymd.y, t1['y'] - t2['y'])
        self.assertAlmostEqual(ymd.m, t1['m'] - t2['m'])
        self.assertAlmostEqual(ymd.dd, t1['dd'] - t2['dd'])
        self.assertAlmostEqual(ymd.hh, t1['hh'] - t2['hh'])
        self.assertAlmostEqual(ymd.mm, t1['mm'] - t2['mm'])
        self.assertAlmostEqual(ymd.ss, t1['ss'] - t2['ss'])

    def testSubtractNonYMD(self):
        """Must raise exception if subtraction involves non YMD value."""
        ymd = tpm.YMD() # All zeros.
        def sub_ymd(ymd,x):
            return ymd - x
        self.assertRaises(TypeError,sub_ymd, ymd, 1)
        
    def testUnicodeAndStr(self):
        """Must be able to get proper string represenations."""
        # The ouput strings were obtained from
        # pytpm/tests/c_tests/fmt_ymd_test.c
        t = dict(y=2010, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        t1 = dict(y=-1, m=10, dd=1.0, hh=23.9999, mm=54.0, ss=9.45)
        ymd = tpm.YMD()
        ymd.y = t['y']
        ymd.m = t['m']
        ymd.dd = t['dd']
        ymd.hh = t['hh']
        ymd.mm = t['mm']
        ymd.ss = t['ss']
        s = str(ymd)
        self.assertEqual(s, "Sun Oct 17 10:36:54.149 2010")
        s = unicode(ymd)
        self.assertEqual(s, u"Sun Oct 17 10:36:54.149 2010")
        ymd = tpm.YMD()
        ymd.y = t1['y']
        ymd.m = t1['m']
        ymd.dd = t1['dd']
        ymd.hh = t1['hh']
        ymd.mm = t1['mm']
        ymd.ss = t1['ss']
        s = str(ymd)
        self.assertEqual(s, "Sat Oct  2 00:54:09.090    2 BC")
        s = unicode(ymd)
        self.assertEqual(s, u"Sat Oct  2 00:54:09.090    2 BC")

    def testNormalize(self):
        """Must properly normalize a YMD value."""
        def verify(t, t_norm):
            ymd = tpm.YMD(**t)
            ymd.normalize()
            self.assertAlmostEqual(ymd.y, t_norm['y'])
            self.assertAlmostEqual(ymd.m, t_norm['m'])
            self.assertAlmostEqual(ymd.dd, t_norm['dd'])
            self.assertAlmostEqual(ymd.mm, t_norm['mm'])
            self.assertAlmostEqual(ymd.ss, t_norm['ss'])

        t = dict(y=2000, m=11, dd=366.0, hh=0.0, mm=0.0, ss=31536000.0)
        t_norm = dict(y=2002, m=11, dd=1.0, hh=0.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(y=2000, m=0, dd=0.0, hh=0.0, mm=0.0, ss=0.0)
        t_norm = dict(y=2000, m=11, dd=30.0, hh=0.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(y=2000, m=-3, dd=0.0, hh=0.0, mm=0.0, ss=0.0)
        t_norm = dict(y=2000, m=8, dd=31.0, hh=0.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(y=2000, m=1, dd=-365.0, hh=0.0, mm=0.0, ss=0.0)
        t_norm = dict(y=1998, m=12, dd=31.0, hh=0.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(y=2000, m=1, dd=1.0, hh=-24.0, mm=0.0, ss=0.0)
        t_norm = dict(y=1999, m=12, dd=31.0, hh=0.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        
    def testToJD(self):
        """Must convert to an equivalent JD."""
        def verify(t, t_norm):
            ymd = tpm.YMD(**t)
            jd = ymd.to_jd()
            self.assertAlmostEqual(jd.dd, t_norm['dd'])
            self.assertAlmostEqual(jd.hh, t_norm['hh'])
            self.assertAlmostEqual(jd.mm, t_norm['mm'])
            self.assertAlmostEqual(jd.ss, t_norm['ss'])

        # See pytpm/tests/c_tests/ymd2jd_test.c
        t = dict(y=1858,m=11,dd=17.0,hh=0.0,mm=0.0,ss=0.0)
        t_norm = dict(dd=2400001.0, hh=-12.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(y=1949,m=12,dd=31.923459,hh=0.0,mm=0.0,ss=0.0)
        t_norm = dict(dd=2433282.923459, hh=-12.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(y=2000,m=1,dd=1.5, hh=0.0,mm=0.0,ss=0.0)
        t_norm = dict(dd=2451545.5, hh=-12.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(y=1984,m=1,dd=1.0,hh=0.0,mm=0.0,ss=0.0)
        t_norm = dict(dd=2445701.0, hh=-12.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

    def testRawStr(self):
        """Proper 'raw' representation of YMD."""
        t = dict(y=2010, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        ymd = tpm.YMD(**t)
        self.assertEqual(ymd.raw_str(), "2010 10 16.789 15.654 1.345 9.45")

        t = dict(y=-1, m=10, dd=1.0, hh=23.9999, mm=54.0, ss=9.45)
        ymd = tpm.YMD(**t)
        self.assertEqual(ymd.raw_str(), "-1 10 1 23.9999 54 9.45")
        
    def testDOY(self):
        """Must convert YMD into day of the year."""
        def verify(t, t_norm):
            ymd = tpm.YMD(**t)
            self.assertAlmostEqual(ymd.doy(), t_norm)

        # See pytpm/tests/c_tests/ymd2dd_test.c
        t = dict(y=1858, m=11, dd=17.0, hh=0.0, mm=0.0, ss=0.0)
        verify(t, 321.0)

        t = dict(y=1949, m=12, dd=31.923459, hh=0.0, mm=0.0, ss=0.0)
        verify(t, 365.9234590)

        t = dict(y=2000, m=1, dd=1.5, hh=0.0, mm=0.0, ss=0.0)
        verify(t, 1.50)

        t = dict(y=1984, m=1, dd=1.0, hh=0.0, mm=0.0, ss=0.0)
        verify(t, 1.0)
        
    def testToY(self):
        """Must convert YMD into a year number."""
        def verify(t, t_norm):
            ymd = tpm.YMD(**t)
            self.assertAlmostEqual(ymd.to_year(), t_norm)

        # See pytpm/tests/c_tests/ymd2y_test.c.
        t = dict(y=1858, m=11.0, dd=17.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 1858.87945205)
        
        t = dict(y=1949, m=12, dd=31.923459,    hh =0.0, mm=0.0, ss=0.0)
        verify(t, 1950.00253002)
        
        t = dict(y=2000, m=1,  dd=1.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 2000.00273224)
        
        t = dict(y=1984, m=1,  dd=1.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 1984.00273224)
        
        t = dict(y=1984, m=1,  dd=0.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 1984.0)
        
        t = dict(y=1984, m=12, dd=31.0, hh =23.0, mm=59.0, ss=60.0)
        verify(t, 1985.00273973)
        
        t = dict(y=1985, m=1,  dd=1.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 1985.00273973)
        
        t = dict(y=1985, m=1,  dd=0.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 1985.0)
        
        t = dict(y=1985, m=12, dd=31.0, hh =23.0, mm=59.0, ss=60.0)
        verify(t, 1986.00273973)


        
class TestJDStructure(unittest.TestCase):
    def testCreate(self):
        """Must be able to create a JD object."""
        jd = tpm.JD()
        self.assertEqual(type(jd), tpm.JD)

    def testGetFields(self):
        """Must be able to retrieve values of fields."""
        jd = tpm.JD()
        self.assertEqual(jd.dd, 0.0)
        self.assertEqual(jd.hh, 0.0)
        self.assertEqual(jd.mm, 0.0)
        self.assertEqual(jd.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """Must be able to set fields of JD at initialization."""
        j = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        jd = tpm.JD(**j)
        self.assertEqual(jd.dd, j['dd'])
        self.assertEqual(jd.hh, j['hh'])
        self.assertEqual(jd.mm, j['mm'])
        self.assertEqual(jd.ss, j['ss'])

    def testSetFieldValues(self):
        """Must be able to set fields of a JD object."""
        j = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        jd = tpm.JD()
        jd.dd = j['dd']
        jd.hh = j['hh']
        jd.mm = j['mm']
        jd.ss = j['ss']
        self.assertEqual(jd.dd, j['dd'])
        self.assertEqual(jd.hh, j['hh'])
        self.assertEqual(jd.mm, j['mm'])
        self.assertEqual(jd.ss, j['ss'])

    def testAddition(self):
        """Must be able to add two JD values."""
        j1 = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        j2 = dict(dd=1.0, hh=2.3, mm=23.4, ss=2.0)
        jd1 = tpm.JD()
        jd1.dd = j1['dd']
        jd1.hh = j1['hh']
        jd1.mm = j1['mm']
        jd1.ss = j1['ss']
        jd2 = tpm.JD()
        jd2.dd = j2['dd']
        jd2.hh = j2['hh']
        jd2.mm = j2['mm']
        jd2.ss = j2['ss']
        jd = jd1 + jd2
        self.assertEqual(jd.dd, jd1.dd + jd2.dd)
        self.assertEqual(jd.hh, jd1.hh + jd2.hh)
        self.assertEqual(jd.mm, jd1.mm + jd2.mm)
        self.assertEqual(jd.ss, jd1.ss + jd2.ss)

    def testAddNonJD(self):
        """Must raise exception if subtraction involves non JD value."""
        jd = tpm.JD() # All zeros.
        def add_jd(jd,x):
            return jd - x
        self.assertRaises(TypeError,add_jd, jd, 1)
                        
    def testSubtraction(self):
        """Must be able to subtract two JD values."""
        j1 = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        j2 = dict(dd=1.0, hh=2.3, mm=23.4, ss=2.0)
        jd1 = tpm.JD()
        jd1.dd = j1['dd']
        jd1.hh = j1['hh']
        jd1.mm = j1['mm']
        jd1.ss = j1['ss']
        jd2 = tpm.JD()
        jd2.dd = j2['dd']
        jd2.hh = j2['hh']
        jd2.mm = j2['mm']
        jd2.ss = j2['ss']
        jd = jd1 - jd2
        self.assertEqual(jd.dd, jd1.dd - jd2.dd)
        self.assertEqual(jd.hh, jd1.hh - jd2.hh)
        self.assertEqual(jd.mm, jd1.mm - jd2.mm)
        self.assertEqual(jd.ss, jd1.ss - jd2.ss)

    def testSubtractNonJD(self):
        """Must raise exception if subtraction involves non JD value."""
        jd = tpm.JD() # All zeros.
        def sub_jd(jd,x):
            return jd - x
        self.assertRaises(TypeError,sub_jd, jd, 1)
    
    def testRepr(self):
        """Must give proper repr string."""
        j = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        jd = tpm.JD()
        jd.dd = j['dd']
        jd.hh = j['hh']
        jd.mm = j['mm']
        jd.ss = j['ss']
        self.assertEqual(j, eval(repr(jd)))

    def testUnicodeAndStr(self):
        """Must give proper string representations."""
        # Output strings used as checks are from the file pytpm/tests
        # /c_tests/fmt_jd_test.c.
        s1 = " 2451545  12H 00M 00.000S"
        s2 = " 2456745  15H 06M 50.515S"
        j1 = dict(dd=2451545.0, hh=12.0, mm=0.0, ss=0.0)
        j2 = dict(dd=2456745.2456, hh=9.0, mm=12.3446, ss=49.99999)
        jd1 = tpm.JD()
        jd2 = tpm.JD()
        jd1.dd = j1['dd']
        jd1.hh = j1['hh']
        jd1.mm = j1['mm']
        jd1.ss = j1['ss']
        jd2.dd = j2['dd']
        jd2.hh = j2['hh']
        jd2.mm = j2['mm']
        jd2.ss = j2['ss']

        self.assertEqual(str(jd1), s1)
        self.assertEqual(unicode(jd1), unicode(s1))
        self.assertEqual(str(jd2), s2)
        self.assertEqual(unicode(jd2), unicode(s2))

    def testNormalize(self):
        """Must properly normalize JD value."""
        def verify(t, t_norm):
            jd = tpm.JD(**t)
            jd.normalize()
            self.assertAlmostEqual(jd.dd, t_norm['dd']) 
            self.assertAlmostEqual(jd.hh, t_norm['hh']) 
            self.assertAlmostEqual(jd.mm, t_norm['mm']) 
            self.assertAlmostEqual(jd.ss, t_norm['ss'], 4) 

        # Why 59 and 60 ?
        t = dict(dd=2451545.0, hh=25.0, mm=0.0, ss=0.0)
        t_norm = dict(dd=2451546.0, hh=0.0, mm=59.0, ss=60.0)
        verify(t, t_norm)

        t = dict(dd=2451545.0, hh=-12.0, mm=0.0, ss=0.0)
        t_norm = dict(dd=2451544.0, hh=12.0000, mm=0.0, ss=0.0)
        verify(t, t_norm)

        t = dict(dd=2441230.0, hh=0.0, mm=12345678.0, ss=12345.0345)
        t_norm = dict(dd=2449803.0, hh=12.0000, mm=43.0, ss=45.0345)
        verify(t, t_norm)

    def testToYMD(self):
        """Must convert properly from JD to YMD."""
        def verify(t,t_norm):
            jd = tpm.JD(**t)
            ymd = jd.to_ymd()
            self.assertAlmostEqual(ymd.y, t_norm['y'])
            self.assertAlmostEqual(ymd.m, t_norm['m'])
            self.assertAlmostEqual(ymd.dd, t_norm['dd'])
            self.assertAlmostEqual(ymd.mm, t_norm['mm'])
            self.assertAlmostEqual(ymd.ss, t_norm['ss'])

        # See pytpm/tests/c_tests/jd2ymd_test.c.
        t = dict(dd=tpm.MJD_0, hh=0.0, mm=0.0, ss=0.0)
        t_norm = dict(y=1858,m=11,dd=17.0,hh=0.0,mm=0.0,ss=0.0)
        verify(t, t_norm)

        t = dict(dd=tpm.B1950, hh=0.0, mm=0.0, ss=0.0)
        t_norm = dict(y=1949,m=12,dd=31.923459,hh=0.0,mm=0.0,ss=0.0)
        verify(t, t_norm)

        t = dict(dd=tpm.J2000, hh=0.0, mm=0.0, ss=0.0)
        t_norm = dict(y=2000,m=1,dd=1.5, hh=0.0,mm=0.0,ss=0.0)
        verify(t, t_norm)

        t = dict(dd=tpm.J1984, hh=0.0, mm=0.0, ss=0.0)
        t_norm = dict(y=1984,m=1,dd=1.0,hh=0.0,mm=0.0,ss=0.0)
        verify(t, t_norm)

    def testToJ(self):
        """Must convert JD into equivalent Julian date."""
        def verify(t, t_norm):
            jd = tpm.JD(**t)
            self.assertAlmostEqual(jd.to_j(), t_norm)

        # See pytpm/tests/c_tests/jd2j_test.c.
        t = dict(dd=2451545.0, hh=10.0, mm=0.0, ss=0.0)
        verify(t, 2451545.41666667)

        t = dict(dd=2433142.678, hh=10.1230, mm=-10.3450, ss=1.0400)
        verify(t, 2433143.09261968)

    
if __name__ == '__main__':
    unittest.main()
