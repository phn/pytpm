"""Tests for functions defined in v6Functions.c.

These functions are used for accessing and manipulating V6 vectors.

:author: Prasanth Nair
:contact: prasanthhn@gmail.com
"""
from pytpm import tpm

# Some values for testing, values themselves do not have any special
# meaning 
t = 0
x = 12.3456
y = 78.9012
z = -34.5678
xdot = 123.456
ydot = 789.012
zdot = 345.678
r = x
alpha = y
delta = z
rdot = xdot
alphadot = ydot
deltadot = zdot
f = 2.0 # decrement, increment, div, mul factor
fdot = 0.2
ra = y
dec = z
radot = ydot
decdot = zdot

v6xyz = tpm.V6()
v6rad = tpm.V6()
v3posxyz = tpm.V3()
v3velxyz = tpm.V3()
v3posrad = tpm.V3()
v3velrad = tpm.V3()

def setup_v3posxyz():
    tpm.v3SetTypef(v3posxyz,0)
    tpm.v3SetXf(v3posxyz,x)
    tpm.v3SetYf(v3posxyz,y)
    tpm.v3SetZf(v3posxyz,z)

def setup_v3posrad():
    tpm.v3SetTypef(v3posrad, 1)
    tpm.v3SetRf(v3posrad,r)
    tpm.v3SetAlphaf(v3posrad,alpha)
    tpm.v3SetDeltaf(v3posrad,delta)

def setup_v3velxyz():
    # There is no v3SetXDotf etc., .
    tpm.v3SetTypef(v3velxyz, 0)
    tpm.v3SetXf(v3velxyz,xdot)
    tpm.v3SetYf(v3velxyz,ydot)
    tpm.v3SetZf(v3velxyz,zdot)

def setup_v3velrad():
    tpm.v3SetTypef(v3velrad, 1)
    tpm.v3SetRf(v3velrad,rdot)
    tpm.v3SetAlphaf(v3velrad,alphadot)
    tpm.v3SetDeltaf(v3velrad,deltadot)

def setup_v6xyz():
    setup_v3posxyz()
    setup_v3velxyz()
    tpm.v6SetPosf(v6xyz, v3posxyz)
    tpm.v6SetVelf(v6xyz, v3velxyz)

def setup_v6rad():
    setup_v3posrad()
    setup_v3velrad()
    tpm.v6SetPosf(v6rad, v3posrad)
    tpm.v6SetVelf(v6rad, v3velrad)

def test_v6SetPosf():
    setup_v6xyz()
    tpm.v6SetPosf(v6xyz, v3posxyz)
    tpm.v6SetPosf(v6rad, v3posrad)
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v3GetXf(v3_tmp) == tpm.v3GetXf(v3posxyz)
    assert tpm.v3GetYf(v3_tmp) == tpm.v3GetYf(v3posxyz)
    assert tpm.v3GetZf(v3_tmp) == tpm.v3GetZf(v3posxyz)
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v3GetRf(v3_tmp) == tpm.v3GetRf(v3posrad)
    assert tpm.v3GetAlphaf(v3_tmp) == tpm.v3GetAlphaf(v3posrad)
    assert tpm.v3GetDeltaf(v3_tmp) == tpm.v3GetDeltaf(v3posrad)


def test_v6DecXf():
    setup_v6xyz()
    tpm.v6DecXf(v6xyz, f)
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v3GetXf(v3_tmp) == x - f

def test_v6DecYf():
    setup_v6xyz()
    tpm.v6DecYf(v6xyz, f)
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v3GetYf(v3_tmp) == y - f

def test_v6DecZf():
    setup_v6xyz()
    tpm.v6DecZf(v6xyz, f)
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v3GetZf(v3_tmp) == z - f

def test_v6DecXDotf():
    setup_v6xyz()
    tpm.v6DecXDotf(v6xyz, fdot)
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v3GetXf(v3_tmp) == xdot - fdot

def test_v6DecYDotf():
    setup_v6xyz()
    tpm.v6DecYDotf(v6xyz, fdot)
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v3GetYf(v3_tmp) == ydot - fdot

def test_v6DecZDotf():
    setup_v6xyz()
    tpm.v6DecZDotf(v6xyz, fdot)
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v3GetZf(v3_tmp) == zdot - fdot

def test_v6DecRf():
    setup_v6rad()
    tpm.v6DecRf(v6rad, f)
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v3GetRf(v3_tmp) == r - f

def test_v6DecAlphaf():
    setup_v6rad()
    tpm.v6DecAlphaf(v6rad, f)
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v3GetAlphaf(v3_tmp) == alpha - f

def test_v6DecDeltaf():
    setup_v6rad()
    tpm.v6DecDeltaf(v6rad, f)
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v3GetDeltaf(v3_tmp) == delta - f

