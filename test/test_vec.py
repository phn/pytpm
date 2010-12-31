# -*- coding: utf-8 -*-
"""Tests for functions defined in tpm/vec.h.

These functions are used for accessing and manipulating vectors and
matrices.

The values that appear in assert statements are, in most cases,
obtained by running the appropriate C program, which can be found in
the ``c_test`` directory.

:author: Prasanth Nair
:contact: prasanthhn@gmail.com
"""
from pytpm import tpm
import math

def setup_cartesian_v3():
    v3 = tpm.V3()
    tpm.v3SetTypef(v3, tpm.CARTESIAN);
    tpm.v3SetXf(v3, 1123.4556);
    tpm.v3SetYf(v3, 4556.1123);
    tpm.v3SetZf(v3, 9876.1267);

    return v3

def setup_m3():
    m3 = tpm.m3I(1.0)
   
    tpm.m3SetXXf(m3, 0.2345) 
    tpm.m3SetXYf(m3, 0.5432)	
    tpm.m3SetXZf(m3, 0.1234)  
    tpm.m3SetYXf(m3, 0.5467)  
    tpm.m3SetYYf(m3, 0.4190)  
    tpm.m3SetYZf(m3, 0.9874)  
    tpm.m3SetZXf(m3, 0.1225)  
    tpm.m3SetZYf(m3, 0.4331)  
    tpm.m3SetZZf(m3, 0.2309)  
   
    return m3

def setup_cartesian_v6_with_2_v3():
    # Create a V6 vector, using 2 V3 vectors.
    v3_1 = tpm.v3init(tpm.CARTESIAN)
    v3_2 = tpm.v3init(tpm.CARTESIAN)
    v6 = tpm.v6init(tpm.CARTESIAN)
  
    tpm.v3SetTypef(v3_1, tpm.CARTESIAN)
    tpm.v3SetXf(v3_1, 1123.4556)
    tpm.v3SetYf(v3_1, 4556.1123)
    tpm.v3SetZf(v3_1, 9876.1267)
    
    tpm.v3SetTypef(v3_2, tpm.CARTESIAN)
    tpm.v3SetXf(v3_2, 2.3456)
    tpm.v3SetYf(v3_2, 6.7891)
    tpm.v3SetZf(v3_2, 7.8912)
    
    tpm.v6SetPosf(v6, v3_1)
    tpm.v6SetVelf(v6, v3_2)
    
    tpm.v6SetTypef(v6, tpm.CARTESIAN)

    return v6

def setup_m6_with_4_m3():
    # Create a M6 matrix, by using 4 M3 matrices.
    m3_1 = tpm.m3I(1.0)
    m6 = tpm.M6()

    tpm.m3SetXXf(m3_1, 0.2345) 
    tpm.m3SetXYf(m3_1, 0.5432)	
    tpm.m3SetXZf(m3_1, 0.1234)  
    tpm.m3SetYXf(m3_1, 0.5467)  
    tpm.m3SetYYf(m3_1, 0.4190)  
    tpm.m3SetYZf(m3_1, 0.9874)  
    tpm.m3SetZXf(m3_1, 0.1225)  
    tpm.m3SetZYf(m3_1, 0.4331)  
    tpm.m3SetZZf(m3_1, 0.2309)  

    tpm.m6SetPPf(m6, m3_1)

    tpm.m3SetXXf(m3_1, 0.4523) 
    tpm.m3SetXYf(m3_1, 0.3254)	
    tpm.m3SetXZf(m3_1, 0.3412)  
    tpm.m3SetYXf(m3_1, 0.6754)  
    tpm.m3SetYYf(m3_1, 0.9041)  
    tpm.m3SetYZf(m3_1, 0.7498)  
    tpm.m3SetZXf(m3_1, 0.2512)  
    tpm.m3SetZYf(m3_1, 0.3143)  
    tpm.m3SetZZf(m3_1, 0.0923)
    
    tpm.m6SetPVf(m6, m3_1)

    tpm.m3SetXXf(m3_1, 0.4253) 
    tpm.m3SetXYf(m3_1, 0.3524)	
    tpm.m3SetXZf(m3_1, 0.3142)  
    tpm.m3SetYXf(m3_1, 0.6574)  
    tpm.m3SetYYf(m3_1, 0.9401)  
    tpm.m3SetYZf(m3_1, 0.7948)  
    tpm.m3SetZXf(m3_1, 0.2152)  
    tpm.m3SetZYf(m3_1, 0.4133)  
    tpm.m3SetZZf(m3_1, 0.2903)
    
    tpm.m6SetVPf(m6, m3_1)

    tpm.m3SetXXf(m3_1, 0.3524) 
    tpm.m3SetXYf(m3_1, 0.4235)	
    tpm.m3SetXZf(m3_1, 0.2413)  
    tpm.m3SetYXf(m3_1, 0.4756)  
    tpm.m3SetYYf(m3_1, 0.1049)  
    tpm.m3SetYZf(m3_1, 0.8497)  
    tpm.m3SetZXf(m3_1, 0.2512)  
    tpm.m3SetZYf(m3_1, 0.3314)  
    tpm.m3SetZZf(m3_1, 0.3092)
    
    tpm.m6SetVVf(m6, m3_1)

    return m6

def compare_m3(m3_1, m3_2):
    assert "{0:8.6f}".format(tpm.m3GetXXf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetXXf(m3_2))
    assert "{0:8.6f}".format(tpm.m3GetXYf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetXYf(m3_2))
    assert "{0:8.6f}".format(tpm.m3GetXZf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetXZf(m3_2))
    
    assert "{0:8.6f}".format(tpm.m3GetYXf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetYXf(m3_2))
    assert "{0:8.6f}".format(tpm.m3GetYYf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetYYf(m3_2))
    assert "{0:8.6f}".format(tpm.m3GetYZf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetYZf(m3_2))

    assert "{0:8.6f}".format(tpm.m3GetZXf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetZXf(m3_2))
    assert "{0:8.6f}".format(tpm.m3GetZYf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetZYf(m3_2))
    assert "{0:8.6f}".format(tpm.m3GetZZf(m3_1)) == \
        "{0:8.6f}".format(tpm.m3GetZZf(m3_2))

def compare_m6(m6_1, m6_2):
    compare_m3(tpm.m6GetPPf(m6_1), tpm.m6GetPPf(m6_2))
    compare_m3(tpm.m6GetPVf(m6_1), tpm.m6GetPVf(m6_2))
    compare_m3(tpm.m6GetVPf(m6_1), tpm.m6GetVPf(m6_2))
    compare_m3(tpm.m6GetVVf(m6_1), tpm.m6GetVVf(m6_2))
    
# extern M3 m3I(double x);
def test_m3I():
    """Identity 3-matrix scaled by the given value."""
    m3 = tpm.m3I(10.0)
    assert tpm.m3GetXXf(m3) == 10.0
    assert tpm.m3GetYYf(m3) == 10.0
    assert tpm.m3GetZZf(m3) == 10.0
    
# extern M3 m3O(void);
def test_m3O():
    """Null 3-matrix."""
    m3 = tpm.m3O()
    assert tpm.m3GetXXf(m3) == 0.0
    assert tpm.m3GetXYf(m3) == 0.0
    assert tpm.m3GetXZf(m3) == 0.0
    assert tpm.m3GetYXf(m3) == 0.0
    assert tpm.m3GetYYf(m3) == 0.0
    assert tpm.m3GetYZf(m3) == 0.0
    assert tpm.m3GetZXf(m3) == 0.0
    assert tpm.m3GetZYf(m3) == 0.0
    assert tpm.m3GetZZf(m3) == 0.0
    
