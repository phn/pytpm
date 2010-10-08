"""Tests for functions defined in tpm/times.h

:Author: Prasanth Nair
:Contact: prasanthhn@gmail.com
"""
from pytpm import tpm, utils

def test_d2dms():
    dms = tpm.d2dms(12.5)
    assert dms.dd == 12.5

def test_dms2dms():
    dms = tpm.d2dms(12.5)
    dms = tpm.dms2dms(dms)
    assert dms.dd == 12.0
    assert dms.mm == 30.0
    assert dms.ss == 0.0

def test_dms_diff():
    dms1 = tpm.d2dms(12.5)
    dms2 = tpm.d2dms(10.5)
    dmsdiff = tpm.dms_diff(dms1, dms2)
    assert dmsdiff.dd == 2.0
    assert dmsdiff.mm == 0.0
    assert dmsdiff.ss == 0.0

def test_dms_sum():
    dms1 = tpm.d2dms(12.5)
    dms2 = tpm.d2dms(10.2)
    dmssum = tpm.dms_sum(dms1, dms2)
    assert dmssum.dd == 22.7

def test_hms2dms():
    hms = tpm.h2hms(12.5)
    hms = tpm.hms2hms(hms)
    dms = tpm.hms2dms(hms)
    assert dms.dd == 180.0
    assert dms.mm == 450.0
    assert dms.ss == 0.0

def test_dms2hms():
    dms = tpm.d2dms(184.5)
    hms = tpm.dms2hms(dms)
    assert hms.hh == 184.5/15.0

def test_h2hms():
    hms = tpm.h2hms(12.5)
    assert hms.hh == 12.5

def test_hms2hms():
    hms = tpm.h2hms(12.245)
    hms = tpm.hms2hms(hms)
    assert hms.hh == 12.0
    assert hms.mm == 14.0
    ss_string = "{0:8.6f}".format(hms.ss)
    assert ss_string == "42.000000"

def test_hms_diff():
    hms1 = tpm.h2hms(12.345)
    hms2 = tpm.h2hms(10.123)
    hmsdiff = tpm.hms_diff(hms1, hms2)
    hmsdiff = tpm.hms2hms(hmsdiff)
    hmsdiff_hh_string = "{0:3.1f}".format(hmsdiff.hh)
    hmsdiff_mm_string = "{0:3.1f}".format(hmsdiff.mm)
    hmsdiff_ss_string = "{0:5.3f}".format(hmsdiff.ss)
    assert hmsdiff_hh_string == "{0:3.1f}".format(12.0 - 10.0)
    assert hmsdiff_mm_string == "{0:3.1f}".format(20.0 - 7.0)
    assert hmsdiff_ss_string == "{0:5.3f}".format(
        (0.345*60-20)*60 - (0.123*60 - 7.0)*60)

def test_hms_sum():
    hms1 = tpm.h2hms(12.345)
    hms2 = tpm.h2hms(10.123)
    h = 12 + 10
    m = int(0.345*60 + 0.123*60)
    s = ((0.345*60+0.123*60) - m)*60
    hmssum = tpm.hms_sum(hms1, hms2)
    hmssum = tpm.hms2hms(hmssum)
    hmssum_hh_string = "{0:2d}".format(int(hmssum.hh))
    hmssum_mm_string = "{0:2d}".format(int(hmssum.mm))
    hmssum_ss_string = "{0:5.3f}".format(hmssum.ss)
    assert hmssum_hh_string == "{0:2d}".format(12+ 10)
    assert hmssum_mm_string == "{0:2d}".format(m)
    assert hmssum_ss_string == "{0:5.3f}".format(s)

def test_j2jd():
    jd = tpm.j2jd(2451545.123)
    assert "{0:10.3f}".format(jd.dd) == "2451545.123"