def test_v6DecRDotf():
    setup_v6rad()
    tpm.v6DecRDotf(v6rad, fdot)
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v3GetRf(v3_tmp) == rdot - fdot

def test_v6DecAlphaDotf():
    setup_v6rad()
    tpm.v6DecAlphaDotf(v6rad, fdot)
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v3GetAlphaf(v3_tmp) == alphadot - fdot

def test_v6DecDeltaDotf():
    setup_v6rad()
    tpm.v6DecDeltaDotf(v6rad, fdot)
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v3GetDeltaf(v3_tmp) == deltadot - fdot

def test_v6DivXf():
    setup_v6xyz()
    tpm.v6DivXf(v6xyz, f)
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v3GetXf(v3_tmp) == x / f

def test_v6DivYf():
    setup_v6xyz()
    tpm.v6DivYf(v6xyz, f)
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v3GetYf(v3_tmp) == y / f

def test_v6DivZf():
    setup_v6xyz()
    tpm.v6DivZf(v6xyz, f)
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v3GetZf(v3_tmp) == z / f

def test_v6DivXDotf():
    setup_v6xyz()
    tpm.v6DivXDotf(v6xyz, fdot)
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v3GetXf(v3_tmp) == xdot / fdot

def test_v6DivYDotf():
    setup_v6xyz()
    tpm.v6DivYDotf(v6xyz, fdot)
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v3GetYf(v3_tmp) == ydot / fdot

def test_v6DivZDotf():
    setup_v6xyz()
    tpm.v6DivZDotf(v6xyz, fdot)
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v3GetZf(v3_tmp) == zdot / fdot

def test_v6DivRf():
    setup_v6rad()
    tpm.v6DivRf(v6rad, f)
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v3GetRf(v3_tmp) == r / f

def test_v6DivAlphaf():
    setup_v6rad()
    tpm.v6DivAlphaf(v6rad, f)
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v3GetAlphaf(v3_tmp) == alpha / f

def test_v6DivDeltaf():
    setup_v6rad()
    tpm.v6DivDeltaf(v6rad, f)
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v3GetDeltaf(v3_tmp) == delta / f

def test_v6DivRDotf():
    setup_v6rad()
    tpm.v6DivRDotf(v6rad, fdot)
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v3GetRf(v3_tmp) == rdot / fdot

def test_v6DivAlphaDotf():
    setup_v6rad()
    tpm.v6DivAlphaDotf(v6rad, fdot)
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v3GetAlphaf(v3_tmp) == alphadot / fdot

def test_v6DivDeltaDotf():
    setup_v6rad()
    tpm.v6DivDeltaDotf(v6rad, fdot)
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v3GetDeltaf(v3_tmp) == deltadot / fdot
    
def test_v6GetTypef():
    setup_v6xyz()
    assert tpm.v6GetTypef(v6xyz) == 0
    setup_v6rad()
    assert tpm.v6GetTypef(v6rad) == 1

def test_v6GetXf():
    setup_v6xyz()
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v6GetXf(v6xyz) == tpm.v3GetXf(v3_tmp)

def test_v6GetYf():
    setup_v6xyz()
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v6GetYf(v6xyz) == tpm.v3GetYf(v3_tmp)

def test_v6GetZf():
    setup_v6xyz()
    v3_tmp = tpm.v6GetPosf(v6xyz)
    assert tpm.v6GetZf(v6xyz) == tpm.v3GetZf(v3_tmp)

def test_v6GetXDotf():
    # There is no v3GetXDotf, v3GetRDotf etc...
    setup_v6xyz()
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v6GetXDotf(v6xyz) == tpm.v3GetXf(v3_tmp)

def test_v6GetYDotf():
    setup_v6xyz()
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v6GetYDotf(v6xyz) == tpm.v3GetYf(v3_tmp)

def test_v6GetZDotf():
    setup_v6xyz()
    v3_tmp = tpm.v6GetVelf(v6xyz)
    assert tpm.v6GetZDotf(v6xyz) == tpm.v3GetZf(v3_tmp)

    
def test_v6GetRf():
    setup_v6rad()
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v6GetRf(v6rad) == tpm.v3GetRf(v3_tmp)

def test_v6GetAlphaf():
    setup_v6rad()
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v6GetAlphaf(v6rad) == tpm.v3GetAlphaf(v3_tmp)

def test_v6GetDeltaf():
    setup_v6rad()
    v3_tmp = tpm.v6GetPosf(v6rad)
    assert tpm.v6GetDeltaf(v6rad) == tpm.v3GetDeltaf(v3_tmp)

def test_v6GetRDotf():
    setup_v6rad()
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v6GetRDotf(v6rad) == tpm.v3GetRf(v3_tmp)

