#-*- coding: utf-8 -*-
# Test various interfaces defined in the pytpm_times.pxi file.
import unittest
from pytpm import tpm

class TestDMSStructure(unittest.TestCase):
    """Test if the methods in the DMS class work."""
    def testCreate(self):
        """DMS() => create an DMS object."""
        dms = tpm.DMS()
        self.assertEqual(type(dms), tpm.DMS)
        
    def testGetFields(self):
        """DMS.x => Retrieve default values of fields."""
        dms = tpm.DMS()
        self.assertAlmostEqual(dms.dd, 0.0)
        self.assertAlmostEqual(dms.mm, 0.0)
        self.assertAlmostEqual(dms.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """DMS(**t) => set values to fields at creation."""
        
        def verify(t, t_norm):
            dms = tpm.DMS(**t)
            self.assertAlmostEqual(dms.dd, t_norm['dd']) 
            self.assertAlmostEqual(dms.mm, t_norm['mm']) 
            self.assertAlmostEqual(dms.ss, t_norm['ss']) 

        t={'dd':1.0,'mm':1.0,'ss':1.34}
        verify(t, t)

        # Check that initialization works with radians.
        import math
        t = dict(r=1.0)
        t_norm = dict(dd=180.0/math.pi, mm=0.0, ss=0.0)
        verify(t, t_norm)

        # Check that initialization works with hours.
        t = dict(h=12.5)
        t_norm = dict(dd=12.5*180.0/12.0, mm=0.0, ss=0.0)
        verify(t, t_norm)

    def testInvalidKeywordAtInit(self):
        """DMS(key=value) => raise TypeError if key is invalid."""
        self.assertRaises(TypeError, lambda: tpm.DMS(d=12.0))
        self.assertRaises(TypeError, lambda: tpm.DMS(radians=12.0))
        
    def testSetFieldValues(self):
        """DMS.x = val => set values after creation."""
        dms = tpm.DMS()
        dms.dd = 1.0
        dms.mm = 1.0
        dms.ss = 1.34
        self.assertAlmostEqual(dms.dd, 1.0)
        self.assertAlmostEqual(dms.mm, 1.0)
        self.assertAlmostEqual(dms.ss, 1.34)
        
    def testAddition(self):
        """DMS.__add__ => DMS + DMS."""
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
        """DMS + x => Exception when addition involves non DMS value."""
        dms = tpm.DMS() # All zeros.
        def add_dms(dms,x):
            return dms + x
        self.assertRaises(TypeError,add_dms, dms, 1)

    def testSubtraction(self):
        """DMS.__sub__ => DMS - DMS."""
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
        """DMS - x => exception when subtraction involves non DMS value."""
        dms = tpm.DMS() # All zeros.
        def sub_dms(dms,x):
            return dms - x
        self.assertRaises(TypeError,sub_dms, dms, 1)

    def testRepr(self):
        """DMS.__repr__ => dictionary as a string."""
        dms = tpm.DMS()
        dms.dd = 1.1
        dms.mm = 1.2
        dms.ss = 1.3
        d = eval(repr(dms))
        self.assertAlmostEqual(d['dd'], dms.dd) 
        self.assertAlmostEqual(d['mm'], dms.mm) 
        self.assertAlmostEqual(d['ss'], dms.ss) 
        
    def testUnicodeAndStr(self):
        """DMS.__str__ => string representation."""
        dms = tpm.DMS()
        dms.dd = 1.0
        dms.mm = 2.0
        dms.ss = 3.0
        self.assertEqual(str(dms), "+01D 02' 03.000\"")

    def testToHMS(self):
        """DMS.to_hms => DMS to HMS object."""
        t = {'dd': 180.0, 'mm':450.0, 'ss':0.0 }
        t_hms = {'hh': 12.0, 'mm':30.0, 'ss': 0.0}
        dms = tpm.DMS(**t)
        hms = dms.to_hms()
        self.assertEqual(type(hms), tpm.HMS)
        self.assertEqual(hms.hh, t_hms['hh'])
        self.assertEqual(hms.mm, t_hms['mm']) 
        self.assertEqual(hms.ss, t_hms['ss'])

    def testNormalize(self):
        """DMS.normalize() => normalize degrees, arc-minutes and arc-seconds."""
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
        """DMS.to_degrees() => decimal degrees of angle in DMS."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.DMS(**t).to_degrees(), t_norm)

        t = dict(dd=12.0, mm=10.0, ss=100.0)
        verify(t, t['dd']+(t['mm']/60.0)+(t['ss']/3600.0))
        
        t = dict(dd=-2.0, mm=-0.0, ss=-0.3)
        verify(t, t['dd']+(t['mm']/60.0)+(t['ss']/3600.0))

    def testToHours(self):
        """DMS.to_hours() => angle in DMS into hours."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.DMS(**t).to_hours(), t_norm)

        def d(t):
            return (t['dd']+t['mm']/60.0+t['ss']/3600.0)/15.0
        
        t = dict(dd=12.0, mm=10.0, ss=100.0)
        verify(t, d(t))
            
        t = dict(dd=-2.0, mm=-0.0, ss=-0.3)
        verify(t, d(t))

        # Verify that initializing with hours and convrting back gives
        # the same value.
        t = dict(h=12.5)
        verify(t, t['h'])

    def testToRadians(self):
        """DMS.to_radians() => angle in DMS into radians."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.DMS(**t).to_radians(), t_norm)

        def r(t):
            import math
            return (t['dd']+t['mm']/60.0+t['ss']/3600.0)*(math.pi/180.0)        

        t = dict(dd=12.0, mm=10.0, ss=100.0)
        verify(t, r(t))
            
        t = dict(dd=-2.0, mm=-0.0, ss=-0.3)
        verify(t, r(t))

        # Verify that initializing with radians and converting back
        # gives the same answer.
        t = dict(r=1.0)
        verify(t, t['r'])


class TestHMSStructure(unittest.TestCase):
    """Test if the methods in the HMS class work."""
    def testCreate(self):
        """HMS() => create an HMS object."""
        hms = tpm.HMS()
        self.assertEqual(type(hms), tpm.HMS)
        
    def testGetFields(self):
        """HMS.x => retrieve values of fields."""
        hms = tpm.HMS()
        self.assertAlmostEqual(hms.hh, 0.0)
        self.assertAlmostEqual(hms.mm, 0.0)
        self.assertAlmostEqual(hms.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """HMS(**vals) => set values to fields at creation."""
        import math
        def verify(t, t_norm):
            hms = tpm.HMS(**t)
            self.assertAlmostEqual(hms.hh, t_norm['hh'])
            self.assertAlmostEqual(hms.mm, t_norm['mm'])
            self.assertAlmostEqual(hms.ss, t_norm['ss'])

        t = {'hh':1.0,'mm':1.0,'ss':1.34}
        verify(t, t)

        # See if initializing with radians work.
        t = dict(r=1.0)
        t_norm = dict(hh= 12/math.pi, mm=0.0, ss=0.0)
        verify(t, t_norm)

        # See if initializing with degrees work.
        t = dict(dd=12.5)
        t_norm = dict(hh=12.5*(12/180.0), mm=0.0, ss=0.0)
        verify(t, t_norm)
        
    def testSetFieldValues(self):
        """DMS.x => set values after creation."""
        hms = tpm.HMS()
        hms.hh = 1.0
        hms.mm = 1.0
        hms.ss = 1.34
        self.assertAlmostEqual(hms.hh, 1.0)
        self.assertAlmostEqual(hms.mm, 1.0)
        self.assertAlmostEqual(hms.ss, 1.34)
        
    def testInvalidKeywordAtInit(self):
        """HMS(key=value) => raise TypeError if key is invalid."""
        self.assertRaises(TypeError, lambda: tpm.HMS(h=12.0))
        self.assertRaises(TypeError, lambda: tpm.HMS(hours=12.0))

    def testAddition(self):
        """HMS.__add__ => HMS + HMS."""
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
        """HMS + x => Exception when addition involves non HMS value."""
        hms = tpm.HMS() # All zeros.
        def add_hms(hms,x):
            return hms + x
        self.assertRaises(TypeError, add_hms, hms, 1)

    def testSubtraction(self):
        """HMS.__sub__ => HMS - HMS."""
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
        """HMS - x => Exception if subtraction involves non HMS value."""
        hms = tpm.HMS() # All zeros.
        def sub_hms(hms,x):
            return hms - x
        self.assertRaises(TypeError,sub_hms, hms, 1)

    def testRepr(self):
        """HMS.__repr__ => dictionary as a string."""
        hms = tpm.HMS()
        hms.hh = 1.1
        hms.mm = 1.2
        hms.ss = 1.3
        h = eval(repr(hms))
        self.assertAlmostEqual(h['hh'], hms.hh) 
        self.assertAlmostEqual(h['mm'], hms.mm) 
        self.assertAlmostEqual(h['ss'], hms.ss) 
        
    def testUnicodeAndStr(self):
        """HMS.__str__ => string representation."""
        hms = tpm.HMS()
        hms.hh = 1.0
        hms.mm = 2.0
        hms.ss = 3.0
        self.assertEqual(str(hms)," 01H 02M 03.000S")

    def testToDMS(self):
        """HMS.to_dms() => HMS to DMS."""
        t = {'hh': 12.0, 'mm':30.0, 'ss': 0.0}
        t_dms = {'dd': 180.0, 'mm':450.0, 'ss':0.0 }
        hms = tpm.HMS(**t)
        dms = hms.to_dms()
        self.assertEqual(type(dms), tpm.DMS)
        self.assertEqual(dms.dd, t_dms['dd'])
        self.assertEqual(dms.mm, t_dms['mm']) 
        self.assertEqual(dms.ss, t_dms['ss'])

    def testNormalize(self):
        """HMS.normalize => normalize hours, minutes and seconds."""
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
        """HMS.to_hours() => HMS into decimal hours."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.HMS(**t).to_hours(), t_norm)
                                   
        t = dict(hh=24.0, mm=0.0, ss=0.0)
        verify(t, t['hh']+(t['mm']/60.0)+(t['ss']/3600.0))

        t = dict(hh=-2.23456, mm=123456.78, ss=0.0)
        verify(t, t['hh']+(t['mm']/60.0)+(t['ss']/3600.0))

    def testToDegrees(self):
        """HMS.to_degrees() => HMS into degrees."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.HMS(**t).to_degrees(), t_norm)

        def d(t):
            return (t['hh']+t['mm']/60.0+t['ss']/3600.0)*15.0 

        t = dict(hh=12.0, mm=10.0, ss=100.0)
        verify(t, d(t))
            
        t = dict(hh=-2.0, mm=-0.0, ss=-0.3)
        verify(t, d(t))

        # Verify that initializing with degrees and then converting
        # back gives the same answer.
        t = dict(dd=12.5)
        verify(t, t['dd'])
        
    def testToRadians(self):
        """HMS.to_radians() => HMS into radians."""
        def verify(t, t_norm):
            self.assertAlmostEqual(tpm.HMS(**t).to_radians(), t_norm)

        def r(t):
            import math
            return (t['hh']+t['mm']/60.0+t['ss']/3600.0)*15.0*(math.pi/180.0)        

        t = dict(hh=12.0, mm=10.0, ss=100.0)
        verify(t, r(t))
            
        t = dict(hh=-2.0, mm=-0.0, ss=-0.3)
        verify(t, r(t))

        # Verify the initializing with radians and then converting back
        # gives the same answer.
        t = dict(r=1.0)
        verify(t, t['r'])
        

class TestYMDStructure(unittest.TestCase):
    def testCreate(self):
        """YMD() => create YMD object."""
        ymd = tpm.YMD()
        self.assertEqual(type(ymd), tpm.YMD)

    def testGetFields(self):
        """YMD.x => retrieve field values."""
        ymd = tpm.YMD()
        self.assertAlmostEqual(ymd.y, 2000)
        self.assertAlmostEqual(ymd.m, 1)
        self.assertAlmostEqual(ymd.dd, 0.0)
        self.assertAlmostEqual(ymd.hh, 0.0)
        self.assertAlmostEqual(ymd.mm, 0.0)
        self.assertAlmostEqual(ymd.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """YMD(**vals) => initialize field values."""
        def verify(t, t_norm):
            ymd = tpm.YMD(**t)
            self.assertAlmostEqual(ymd.y, t_norm['y'])
            self.assertAlmostEqual(ymd.m, t_norm['m'])
            self.assertAlmostEqual(ymd.dd, t_norm['dd'])
            self.assertAlmostEqual(ymd.hh, t_norm['hh'])
            self.assertAlmostEqual(ymd.mm, t_norm['mm'])
            self.assertAlmostEqual(ymd.ss, t_norm['ss'])
            
        t = dict(y=2000, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        verify(t, t)

        # For initialization with year see
        # pytpm/tests/c_tests/y2ymd_test.c
        t_norm = dict(y=1858, m=1, dd=321.0, hh =0.0, mm=0.0, ss=0.0)
        verify(dict(year=1858.879452054794), t_norm)
        
        t_norm = dict(y=1950, m=1, dd=0.923459,    hh =0.0, mm=0.0, ss=0.0)
        verify(dict(year=1950.002530024794), t_norm)

        # For initialization with Julian date.
        t_norm = dict(y=1949, m=12, dd=31.923459,    hh =0.0, mm=0.0, ss=0.0)
        verify(dict(j=2433282.42345900), t_norm)
        
        t_norm = dict(y=2000, m=1,  dd=1.0, hh =0.0, mm=0.0, ss=0.0)
        verify(dict(j=2451544.5), t_norm)

        # Check to see if initialization with year and day number gives
        # correct results.
        # See pytpm/tests/c_tests/ydd2ymd_test.c.
        t_norm = dict(y=2000, m=1, dd=1.5, hh=0.0, mm=0.0, ss=0.0)
        verify(dict(ydd=(2000, 1.5)), t_norm)
        
        t_norm = dict(y=1858, m=1, dd=321.0, hh=0.0, mm=0.0, ss=0.0)
        verify(dict(ydd=(1858, 321.0)), t_norm)

        t_norm = dict(y=1949, m=1, dd=365.923459, hh=0.0, mm=0.0, ss=0.0)
        verify(dict(ydd=(1949, 365.9234590)), t_norm)

        # Verify that using non-integer year and month raises
        # AssertionError. 
        self.assertRaises(AssertionError, lambda: tpm.YMD(y=2000.12))
        self.assertRaises(AssertionError, lambda: tpm.YMD(m=12.0))
        
        
    def testSetFieldValues(self):
        """YMD.x => set field values."""
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

    def testInvalidKeywordAtInit(self):
        """YMD(key=value) => raise TypeError if key is invalid."""
        self.assertRaises(TypeError, lambda: tpm.YMD(h=12.0))
        self.assertRaises(TypeError, lambda: tpm.YMD(years=12.0))

    def testNonIntegerYearMonth(self):
        """YMD.x => Exception for non-integer year and month."""
        ymd = tpm.YMD()
        def non_int(ymd,y,m):
            ymd.y = y
            ymd.m = m
        self.assertRaises(AssertionError, non_int, ymd, 1.0, 1.0)

    def testSubtract(self):
        """YMD.__sub__ => YMD - YMD."""
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
        """YMD - x => Exception if subtraction involves non YMD value."""
        ymd = tpm.YMD() # All zeros.
        def sub_ymd(ymd,x):
            return ymd - x
        self.assertRaises(TypeError,sub_ymd, ymd, 1)
        
    def testUnicodeAndStr(self):
        """YMD.__str__ => string representations."""
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
        ymd = tpm.YMD()
        ymd.y = t1['y']
        ymd.m = t1['m']
        ymd.dd = t1['dd']
        ymd.hh = t1['hh']
        ymd.mm = t1['mm']
        ymd.ss = t1['ss']
        s = str(ymd)
        self.assertEqual(s, "Sat Oct  2 00:54:09.090    2 BC")

    def testNormalize(self):
        """YMD.normalize() => normalize a YMD value."""
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
        """YMD.to_jd() => convert YMD to an equivalent JD."""
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
        """ymd.raw_str() => 'raw' representation of YMD."""
        t = dict(y=2010, m=10, dd=16.789, hh=15.654, mm=1.345, ss=9.45)
        ymd = tpm.YMD(**t)
        self.assertEqual(ymd.raw_str(), "2010 10 16.789 15.654 1.345 9.45")

        t = dict(y=-1, m=10, dd=1.0, hh=23.9999, mm=54.0, ss=9.45)
        ymd = tpm.YMD(**t)
        self.assertEqual(ymd.raw_str(), "-1 10 1 23.9999 54 9.45")
        
    def testDOY(self):
        """YMD.doy() => day of the year, for the YMD."""
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

        # See if initializing with year and day of year and then
        # calculating day of year gives the same value.
        t = dict(ydd=(2000, 321.9))
        verify(t, 321.9)
        
    def testToYear(self):
        """YMD.to_year() => YMD into a year number."""
        def verify(t, t_norm):
            ymd = tpm.YMD(**t)
            self.assertAlmostEqual(ymd.to_year(), t_norm)

        # See pytpm/tests/c_tests/ymd2y_test.c.
        t = dict(y=1858, m=11, dd=17.0, hh =0.0, mm=0.0, ss=0.0)
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

        # To and from year; this test was added after the
        # initialization with "year=value" was defined.
        self.assertAlmostEqual(tpm.YMD(year= 1986.00273973).to_year(),
                               1986.00273973)

    def testToJ(self):
        """YMD.to_j() => Convert YMD into a scalar Julian date."""
        def verify(t, t_norm):
            ymd = tpm.YMD(**t)
            self.assertAlmostEqual(ymd.to_j(), t_norm)

        # See pytpm/tests/c_tests/ymd2j_test.c.
        t = dict(y=1858, m=11, dd=17.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 2400000.5)
        
        t = dict(y=1949, m=12, dd=31.923459,    hh =0.0, mm=0.0, ss=0.0)
        verify(t, 2433282.42345900)
        
        t = dict(y=2000, m=1,  dd=1.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 2451544.5)
        
        t = dict(y=1984, m=1,  dd=1.0, hh =0.0, mm=0.0, ss=0.0)
        verify(t, 2445700.5)
        
        t = dict(y=1985, m=12,  dd=31.0, hh =23.0, mm=59.0, ss=60.0)
        verify(t, 2446431.50)
        
        # Check if YMD initialized with Julian date gives back the
        # Julian date; added after initialization was set to accept a
        # Julian date.
        self.assertAlmostEqual(tpm.YMD(j=2433282.42345900).to_j(),
                               2433282.42345900)
        

class TestJDStructure(unittest.TestCase):
    def testCreate(self):
        """JD() => create a JD object."""
        jd = tpm.JD()
        self.assertEqual(type(jd), tpm.JD)

    def testGetFields(self):
        """JD.x => retrieve values of fields."""
        jd = tpm.JD()
        self.assertEqual(jd.dd, 0.0)
        self.assertEqual(jd.hh, 0.0)
        self.assertEqual(jd.mm, 0.0)
        self.assertEqual(jd.ss, 0.0)

    def testSetFieldValuesAtInit(self):
        """JD(**vals) => set fields of JD at initialization."""
        def verify(t, t_norm):
             jd = tpm.JD(**t)
             self.assertEqual(jd.dd, t_norm['dd'])
             self.assertEqual(jd.hh, t_norm['hh'])
             self.assertEqual(jd.mm, t_norm['mm'])
             self.assertEqual(jd.ss, t_norm['ss'])

        t = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        verify(t, t)

        # Verify if passing a Julian date will result in proper
        # initialization.
        t = dict(j=2451545.0)
        verify(t, dict(dd=t['j'], hh=0.0, mm=0.0, ss=0.0))

        # Verify that a year passed at initialization will result in
        # proper initialization.
        t = dict(year=2000.004098360656)
        verify(t, dict(dd=2451545.5,hh=-12.0, mm=0.0, ss=0.0))
        
    def testSetFieldValues(self):
        """JD.x = val => Set fields of a JD object."""
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

    def testInvalidKeywordAtInit(self):
        """JD(key=value) => raise TypeError if key is invalid."""
        self.assertRaises(TypeError, lambda: tpm.JD(h=12.0))
        self.assertRaises(TypeError, lambda: tpm.JD(hours=12.0))

    def testAddition(self):
        """JD.__add__ => JD + JD."""
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
        """JD + x => Exception if addition involves non JD value."""
        jd = tpm.JD() # All zeros.
        def add_jd(jd,x):
            return jd - x
        self.assertRaises(TypeError,add_jd, jd, 1)
                        
    def testSubtraction(self):
        """JD.__sub__ => JD - JD."""
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
        """JD - x => Exception if subtraction involves non JD value."""
        jd = tpm.JD() # All zeros.
        def sub_jd(jd,x):
            return jd - x
        self.assertRaises(TypeError,sub_jd, jd, 1)
    
    def testRepr(self):
        """JD__repr__ => dictionary as a string."""
        j = dict(dd=2451445.0, hh=12.0, mm=0.0, ss=0.0)
        jd = tpm.JD()
        jd.dd = j['dd']
        jd.hh = j['hh']
        jd.mm = j['mm']
        jd.ss = j['ss']
        self.assertEqual(j, eval(repr(jd)))

    def testUnicodeAndStr(self):
        """JD.__str__ => string representations."""
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
        self.assertEqual(str(jd2), s2)

    def testNormalize(self):
        """JD.normalize() => normalize JD value."""
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
        """JD.to_ymd() => convert JD to YMD."""
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
        """JD.to_J() => convert JD into equivalent Julian date."""
        def verify(t, t_norm):
            jd = tpm.JD(**t)
            self.assertAlmostEqual(jd.to_j(), t_norm)

        # See pytpm/tests/c_tests/jd2j_test.c.
        t = dict(dd=2451545.0, hh=10.0, mm=0.0, ss=0.0)
        verify(t, 2451545.41666667)

        t = dict(dd=2433142.678, hh=10.1230, mm=-10.3450, ss=1.0400)
        verify(t, 2433143.09261968)

        # See if initializing with j=value and then calculating to_j
        # will give the same result.
        t = dict(j= 2451545.123456)
        verify(t, t['j'])
        
    def testToYear(self):
        """JD.to_year() => convert JD into equivalent year (Gregorian calendar)."""
        def verify(t, t_norm):
            jd = tpm.JD(**t)
            self.assertAlmostEqual(jd.to_year(), t_norm)

        # See pytpm/tests/c_tests/jd2y_test.c.
        t = dict(dd=2451545.0, hh=10.0, mm=0.0, ss=0.0)
        verify(t, 2000.00523679)

        t = dict(dd=2433142.678, hh=10.1230, mm=-10.3450, ss=1.0400)
        verify(t, 1949.62080170)

        # See that initializing with a year and hen converting back
        # into a year gives the same value.
        t = dict(year=2000.004098360656)
        verify(t, t['year'])


class TestScalarValueConversions(unittest.TestCase):
    """Test conversions between scalar values."""
    def testD2D(self):
        """tpm.d2d() => normalize degrees."""
        # See pytpm/tests/c_tests/d2d_test.c.
        self.assertAlmostEqual(tpm.d2d(0.0), 0.0)
        self.assertAlmostEqual(tpm.d2d(-0.0), -0.0)
        self.assertAlmostEqual(tpm.d2d(360.0), 0.0)
        self.assertAlmostEqual(tpm.d2d(-360.0), 0.0)
        self.assertAlmostEqual(tpm.d2d(12.3), 12.3)
        self.assertAlmostEqual(tpm.d2d(-12.3), -12.3)
        self.assertAlmostEqual(tpm.d2d(361),   1.0)
        self.assertAlmostEqual(tpm.d2d(-361.0),359.0)
        self.assertAlmostEqual(tpm.d2d(710.0), 350.0)
        self.assertAlmostEqual(tpm.d2d(-710.0),10.0)
        self.assertAlmostEqual(tpm.d2d(730.0), 10.0)
        self.assertAlmostEqual(tpm.d2d(-730.0),350.0)

    def testH2H(self):
        """tpm.h2h() => normalize hours."""
        # See pytpm/tests/c_tests/h2h_test.c.
        self.assertAlmostEqual(tpm.h2h(  0.0000),   0.0000)
        self.assertAlmostEqual(tpm.h2h( -0.0000),  -0.0000) 
        self.assertAlmostEqual(tpm.h2h( 13.4500),  13.4500) 
        self.assertAlmostEqual(tpm.h2h(-13.4500),  10.5500) 
        self.assertAlmostEqual(tpm.h2h( 24.0000),   0.0000) 
        self.assertAlmostEqual(tpm.h2h(-24.0000),   0.0000) 
        self.assertAlmostEqual(tpm.h2h( 25.0000),   1.0000) 
        self.assertAlmostEqual(tpm.h2h(-25.0000),  23.0000) 
        self.assertAlmostEqual(tpm.h2h( 50.0000),   2.0000) 
        self.assertAlmostEqual(tpm.h2h(-50.0000),  22.0000) 
        self.assertAlmostEqual(tpm.h2h( 64.1230),  16.1230) 
        self.assertAlmostEqual(tpm.h2h(-64.1230),   7.8770) 

    def testR2R(self):
        """tpm.r2r() => properly normalize radians."""
        import math
        self.assertAlmostEqual(tpm.r2r(  0.00000000),   0.00000000) 
        self.assertAlmostEqual(tpm.r2r( -0.00000000),  -0.00000000) 
        self.assertAlmostEqual(tpm.r2r(  math.pi/2.0),   1.57079633) 
        self.assertAlmostEqual(tpm.r2r( -math.pi/2.0),   4.71238898) 
        self.assertAlmostEqual(tpm.r2r(  2*math.pi),   0.00000000) 
        self.assertAlmostEqual(tpm.r2r( -2*math.pi),   0.00000000) 
        self.assertAlmostEqual(tpm.r2r( -3*math.pi),   3.14159265) 
        self.assertAlmostEqual(tpm.r2r(  3*math.pi),   3.14159265) 
        self.assertAlmostEqual(tpm.r2r( 4*math.pi),   0.00000000) 
        self.assertAlmostEqual(tpm.r2r(-4*math.pi),   0.00000000) 
        self.assertAlmostEqual(tpm.r2r( 4.2*math.pi),   0.62831853) 
        self.assertAlmostEqual(tpm.r2r(-4.2*math.pi),   5.65486678) 

    def testD2H(self):
        """"tpm.d2h() => convert degrees into hours."""
        self.assertAlmostEqual(tpm.d2h(180.0), 12.0)
        self.assertAlmostEqual(tpm.d2h(-180.0), -12.0)
        self.assertAlmostEqual(tpm.d2h(360.0), 24.0)
        self.assertAlmostEqual(tpm.d2h(-360.0), -24.0)
        self.assertAlmostEqual(tpm.d2h(720.0), 48.0)

    def testH2D(self):
        """tpm.h2d() => convert hours into degrees."""
        self.assertAlmostEqual(tpm.h2d(12.0), 180.0)
        self.assertAlmostEqual(tpm.h2d(-12.0), -180.0)
        self.assertAlmostEqual(tpm.h2d(24.0), 360.0)
        self.assertAlmostEqual(tpm.h2d(-24.0), -360.0)
        self.assertAlmostEqual(tpm.h2d(48.0), 720.0)
        self.assertAlmostEqual(tpm.h2d(-48.0), -720.0)
        self.assertAlmostEqual(tpm.h2d(12.5), 180.0+7.5)
        
    def testD2R(self):
        """tpm.d2r() => convert degrees into radians."""
        import math
        self.assertAlmostEqual(tpm.d2r(180.0), math.pi)
        self.assertAlmostEqual(tpm.d2r(360.0), 2*math.pi)
        self.assertAlmostEqual(tpm.d2r(-360.0), -2*math.pi)
        self.assertAlmostEqual(tpm.d2r(720.0), 4*math.pi)
        self.assertAlmostEqual(tpm.d2r(-720.0), -4*math.pi)

    def testR2D(self):
       """tpm.r2d() => convert radians into degrees."""
       import math
       self.assertAlmostEqual(tpm.r2d(math.pi), 180.0)
       self.assertAlmostEqual(tpm.r2d(4*math.pi), 720.0)
       self.assertAlmostEqual(tpm.r2d(-4*math.pi), -720.0)
       self.assertAlmostEqual(tpm.r2d(-2.5*math.pi), -450.0)
       
    def testH2R(self):
        """tpm.h2r() => convert hours into radians."""
        import math
        self.assertAlmostEqual(tpm.h2r(12.0), math.pi)
        self.assertAlmostEqual(tpm.h2r(24.0), 2*math.pi)
        self.assertAlmostEqual(tpm.h2r(-12.5), -(12.5/12.0)*math.pi)

    def testR2H(self):
        """tpm.r2h() => convert radians into hours."""
        import math
        self.assertAlmostEqual(tpm.r2h(math.pi), 12.0)
        self.assertAlmostEqual(tpm.r2h(2*math.pi), 24.0)
        self.assertAlmostEqual(tpm.r2h(-(12.5/12.0)*math.pi), -12.5)
        
    def testD2AS(self):
        """tpm.d2as() => convert degrees into arcseconds."""
        self.assertAlmostEqual(tpm.d2as(1.0), 3600.0)
        self.assertAlmostEqual(tpm.d2as(-12.45), -12.45*3600.0)
        
    def testAS2D(self):
        """tpm.as2d() => convert arcseconds into degrees."""
        self.assertAlmostEqual(tpm.as2d(3600.0), 1.0)
        self.assertAlmostEqual(tpm.as2d(-12.45*3600.0), -12.45)

    def testAS2H(self):
        """tpm.as2h() => convert arcseconds into hours."""
        self.assertAlmostEqual(tpm.as2h(3600.0), 1/15.0)
        self.assertAlmostEqual(tpm.as2h(-12.45*3600), -12.45/15.0)

    def testH2AS(self):
        """tpm.h2as() => convert hours into arcseconds."""
        self.assertAlmostEqual(tpm.h2as(1/15.0), 3600.0)
        self.assertAlmostEqual(tpm.h2as(-12.45/15.0), -12.45*3600.0)

    def testR2AS(self):
        """tpm.r2as() => convert radians into arcseconds."""
        import math
        self.assertAlmostEqual(tpm.r2as(math.pi), 180.0*3600.0)
        self.assertAlmostEqual(tpm.r2as(-math.pi), -180.0*3600.0)

    def testAS2R(self):
        """tpm.as2r() => convert arcseconds into radians."""
        import math
        self.assertAlmostEqual(tpm.as2r(180.0*3600), math.pi)
        self.assertAlmostEqual(tpm.as2r(-180.0*3600), -math.pi)


class TestFormattedStringFunction(unittest.TestCase):
    """Test all functions that return formatted string."""
    def testFmtAlpha(self):
        """tpm.fmt_alpha() => radians into right ascension string."""
        self.assertEqual(tpm.fmt_alpha(tpm.M_PI/3.0), " 03H 59M 59.999S")
        self.assertEqual(tpm.fmt_alpha(tpm.M_PI*1.234), " 14H 48M 28.799S")

    def testFmtD(self):
        """tpm.fmt_d() => a formatted string of the angle in radians."""
        self.assertEqual(tpm.fmt_d(180.0), "+180D 00\' 00.000\"")
        self.assertEqual(tpm.fmt_d(45.12345), "+45D 07\' 24.419\"")

    def testFmtDelta(self):
        """tpm.fmt_delta() => convert radians into declination string."""
        self.assertEqual(tpm.fmt_delta(tpm.M_PI), "+00D 00\' 00.000\"")
        self.assertEqual(tpm.fmt_delta(tpm.M_PI/2.0), "+90D 00\' 00.000\"")
        self.assertEqual(tpm.fmt_delta(tpm.M_PI*1.2345), "-42D 12\' 35.999\"")

    def testFmtH(self):
        """tpm.fmt_h() => convert hours into a formatted string."""
        self.assertEqual(tpm.fmt_h(12.0), " 12H 00M 00.000S")
        self.assertEqual(tpm.fmt_h(36.12345), " 36H 07M 24.419S")

    def testFmtJ(self):
        """tpm.fmt_j() => convert Julian date into a formatted string."""
        self.assertEqual(tpm.fmt_j(2451545.0), " 2451545  00H 00M 00.000S")
        self.assertEqual(tpm.fmt_j(1111111.1234), " 1111111  02H 57M 41.759S")

    def testFmtR(self):
        """tpm.fmt_r() => radians into degrees, as a formatted string."""
        self.assertEqual(tpm.fmt_r(1.230000), "+70D 28' 25.711\"")
        self.assertEqual(tpm.fmt_r(-1.230000), "-70D 28' 25.711\"")

    def testFmtY(self):
        """tpm.fmt_y() => year with fractional part into a formatted string."""
        self.assertEqual(tpm.fmt_y(2000.000000), "Fri Dec 31 00:00:00.000 1999") 
        self.assertEqual(tpm.fmt_y(1984.000000), "Sat Dec 31 00:00:00.000 1983") 
        self.assertEqual(tpm.fmt_y(1950.000000), "Sat Dec 31 00:00:00.000 1949") 


class TestYearJulianDateConversion(unittest.TestCase):
    """Test the functions for convertion years into Julian dates."""
    def testJ2Y(self):
        """tpm.j2y() => scalar Julian date into a year number."""
        # See pytpm/tests/c_test/j2y_test.c
        self.assertAlmostEqual(tpm.j2y(2400000.5), 1858.879452054794, 12)
        self.assertAlmostEqual(tpm.j2y(2433282.42345905), 1950.002530024794, 12)
        self.assertAlmostEqual(tpm.j2y(2451545.0), 2000.004098360656, 12)
        self.assertAlmostEqual(tpm.j2y(2445700.5), 1984.002732240437, 12)

    def testY2J(self):
        """tpm.y2j() => year number into a scalar Julian date."""
        # This is just the inverse of testJ2Y.
        self.assertAlmostEqual(2400000.5, tpm.y2j(1858.879452054794), 12)
        self.assertAlmostEqual(2433282.42345905, tpm.y2j(1950.002530024794), 12)
        self.assertAlmostEqual(2451545.0, tpm.y2j(2000.004098360656), 12)
        self.assertAlmostEqual(2445700.5, tpm.y2j(1984.002732240437), 12)

    def testByear2jd(self):
        """tpm.byear2jd() => convert Besselian year into Julian date."""
        self.assertAlmostEqual(tpm.byear2jd(1950.0), tpm.B1950)
        
    def testJd2byear(self):
        """tpm.jd2byear() => convert Julian date into Besselian year."""
        self.assertAlmostEqual(tpm.jd2byear(tpm.B1950), 1950.0)
        
    def testJyear2Jd(self):
        """tpm.jyear2jd() => convert Julian year into Julian date."""
        self.assertAlmostEqual(tpm.jyear2jd(2000.0), tpm.J2000)
                
    def testJd2Jyear(self):
        """tpm.jd2jyear() => convert Julian date into Julian year."""
        self.assertAlmostEqual(tpm.jd2jyear(tpm.J2000), 2000.0)


class CurrentTime(unittest.TestCase):
    """Test the jd_now and utc_now functions."""
    def testUTCNow(self):
        """tpm.utc_now() => the current Julian date; nearest second."""
        from datetime import datetime
        j = tpm.utc_now()
        d = datetime.utcnow()
        ymd = tpm.YMD(j=j)
        ymd.normalize()
        self.assertAlmostEqual(ymd.y, d.year)
        self.assertAlmostEqual(ymd.m, d.month)
        self.assertAlmostEqual(ymd.dd, d.day)
        self.assertAlmostEqual(ymd.hh, d.hour)
        self.assertAlmostEqual(ymd.mm, d.minute)
        self.assertAlmostEqual(ymd.ss, d.second, 1)

    def testJDNow(self):
        """tpm.jd_now() => return the current Julian date as a JD."""
        from datetime import datetime
        j = tpm.jd_now()
        d = datetime.utcnow()
        ymd = j.to_ymd()
        ymd.normalize()
        self.assertAlmostEqual(ymd.y, d.year)
        self.assertAlmostEqual(ymd.m, d.month)
        self.assertAlmostEqual(ymd.dd, d.day)
        self.assertAlmostEqual(ymd.hh, d.hour)
        self.assertAlmostEqual(ymd.mm, d.minute)
        self.assertAlmostEqual(ymd.ss, d.second, 1)


class CalendarCalculations(unittest.TestCase):
    """Test calendar calculation functions."""
    def testJ2DOW(self):
        """tpm.j2dow() => day of the week for the Julian date."""
        self.assertEqual(tpm.j2dow(tpm.J2000), 6)
        self.assertEqual(tpm.j2dow(tpm.YMD(y=2010,m=11,dd=13).to_j()), 6)
        self.assertEqual(tpm.j2dow(tpm.YMD(y=2010,m=11,dd=12).to_j()), 5)

    def testY2DOY(self):
        """tpm.y2doy() => number of days in the Gregorian year."""
        self.assertEqual(tpm.y2doy(2000), 366)
        self.assertEqual(tpm.y2doy(1900), 365)

    def testJ2Gcal(self):
        """tpm.j2gcal() => Gregorian calendar date for given Julian date"""
        def verify(t, t_norm):
            g = tpm.j2gcal(t)
            self.assertEqual(g['y'], t_norm['y'])
            self.assertEqual(g['m'], t_norm['m'])
            self.assertEqual(g['dd'], t_norm['dd'])

        verify(tpm.J2000, dict(y=2000, m=1, dd=1))
        verify(2400000.5, dict(y=1858, m=11, dd=17))
        verify(2446431.50, dict(y=1986, m=1, dd=1))
        
    def testJ2Jcal(self):
        """tpm.j2jcal() => Julian calendar date for the given Julian date"""
        def verify(t, t_norm):
            g = tpm.j2jcal(t)
            self.assertEqual(g['y'], t_norm['y'])
            self.assertEqual(g['m'], t_norm['m'])
            self.assertEqual(g['dd'], t_norm['dd'])

        verify(t=2299160.0, t_norm=dict(y=1582, m=10, dd=4))
        verify(t=1143752.0, t_norm=dict(y=-1581, m=6, dd=4))
        verify(t=0.0, t_norm=dict(y=-4712, m=1, dd=1))

    def testGcal2j(self):
        """tpm.gcal2j() => Julian day number for Gregorian calendar date"""
        def verify(t, t_norm):
            g = tpm.gcal2j(**t)
            self.assertAlmostEqual(g, t_norm)

        verify(dict(y=2000, m=1, dd=1), tpm.J2000)
        verify(dict(y=1913, m=1, dd=1), 2419769.0)
        verify(dict(y=1582, m=10, dd=15), 2299161.0)

    def testJcal2J(self):
        """tpm.jcal2j() => Julian day number for Julian calendar date """
        def verify(t, t_norm):
            g = tpm.jcal2j(**t)
            self.assertAlmostEqual(g, t_norm)

        verify(dict(y=-4712, m=1, dd=1), 0.0)
        verify(dict(y=-1581, m=6, dd=4), 1143752.0)
        verify(dict(y=1582, m=10, dd=4), 2299160.0)


if __name__ == '__main__':
    unittest.main()