# extern M3 m3Rx(double x);
def test_m3Rx():
    # Rotation matrix from Yallop et. al., .
    m3 = tpm.m3Rx(12.345)
    assert "{0:8.6f}".format(tpm.m3GetYYf(m3)) == \
        "{0:8.6f}".format(0.975597)
    assert "{0:8.6f}".format(tpm.m3GetYZf(m3)) == \
        "{0:8.6f}".format(-0.219567)
    assert "{0:8.6f}".format(tpm.m3GetZYf(m3)) == \
        "{0:8.6f}".format(0.219567)
    assert "{0:8.6f}".format(tpm.m3GetZZf(m3)) == \
        "{0:8.6f}".format(0.975597)
    
# extern M3 m3RxDot(double x, double xdot);
def test_m3RxDot():
    m3 = tpm.m3RxDot(12.345, 1.2345)
    assert "{0:8.6f}".format(tpm.m3GetYYf(m3)) == \
        "{0:8.6f}".format(0.271055)
    assert "{0:8.6f}".format(tpm.m3GetYZf(m3)) == \
        "{0:8.6f}".format(1.204375)
    assert "{0:8.6f}".format(tpm.m3GetZYf(m3)) == \
        "{0:8.6f}".format(-1.204375)
    assert "{0:8.6f}".format(tpm.m3GetZZf(m3)) == \
        "{0:8.6f}".format(0.271055)
    
# extern M3 m3Ry(double y);
def test_m3Ry():
    # Rotation matrix from Yallop et. al., .
    m3 = tpm.m3Ry(12.345)
    assert "{0:8.6f}".format(tpm.m3GetXXf(m3)) == \
        "{0:8.6f}".format(0.975597)
    assert "{0:8.6f}".format(tpm.m3GetXZf(m3)) == \
        "{0:8.6f}".format(0.219567)
    assert "{0:8.6f}".format(tpm.m3GetZXf(m3)) == \
        "{0:8.6f}".format(-0.219567)
    assert "{0:8.6f}".format(tpm.m3GetZZf(m3)) == \
        "{0:8.6f}".format(0.975597)

# extern M3 m3RyDot(double y, double ydot);
def test_m3RyDot():
    m3 = tpm.m3RyDot(12.345, 1.2345)
    assert "{0:8.6f}".format(tpm.m3GetXXf(m3)) == \
        "{0:8.6f}".format(0.271055)
    assert "{0:8.6f}".format(tpm.m3GetXZf(m3)) == \
        "{0:8.6f}".format(-1.204375)
    assert "{0:8.6f}".format(tpm.m3GetZXf(m3)) == \
        "{0:8.6f}".format(1.204375)
    assert "{0:8.6f}".format(tpm.m3GetZZf(m3)) == \
        "{0:8.6f}".format(0.271055)

# extern M3 m3Rz(double z);
def test_m3Rz():
    # Rotation matrix from Yallop et. al., .
    m3 = tpm.m3Rz(12.345)
    assert "{0:8.6f}".format(tpm.m3GetXXf(m3)) == \
        "{0:8.6f}".format(0.975597)
    assert "{0:8.6f}".format(tpm.m3GetXYf(m3)) == \
        "{0:8.6f}".format(-0.219567)
    assert "{0:8.6f}".format(tpm.m3GetYXf(m3)) == \
        "{0:8.6f}".format(0.219567)
    assert "{0:8.6f}".format(tpm.m3GetYYf(m3)) == \
        "{0:8.6f}".format(0.975597)

# extern M3 m3RzDot(double z, double zdot);
def test_m3RzDot():
    m3 = tpm.m3RzDot(12.345, 1.2345)
    assert "{0:8.6f}".format(tpm.m3GetXXf(m3)) == \
        "{0:8.6f}".format(0.271055)
    assert "{0:8.6f}".format(tpm.m3GetXYf(m3)) == \
        "{0:8.6f}".format(1.204375)
    assert "{0:8.6f}".format(tpm.m3GetYXf(m3)) == \
        "{0:8.6f}".format(-1.204375)
    assert "{0:8.6f}".format(tpm.m3GetYYf(m3)) == \
        "{0:8.6f}".format(0.271055)
    
# extern M3 m3diff(M3 m1, M3 m2);
def test_m3diff():
    m3_1 = tpm.m3Rx(12.345)
    m3_2 = tpm.m3Rx(10.123)
    yy_diff = math.cos(12.345)-math.cos(10.123)
    yz_diff = math.sin(12.345)-math.sin(10.123)
    zy_diff = -yz_diff
    zz_diff = yy_diff
    m3_diff = tpm.m3diff(m3_1, m3_2)
    assert "{0:8.6f}".format(tpm.m3GetYYf(m3_diff)) == \
        "{0:8.6f}".format(yy_diff)
    assert "{0:8.6f}".format(tpm.m3GetYZf(m3_diff)) == \
        "{0:8.6f}".format(yz_diff)
    assert "{0:8.6f}".format(tpm.m3GetZYf(m3_diff)) == \
        "{0:8.6f}".format(zy_diff)
    assert "{0:8.6f}".format(tpm.m3GetZZf(m3_diff)) == \
        "{0:8.6f}".format(zz_diff)
    
# extern M3 m3inv(M3 m);
def test_m3inv():
    # Rotation matrix; so inverse is just the transpose
    m3 = tpm.m3Rx(12.345)
    m3_inv = tpm.m3inv(m3)
    assert "{0:8.6f}".format(tpm.m3GetXXf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetXXf(m3_inv))
    assert "{0:8.6f}".format(tpm.m3GetYXf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetXYf(m3_inv))
    assert "{0:8.6f}".format(tpm.m3GetZXf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetXZf(m3_inv))
    
    assert "{0:8.6f}".format(tpm.m3GetXYf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetYXf(m3_inv))
    assert "{0:8.6f}".format(tpm.m3GetYYf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetYYf(m3_inv))
    assert "{0:8.6f}".format(tpm.m3GetZYf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetYZf(m3_inv))

    assert "{0:8.6f}".format(tpm.m3GetXZf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetZXf(m3_inv))
    assert "{0:8.6f}".format(tpm.m3GetYZf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetZYf(m3_inv))
    assert "{0:8.6f}".format(tpm.m3GetZZf(m3)) == \
        "{0:8.6f}".format(tpm.m3GetZZf(m3_inv))
     
# extern M3 m3m3(M3 m1, M3 m2);
def test_m3m3():
    m3_1 = tpm.m3I(1.0)
    m3_2 = tpm.m3I(2.0)
    tpm.m3SetXXf(m3_1, 1.000)
    tpm.m3SetXXf(m3_2, 2.000985)
    tpm.m3SetXYf(m3_1, 0.041631)
    tpm.m3SetXYf(m3_2, 0.176643)
    tpm.m3SetXZf(m3_1, 0.364602)
    tpm.m3SetXZf(m3_2, 0.091331)

    tpm.m3SetYXf(m3_1, 0.092298)
    tpm.m3SetYXf(m3_2, 0.487217)
    tpm.m3SetYYf(m3_1, 1.526750)
    tpm.m3SetYYf(m3_2, 2.454433)
    tpm.m3SetYZf(m3_1, 0.233178)
    tpm.m3SetYZf(m3_2, 0.831292)

    tpm.m3SetZXf(m3_1, 0.931731)
    tpm.m3SetZXf(m3_2, 0.568060)
    tpm.m3SetZYf(m3_1, 0.556094)
    tpm.m3SetZYf(m3_2, 0.050832)
    tpm.m3SetZZf(m3_1, 1.767051)
    tpm.m3SetZZf(m3_2, 2.018915)

    m = tpm.m3m3(m3_1, m3_2)

    assert "{0:8.5f}".format(tpm.m3GetXXf(m)) == \
        "{0:8.5f}".format(2.228385)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m)) == \
        "{0:8.5f}".format(0.297357)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m)) == \
        "{0:8.5f}".format(0.862039)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m)) == \
        "{0:8.5f}".format(1.061005)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m)) == \
        "{0:8.5f}".format(3.775464)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m)) == \
        "{0:8.5f}".format(1.748372)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m)) == \
        "{0:8.5f}".format(3.139110)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m)) == \
        "{0:8.5f}".format(1.619303)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m)) == \
        "{0:8.5f}".format(4.114898)
        