def test_v6GetAlphaDotf():
    setup_v6rad()
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v6GetAlphaDotf(v6rad) == tpm.v3GetAlphaf(v3_tmp)

def test_v6GetDeltaDotf():
    setup_v6rad()
    v3_tmp = tpm.v6GetVelf(v6rad)
    assert tpm.v6GetDeltaDotf(v6rad) == tpm.v3GetDeltaf(v3_tmp)
                                                        
def test_v6IncXf():
    setup_v6xyz()
    tpm.v6IncXf(v6xyz, f)
    assert tpm.v6GetXf(v6xyz) == x + f

def test_v6IncYf():
    setup_v6xyz()
    tpm.v6IncYf(v6xyz, f)
    assert tpm.v6GetYf(v6xyz) == y + f

def test_v6IncZf():
    setup_v6xyz()
    tpm.v6IncZf(v6xyz, f)
    assert tpm.v6GetZf(v6xyz) == z + f

def test_v6IncXDotf():
    setup_v6xyz()
    tpm.v6IncXDotf(v6xyz, fdot)
    assert tpm.v6GetXDotf(v6xyz) == xdot + fdot

def test_v6IncYDotf():
    setup_v6xyz()
    tpm.v6IncYDotf(v6xyz, fdot)
    assert tpm.v6GetYDotf(v6xyz) == ydot + fdot

def test_v6IncZDotf():
    setup_v6xyz()
    tpm.v6IncZDotf(v6xyz, fdot)
    assert tpm.v6GetZDotf(v6xyz) == zdot + fdot

def test_v6IncRf():
    setup_v6rad()
    tpm.v6IncRf(v6rad, f)
    assert tpm.v6GetRf(v6rad) == r + f

def test_v6IncAlphaf():
    setup_v6rad()
    tpm.v6IncAlphaf(v6rad, f)
    assert tpm.v6GetAlphaf(v6rad) == alpha + f

def test_v6IncDeltaf():
    setup_v6rad()
    tpm.v6IncDeltaf(v6rad, f)
    assert tpm.v6GetDeltaf(v6rad) == delta + f
    

def test_v6IncRDotf():
    setup_v6rad()
    tpm.v6IncRDotf(v6rad, fdot)
    assert tpm.v6GetRDotf(v6rad) == rdot + fdot

def test_v6IncAlphaDotf():
    setup_v6rad()
    tpm.v6IncAlphaDotf(v6rad, fdot)
    assert tpm.v6GetAlphaDotf(v6rad) == alphadot + fdot

def test_v6IncDeltaDotf():
    setup_v6rad()
    tpm.v6IncDeltaDotf(v6rad, fdot)
    assert tpm.v6GetDeltaDotf(v6rad) == deltadot + fdot

def test_v6MulXf():
    setup_v6xyz()
    tpm.v6MulXf(v6xyz, f)
    assert tpm.v6GetXf(v6xyz) == x * f

def test_v6MulYf():
    setup_v6xyz()
    tpm.v6MulYf(v6xyz, f)
    assert tpm.v6GetYf(v6xyz) == y * f

def test_v6MulZf():
    setup_v6xyz()
    tpm.v6MulZf(v6xyz, f)
    assert tpm.v6GetZf(v6xyz) == z * f

def test_v6MulXDotf():
    setup_v6xyz()
    tpm.v6MulXDotf(v6xyz, fdot)
    assert tpm.v6GetXDotf(v6xyz) == xdot * fdot

def test_v6MulYDotf():
    setup_v6xyz()
    tpm.v6MulYDotf(v6xyz, fdot)
    assert tpm.v6GetYDotf(v6xyz) == ydot * fdot

def test_v6MulZDotf():
    setup_v6xyz()
    tpm.v6MulZDotf(v6xyz, fdot)
    assert tpm.v6GetZDotf(v6xyz) == zdot * fdot

def test_v6MulRf():
    setup_v6rad()
    tpm.v6MulRf(v6rad, f)
    assert tpm.v6GetRf(v6rad) == r * f

def test_v6MulAlphaf():
    setup_v6rad()
    tpm.v6MulAlphaf(v6rad, f)
    assert tpm.v6GetAlphaf(v6rad) == alpha * f

def test_v6MulDeltaf():
    setup_v6rad()
    tpm.v6MulDeltaf(v6rad, f)
    assert tpm.v6GetDeltaf(v6rad) == delta * f
    
def test_v6MulRDotf():
    setup_v6rad()
    tpm.v6MulRDotf(v6rad, fdot)
    assert tpm.v6GetRDotf(v6rad) == rdot * fdot

def test_v6MulAlphaDotf():
    setup_v6rad()
    tpm.v6MulAlphaDotf(v6rad, fdot)
    assert tpm.v6GetAlphaDotf(v6rad) == alphadot * fdot

