"""Tests for functions defined in m3Functions.c.

These functions are used for accessing and manipulating M3 vectors.

:author: Prasanth Nair
:contact: prasanthhn@gmail.com
"""
import setup_path
setup_path.run()

from pytpm import tpm

m3 = tpm.M3()
XX = 1.0
XY = 2.0
XZ = 3.0
YX = 4.0
YY = 5.0
YZ = 6.0
ZX = 7.0
ZY = 8.0
ZZ = 9.0
f = 2.2 # decrement, increment etc.,

# TODO: test m3Set* after wrapping m3I.

def setup_m3():
    # perhaps there is a simpler C routine (m3I?).
    tpm.m3SetXXf(m3, XX)
    tpm.m3SetXYf(m3, XY)
    tpm.m3SetXZf(m3, XZ)
    tpm.m3SetYXf(m3, YX)
    tpm.m3SetYYf(m3, YY)
    tpm.m3SetYZf(m3, YZ)
    tpm.m3SetZXf(m3, ZX)
    tpm.m3SetZYf(m3, ZY)
    tpm.m3SetZZf(m3, ZZ)

def test_m3DecXXf():
    setup_m3()
    tpm.m3DecXXf(m3, f)
    assert tpm.m3GetXXf(m3) == XX - f
    
def test_m3DecXYf():
    setup_m3()
    tpm.m3DecXYf(m3, f)
    assert tpm.m3GetXYf(m3) == XY - f

def test_m3DecXZf():
    setup_m3()
    tpm.m3DecXZf(m3, f)
    assert tpm.m3GetXZf(m3) == XZ - f

def test_m3DecYXf():
    setup_m3()
    tpm.m3DecYXf(m3, f)
    assert tpm.m3GetYXf(m3) == YX - f

def test_m3DecYYf():
    setup_m3()
    tpm.m3DecYYf(m3, f)
    assert tpm.m3GetYYf(m3) == YY - f

def test_m3DecYZf():
    setup_m3()
    tpm.m3DecYZf(m3, f)
    assert tpm.m3GetYZf(m3) == YZ - f

def test_m3DecZXf():
    setup_m3()
    tpm.m3DecZXf(m3, f)
    assert tpm.m3GetZXf(m3) == ZX - f

def test_m3DecZYf():
    setup_m3()
    tpm.m3DecZYf(m3, f)
    assert tpm.m3GetZYf(m3) == ZY - f

def test_m3DecZZf():
    setup_m3()
    tpm.m3DecZZf(m3, f)
    assert tpm.m3GetZZf(m3) == ZZ - f

def test_m3DivXXf():
    setup_m3()
    tpm.m3DivXXf(m3, f)
    assert tpm.m3GetXXf(m3) == XX / f

def test_m3DivXYf():
    setup_m3()
    tpm.m3DivXYf(m3, f)
    assert tpm.m3GetXYf(m3) == XY / f

def test_m3DivXZf():
    setup_m3()
    tpm.m3DivXZf(m3, f)
    assert tpm.m3GetXZf(m3) == XZ / f

def test_m3DivYXf():
    setup_m3()
    tpm.m3DivYXf(m3, f)
    assert tpm.m3GetYXf(m3) == YX / f

def test_m3DivYYf():
    setup_m3()
    tpm.m3DivYYf(m3, f)
    assert tpm.m3GetYYf(m3) == YY / f

def test_m3DivYZf():
    setup_m3()
    tpm.m3DivYZf(m3, f)
    assert tpm.m3GetYZf(m3) == YZ / f

def test_m3DivZXf():
    setup_m3()
    tpm.m3DivZXf(m3, f)
    assert tpm.m3GetZXf(m3) == ZX / f

def test_m3DivZYf():
    setup_m3()
    tpm.m3DivZYf(m3, f)
    assert tpm.m3GetZYf(m3) == ZY / f

def test_m3DivZZf():
    setup_m3()
    tpm.m3DivZZf(m3, f)
    assert tpm.m3GetZZf(m3) == ZZ / f

def test_m3IncXXf():
    setup_m3()
    tpm.m3IncXXf(m3, f)
    assert tpm.m3GetXXf(m3) == XX + f