# extern M3 m3scale(M3 m, double s);
def test_m3scale():
    m = tpm.m3I(1.0)
    m = tpm.m3scale(m, 1.23456789)
    assert "{0:8.6f}".format(tpm.m3GetXXf(m)) == \
        "{0:8.6f}".format(1.23456789)
    assert "{0:8.6f}".format(tpm.m3GetYYf(m)) == \
        "{0:8.6f}".format(1.23456789)
    assert "{0:8.6f}".format(tpm.m3GetZZf(m)) == \
        "{0:8.6f}".format(1.23456789)
    
# extern M3 m3sum(M3 m1, M3 m2);
def test_m3sum():
    m3_1 = tpm.m3I(1.23456789)
    m3_2 = tpm.m3I(2.98765431)
    m3_sum = 1.23456789 + 2.98765431
    m = tpm.m3sum(m3_1, m3_2)
    assert "{0:8.6f}".format(tpm.m3GetXXf(m)) == \
        "{0:8.6f}".format(m3_sum)
    assert "{0:8.6f}".format(tpm.m3GetYYf(m)) == \
        "{0:8.6f}".format(m3_sum)
    assert "{0:8.6f}".format(tpm.m3GetZZf(m)) == \
        "{0:8.6f}".format(m3_sum)
    
# extern M6 m6I(double x);
def test_m6I():
    m6 = tpm.m6I(1.23456789)
    compare_m3(tpm.m6GetPPf(m6), tpm.m3I(1.23456789))
    compare_m3(tpm.m6GetPVf(m6), tpm.m3O())
    compare_m3(tpm.m6GetVPf(m6), tpm.m3O())
    compare_m3(tpm.m6GetVVf(m6), tpm.m3I(1.23456789))
    
# extern M6 m6O(void);
def test_m6O():
    m6 = tpm.m6O()
    compare_m3(tpm.m6GetPPf(m6), tpm.m3O())
    compare_m3(tpm.m6GetPVf(m6), tpm.m3O())
    compare_m3(tpm.m6GetVPf(m6), tpm.m3O())
    compare_m3(tpm.m6GetVVf(m6), tpm.m3O())
    
# extern M6 m6Qx(double x, double xdot);
def test_m6Qx():
    x = 1.23456789
    xdot = 0.3456
    m6 = tpm.m6Qx(x, xdot)
    compare_m3(tpm.m6GetPPf(m6), tpm.m3Rx(x))
    compare_m3(tpm.m6GetPVf(m6), tpm.m3O())
    compare_m3(tpm.m6GetVPf(m6), tpm.m3RxDot(x, xdot))
    compare_m3(tpm.m6GetVVf(m6), tpm.m3Rx(x))
    
# extern M6 m6Qy(double y, double ydot);
def test_m6Qy():
    y = 1.23456789
    ydot = 0.3456
    m6 = tpm.m6Qy(y, ydot)
    compare_m3(tpm.m6GetPPf(m6), tpm.m3Ry(y))
    compare_m3(tpm.m6GetPVf(m6), tpm.m3O())
    compare_m3(tpm.m6GetVPf(m6), tpm.m3RyDot(y, ydot))
    compare_m3(tpm.m6GetVVf(m6), tpm.m3Ry(y))

# extern M6 m6Qz(double z, double zdot);
def test_m6Qz():
    z = 1.23456789
    zdot = 0.3456
    m6 = tpm.m6Qz(z, zdot)
    compare_m3(tpm.m6GetPPf(m6), tpm.m3Rz(z))
    compare_m3(tpm.m6GetPVf(m6), tpm.m3O())
    compare_m3(tpm.m6GetVPf(m6), tpm.m3RzDot(z, zdot))
    compare_m3(tpm.m6GetVVf(m6), tpm.m3Rz(z))

# extern M6 m6diff(M6 m1, M6 m2);
def test_m6diff():
    m6_1 = tpm.m6Qx(1.23456789, 0.34567)
    m6_2 = tpm.m6Qy(1.98765432, 0.76543)
    m6_diff = tpm.m6diff(m6_1, m6_2)
    m3_00 = tpm.m6GetPPf(m6_diff)
    m3_01 = tpm.m6GetPVf(m6_diff)
    m3_10 = tpm.m6GetVPf(m6_diff)
    m3_11 = tpm.m6GetVVf(m6_diff)

    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_00)) == \
        "{0:8.5f}".format(1.404890)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_10)) == \
        "{0:8.5f}".format(0.699883)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_11)) == \
        "{0:8.5f}".format(1.404890)

    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_00)) == \
        "{0:8.5f}".format(0.914366)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_10)) == \
        "{0:8.5f}".format(-0.309915)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_11)) == \
        "{0:8.5f}".format(0.914366)

    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_00)) == \
        "{0:8.5f}".format(-0.670071)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_10)) == \
        "{0:8.5f}".format(-0.326314)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_11)) == \
        "{0:8.5f}".format(-0.670071)
    
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_00)) == \
        "{0:8.5f}".format(0.944006)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_10)) == \
        "{0:8.5f}".format(0.114047)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_11)) == \
        "{0:8.5f}".format(0.944006)

    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_00)) == \
        "{0:8.5f}".format(-0.914366)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_10)) == \
        "{0:8.5f}".format(0.309915)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_11)) == \
        "{0:8.5f}".format(-0.914366)

    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_00)) == \
        "{0:8.5f}".format(-0.944006)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_10)) == \
        "{0:8.5f}".format(-0.114047)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_11)) == \
        "{0:8.5f}".format(-0.944006)

    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_00)) == \
        "{0:8.5f}".format(0.734819)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_10)) == \
        "{0:8.5f}".format(0.373568)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_11)) == \
        "{0:8.5f}".format(0.734819)
    
# extern M6 m6inv(M6 m);
def test_m6inv():
    m6 = tpm.m6Qx(1.23456789, 0.34567)
    m6_inv = tpm.m6inv(m6)
    m3_00 = tpm.m6GetPPf(m6_inv)
    m3_01 = tpm.m6GetPVf(m6_inv)
    m3_10 = tpm.m6GetVPf(m6_inv)
    m3_11 = tpm.m6GetVVf(m6_inv)

    
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_00)) == \
        "{0:8.5f}".format(1.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_11)) == \
        "{0:8.5f}".format(1.0)

    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_00)) == \
        "{0:8.5f}".format(0.329929)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_10)) == \
        "{0:8.5f}".format(-0.326314)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_11)) == \
        "{0:8.5f}".format(0.329929)
    
    
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_00)) == \
        "{0:8.5f}".format(-0.944006)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_10)) == \
        "{0:8.5f}".format(-0.114047)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_11)) == \
        "{0:8.5f}".format(-0.944006)

    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_00)) == \
        "{0:8.5f}".format(0.944006)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_10)) == \
        "{0:8.5f}".format(0.114047)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_11)) == \
        "{0:8.5f}".format(0.944006)

    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_00)) == \
        "{0:8.5f}".format(0.329929)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_10)) == \
        "{0:8.5f}".format(-0.326314)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_11)) == \
        "{0:8.5f}".format(0.329929)
    
