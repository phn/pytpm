"""Tests for functions defined in tpm/times.h

:Author: Prasanth Nair
:Contact: prasanthhn@gmail.com
"""
from pytpm import tpm, utils
import math

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

def test_jd_diff():
    jd1 = tpm.j2jd(2451545.123)
    jd1 = tpm.jd2jd(jd1)
    jd2 = tpm.j2jd(2451545.0)
    jd2 = tpm.jd2jd(jd2)
    jd_diff = tpm.jd_diff(jd1, jd2)
    jd_diff = tpm.jd2jd(jd_diff)
    dd = utils.jdGetDay(jd_diff)
    assert "{0:8.1f}".format(dd) == "{0:8.1f}".format(0.0)

    hh_diff = int(0.123*24.0)
    temp = ((0.123*24.0)-hh_diff)*60.0
    mm_diff = int(temp)
    ss_diff = (temp - mm_diff)*60.0
    hh = utils.jdGetHours(jd_diff)
    mm = utils.jdGetMinutes(jd_diff)
    ss = utils.jdGetSeconds(jd_diff)
    assert "{0:4.2f}".format(hh) == "{0:4.2f}".format(hh_diff)
    assert "{0:4.2f}".format(mm) == "{0:4.2f}".format(mm_diff)
    assert "{0:2.1f}".format(ss) == "{0:2.1f}".format(ss_diff)

def test_jd_now():
    # How do I test this?
    #raise AssertionError
    pass

def test_jd_sum():
    jd1 = tpm.j2jd(2451545.123)
    jd1 = tpm.jd2jd(jd1)
    jd2 = tpm.j2jd(5.0)
    jd2 = tpm.jd2jd(jd2)
    jd_sum = tpm.jd_sum(jd1, jd2)
    jd_sum = tpm.jd2jd(jd_sum)
    dd = utils.jdGetDay(jd_sum)
    assert "{0:8.1f}".format(dd) == "{0:8.1f}".format(2451550.0)

    hh_sum = int(0.123*24.0)
    temp = ((0.123*24.0)-hh_sum)*60.0
    mm_sum = int(temp)
    ss_sum = (temp - mm_sum)*60.0
    hh = utils.jdGetHours(jd_sum)
    mm = utils.jdGetMinutes(jd_sum)
    ss = utils.jdGetSeconds(jd_sum)
    print hh,mm,ss
    assert "{0:4.2f}".format(hh) == "{0:4.2f}".format(hh_sum)
    assert "{0:4.2f}".format(mm) == "{0:4.2f}".format(mm_sum)
    assert "{0:2.1f}".format(ss) == "{0:2.1f}".format(ss_sum)


def test_ymd2jd():
    ymd = tpm.YMD()
    utils.ymdSetYear(ymd, 2000)
    utils.ymdSetMonth(ymd, 1)
    utils.ymdSetDay(ymd, 1)
    utils.ymdSetHours(ymd,13.0)
    utils.ymdSetMinutes(ymd, 34.0)
    utils.ymdSetSeconds(ymd, 23.0)
    jd = tpm.ymd2jd(ymd)
    jd = tpm.jd2jd(jd)

    j = tpm.jd2j(jd)
    # Julian day starts at noon so hours-12.0
    h = 1.0 + 34.0/60.0 + 23.0/3600.0
    j_string = "{0:15.6f}".format(2451545.0+h/24.0)

    assert "{0:15.6f}".format(j) == j_string
    
def test_jd2ymd():
    # Converts JD into YMD in the Gregorian Calendar.
    jd = tpm.j2jd(2451545.0)
    jd = tpm.jd2jd(jd)
    ymd = tpm.jd2ymd(jd)
    ymd = tpm.ymd2ymd(ymd)
    assert utils.ymdGetYear(ymd) == 2000
    assert utils.ymdGetMonth(ymd) == 1
    assert utils.ymdGetDay(ymd) == 1

    jd = tpm.j2jd(2419769.123)
    jd = tpm.jd2jd(jd)
    ymd = tpm.jd2ymd(jd)
    ymd = tpm.ymd2ymd(ymd)
    assert utils.ymdGetYear(ymd) == 1913
    assert utils.ymdGetMonth(ymd) == 1
    assert utils.ymdGetDay(ymd) == 1

    h = math.floor(0.123*24.0) + 12
    h_string = "{0:4.1f}".format(h)
    assert "{0:4.1f}".format(utils.ymdGetHours(ymd)) == h_string
    temp = 0.123*24.0-(h-12)
    m = math.floor(temp*60.0)
    m_string = "{0:4.1f}".format(m)
    assert "{0:4.1f}".format(utils.ymdGetMinutes(ymd)) == m_string
    s = (temp*60.0-m)*60.0
    s_string = "{0:4.1f}".format(s)
    assert "{0:4.1f}".format(utils.ymdGetSeconds(ymd)) == s_string
    
