"""Tests for functions defined in m6Functions.c.

These functions are used for accessing and manipulating M6 vectors.

:author: Prasanth Nair
:contact: prasanthhn@gmail.com
"""
from pytpm import tpm

m3_00 = tpm.M3()
m3_01 = tpm.M3()
m3_10 = tpm.M3()
m3_11 = tpm.M3()
m6 = tpm.M6()
XX = 1.0
XY = 2.0
XZ = 3.0
YX = 4.0
YY = 5.0
YZ = 6.0
ZX = 7.0
ZY = 8.0
ZZ = 9.0

def setup_m3_00():
    # perhaps there is a simpler C routine (m3I?).
    tpm.m3SetXXf(m3_00, XX)
    tpm.m3SetXYf(m3_00, XY)
    tpm.m3SetXZf(m3_00, XZ)
    tpm.m3SetYXf(m3_00, YX)
    tpm.m3SetYYf(m3_00, YY)
    tpm.m3SetYZf(m3_00, YZ)
    tpm.m3SetZXf(m3_00, ZX)
    tpm.m3SetZYf(m3_00, ZY)
    tpm.m3SetZZf(m3_00, ZZ)

def setup_m3_01():
    # perhaps there is a simpler C routine (m3I?).
    tpm.m3SetXXf(m3_01, XX+1)
    tpm.m3SetXYf(m3_01, XY+1)
    tpm.m3SetXZf(m3_01, XZ+1)
    tpm.m3SetYXf(m3_01, YX+1)
    tpm.m3SetYYf(m3_01, YY+1)
    tpm.m3SetYZf(m3_01, YZ+1)
    tpm.m3SetZXf(m3_01, ZX+1)
    tpm.m3SetZYf(m3_01, ZY+1)
    tpm.m3SetZZf(m3_01, ZZ+1)

def setup_m3_10():
    # perhaps there is a simpler C routine (m3I?).
    tpm.m3SetXXf(m3_10, XX+2)
    tpm.m3SetXYf(m3_10, XY+2)
    tpm.m3SetXZf(m3_10, XZ+2)
    tpm.m3SetYXf(m3_10, YX+2)
    tpm.m3SetYYf(m3_10, YY+2)
    tpm.m3SetYZf(m3_10, YZ+2)
    tpm.m3SetZXf(m3_10, ZX+2)
    tpm.m3SetZYf(m3_10, ZY+2)
    tpm.m3SetZZf(m3_10, ZZ+2)

def setup_m3_11():
    # perhaps there is a simpler C routine (m3I?).
    tpm.m3SetXXf(m3_11, XX+3)
    tpm.m3SetXYf(m3_11, XY+3)
    tpm.m3SetXZf(m3_11, XZ+3)
    tpm.m3SetYXf(m3_11, YX+3)
    tpm.m3SetYYf(m3_11, YY+3)
    tpm.m3SetYZf(m3_11, YZ+3)
    tpm.m3SetZXf(m3_11, ZX+3)
    tpm.m3SetZYf(m3_11, ZY+3)
    tpm.m3SetZZf(m3_11, ZZ+3)

def test_m6GetPPf():
    setup_m3_00()
    tpm.m6SetPPf(m6, m3_00)
    m3_tmp = tpm.m6GetPPf(m6)
    assert tpm.m3GetXXf(m3_tmp) == XX
    assert tpm.m3GetXYf(m3_tmp) == XY
    assert tpm.m3GetXZf(m3_tmp) == XZ
    assert tpm.m3GetYXf(m3_tmp) == YX
    assert tpm.m3GetYYf(m3_tmp) == YY
    assert tpm.m3GetYZf(m3_tmp) == YZ
    assert tpm.m3GetZXf(m3_tmp) == ZX
    assert tpm.m3GetZYf(m3_tmp) == ZY
    assert tpm.m3GetZZf(m3_tmp) == ZZ

def test_m6GetPVf():
    setup_m3_01()
    tpm.m6SetPPf(m6, m3_01)
    m3_tmp = tpm.m6GetPPf(m6)
    assert tpm.m3GetXXf(m3_tmp) == XX + 1 
    assert tpm.m3GetXYf(m3_tmp) == XY + 1 
    assert tpm.m3GetXZf(m3_tmp) == XZ + 1 
    assert tpm.m3GetYXf(m3_tmp) == YX + 1 
    assert tpm.m3GetYYf(m3_tmp) == YY + 1 
    assert tpm.m3GetYZf(m3_tmp) == YZ + 1 
    assert tpm.m3GetZXf(m3_tmp) == ZX + 1 
    assert tpm.m3GetZYf(m3_tmp) == ZY + 1 
    assert tpm.m3GetZZf(m3_tmp) == ZZ + 1 

def test_m6GetVPf():
    setup_m3_10()
    tpm.m6SetPPf(m6, m3_10)
    m3_tmp = tpm.m6GetPPf(m6)
    assert tpm.m3GetXXf(m3_tmp) == XX + 2 
    assert tpm.m3GetXYf(m3_tmp) == XY + 2 
    assert tpm.m3GetXZf(m3_tmp) == XZ + 2 
    assert tpm.m3GetYXf(m3_tmp) == YX + 2 
    assert tpm.m3GetYYf(m3_tmp) == YY + 2 
    assert tpm.m3GetYZf(m3_tmp) == YZ + 2 
    assert tpm.m3GetZXf(m3_tmp) == ZX + 2 
    assert tpm.m3GetZYf(m3_tmp) == ZY + 2 
    assert tpm.m3GetZZf(m3_tmp) == ZZ + 2 

def test_m6GetVVf():
    setup_m3_11()
    tpm.m6SetPPf(m6, m3_11)
    m3_tmp = tpm.m6GetPPf(m6)
    assert tpm.m3GetXXf(m3_tmp) == XX + 3 
    assert tpm.m3GetXYf(m3_tmp) == XY + 3 
    assert tpm.m3GetXZf(m3_tmp) == XZ + 3 
    assert tpm.m3GetYXf(m3_tmp) == YX + 3 
    assert tpm.m3GetYYf(m3_tmp) == YY + 3 
    assert tpm.m3GetYZf(m3_tmp) == YZ + 3 
    assert tpm.m3GetZXf(m3_tmp) == ZX + 3 
    assert tpm.m3GetZYf(m3_tmp) == ZY + 3 
    assert tpm.m3GetZZf(m3_tmp) == ZZ + 3 

def run():
    test_m6GetPPf()
    test_m6GetPVf()
    test_m6GetVPf()
    test_m6GetVVf()

if __name__ == '__main__':
    print "Running tests on functions in m6Functions.c ..."
    run()