# extern M6 m6m6(M6 m1, M6 m2);
def test_m6m6():

    m6_1 = tpm.m6Qx(1.23456789, 0.34567);
    m6_2 = tpm.m6Qy(1.98765432, 0.76543);
    m6 = tpm.m6m6(m6_1, m6_2);

    m3_00 = tpm.m6GetPPf(m6)
    m3_01 = tpm.m6GetPVf(m6)
    m3_10 = tpm.m6GetVPf(m6)
    m3_11 = tpm.m6GetVVf(m6)

    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_00)) == \
        "{0:8.5f}".format(-0.404890)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_10)) == \
        "{0:8.5f}".format(-0.699883)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_11)) == \
        "{0:8.5f}".format(-0.404890)

    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_00)) == \
        "{0:8.5f}".format(-0.914366)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_10)) == \
        "{0:8.5f}".format(0.309915)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_11)) == \
        "{0:8.5f}".format(-0.914366)

    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_00)) == \
        "{0:8.5f}".format(0.863166)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_10)) == \
        "{0:8.5f}".format(-0.188281)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_11)) == \
        "{0:8.5f}".format(0.863166)

    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_00)) == \
        "{0:8.5f}".format(0.329929)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_10)) == \
        "{0:8.5f}".format(-0.326314)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_11)) == \
        "{0:8.5f}".format(0.329929)
    
    
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_00)) == \
        "{0:8.5f}".format(-0.382218)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_10)) == \
        "{0:8.5f}".format(-0.706870)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_11)) == \
        "{0:8.5f}".format(-0.382218)

    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_00)) == \
        "{0:8.5f}".format(0.301676)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_10)) == \
        "{0:8.5f}".format(-0.400621)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_11)) == \
        "{0:8.5f}".format(0.301676)

    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_00)) == \
        "{0:8.5f}".format(-0.944006)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_10)) == \
        "{0:8.5f}".format(-0.114047)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_11)) == \
        "{0:8.5f}".format(-0.944006)

    # -0.133585 goes to -0.13359
    # python code give: -0.133584 which goes to -0.13358
    # So using 8.4f instead of 8.5f.
    assert "{0:8.4f}".format(tpm.m3GetZZf(m3_00)) == \
        "{0:8.4f}".format(-0.133585)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_10)) == \
        "{0:8.5f}".format(-0.098790)
    assert "{0:8.4f}".format(tpm.m3GetZZf(m3_11)) == \
        "{0:8.4f}".format(-0.133585)
    
# extern M6 m6scale(M6 m, double s);
def test_m6scale():
    
    m6_1 = tpm.m6Qx(1.23456789, 0.34567);
    m6 = tpm.m6scale(m6_1, 7.65432);

    m3_00 = tpm.m6GetPPf(m6)
    m3_01 = tpm.m6GetPVf(m6)
    m3_10 = tpm.m6GetVPf(m6)
    m3_11 = tpm.m6GetVVf(m6)

    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_00)) == \
        "{0:8.5f}".format(7.654320)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_11)) == \
        "{0:8.5f}".format(7.654320)

    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_00)) == \
        "{0:8.5f}".format(02.525383)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.4f}".format(tpm.m3GetYYf(m3_10)) == \
        "{0:8.4f}".format(-2.497715)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_11)) == \
        "{0:8.5f}".format(2.525383)
    
    
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_00)) == \
        "{0:8.5f}".format(7.225722)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_10)) == \
        "{0:8.5f}".format(0.872949)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_11)) == \
        "{0:8.5f}".format(7.225722)

    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_00)) == \
        "{0:8.5f}".format(-7.225722)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_10)) == \
        "{0:8.5f}".format(-0.872949)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_11)) == \
        "{0:8.5f}".format(-7.225722)

    assert "{0:8.4f}".format(tpm.m3GetZZf(m3_00)) == \
        "{0:8.4f}".format(2.525383)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.4f}".format(tpm.m3GetZZf(m3_10)) == \
        "{0:8.4f}".format(-2.497715)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_11)) == \
        "{0:8.5f}".format(2.525383)

# extern M6 m6sum(M6 m1, M6 m2);
def test_m6sum():
    
    m6_1 = tpm.m6Qx(1.23456789, 0.34567);
    m6_2 = tpm.m6Qy(1.98765432, 0.76543);
    m6 = tpm.m6sum(m6_1, m6_2);
    
    m3_00 = tpm.m6GetPPf(m6)
    m3_01 = tpm.m6GetPVf(m6)
    m3_10 = tpm.m6GetVPf(m6)
    m3_11 = tpm.m6GetVVf(m6)

    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_00)) == \
        "{0:8.5f}".format(0.595110)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_10)) == \
        "{0:8.5f}".format(-0.699883)
    assert "{0:8.5f}".format(tpm.m3GetXXf(m3_11)) == \
        "{0:8.5f}".format(0.595110)

    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXYf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_00)) == \
        "{0:8.5f}".format(-0.914366)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_10)) == \
        "{0:8.5f}".format(0.309915)
    assert "{0:8.5f}".format(tpm.m3GetXZf(m3_11)) == \
        "{0:8.5f}".format(-0.914366)

    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_00)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_10)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYXf(m3_11)) == \
        "{0:8.5f}".format(0.0)

    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_00)) == \
        "{0:8.5f}".format(1.329929)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.4f}".format(tpm.m3GetYYf(m3_10)) == \
        "{0:8.4f}".format(-0.326314)
    assert "{0:8.5f}".format(tpm.m3GetYYf(m3_11)) == \
        "{0:8.5f}".format(1.329929)
    
    
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_00)) == \
        "{0:8.5f}".format(0.944006)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_10)) == \
        "{0:8.5f}".format(0.114047)
    assert "{0:8.5f}".format(tpm.m3GetYZf(m3_11)) == \
        "{0:8.5f}".format(0.944006)

    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_00)) == \
        "{0:8.5f}".format(0.914366)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_10)) == \
        "{0:8.5f}".format(-0.309915)
    assert "{0:8.5f}".format(tpm.m3GetZXf(m3_11)) == \
        "{0:8.5f}".format(0.914366)

    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_00)) == \
        "{0:8.5f}".format(-0.944006)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_10)) == \
        "{0:8.5f}".format(-0.114047)
    assert "{0:8.5f}".format(tpm.m3GetZYf(m3_11)) == \
        "{0:8.5f}".format(-0.944006)

    assert "{0:8.4f}".format(tpm.m3GetZZf(m3_00)) == \
        "{0:8.4f}".format(-0.074960)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_01)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.4f}".format(tpm.m3GetZZf(m3_10)) == \
        "{0:8.4f}".format(-1.026197)
    assert "{0:8.5f}".format(tpm.m3GetZZf(m3_11)) == \
        "{0:8.5f}".format(-0.074960)
    
# extern V3 m3v3(M3 m, V3 v1);
def test_m3v3():
    m3 = tpm.m3I(1.0)
    tpm.m3SetXXf(m3, 1.000985)
    tpm.m3SetXYf(m3, 0.041631)
    tpm.m3SetXZf(m3, 0.176643)
    tpm.m3SetYXf(m3, 0.091331)
    tpm.m3SetYYf(m3, 1.092298)
    tpm.m3SetYZf(m3, 0.487217)
    tpm.m3SetZXf(m3, 0.454433)
    tpm.m3SetZYf(m3, 0.233178)
    tpm.m3SetZZf(m3, 1.831292)
    
    v3 = tpm.v3init(tpm.CARTESIAN)
    tpm.v3SetXf(v3, 0.0)
    tpm.v3SetYf(v3, 0.364602)
    tpm.v3SetZf(v3, 0.526750)

    v3 = tpm.m3v3(m3, v3)

    assert "{0:8.5f}".format(tpm.v3GetXf(v3)) == \
        "{0:8.5f}".format(0.108225)
    assert "{0:8.5f}".format(tpm.v3GetYf(v3)) == \
        "{0:8.5f}".format(0.654896)
    assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
        "{0:8.5f}".format(1.049651)

