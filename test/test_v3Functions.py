"""Tests for functions defined in v3Functions.c.

These functions are used for accessing and manipulating V3 vectors.

:author: Prasanth Nair
:contact: prasanthhn@gmail.com
"""
from pytpm import tpm

v3 = tpm.V3()
t = 1
x = 12.3456
y = 78.9012
z = -34.5678
r = x
alpha = y
delta = z
f = 2.0 # decrement, increment, div, mul factor
ra = y
dec = z

tpm.v3SetTypef(v3, t)
assert tpm.v3GetTypef(v3) == t

tpm.v3SetXf(v3, x)
assert tpm.v3GetXf(v3) == x

tpm.v3SetYf(v3, y)
assert tpm.v3GetYf(v3) == y 

tpm.v3SetZf(v3, z)
assert tpm.v3GetZf(v3) == z

tpm.v3SetRf(v3, r)
assert tpm.v3GetRf(v3) == r

tpm.v3SetAlphaf(v3, alpha)
assert tpm.v3GetAlphaf(v3) == alpha

tpm.v3SetDeltaf(v3, delta)
assert tpm.v3GetDeltaf(v3) == delta

tpm.v3SetXf(v3, x)
tpm.v3DecXf(v3, f)
assert tpm.v3GetXf(v3) == x - f

tpm.v3SetYf(v3, y)
tpm.v3DecYf(v3, f)
assert tpm.v3GetYf(v3) == y - f

tpm.v3SetZf(v3, z)
tpm.v3DecZf(v3, f);
assert tpm.v3GetZf(v3) == z - f

tpm.v3SetRf(v3, r)
tpm.v3DecRf(v3, f)
assert tpm.v3GetRf(v3) == r - f

tpm.v3SetAlphaf(v3, alpha)
tpm.v3DecAlphaf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha -f 

tpm.v3SetDeltaf(v3, delta)
tpm.v3DecDeltaf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta - f

tpm.v3SetXf(v3, x)
tpm.v3DivXf(v3, f)
assert tpm.v3GetXf(v3) == x/f

tpm.v3SetYf(v3, y)
tpm.v3DivYf(v3, f)
assert tpm.v3GetYf(v3) == y/f

tpm.v3SetZf(v3, z)
tpm.v3DivZf(v3, f)
assert tpm.v3GetZf(v3) == z/f

tpm.v3SetRf(v3, r)
tpm.v3DivRf(v3, f)
assert tpm.v3GetRf(v3) == r/f

tpm.v3SetAlphaf(v3, alpha)
tpm.v3DivAlphaf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha/f

tpm.v3SetDeltaf(v3, delta)
tpm.v3DivDeltaf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta/f

"""
int v3GetTypef(const V3 v3);

double v3GetXf(const V3 v3);

double v3GetYf(const V3 v3);

double v3GetZf(const V3 v3);

double v3GetRf(const V3 v3);

double v3GetAlphaf(const V3 v3);

double v3GetDeltaf(const V3 v3);
"""

tpm.v3SetXf(v3, x)
tpm.v3IncXf(v3, f)
assert tpm.v3GetXf(v3) == x + f

tpm.v3SetYf(v3, y)
tpm.v3IncYf(v3, f)
assert tpm.v3GetYf(v3) == y + f

tpm.v3SetZf(v3, z)
tpm.v3IncZf(v3, f)
assert tpm.v3GetZf(v3) == z + f

tpm.v3SetRf(v3, r)
tpm.v3IncRf(v3, f)
assert tpm.v3GetRf(v3) == r + f

tpm.v3SetAlphaf(v3, alpha)
tpm.v3IncAlphaf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha + f

tpm.v3SetDeltaf(v3, delta)
tpm.v3IncDeltaf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta + f

tpm.v3SetXf(v3, x)
tpm.v3MulXf(v3, f)
assert tpm.v3GetXf(v3) == x * f

tpm.v3SetYf(v3, y)
tpm.v3MulYf(v3, f)
assert tpm.v3GetYf(v3) == y * f

tpm.v3SetZf(v3, z)
tpm.v3MulZf(v3, f)
assert tpm.v3GetZf(v3) == z * f

tpm.v3SetRf(v3, r)
tpm.v3MulRf(v3, f)
assert tpm.v3GetRf(v3) == r * f

tpm.v3SetAlphaf(v3, alpha)
tpm.v3MulAlphaf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha * f

tpm.v3SetDeltaf(v3, delta)
tpm.v3MulDeltaf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta * f

# some astro convenience macros

tpm.v3SetAlphaf(v3, alpha)
tpm.v3DecRAf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha - f

tpm.v3SetDeltaf(v3, delta)
tpm.v3DecDecf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta - f

tpm.v3SetAlphaf(v3, alpha)
tpm.v3DivRAf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha/f

tpm.v3SetDeltaf(v3, delta)
tpm.v3DivDecf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta/f

tpm.v3SetAlphaf(v3, alpha)
assert tpm.v3GetRAf(v3) == alpha

tpm.v3SetDeltaf(v3, delta)
assert tpm.v3GetDecf(v3) == delta

tpm.v3SetAlphaf(v3, alpha)
tpm.v3IncRAf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha + f

tpm.v3SetDeltaf(v3, delta)
tpm.v3IncDecf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta + f

tpm.v3SetAlphaf(v3, alpha)
tpm.v3MulRAf(v3, f)
assert tpm.v3GetAlphaf(v3) == alpha * f

tpm.v3SetDeltaf(v3, delta)
tpm.v3MulDecf(v3, f)
assert tpm.v3GetDeltaf(v3) == delta * f

tpm.v3SetRAf(v3, alpha)
assert tpm.v3GetAlphaf(v3) == alpha

tpm.v3SetDecf(v3, delta)
assert tpm.v3GetDeltaf(v3) == delta