def test_v6MulDeltaDotf():
    setup_v6rad()
    tpm.v6MulDeltaDotf(v6rad, fdot)
    assert tpm.v6GetDeltaDotf(v6rad) == deltadot * fdot

def test_v6SetXf():
    setup_v6xyz()
    tpm.v6SetXf(v6xyz, x)
    assert tpm.v6GetXf(v6xyz) == x

def test_v6SetYf():
    setup_v6xyz()
    tpm.v6SetYf(v6xyz, y)
    assert tpm.v6GetYf(v6xyz) == y

def test_v6SetZf():
    setup_v6xyz()
    tpm.v6SetZf(v6xyz, z)
    assert tpm.v6GetZf(v6xyz) == z

def test_v6SetXDotf():
    setup_v6xyz()
    tpm.v6SetXDotf(v6xyz, xdot)
    assert tpm.v6GetXDotf(v6xyz) == xdot

def test_v6SetYDotf():
    setup_v6xyz()
    tpm.v6SetYDotf(v6xyz, xdot)
    assert tpm.v6GetYDotf(v6xyz) == xdot

def test_v6SetZDotf():
    setup_v6xyz()
    tpm.v6SetYDotf(v6xyz, xdot)
    assert tpm.v6GetYDotf(v6xyz) == xdot

def test_v6SetRf():
    setup_v6rad()
    tpm.v6SetRf(v6rad, r)
    assert tpm.v6GetRf(v6rad) == r

def test_v6SetAlphaf():
    setup_v6rad()
    tpm.v6SetAlphaf(v6rad, alpha)
    assert tpm.v6GetAlphaf(v6rad) == alpha

def test_v6SetDeltaf():
    setup_v6rad()
    tpm.v6SetDeltaf(v6rad, delta)
    assert tpm.v6GetDeltaf(v6rad) == delta

def test_v6SetRDotf():
    setup_v6rad()
    tpm.v6SetRDotf(v6rad, rdot)
    assert tpm.v6GetRDotf(v6rad) == rdot

def test_v6SetAlphaDotf():
    setup_v6rad()
    tpm.v6SetAlphaDotf(v6rad, alphadot)
    assert tpm.v6GetalphaDotf(v6rad) == alphadot

def test_v6SetDeltaDotf():
    setup_v6rad()
    tpm.v6SetDeltaDotf(v6rad, deltadot)
    assert tpm.v6GetDeltaDotf(v6rad) == deltadot

def run():
    test_v6SetPosf()
    test_v6DecXf()
    test_v6DecYf()
    test_v6DecZf()
    test_v6DecXDotf()
    test_v6DecYDotf()
    test_v6DecZDotf()
    test_v6DecXDotf()
    test_v6DecYDotf()
    test_v6DecZDotf()
    test_v6DecRDotf()
    test_v6DecAlphaDotf()
    test_v6DecDeltaDotf()
    test_v6DivXf()
    test_v6DivYf()
    test_v6DivZf()
    test_v6DivXDotf()
    test_v6DivYDotf()
    test_v6DivZDotf()
    test_v6DivRf()
    test_v6DivAlphaf()
    test_v6DivDeltaf()
    test_v6DivRDotf()
    test_v6DivAlphaDotf()
    test_v6DivDeltaDotf()
    test_v6GetTypef()
    test_v6GetXf()
    test_v6GetYf()
    test_v6GetZf()
    test_v6GetXDotf()
    test_v6GetYDotf()
    test_v6GetZDotf()
    test_v6GetRf()
    test_v6GetAlphaf()
    test_v6GetDeltaf()
    test_v6GetRDotf()
    test_v6GetAlphaDotf()
    test_v6GetDeltaDotf()
    test_v6IncXf()
    test_v6IncYf()
    test_v6IncZf()
    test_v6IncXDotf()
    test_v6IncYDotf()
    test_v6IncZDotf()
    test_v6IncRf()
    test_v6IncAlphaf()
    test_v6IncDeltaf()
    test_v6IncRDotf()
    test_v6IncAlphaDotf()
    test_v6IncDeltaDotf()
    test_v6MulXf()
    test_v6MulYf()
    test_v6MulZf()
    test_v6MulXDotf()
    test_v6MulYDotf()
    test_v6MulZDotf()
    test_v6MulRf()
    test_v6MulAlphaf()
    test_v6MulDeltaf()
    test_v6MulRDotf()
    test_v6MulAlphaf()
    test_v6MulDeltaDotf()
    test_v6SetXDotf()
    test_v6SetYDotf()
    test_v6SetZDotf()
    test_v6SetRf()
    test_v6SetAlphaf()
    test_v6SetDeltaf()
    test_v6SetRDotf()
    test_v6SetAlphaf()
    test_v6SetDeltaDotf()

if __name__ == '__main__':
    print "Running tests on functions for V6 vectors..."
    run()