# extern V3 m6v3(M6 m, V3 v);
def test_m6v3():
    v3 = tpm.V3()
    tpm.v3SetXf(v3, 1.2345)
    tpm.v3SetYf(v3, 2.3456)
    tpm.v3SetZf(v3, 3.4567)
    m6 = tpm.m6Qy(1.98765432, 0.76543)

    v3 = tpm.m6v3(m6, v3)
    
    assert "{0:8.5f}".format(tpm.v3GetXf(v3)) == \
        "{0:8.5f}".format(-3.660524)
    assert "{0:8.5f}".format(tpm.v3GetYf(v3)) == \
        "{0:8.5f}".format(2.345600)
    assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
        "{0:8.5f}".format(-0.270797)

# extern V3 v3c2s(V3 vc);
def test_v3c2s():
    v3 = tpm.V3()
    tpm.v3SetTypef(v3, tpm.CARTESIAN);
    tpm.v3SetXf(v3, 1123.4556);
    tpm.v3SetYf(v3, 4556.1123);
    tpm.v3SetZf(v3, 9876.1267);

    v3 = tpm.v3c2s(v3)
    
    assert "{0}".format(tpm.v3GetTypef(v3)) == \
        "{0}".format(tpm.SPHERICAL)
    assert "{0:8.5f}".format(tpm.v3GetRf(v3)) == \
        "{0:8.5f}".format(10934.266796)
    assert "{0:8.5f}".format(tpm.v3GetAlphaf(v3)) == \
        "{0:8.5f}".format(1.329037)
    assert "{0:8.5f}".format(tpm.v3GetDeltaf(v3)) == \
        "{0:8.5f}".format(1.127231)

# extern V3 v3cross(V3 v1, V3 v2);
def test_v3cross():
  v3_1 = tpm.V3()
  v3_2 = tpm.V3()
  
  tpm.v3SetTypef(v3_1, tpm.CARTESIAN);
  tpm.v3SetXf(v3_1, 1123.4556);
  tpm.v3SetYf(v3_1, 4556.1123);
  tpm.v3SetZf(v3_1, 9876.1267);

  tpm.v3SetTypef(v3_2, tpm.CARTESIAN);
  tpm.v3SetXf(v3_2, 2.3456);
  tpm.v3SetYf(v3_2, 6.7891);
  tpm.v3SetZf(v3_2, 7.8912);

  v3 = tpm.v3cross(v3_1, v3_2);

  assert "{0}".format(tpm.v3GetTypef(v3)) == \
      "{0}".format(tpm.CARTESIAN)
  assert "{0:8.5f}".format(tpm.v3GetRf(v3)) == \
      "{0:8.5f}".format(-31096.818397)
  assert "{0:8.5f}".format(tpm.v3GetAlphaf(v3)) == \
      "{0:8.5f}".format(14300.029957)
  assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
      "{0:8.5f}".format(-3059.564597)
  
# extern V3 v3diff(V3 v1, V3 v2);
def test_v3diff():
  v3_1 = tpm.V3()
  v3_2 = tpm.V3()
  
  tpm.v3SetTypef(v3_1, tpm.CARTESIAN);
  tpm.v3SetXf(v3_1, 1123.4556);
  tpm.v3SetYf(v3_1, 4556.1123);
  tpm.v3SetZf(v3_1, 9876.1267);

  tpm.v3SetTypef(v3_2, tpm.CARTESIAN);
  tpm.v3SetXf(v3_2, 2.3456);
  tpm.v3SetYf(v3_2, 6.7891);
  tpm.v3SetZf(v3_2, 7.8912);

  v3 = tpm.v3diff(v3_1, v3_2);

  assert "{0}".format(tpm.v3GetTypef(v3)) == \
      "{0}".format(tpm.CARTESIAN)
  assert "{0:8.5f}".format(tpm.v3GetRf(v3)) == \
      "{0:8.5f}".format(1123.4556 - 2.3456)
  assert "{0:8.5f}".format(tpm.v3GetAlphaf(v3)) == \
      "{0:8.5f}".format(4556.1123 - 6.7891)
  assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
      "{0:8.5f}".format(9876.1267 - 7.8912)

# extern V3 v3init(int type);
def test_v3init():

    v3 = tpm.v3init(tpm.CARTESIAN)
    
    assert "{0}".format(tpm.v3GetTypef(v3)) == \
        "{0}".format(tpm.CARTESIAN)
    assert "{0:8.5f}".format(tpm.v3GetXf(v3)) == \
        "{0:8.5f}".format(0)
    assert "{0:8.5f}".format(tpm.v3GetYf(v3)) == \
        "{0:8.5f}".format(0)
    assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
        "{0:8.5f}".format(0)

    v3 = tpm.v3init(tpm.SPHERICAL)
    
    assert "{0}".format(tpm.v3GetTypef(v3)) == \
        "{0}".format(tpm.SPHERICAL)
    assert "{0:8.5f}".format(tpm.v3GetRf(v3)) == \
        "{0:8.5f}".format(0)
    assert "{0:8.5f}".format(tpm.v3GetAlphaf(v3)) == \
        "{0:8.5f}".format(0)
    assert "{0:8.5f}".format(tpm.v3GetDeltaf(v3)) == \
        "{0:8.5f}".format(0)
    
    
# extern V3 v3s2c(V3 vs);
def test_v3s2c():
    v3 = tpm.V3()
    tpm.v3SetTypef(v3, tpm.SPHERICAL)
    tpm.v3SetRf(v3, 10934.266796);
    tpm.v3SetAlphaf(v3, 1.329037);
    tpm.v3SetDeltaf(v3, 1.127231);

    v3 = tpm.v3s2c(v3)
    # THIS IS REVERSE OF test_v3c2s BUT CAN ONLY GET ACCURACY OF
    # 8.2! WHY?
    #print tpm.v3GetXf(v3), tpm.v3GetYf(v3), tpm.v3GetZf(v3)
    assert "{0}".format(tpm.v3GetTypef(v3)) == \
        "{0}".format(tpm.CARTESIAN)
    assert "{0:8.2f}".format(tpm.v3GetXf(v3)) == \
        "{0:8.2f}".format(1123.4556)
    assert "{0:8.2f}".format(tpm.v3GetYf(v3)) == \
        "{0:8.2f}".format(4556.1123)
    assert "{0:8.2f}".format(tpm.v3GetZf(v3)) == \
        "{0:8.2f}".format(9876.1267)

# extern V3 v3scale(V3 v, double s);
def test_v3scale():
    v3 = tpm.V3()
    tpm.v3SetTypef(v3, tpm.SPHERICAL)
    tpm.v3SetRf(v3, 10934.266796);
    tpm.v3SetAlphaf(v3, 1.329037);
    tpm.v3SetDeltaf(v3, 1.127231);

    x = 12.345
    v3 = tpm.v3scale(v3, x)
    
    assert "{0}".format(tpm.v3GetTypef(v3)) == \
        "{0}".format(tpm.SPHERICAL)
    assert "{0:13.5f}".format(tpm.v3GetRf(v3)) == \
        "{0:13.5f}".format(10934.266796*x)

    v3 = tpm.v3init(tpm.CARTESIAN)
    tpm.v3SetXf(v3, 1.2345)
    tpm.v3SetYf(v3, 2.3456)
    tpm.v3SetZf(v3, 3.4567)

    v3 = tpm.v3scale(v3, x)
    assert "{0}".format(tpm.v3GetTypef(v3)) == \
        "{0}".format(tpm.CARTESIAN)
    assert "{0:8.5f}".format(tpm.v3GetXf(v3)) == \
        "{0:8.5f}".format(1.2345*x)
    assert "{0:8.5f}".format(tpm.v3GetYf(v3)) == \
        "{0:8.5f}".format(2.3456*x)
    assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
        "{0:8.5f}".format(3.4567*x)
    