def test_m3IncXYf():
    setup_m3()
    tpm.m3IncXYf(m3, f)
    assert tpm.m3GetXYf(m3) == XY + f

def test_m3IncXZf():
    setup_m3()
    tpm.m3IncXZf(m3, f)
    assert tpm.m3GetXZf(m3) == XZ + f

def test_m3IncYXf():
    setup_m3()
    tpm.m3IncYXf(m3, f)
    assert tpm.m3GetYXf(m3) == YX + f

def test_m3IncYYf():
    setup_m3()
    tpm.m3IncYYf(m3, f)
    assert tpm.m3GetYYf(m3) == YY + f

def test_m3IncYZf():
    setup_m3()
    tpm.m3IncYZf(m3, f)
    assert tpm.m3GetYZf(m3) == YZ + f

def test_m3IncZXf():
    setup_m3()
    tpm.m3IncZXf(m3, f)
    assert tpm.m3GetZXf(m3) == ZX + f

def test_m3IncZYf():
    setup_m3()
    tpm.m3IncZYf(m3, f)
    assert tpm.m3GetZYf(m3) == ZY + f

def test_m3IncZZf():
    setup_m3()
    tpm.m3IncZZf(m3, f)
    assert tpm.m3GetZZf(m3) == ZZ + f

def test_m3MulXXf():
    setup_m3()
    tpm.m3MulXXf(m3, f)
    assert tpm.m3GetXXf(m3) == XX * f

def test_m3MulXYf():
    setup_m3()
    tpm.m3MulXYf(m3, f)
    assert tpm.m3GetXYf(m3) == XY * f

def test_m3MulXZf():
    setup_m3()
    tpm.m3MulXZf(m3, f)
    assert tpm.m3GetXZf(m3) == XZ * f

def test_m3MulYXf():
    setup_m3()
    tpm.m3MulYXf(m3, f)
    assert tpm.m3GetYXf(m3) == YX * f

def test_m3MulYYf():
    setup_m3()
    tpm.m3MulYYf(m3, f)
    assert tpm.m3GetYYf(m3) == YY * f

def test_m3MulYZf():
    setup_m3()
    tpm.m3MulYZf(m3, f)
    assert tpm.m3GetYZf(m3) == YZ * f

def test_m3MulZXf():
    setup_m3()
    tpm.m3MulZXf(m3, f)
    assert tpm.m3GetZXf(m3) == ZX * f

def test_m3MulZYf():
    setup_m3()
    tpm.m3MulZYf(m3, f)
    assert tpm.m3GetZYf(m3) == ZY * f

def test_m3MulZZf():
    setup_m3()
    tpm.m3MulZZf(m3, f)
    assert tpm.m3GetZZf(m3) == ZZ * f
    
def run():
    test_m3DecXXf()
    test_m3DecXYf()
    test_m3DecXZf()
    test_m3DecYXf()
    test_m3DecYXf()
    test_m3DecYYf()
    test_m3DecYZf()
    test_m3DecZXf()
    test_m3DecZYf()
    test_m3DecZZf()
    test_m3DivXXf()
    test_m3DivXYf()
    test_m3DivXZf()
    test_m3DivYXf()
    test_m3DivYXf()
    test_m3DivYYf()
    test_m3DivYZf()
    test_m3DivZXf()
    test_m3DivZYf()
    test_m3DivZZf()
    test_m3IncXXf()
    test_m3IncXYf()
    test_m3IncXZf()
    test_m3IncYXf()
    test_m3IncYXf()
    test_m3IncYYf()
    test_m3IncYZf()
    test_m3IncZXf()
    test_m3IncZYf()
    test_m3IncZZf()
    test_m3MulXXf()
    test_m3MulXYf()
    test_m3MulXZf()
    test_m3MulYXf()
    test_m3MulYXf()
    test_m3MulYYf()
    test_m3MulYZf()
    test_m3MulZXf()
    test_m3MulZYf()
    test_m3MulZZf()

                  
    
if __name__ == '__main__':
    print "Running test on functions defined in m3Functions.c ..."
    run()
