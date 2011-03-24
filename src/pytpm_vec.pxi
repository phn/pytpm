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

    cdef setType(self, int t):
        self._v3.type = t
    
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


cdef class V3CP(V3):
    """A V3 Cartesian position vector."""
    # The following are read only.
    ctype = CARTESIAN
    vtype = POS
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.setType(self.ctype)

    def __getx(self):
        return self.getX()
    def __setx(self, x):
        self.setX(x)
    x = property(__getx, __setx, doc="X coordinate.")

    def __gety(self):
        return self.getY()
    def __sety(self, y):
        self.setY(y)
    y = property(__gety, __sety, doc="Y coordinate.")

    def __getz(self):
        return self.getZ()
    def __setz(self, z):
        self.setZ(z)
    z = property(__getz, __setz, doc="Z coordinate.")

    def c2s(self):
        """Convert Cartesian position vector into spherical vector."""
        cdef _tpm_vec.V3 _v3
        _v3 = _tpm_vec.v3c2s(self.getV3())
        #v3 = V3SP(r=_v3.v[0], alpha=_v3.v[1], delta=_v3[2])
        v3sp = V3SP()
        v3sp.setV3(_v3)
        return v3sp

    def __sub__(V3CP self, V3CP other):
        """Return V3CP that holds difference between two V3CPs."""
        if isinstance(self, V3CP) and isinstance(other, V3CP):
            v3cp = V3CP()
            v3cp.setV3(_tpm_vec.v3diff(self.getV3(), other.getV3()))
            return v3cp
        else:
            raise TypeError, "Can only subtract two V3CP values."

    def __add__(V3CP self, V3CP other):
        """Return V3CP that holds the sum of two V3CPs."""
        if isinstance(self, V3CP) and isinstance(other, V3CP):
            v3cp = V3CP()
            v3cp.setV3(_tpm_vec.v3sum(self.getV3(), other.getV3()))
            return v3cp
        else:
            raise TypeError, "Can only add two V3CP values."

    def __mul__(V3CP self, double n):
        """Scale X,Y and Z components with the scalar number."""
        v3cp = V3CP()
        v3cp.setV3(_tpm_vec.v3scale(self.getV3(), n))
        return v3cp
    
    def unit(self):
        """Return unit V3CP vector."""
        v3cp = V3CP()
        v3cp.setV3(_tpm_vec.v3unit(self.getV3()))
        return v3cp

    def mod(self):
        """Return modulus of the V3CP vector."""
        return _tpm_vec.v3mod(self.getV3())

    def dot(V3CP self, V3CP other):
        """Return the dot product of two V3CP vectors."""
        return _tpm_vec.v3dot(self.getV3(), other.getV3())

    def cross(V3CP self, V3CP other):
        """Return the cross product of two V3CP vectors."""
        v3cp = V3CP()
        v3cp.setV3(_tpm_vec.v3cross(self.getV3(), other.getV3()))
        return v3cp
    
    
cdef class V3SP(V3):
    """A V3 spherical position vector."""
    # The following are read only.
    ctype = SPHERICAL
    vtype = POS
    def __init__(self, r=0.0, alpha=0.0, delta=0.0):
        self.r = r
        self.alpha = alpha
        self.delta = delta
        self.setType(self.ctype)

    def __getr(self):
        return self.getX()
    def __setr(self, r):
        self.setX(r)
    r = property(__getr, __setr, doc="Radial coordinate.")

    def __getalpha(self):
        return self.getY()
    def __setalpha(self, alpha):
        self.setY(alpha)
    alpha = property(__getalpha, __setalpha, doc="Alpha coordinate.")

    def __getdelta(self):
        return self.getZ()
    def __setdelta(self, delta):
        self.setZ(delta)
    delta = property(__getdelta, __setdelta, doc="Delta coordinate.")

    def __getnalpha(self):
        return _tpm_vec.v3alpha(self.getV3())
    nalpha = property(__getnalpha, doc="Normalized alpha coordinate.")

    def s2c(self):
        """Convert spherical position vector into Cartesian vector."""
        cdef _tpm_vec.V3 _v3
        _v3 = _tpm_vec.v3s2c(self.getV3())
        v3cp = V3CP()
        v3cp.setV3(_v3)
        return v3cp
        
    def __sub__(V3SP self, V3SP other):
        """Return V3SP that holds difference between two V3SPs."""
        if isinstance(self, V3SP) and isinstance(other, V3SP):
            v3cp = V3CP()
            v3cp.setV3(_tpm_vec.v3diff(self.getV3(), other.getV3()))
            return v3cp.c2s()
        else:
            raise TypeError, "Can only subtract two V3SP values."

    def __add__(V3SP self, V3SP other):
        """Return V3SP that holds the sum of two V3SPs."""
        if isinstance(self, V3SP) and isinstance(other, V3SP):
            v3cp = V3CP()
            v3cp.setV3(_tpm_vec.v3sum(self.getV3(), other.getV3()))
            return v3cp.c2s()
        else:
            raise TypeError, "Can only add two V3SP values."

    def __mul__(V3SP self, double n):
        """Scale R with the scalar number."""
        v3sp = V3SP()
        v3sp.setV3(_tpm_vec.v3scale(self.getV3(), n))
        return v3sp

    def mod(self):
        """Return modulus of the V3SP vector; magnitude of R component."""
        return _tpm_vec.v3mod(self.getV3())

    def dot(V3SP self, V3SP other):
        """Return the dot product of two V3SP vectors."""
        return _tpm_vec.v3dot(self.getV3(), other.getV3())
    
    def cross(V3SP self, V3SP other):
        """Return the cross product of two V3SP vectors."""
        v3cp = V3CP()
        v3cp.setV3(_tpm_vec.v3cross(self.getV3(), other.getV3()))
        return v3cp.c2s()
        