# extern V3 v3sum(V3 v1, V3 v2);
def test_v3sum():
    v3_1 = tpm.V3()
    tpm.v3SetTypef(v3_1, tpm.CARTESIAN)
    tpm.v3SetRf(v3_1, 10934.266796);
    tpm.v3SetAlphaf(v3_1, 1.329037);
    tpm.v3SetDeltaf(v3_1, 1.127231);

    v3_2 = tpm.V3()
    tpm.v3SetTypef(v3_2, tpm.CARTESIAN)
    tpm.v3SetRf(v3_2, 10934.266796);
    tpm.v3SetAlphaf(v3_2, 1.329037);
    tpm.v3SetDeltaf(v3_2, 1.127231);

    v3 = tpm.v3sum(v3_1, v3_2)

    assert "{0:8.5f}".format(tpm.v3GetXf(v3)) == \
        "{0:8.5f}".format(10934.266796 * 2)
    assert "{0:8.5f}".format(tpm.v3GetYf(v3)) == \
        "{0:8.5f}".format(1.329037*2)
    assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
        "{0:8.5f}".format(1.127231*2)
    
# extern V3 v3unit(V3 v);
def test_v3unit():
    v3 = tpm.v3init(tpm.CARTESIAN)
    tpm.v3SetXf(v3, 12.34567)
    tpm.v3SetYf(v3, 34.56712)
    tpm.v3SetZf(v3, 56.71234)

    v3 = tpm.v3unit(v3)

    assert "{0:8.6f}".format(tpm.v3GetXf(v3)) == \
        "{0:8.6f}".format(0.182752)
    assert "{0:8.6f}".format(tpm.v3GetYf(v3)) == \
        "{0:8.6f}".format(0.511693)
    assert "{0:8.5f}".format(tpm.v3GetZf(v3)) == \
        "{0:8.5f}".format(0.839507)
    
# extern V3 v62v3(V6 v6, double dt);
def test_v62v3():
  v6 = setup_cartesian_v6_with_2_v3()
  v3_1 = tpm.v62v3(v6, 1.234);

  assert "{0:8.6f}".format(tpm.v3GetXf(v3_1)) == \
      "{0:8.6f}".format(1126.350070)
  assert "{0:8.6f}".format(tpm.v3GetYf(v3_1)) == \
      "{0:8.6f}".format(4564.490049)
  assert "{0:8.6f}".format(tpm.v3GetZf(v3_1)) == \
      "{0:8.6f}".format(9885.864441)
  
# extern V6 m3v6(M3 m, V6 v1);
def test_m3v6():

  v6 = setup_cartesian_v6_with_2_v3()
  m3_1 = setup_m3()
  
  v6 = tpm.m3v6(m3_1, v6)

  assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
      "{0:8.5f}".format(3957.044574)
  assert "{0:11.5f}".format(tpm.v6GetYf(v6)) == \
      "{0:11.5f}".format(12274.891734)
  assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
      "{0:8.5f}".format(4391.273203)
  assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
      "{0:8.5f}".format(5.211656)
  assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
      "{0:8.5f}".format(11.918743)
  assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
      "{0:8.5f}".format(5.049773)

  
# extern V6 m6v6(M6 m, V6 v1);
def test_m6v6():
    v6 = setup_cartesian_v6_with_2_v3()
    m6 = setup_m6_with_4_m3()
    
    v6 = tpm.m6v6(m6, v6)
    
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
      "{0:8.5f}".format(3963.007140)
    assert "{0:11.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:11.5f}".format(12288.530799)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(4394.724590)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(5192.064570)
    assert "{0:9.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:9.5f}".format(12879.839282)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(4997.127521)

# extern V6 v32v6(V3 v3);
def test_v32v6():
    v6 = tpm.v6init(tpm.CARTESIAN)
    v3 = setup_cartesian_v3()
    v6 = tpm.v32v6(v3)
    
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
        "{0:8.5f}".format(1123.4556)
    assert "{0:11.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:11.5f}".format(4556.1123)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(9876.1267)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(0.0)


# extern V6 v6c2s(V6 vc);
def test_v6c2s():
    v6 = setup_cartesian_v6_with_2_v3()
    v6 = tpm.v6c2s(v6)

    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
        "{0:8.5f}".format(10934.266796)
    assert "{0:11.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:11.5f}".format(1.329037)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(1.127231)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(10.197444)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(-0.000139)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(-0.000281)
    
# extern V6 v6cross(V6 v1, V6 v2);
def test_v6cross():
    v6_1 = setup_cartesian_v6_with_2_v3()
    
    v3_1 = tpm.v3init(tpm.CARTESIAN)
    v3_2 = tpm.v3init(tpm.CARTESIAN)
    v6_2 = tpm.v6init(tpm.CARTESIAN)
 
    tpm.v3SetTypef(v3_1, tpm.CARTESIAN)
    tpm.v3SetXf(v3_1, 65.234556)
    tpm.v3SetYf(v3_1, 32.561123)
    tpm.v3SetZf(v3_1, 76.761267)
        
    tpm.v3SetTypef(v3_2, tpm.CARTESIAN)
    tpm.v3SetXf(v3_2, 0.6543)
    tpm.v3SetYf(v3_2, 0.1987)
    tpm.v3SetZf(v3_2, 0.2189)
    
    tpm.v6SetPosf(v6_2, v3_1)
    tpm.v6SetVelf(v6_2, v3_2)
        
    tpm.v6SetTypef(v6_2, tpm.CARTESIAN)
        
    v6 = tpm.v6cross(v6_1, v6_2)
 
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
        "{0:8.5f}".format(28155.176500)
    assert "{0:11.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:11.5f}".format(558026.865000)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(-260634.987000)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    
# extern V6 v6diff(V6 v1, V6 v2);
def test_v6diff():
    v6_1 = setup_cartesian_v6_with_2_v3()
    
    v3_1 = tpm.v3init(tpm.CARTESIAN)
    v3_2 = tpm.v3init(tpm.CARTESIAN)
    v6_2 = tpm.v6init(tpm.CARTESIAN)
 
    tpm.v3SetTypef(v3_1, tpm.CARTESIAN)
    tpm.v3SetXf(v3_1, 65.234556)
    tpm.v3SetYf(v3_1, 32.561123)
    tpm.v3SetZf(v3_1, 76.761267)
        
    tpm.v3SetTypef(v3_2, tpm.CARTESIAN)
    tpm.v3SetXf(v3_2, 0.6543)
    tpm.v3SetYf(v3_2, 0.1987)
    tpm.v3SetZf(v3_2, 0.2189)
    
    tpm.v6SetPosf(v6_2, v3_1)
    tpm.v6SetVelf(v6_2, v3_2)
        
    tpm.v6SetTypef(v6_2, tpm.CARTESIAN)
        
    v6 = tpm.v6diff(v6_1, v6_2)
 
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
        "{0:8.5f}".format(1123.4556 - 65.234556)
    assert "{0:11.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:11.5f}".format(4556.1123 - 32.561123)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(9876.1267 - 76.761267)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(2.3456 - 0.6543)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(6.7891 - 0.1987)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(7.8912 - 0.2189)

