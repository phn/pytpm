# -*- coding: utf-8 -*-
# The following line must be present in the pytpm.pyx file.
# cimport _tpm_vec

POS = _tpm_vec.POS
VEL = _tpm_vec.VEL
CARTESIAN = _tpm_vec.CARTESIAN
SPHERICAL = _tpm_vec.SPHERICAL
POLAR = _tpm_vec.POLAR

cdef class V3(object):
    """Class that wraps _tpm_vec.V3; for use from Cython only."""
    cdef _tpm_vec.V3 _v3

    def __cinit__(self):
        self._v3.type = CARTESIAN
        self._v3.v[0] = 0.0
        self._v3.v[1] = 0.0
        self._v3.v[2] = 0.0

    def __init__(self, ctype=CARTESIAN, X=0.0, Y=0.0, Z=0.0):
        self._v3.type = ctype
        self._v3.v[0] = X
        self._v3.v[1] = Y
        self._v3.v[2] = Z

    cdef int getType(self):
        return self._v3.type
    
    cdef setX(self, double X):
        self._v3.v[0] = X
        
    cdef setY(self, double Y):
        self._v3.v[1] = Y

    cdef setZ(self, double Z):
        self._v3.v[2] = Z

    cdef double getX(self):
        return self._v3.v[0]
        
    cdef double getY(self):
        return self._v3.v[1]

    cdef double getZ(self):
        return self._v3.v[2]

    cdef _tpm_vec.V3 getV3(self):
        return self._v3

    cdef setV3(self, _tpm_vec.V3 _v3):
        self._v3 = _v3

