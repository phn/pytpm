"""Tests for functions defined in tpm/vec.h.

These functions are used for accessing and manipulating vectors and
matrices.

:author: Prasanth Nair
:contact: prasanthhn@gmail.com
"""
import setup_path
setup_path.run()

from pytpm import tpm

def test_m3I():
    """Identify 3-matrix scaled by the given value."""
    m3 = tpm.m3I(10.0)
    assert tpm.m3GetXXf(m3) == 10.0
    assert tpm.m3GetYYf(m3) == 10.0
    assert tpm.m3GetZZf(m3) == 10.0

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
    

def run():
    test_m3I()
    test_m3O()


if __name__ == '__main__':
    run()