def test_y2ymd():
    # 2010 October 14 15 hours 23 minutes 12.3 seconds
    y = 2010
    m = 10
    d = 14.0
    h = 15.0
    mi = 23.0
    s = 12.3
    yy = 2010+(287 + (15.0+23.0/60.0+12.3/3600.0)/24.0)/365.0
    ymd = tpm.y2ymd(yy)
    ymd = tpm.ymd2ymd(ymd)
    assert ymd.y == y
    assert ymd.m == m
    assert ymd.dd == 14.0
    assert ymd.hms.hh == h
    assert ymd.hms.mm == mi
    assert "{0:4.1f}".format(ymd.hms.ss) == "{0:4.1f}".format(s)
    
def test_ydd2ymd():
    # takes an integer year and a double day and returns a YMD
    # 2010 October 14 15 hours 23 minutes 12.3 seconds
    y = 2010
    m = 10
    d = 14.0
    h = 15.0
    mi = 23.0
    s = 12.3
    dd = (287 + (15.0+23.0/60.0+12.3/3600.0)/24.0)
    ymd = tpm.ydd2ymd(y,dd)
    ymd = tpm.ymd2ymd(ymd)
    assert ymd.y == y
    assert ymd.m == m
    assert ymd.dd == 14.0
    assert ymd.hms.hh == h
    assert ymd.hms.mm == mi
    assert "{0:4.1f}".format(ymd.hms.ss) == "{0:4.1f}".format(s)
   
def test_ymd2ymd():
    ymd = tpm.YMD()
    ymd.y = 2000
    ymd.m = 1
    ymd.dd = 286.0
    ymd.hms.hh = 12.123456
    ymd.hms.mm = 0.0
    ymd.hms.ss = 0.0
    ymd = tpm.ymd2ymd(ymd)
    assert ymd.y == 2000
    assert ymd.m == 10
    assert ymd.dd == 12.0
    assert ymd.hms.hh == 12.0
    assert ymd.hms.mm == 7.0
    assert "{0:9.6f}".format(ymd.hms.ss) == "{0:9.6f}".format(24.441605)
    
def test_fmt_alpha():
    # Format angle as time from 0 to 24. Used for converting ra in
    # radians into hours;
    # tpm.M_PI/3.0 -> 03H 59M 59.999S
    assert tpm.fmt_alpha(tpm.M_PI/3.0).strip() == "03H 59M 59.999S"
    assert tpm.fmt_alpha(tpm.M_PI*1.234).strip() == "14H 48M 28.799S"

def test_fmt_d():
    # Format degrees into a string
    assert tpm.fmt_d(180.0).strip() == "+180D 00\' 00.000\""
    assert tpm.fmt_d(45.12345).strip() == "+45D 07\' 24.419\""

def test_fmt_delta():
    # format angle in radians into string with value -90 to 90
    # Here the value is cycled through -90 0 90 0 -90 0 -90 and so on
    # staring from 0. So 91 is 89.
    # In my pam.time_angle_format.normalize function i do folding i.e.,
    # -90 0 90 then go back to -90 0 90 and so on and so 91 is -89.
    assert tpm.fmt_delta(tpm.M_PI).strip() == "+00D 00\' 00.000\""
    assert tpm.fmt_delta(tpm.M_PI/2.0).strip() == "+90D 00\' 00.000\""
    assert tpm.fmt_delta(tpm.M_PI*1.2345).strip() == "-42D 12\' 35.999\""

def test_fmt_h():
    # Format hours into hms string
    assert tpm.fmt_h(12.0).strip() == "12H 00M 00.000S"
    assert tpm.fmt_h(36.12345).strip() == "36H 07M 24.419S"