def test_jd2jd():
    jd = tpm.j2jd(2451545.123)
    jd = tpm.jd2jd(jd)
    dd = 2451545.0
    hh = int(0.123*24)
    mm = int((0.123*24-hh)*60)
    ss = ((0.123*24-hh)*60-mm)*60
    assert "{0:.1f}".format(jd.dd) ==  "{0:.1f}".format(dd)
    assert "{0:2d}".format(int(jd.hms.hh)) == "{0:2d}".format(hh)
    assert "{0:2d}".format(int(jd.hms.mm)) == "{0:2d}".format(mm)
    assert "{0:5.3f}".format(jd.hms.ss) == "{0:5.3f}".format(ss) 

def test_gcal2j():
    # This is date in PROLEPTIC gregorian calendar
    # Time is mid-day
    # Test values are from
    # http://www.usno.navy.mil/USNO/astronomical-applications/data-services/cal-to-jd-conv
    # which uses Julian Calendar for days on or before 4 th October 1582.
    
    # 2000/1/1 12:00:00 UTC 
    j_string = "{0:8.1f}".format(2451545.0)
    j = tpm.gcal2j(2000,1,1)
    assert "{0:8.1f}".format(j) == j_string
    
    j_string = "{0:8.1f}".format(2419769.0)
    j = tpm.gcal2j(1913,1,1)
    assert "{0:8.1f}".format(j) == j_string

    j_string = "{0:8.1f}".format(2299161.0)
    j = tpm.gcal2j(1582,10,15)
    assert "{0:8.1f}".format(j) == j_string

def test_jcal2j():
    # PROLEPTIC Julian calendar to Julian day number
    # Time is mid-day
    # BC YYYY is -(YYYY-1)

    j_string = "{0:8.1f}".format(2299160.0)
    j = tpm.jcal2j(1582,10,4)
    assert "{0:8.1f}".format(j) == j_string

    # BC 1582 June 4
    j_string = "{0:8.1f}".format(1143752.0)
    j = tpm.jcal2j(-1581,6,4)
    assert "{0:8.1f}".format(j) == j_string

    # Starting date for Julian day numbers
    j_string = "{0:8.1f}".format(0.0)
    j = tpm.jcal2j(-4712,1,1)
    assert "{0:8.1f}".format(j) == j_string

def test_j2dow():
    # Test data from linux program 'cal'

    # 2000/1/1 Saturday -> dow = 6
    dow = tpm.j2dow(tpm.gcal2j(2000,1,1))
    assert dow == 6

    # 1582/10/15 Friday -> dow = 5
    dow = tpm.j2dow(tpm.gcal2j(1582,10,15))
    assert dow == 5

    # 1582/10/4 Thursday -> dow = 4
    dow = tpm.j2dow(tpm.jcal2j(1582,10,4))
    assert dow == 4

def test_y2doy():
    # Number of days in a proleptic gregorian calendar year
    assert tpm.y2doy(2010) == 365
    assert tpm.y2doy(2000) == 366
    assert tpm.y2doy(1672) == 366

def test_j2gcal():
    # Map julian day number onto the proleptic gregorian cal.
    
    y,m,d = tpm.j2gcal(2451545.0)
    assert y == 2000
    assert m == 1
    assert d == 1

    y,m,d = tpm.j2gcal(2419769.0)
    assert y == 1913
    assert m == 1
    assert d == 1
    
    y,m,d = tpm.j2gcal(2299161.0)
    assert y == 1582
    assert m == 10
    assert d == 15

def test_j2jcal():
    # map julian day number onto proletic Julian calendar
    y,m,d = tpm.j2jcal(2299160.0)
    assert y == 1582
    assert m == 10
    assert d == 4

    y,m,d = tpm.j2jcal(1143752.0)
    assert y == -1581
    assert m == 6
    assert d == 4

    y,m,d = tpm.j2jcal(0.0)
    assert y == -4712
    assert m == 1
    assert d == 1

if __name__ == '__main__':
    test_d2dms()
    test_dms2dms()
    test_dms_diff()
    test_dms_sum()
    test_hms2dms()
    test_dms2hms()
    test_h2hms()
    test_hms2hms()
    test_hms_diff()
    test_hms_sum()
    test_j2jd()
    test_jd2jd()
    test_gcal2j()
    test_jcal2j()
    test_j2dow()
    test_y2doy()
    test_j2gcal()
    test_j2jcal()