# extern V6 v6init(int type);
def test_v6init():
    v6 = tpm.v6init(tpm.CARTESIAN)

    assert tpm.v6GetTypef(v6) == tpm.CARTESIAN
    
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:11.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:11.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(0.0)

    v6 = tpm.v6init(tpm.SPHERICAL)

    assert tpm.v6GetTypef(v6) == tpm.SPHERICAL
    
    assert "{0:8.5f}".format(tpm.v6GetRf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:11.5f}".format(tpm.v6GetAlphaf(v6)) == \
        "{0:11.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetDeltaf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetRDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetAlphaDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    assert "{0:8.5f}".format(tpm.v6GetDeltaDotf(v6)) == \
        "{0:8.5f}".format(0.0)
    
# extern V6 v6s2c(V6 vs);
def test_v6s2c():
    v3_1 = tpm.v3init(tpm.SPHERICAL)
    v3_2 = tpm.v3init(tpm.SPHERICAL)
    v6 = tpm.v6init(tpm.SPHERICAL)
  
    tpm.v3SetTypef(v3_1, tpm.SPHERICAL)
    tpm.v3SetRf(v3_1, 10934.266796)
    tpm.v3SetAlphaf(v3_1, 1.329037)
    tpm.v3SetDeltaf(v3_1, 1.127231)
    
    tpm.v3SetTypef(v3_2, tpm.SPHERICAL)
    tpm.v3SetXf(v3_2, 10.197444)
    tpm.v3SetYf(v3_2, -0.000139)
    tpm.v3SetZf(v3_2, -0.000281)
    
    tpm.v6SetPosf(v6, v3_1)
    tpm.v6SetVelf(v6, v3_2)
    
    tpm.v6SetTypef(v6, tpm.SPHERICAL)

    v6 = tpm.v6s2c(v6)
    
    # THIS IS REVERSE OF test_v6c2s BUT CAN ONLY GET ACCURACY OF
    # 8.2! WHY?
    # Also see test_v3c2s.
    assert "{0:8.2f}".format(tpm.v6GetXf(v6)) == \
       "{0:8.2f}".format(1123.4556)
    assert "{0:8.2f}".format(tpm.v6GetYf(v6)) == \
        "{0:8.2f}".format(4556.1123)
    assert "{0:8.2f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.2f}".format(9876.1267)
    assert "{0:8.2f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.2f}".format(2.3456)
    assert "{0:8.2f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.2f}".format(6.7891)
    assert "{0:8.2f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.2f}".format(7.8912)
    
# extern V6 v6scale(V6 v, double s);
def test_v6scale():
    v6 = setup_cartesian_v6_with_2_v3()
    v6 = tpm.v6scale(v6, 1.2345)
    
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
       "{0:8.5f}".format(1123.4556*1.2345)
    assert "{0:8.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:8.5f}".format(4556.1123*1.2345)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(9876.1267*1.2345)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(2.3456*1.2345)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(6.7891*1.2345)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(7.8912*1.2345)
        
# extern V6 v6sum(V6 v1, V6 v2);
def test_v6sum():
    v6_1 = setup_cartesian_v6_with_2_v3()
    v6_2 = tpm.v6scale(v6_1, 1.2345)
    v6 = tpm.v6sum(v6_1, v6_2)
    
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
       "{0:8.5f}".format(1123.4556 * 2.2345)
    assert "{0:8.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:8.5f}".format(4556.1123*2.2345)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(9876.1267*2.2345)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(2.3456*2.2345)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(6.7891*2.2345)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(7.8912*2.2345)
        
# extern V6 v6unit(V6 v);
def test_v6unit():
    v6 = setup_cartesian_v6_with_2_v3()
    v6 = tpm.v6unit(v6)
    
    assert "{0:8.5f}".format(tpm.v6GetXf(v6)) == \
       "{0:8.5f}".format(0.102746)
    assert "{0:8.5f}".format(tpm.v6GetYf(v6)) == \
        "{0:8.5f}".format(0.416682)
    assert "{0:8.5f}".format(tpm.v6GetZf(v6)) == \
        "{0:8.5f}".format(0.903227)
    assert "{0:8.5f}".format(tpm.v6GetXDotf(v6)) == \
        "{0:8.5f}".format(0.000215)
    assert "{0:8.5f}".format(tpm.v6GetYDotf(v6)) == \
        "{0:8.5f}".format(0.000621)
    assert "{0:8.5f}".format(tpm.v6GetZDotf(v6)) == \
        "{0:8.5f}".format(0.000722)
    
# extern char *m3fmt(M3 m);
def test_m3fmt():
    m3 = setup_m3()
    s = tpm.m3fmt(m3)
    s = s.splitlines()

    assert s[0].strip() ==\
        "2.345000000000000e-01  5.432000000000000e-01  1.234000000000000e-01"
    assert s[1].strip() == \
        "5.467000000000000e-01  4.190000000000000e-01  9.874000000000001e-01"
    assert s[2].strip() == \
        "1.225000000000000e-01  4.331000000000000e-01  2.309000000000000e-01"

# extern char *m6fmt(M6 m);
def test_m6fmt():
    m6 = setup_m6_with_4_m3()
    s = tpm.m6fmt(m6)
    s = s.splitlines()

    assert s[0].strip() == \
        """2.345000000000000e-01  5.432000000000000e-01  1.234000000000000e-01  4.523000000000000e-01  3.254000000000000e-01  3.412000000000000e-01"""
    assert s[1].strip() == \
        """5.467000000000000e-01  4.190000000000000e-01  9.874000000000001e-01  6.754000000000000e-01  9.041000000000000e-01  7.498000000000000e-01"""
    assert s[2].strip() == \
        """1.225000000000000e-01  4.331000000000000e-01  2.309000000000000e-01  2.512000000000000e-01  3.143000000000000e-01  9.229999999999999e-02"""
    assert s[3].strip() == \
        """4.253000000000000e-01  3.524000000000000e-01  3.142000000000000e-01  3.524000000000000e-01  4.235000000000000e-01  2.413000000000000e-01"""
    assert s[4].strip() == \
        """6.574000000000000e-01  9.401000000000000e-01  7.948000000000000e-01  4.756000000000000e-01  1.049000000000000e-01  8.497000000000000e-01"""
    assert s[5].strip() == \
        """2.152000000000000e-01  4.133000000000000e-01  2.903000000000000e-01  2.512000000000000e-01  3.314000000000000e-01  3.092000000000000e-01"""


# extern char *v3fmt(V3 v);
def test_v3fmt():
    v3 = setup_cartesian_v3()
    s = tpm.v3fmt(v3)
    s = s.strip()

    assert s == \
        "1.123455600000000e+03  4.556112300000000e+03  9.876126700000001e+03"

# extern char *v6fmt(V6 v);
def test_v6fmt():
    v6 = setup_cartesian_v6_with_2_v3()
    s = tpm.v6fmt(v6).strip()
    assert s == \
        """1.123455600000000e+03  4.556112300000000e+03  9.876126700000001e+03  2.345600000000000e+00  6.789100000000000e+00  7.891200000000000e+00"""


# extern double v3alpha(V3 v);
def test_v3alpha():
    # Return ra in V3 scaled to [0, 2 π]
    # Loops over this range i.e.,  0 2π|0 2π ; 361 is 1; -1 is 359.0
    # As opposed to wrapping i.e., 2π 0 2π 0 2π; 361 is 359, -1 is 359

    v3 = tpm.v3init(tpm.SPHERICAL)

    tpm.v3SetAlphaf(v3, math.radians(-180.0))
    assert "{0:7.3f}".format(tpm.v3alpha(v3)) == \
        "{0:7.3f}".format(math.radians(180.0))

    tpm.v3SetAlphaf(v3, math.radians(-45.0))
    assert "{0:7.3f}".format(tpm.v3alpha(v3)) == \
        "{0:7.3f}".format(math.radians(360-45))
    
    tpm.v3SetAlphaf(v3, math.radians(20.0))
    assert "{0:7.3f}".format(tpm.v3alpha(v3)) == \
        "{0:7.3f}".format(math.radians(20.0))

    tpm.v3SetAlphaf(v3, math.radians(361.0))
    assert "{0:7.3f}".format(tpm.v3alpha(v3)) == \
        "{0:7.3f}".format(math.radians(1.0))

    tpm.v3SetAlphaf(v3, math.radians(-1))
    assert "{0:7.3f}".format(tpm.v3alpha(v3)) == \
        "{0:7.3f}".format(math.radians(359.0))

# extern double v3delta(V3 v);    
def test_v3delta():
    # Return ra in V3 scaled to [-π/2, π/2]
    # Wraps over this range i.e., 90 0 -90 0 90 0 90; -91 is -89
    # As opposed to looping i.e., 0 90|-90 0 90|-90 0 90|-90; -91 is 89
    v3 = tpm.v3init(tpm.SPHERICAL)

    tpm.v3SetDeltaf(v3, math.radians(-180.0))
    assert "{0:7.3f}".format(tpm.v3delta(v3)) == \
        "{0:7.3f}".format(math.radians(0.0))

    tpm.v3SetDeltaf(v3, math.radians(-45.0))
    assert "{0:7.3f}".format(tpm.v3delta(v3)) == \
        "{0:7.3f}".format(math.radians(-45.0))
    
    tpm.v3SetDeltaf(v3, math.radians(200.0))
    assert "{0:7.3f}".format(tpm.v3delta(v3)) == \
        "{0:7.3f}".format(math.radians(-20.0))

    tpm.v3SetDeltaf(v3, math.radians(-280.0))
    assert "{0:7.3f}".format(tpm.v3delta(v3)) == \
        "{0:7.3f}".format(math.radians(90-10.0))

    tpm.v3SetDeltaf(v3, math.radians(-91))
    assert "{0:7.3f}".format(tpm.v3delta(v3)) == \
        "{0:7.3f}".format(math.radians(-89))    
    
# extern double v3dot(V3 v1, V3 v2);
def test_v3dot():
    v3_1 = tpm.v3init(tpm.CARTESIAN)
    v3_2 = tpm.v3init(tpm.CARTESIAN)
    
    tpm.v3SetTypef(v3_1, tpm.CARTESIAN)
    tpm.v3SetXf(v3_1, 1123.4556)
    tpm.v3SetYf(v3_1, 4556.1123)
    tpm.v3SetZf(v3_1, 9876.1267)
    
    tpm.v3SetTypef(v3_2, tpm.CARTESIAN)
    tpm.v3SetXf(v3_2, 2.3456)
    tpm.v3SetYf(v3_2, 6.7891)
    tpm.v3SetZf(v3_2, 7.8912)

    x = tpm.v3dot(v3_1, v3_2)

    assert "{0:11.5f}".format(x) == \
        "{0:11.5f}".format(111501.570486)
    
# extern double v3mod(V3 v);
def test_v3mod():
    v3 = setup_cartesian_v3()
    x = tpm.v3mod(v3)

    assert "{0:11.5f}".format(x) == \
        "{0:11.5f}".format(10934.266796)


# extern double v6alpha(V6 v);
def test_v6alpha():
    # Return ra in V3 scaled to [0, 2 π]
    # Loops over this range i.e.,  0 2π|0 2π ; 361 is 1; -1 is 359.0
    # As opposed to wrapping i.e., 2π 0 2π 0 2π; 361 is 359, -1 is 359

    v6 = tpm.v6init(tpm.SPHERICAL)

    tpm.v6SetAlphaf(v6, math.radians(-180.0))
    assert "{0:7.3f}".format(tpm.v6alpha(v6)) == \
        "{0:7.3f}".format(math.radians(180.0))

    tpm.v6SetAlphaf(v6, math.radians(-45.0))
    assert "{0:7.3f}".format(tpm.v6alpha(v6)) == \
        "{0:7.3f}".format(math.radians(360-45))
    
    tpm.v6SetAlphaf(v6, math.radians(20.0))
    assert "{0:7.3f}".format(tpm.v6alpha(v6)) == \
        "{0:7.3f}".format(math.radians(20.0))

    tpm.v6SetAlphaf(v6, math.radians(361.0))
    assert "{0:7.3f}".format(tpm.v6alpha(v6)) == \
        "{0:7.3f}".format(math.radians(1.0))

    tpm.v6SetAlphaf(v6, math.radians(-1))
    assert "{0:7.3f}".format(tpm.v6alpha(v6)) == \
        "{0:7.3f}".format(math.radians(359.0))

# extern double v6delta(V6 v);
def test_v6delta():
    # Return ra in V6 scaled to [-π/2, π/2]
    # Wraps over this range i.e., 90 0 -90 0 90 0 90; -91 is -89
    # As opposed to looping i.e., 0 90|-90 0 90|-90 0 90|-90; -91 is 89
    v6 = tpm.v6init(tpm.SPHERICAL)

    tpm.v6SetDeltaf(v6, math.radians(-180.0))
    assert "{0:7.3f}".format(tpm.v6delta(v6)) == \
        "{0:7.3f}".format(math.radians(0.0))

    tpm.v6SetDeltaf(v6, math.radians(-45.0))
    assert "{0:7.3f}".format(tpm.v6delta(v6)) == \
        "{0:7.3f}".format(math.radians(-45.0))
    
    tpm.v6SetDeltaf(v6, math.radians(200.0))
    assert "{0:7.3f}".format(tpm.v6delta(v6)) == \
        "{0:7.3f}".format(math.radians(-20.0))

    tpm.v6SetDeltaf(v6, math.radians(-280.0))
    assert "{0:7.3f}".format(tpm.v6delta(v6)) == \
        "{0:7.3f}".format(math.radians(90-10.0))

    tpm.v6SetDeltaf(v6, math.radians(-91))
    assert "{0:7.3f}".format(tpm.v6delta(v6)) == \
        "{0:7.3f}".format(math.radians(-89))    

# extern double v6dot(V6 v1, V6 v2);
def test_v6dot():
    v6_1 = setup_cartesian_v6_with_2_v3()
    
    v3_1 = tpm.v3init(tpm.CARTESIAN)
    v3_2 = tpm.v3init(tpm.CARTESIAN)
    v6_2 = tpm.v6init(tpm.CARTESIAN)
 
    tpm.v3SetTypef(v3_1, tpm.CARTESIAN)
    tpm.v3SetXf(v3_1, 65.234556)
    tpm.v3SetYf(v3_1, 32.561123)
    tpm.v3SetZf(v3_1, 76.761267)
        
    tpm.v3SetTypef(v3_2, tpm.CARTESIAN)
    tpm.v3SetXf(v3_2, 0.6543)
    tpm.v3SetYf(v3_2, 0.1987)
    tpm.v3SetZf(v3_2, 0.2189)
    
    tpm.v6SetPosf(v6_2, v3_1)
    tpm.v6SetVelf(v6_2, v3_2)
        
    tpm.v6SetTypef(v6_2, tpm.CARTESIAN)
        
    x = tpm.v6dot(v6_1, v6_2)
 
    assert "{0:12.5f}".format(x) == \
        "{0:12.5f}".format(979744.258798)
    
# extern double v6mod(V6 v);
def test_v6mod():
    v6 = setup_cartesian_v6_with_2_v3()

    assert "{0:12.5f}".format(tpm.v6mod(v6)) == \
        "{0:12.5f}".format(10934.266796)