def test_fmt_j():
    assert tpm.fmt_j(2451545.0).strip() == "2451545  00H 00M 00.000S"
    assert tpm.fmt_j(1111111.1234).strip() == "1111111  02H 57M 41.759S"

def test_fmt_ymd():
    #
    assert tpm.fmt_ymd(utils.j2ymd(2451545.0)).strip() == \
        "Sat Jan  1 12:00:00.000 2000"
    assert tpm.fmt_ymd(utils.j2ymd(1111111.12345)).strip() == \
        "Tue Jan  7 14:57:46.080 1671 BC"
    
def test_fmt_ymd_raw():
    assert tpm.fmt_ymd_raw(utils.j2ymd(2451545.0)).strip() == \
        "2000 1 1.5 0 0 0"
    assert tpm.fmt_ymd_raw(utils.j2ymd(1111111.12345)).strip() == \
        "-1670 1 7.6234500000719 0 0 0"

def test_d2d():
    # Normalize degrees to 0 360
    # -361 is 359 361 is 1
    assert tpm.d2d(360.0) == 0.0
    assert tpm.d2d(361.0) == 1.0
    assert tpm.d2d(-361.0) == 359.0

def test_dms2d():
    dms = tpm.DMS()
    dms.dd = 12.1
    dms.mm = 13.2
    dms.ss = 23.0

    d = tpm.dms2d(dms)
    assert "{0:7.5f}".format(d) == "{0:7.5f}".format(12.1+13.2/60.0+23.0/3600.0)
    
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

def test_h2h():
    assert tpm.h2h(-23.0) == 1.0
    assert tpm.h2h(-1.0) == 23.0
    assert tpm.h2h(25.0) == 1.0

def test_hms2h():
    hms = tpm.HMS()
    hms.hh = 12.0
    hms.mm = 13.2
    hms.ss = 23.4    
    assert "{0:7.5f}".format(tpm.hms2h(hms)) == \
        "{0:7.5f}".format(12.0+13.2/60.0+23.4/3600.0)

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

def test_jd2j():
    assert "{0:13.5f}".format(tpm.jd2j(tpm.j2jd(2455480.9334953702)))==\
        "{0:13.5f}".format(2455480.9334953702)

def test_r2r():
    # radians to 0 - 2pi
    # 0  2pi then 2pi - 0 and so on
    assert "{0:8.5f}".format(tpm.r2r(-2*tpm.M_PI)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.r2r(-0.5*tpm.M_PI)) == \
        "{0:8.5f}".format(1.5*tpm.M_PI)

def test_utc_now():
    # How do I test this?
    pass

def test_ymd2dd():
    ymd = tpm.YMD()
    ymd.y = 2000
    ymd.m = 10
    ymd.dd = 12.0
    ymd.hms.hh = 12.0
    ymd.hms.mm = 12.0
    ymd.hms.ss = 12.345
    assert "{0:10.6f}".format(tpm.ymd2dd(ymd)) == \
        "{0:10.6f}".format(286.508476)

def test_ymd2y():
    ymd = tpm.YMD()
    ymd.y = 2000
    ymd.m = 10
    ymd.dd = 12.0
    ymd.hms.hh = 12.0
    ymd.hms.mm = 12.0
    ymd.hms.ss = 12.345
    assert "{0:12.6f}".format(tpm.ymd2y(ymd)) == \
        "{0:12.6f}".format(2000.782810)

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
    test_jd_diff()
    test_jd_now()
    test_jd_sum()
    test_ymd2jd()
    test_jd2ymd()
    test_y2ymd()
    test_ydd2ymd()
    test_ymd2ymd()
    test_fmt_alpha()
    test_fmt_d()
    test_fmt_delta()
    test_fmt_h()
    test_fmt_j()
    test_fmt_ymd()
    test_fmt_ymd_raw()
    test_d2d()
    test_dms2d()
    test_gcal2j()
    test_h2h()
    test_hms2h()
    test_jcal2j()
    test_jd2j()
    test_r2r()
    test_utc_now()
    test_ymd2dd()
    test_ymd2y()
    test_j2dow()
    test_y2doy()
    test_j2gcal()
    test_j2jcal()
