# -*- coding: utf-8 -*-
# The following line must be present in the tpm.pyx file.
# cimport tpm_vec

POS = tpm_vec.POS
VEL = tpm_vec.VEL
CARTESIAN = tpm_vec.CARTESIAN
SPHERICAL = tpm_vec.SPHERICAL
POLAR = tpm_vec.POLAR

cdef class V3(object):
    """Class that wraps tpm_vec.V3; for use from Cython only."""
    cdef tpm_vec.V3 _v3

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

    cdef tpm_vec.V3 getV3(self):
        return self._v3

    cdef setV3(self, tpm_vec.V3 _v3):
        self._v3 = _v3


cdef class V3CP(V3):
    """A V3 Cartesian position vector.

    Parameters
    ----------
    x : float
        X coordinate.
    y : float
        Y coordinate.
    z : float
        Z coordinate.

    Attributes
    ----------
    x
    y
    z
    
    """
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
        """Convert Cartesian position vector into spherical vector.

        Returns
        -------
        v3 : tpm.V3SP
            The position in spherical coordinates.
            
        """
        cdef tpm_vec.V3 _v3
        _v3 = tpm_vec.v3c2s(self.getV3())
        #v3 = V3SP(r=_v3.v[0], alpha=_v3.v[1], delta=_v3[2])
        v3sp = V3SP()
        v3sp.setV3(_v3)
        return v3sp
    
    def unit(self):
        """Return unit V3CP vector.

        Returns
        -------
        x : tpm.V3CP
            Unit vector in the direction of this vector.
            
        """
        v3cp = V3CP()
        v3cp.setV3(tpm_vec.v3unit(self.getV3()))
        return v3cp

    def mod(self):
        """Return modulus (length) of the V3CP vector.

        Returns
        -------
        x : float
            Length of the vector.
            
        """
        return tpm_vec.v3mod(self.getV3())

    def dot(V3CP self, V3CP other):
        """Return the dot product of two V3CP vectors.

        Returns
        -------
        d : float
            Dot product of the given vector with this vector.
            
        """
        return tpm_vec.v3dot(self.getV3(), other.getV3())

    def cross(V3CP self, V3CP other):
        """Return the cross product of two V3CP vectors.

        Returns
        -------
        x : tpm.V3CP
            Cross product of this vector with the given vector.
            
        """
        v3cp = V3CP()
        v3cp.setV3(tpm_vec.v3cross(self.getV3(), other.getV3()))
        return v3cp

    def __sub__(V3CP self, V3CP other):
        """Return V3CP that holds difference between two V3CPs."""
        if isinstance(self, V3CP) and isinstance(other, V3CP):
            v3cp = V3CP()
            v3cp.setV3(tpm_vec.v3diff(self.getV3(), other.getV3()))
            return v3cp
        else:
            raise TypeError, "Can only subtract two V3CP values."

    def __add__(V3CP self, V3CP other):
        """Return V3CP that holds the sum of two V3CPs."""
        if isinstance(self, V3CP) and isinstance(other, V3CP):
            v3cp = V3CP()
            v3cp.setV3(tpm_vec.v3sum(self.getV3(), other.getV3()))
            return v3cp
        else:
            raise TypeError, "Can only add two V3CP values."

    def __mul__(V3CP self, double n):
        """Scale X,Y and Z components with the scalar number."""
        v3cp = V3CP()
        v3cp.setV3(tpm_vec.v3scale(self.getV3(), n))
        return v3cp
    
    def __str__(self):
        """Return string representation of V3CP."""
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        """Return unicode representation of V3CP."""
        s = tpm_vec.v3fmt(self.getV3())
        return unicode(s)

    
cdef class V3SP(V3):
    """A V3 spherical position vector.

    Parameters
    ----------
    r : float
        Radial coordinate.
    alpha : float
        Longitudinal angle in radians.
    delta : float
        Latitudinal angle in radians.

    Attributes
    ----------
    r
    alpha
    delta

    Notes
    -----
    The following attributes are also present:
    
    nalpha : `alpha` normalized to [0, 2π).
    ndelta : `delta` normalized to [-π/2, π/2].
    
    """
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
        
    alpha = property(__getalpha, __setalpha,
                     doc="Longitudinal coordinate.")

    def __getdelta(self):
        return self.getZ()
    
    def __setdelta(self, delta):
        self.setZ(delta)
        
    delta = property(__getdelta, __setdelta,
                     doc="Latitudinal coordinate.")

    def __getnalpha(self):
        return tpm_vec.v3alpha(self.getV3())
    
    nalpha = property(__getnalpha, doc="alpha normalized to [0, 2π).")

    def __getndelta(self):
        return tpm_vec.v3delta(self.getV3())
    
    ndelta = property(__getndelta, doc="delta normalized to [-π/2, π/2].")

    def s2c(self):
        """Convert spherical position vector into Cartesian vector.
        
        Returns
        -------
        v : tpm.V3CP
            Spherical vector converted into Cartesian.
            
        """
        cdef tpm_vec.V3 _v3
        _v3 = tpm_vec.v3s2c(self.getV3())
        v3cp = V3CP()
        v3cp.setV3(_v3)
        return v3cp

    def mod(self):
        """Return magnitude of radial component R.

        Returns
        -------
        m : float
            Length of the radial component.
            
        """
        return tpm_vec.v3mod(self.getV3())

    def dot(V3SP self, V3SP other):
        """Return the dot product of two V3SP vectors.

        Dot product is calculated after converting to Cartesian
        coordinates.

        Returns
        -------
        d : float
            Dot product.
            
        """
        return tpm_vec.v3dot(self.getV3(), other.getV3())
    
    def cross(V3SP self, V3SP other):
        """Return the cross product of two V3SP vectors.

        Cross product is calculated after converting to Cartesian
        coordinates.

        Returns
        -------
        v : tpm.V3SP
            Spherical vector.
            
        """
        v3cp = V3CP()
        v3cp.setV3(tpm_vec.v3cross(self.getV3(), other.getV3()))
        return v3cp.c2s()
    
    def __sub__(V3SP self, V3SP other):
        """Return V3SP that holds difference between two V3SPs.

        Difference is taken after conversion to Cartesian coordinates.
        """
        if isinstance(self, V3SP) and isinstance(other, V3SP):
            v3cp = V3CP()
            v3cp.setV3(tpm_vec.v3diff(self.getV3(), other.getV3()))
            return v3cp.c2s()
        else:
            raise TypeError, "Can only subtract two V3SP values."

    def __add__(V3SP self, V3SP other):
        """Return V3SP that holds the sum of two V3SPs.
        
        Addition is performed after conversion to Cartesian coordinates.
        """
        if isinstance(self, V3SP) and isinstance(other, V3SP):
            v3cp = V3CP()
            v3cp.setV3(tpm_vec.v3sum(self.getV3(), other.getV3()))
            return v3cp.c2s()
        else:
            raise TypeError, "Can only add two V3SP values."

    def __mul__(V3SP self, double n):
        """Scale R with the scalar number."""
        v3sp = V3SP()
        v3sp.setV3(tpm_vec.v3scale(self.getV3(), n))
        return v3sp
    
    def __str__(self):
        """Return string representation of V3SP"""
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        """Return unicode representation of V3SP"""
        s = tpm_vec.v3fmt(self.getV3())
        return unicode(s)


cdef class V6(object):
    """Class that wraps tpm_vec.V6; for use from Cython only."""
    cdef tpm_vec.V6 _v6

    def __cinit__(self):
        self._v6.v[POS].type = CARTESIAN
        self._v6.v[POS].v[0] = 0.0
        self._v6.v[POS].v[1] = 0.0
        self._v6.v[POS].v[2] = 0.0
        self._v6.v[VEL].type = CARTESIAN
        self._v6.v[VEL].v[0] = 0.0
        self._v6.v[VEL].v[1] = 0.0
        self._v6.v[VEL].v[2] = 0.0

    def __init__(self, ctype=CARTESIAN, x=0.0, y=0.0, z=0.0,
                 xdot=0.0, ydot=0.0, zdot=0.0):
        self._v6.v[POS].type = ctype
        self._v6.v[POS].v[0] = x
        self._v6.v[POS].v[1] = y
        self._v6.v[POS].v[2] = z
        self._v6.v[VEL].type = ctype
        self._v6.v[VEL].v[0] = xdot
        self._v6.v[VEL].v[1] = ydot
        self._v6.v[VEL].v[2] = zdot

    cdef int getType(self):
        return self._v6.v[POS].type

    cdef setType(self, int t):
        self._v6.v[POS].type = t
        self._v6.v[VEL].type = t

    cdef getX(self):
        return self._v6.v[POS].v[0]

    cdef setX(self, double x):
        self._v6.v[POS].v[0] = x

    cdef getY(self):
        return self._v6.v[POS].v[1]

    cdef setY(self, double y):
        self._v6.v[POS].v[1] = y

    cdef getZ(self):
        return self._v6.v[POS].v[2]

    cdef setZ(self, double z):
        self._v6.v[POS].v[2] = z

    cdef getXdot(self):
        return self._v6.v[VEL].v[0]

    cdef setXdot(self, double xdot):
        self._v6.v[VEL].v[0] = xdot

    cdef getYdot(self):
        return self._v6.v[VEL].v[1]

    cdef setYdot(self, double ydot):
        self._v6.v[VEL].v[1] = ydot

    cdef getZdot(self):
        return self._v6.v[VEL].v[2]

    cdef setZdot(self, double zdot):
        self._v6.v[VEL].v[2] = zdot

    cdef tpm_vec.V6 getV6(self):
        return self._v6

    cdef setV6(self, tpm_vec.V6 _v6):
        self._v6 = _v6

    cdef tpm_vec.V3 getPOS(self):
        return self._v6.v[POS]

    cdef setPOS(self, tpm_vec.V3 _v3):
        if (_v3.type != self.getType()):
            raise ValueError, "Type of V3 must be the same as that of V6."
        self._v6.v[POS] = _v3

    cdef tpm_vec.V3 getVEL(self):
        return self._v6.v[VEL]

    cdef setVEL(self, tpm_vec.V3 _v3):
        if (_v3.type != self.getType()):
            raise ValueError, "Type of V3 must be the same as that of V6."
        self._v6.v[VEL] = _v3


cdef class V6C(V6):
    """Class for Cartesian V6 vector.

    Parameters
    ----------
    x : float
        X coordinate.
    y : float
        Y coordinate.
    z : float
        Z coordinate.
    xdot : float
        Rate of change of `x`.
    ydot : float
        Rate of change of `y`.
    zdot : float
        Rate of change of `z`.

    Attributes
    ----------
    x
    y
    z
    xdot
    ydot
    zdot
    
    """
    # The following is read only.
    ctype = CARTESIAN
    def __init__(self, x=0.0, y=0.0, z=0.0, xdot=0.0, ydot=0.0, zdot=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.xdot = xdot
        self.ydot = ydot
        self.zdot = zdot

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

    def __getxdot(self):
        return self.getXdot()
    
    def __setxdot(self, xdot):
        self.setXdot(xdot)
        
    xdot = property(__getxdot, __setxdot,
                    doc="Rate of change of X coordinate.")

    def __getydot(self):
        return self.getYdot()
    
    def __setydot(self, ydot):
        self.setYdot(ydot)
        
    ydot = property(__getydot, __setydot,
                    doc="Rate of change of Y coordinate.")

    def __getzdot(self):
        return self.getZdot()
    
    def __setzdot(self, zdot):
        self.setZdot(zdot)
        
    zdot = property(__getzdot, __setzdot,
                    doc="Rate of change of Z coordinate.")

    def __getPOS(self):
        v3p = V3CP()
        v3p.setV3(self.getPOS())
        return v3p
    
    def __setPOS(self, V3CP v3cp):
        self.setPOS(v3cp.getV3())
        
    pos = property(__getPOS, __setPOS, doc="The position component.")
        
    def __sub__(V6C self, V6C other):
        """Return V6C that holds difference between two V6C vectors."""
        if isinstance(self, V6C) and isinstance(other, V6C):
            v6c = V6C()
            v6c.setV6(tpm_vec.v6diff(self.getV6(), other.getV6()))
            return v6c
        else:
            raise TypeError, "Can only subtract two V6C values."

    def __add__(V6C self, V6C other):
        """Return V6C that holds the sum of two V6C vectors."""
        if isinstance(self, V6C) and isinstance(other, V6C):
            v6c = V6C()
            v6c.setV6(tpm_vec.v6sum(self.getV6(), other.getV6()))
            return v6c
        else:
            raise TypeError, "Can only add two V6C values."

    def mod(self):
        """Return modulus of position component of V6C vector.

        Returns
        -------
        x : float
            The length of the position component.
            
        """
        return tpm_vec.v6mod(self.getV6())

    def unit(self):
        """Return V6C with unit position and scaled velocity components.

        The velocity component is scaled by inverse of length of the
        position component.

        Returns
        -------
        v : tpm.V6C
            A V6C vector.
            
        """
        v6c = V6C()
        v6c.setV6(tpm_vec.v6unit(self.getV6()))
        return v6c

    def scale(self, x):
        """Return V6C with components scaled by the given factor.

        Returns
        -------
        v : tpm.V6C
            A vector with components set to those in this vector
            multiplied by the given `x`.
            
        """
        v6c = V6C()
        v6c.setV6(tpm_vec.v6scale(self.getV6(), x))
        return v6c

    def v62v3(self, dt):
        """Convert V6C into V3CP by addding space motion.

        The positon component is increment by the product of space motion
        and given number of days, dt.

        Returns
        -------
        v : tpm.V6CP
            The position vector at the end of time `dt`.
            
        """
        v3cp = V3CP()
        v3cp.setV3(tpm_vec.v62v3(self.getV6(), dt))
        return v3cp

    def dot(V6C self, V6C other):
        """Dot product of the position components.

        Returns
        -------
        x : float
            The dot product of the position component of this vector
            with that of the given vector.
            
        """
        if isinstance(self, V6C) and isinstance(other, V6C):
            return tpm_vec.v6dot(self.getV6(), other.getV6())
        else:
            raise TypeError, "Can only take dot product of two V6C values."

    def cross(V6C self, V6C other):
        """Cross product of the position components.

        The velocity component of the resulting V6 vector is set to 0.

        Returns
        -------
        v : tpm.V6C
            A V6C vector with position component set to the cross
            product of the position component of this vector and the given
            vector. The velocity component is set ot 0.
            
        """
        if isinstance(self, V6C) and isinstance(other, V6C):
            v6c = V6C()
            v6c.setV6(tpm_vec.v6cross(self.getV6(), other.getV6()))
            return v6c
        else:
            raise TypeError, "Can only take cross product of two V6C values."

    def c2s(self):
        """Cartesian to spherical conversion.

        Returns
        -------
        v : tpm.V6S
            The spherical equivalent of this vector.
            
        """
        v6s = V6S()
        v6s.setV6(tpm_vec.v6c2s(self.getV6()))
        return v6s

    
cdef class V6S(V6):
    """Class for spherical V6 vector.

    Parameters
    ----------
    r : float
        Radial coordinate.
    alpha : float
        Longitudinal angle.
    delta : float
        Latitudinal angle.
    rdot : float
        Rate of change in `r`.
    alphadot : float
        Rate of change in `alpha`.
    deltadot : float
        Rate of change in `delta`.

    Attributes
    ----------
    r
    alpha
    delta
    rdot
    alphadot
    deltadot

    Notes
    -----
    The following attributes are also present:
    
    nalpha : `alpha` normalized to [0, 2π).
    ndelta : `delta` normalized to [-π/2, π/2].
    
    """
    # The following is read only.
    ctype = SPHERICAL
    def __init__(self, r=0.0, alpha=0.0, delta=0.0, rdot=0.0,
                 alphadot=0.0, deltadot=0.0):
        self.setType(SPHERICAL) # Set type of the underlying V6. Why
                                # can't I call the inherited V6.__init__()?
        self.r = r
        self.alpha = alpha
        self.delta = delta
        self.rdot = rdot
        self.alphadot = alphadot
        self.deltadot = deltadot

    def __getr(self):
        return self.getX()
    
    def __setr(self, r):
        self.setX(r)
        
    r = property(__getr, __setr, doc="R coordinate.")

    def __getalpha(self):
        return self.getY()
    
    def __setalpha(self, alpha):
        self.setY(alpha)
        
    alpha = property(__getalpha, __setalpha, doc="ALPHA coordinate.")

    def __getdelta(self):
        return self.getZ()
    def __setdelta(self, delta):
        self.setZ(delta)
    delta = property(__getdelta, __setdelta, doc="DELTA coordinate.")

    def __getrdot(self):
        return self.getXdot()
    
    def __setrdot(self, rdot):
        self.setXdot(rdot)
        
    rdot = property(__getrdot, __setrdot,
                    doc="Rate of change of R coordinate.")

    def __getalphadot(self):
        return self.getYdot()
    
    def __setalphadot(self, alphadot):
        self.setYdot(alphadot)
        
    alphadot = property(__getalphadot, __setalphadot,
                        doc="Rate of change of ALPHA coordinate.")

    def __getdeltadot(self):
        return self.getZdot()
    
    def __setdeltadot(self, deltadot):
        self.setZdot(deltadot)
        
    deltadot = property(__getdeltadot, __setdeltadot,
                        doc="Rate of change of DELTA coordinate.")

    def __getnalpha(self):
        return tpm_vec.v6alpha(self.getV6())
    
    nalpha = property(__getnalpha, doc="alpha normalized to [0, 2π).")
    
    def __getndelta(self):
        return tpm_vec.v6delta(self.getV6())
    
    ndelta = property(__getndelta, doc="delta normalized to [-π/2, π/2].")
    
    def s2c(self):
        """Spherical to Cartesian.

        Returns
        -------
        v : tpm.V6C
            The Cartesian equivalent of this vector.
            
        """
        v6c = V6C()
        v6c.setV6(tpm_vec.v6s2c(self.getV6()))
        return v6c


cdef class M3(object):
    """Class that wraps M3 structure, representing a matrix.

    Parameters
    ----------
    xx : float
        m[0][0].
    xy : float
        m[0][1].
    xz : float
        m[0][2].
    yx : float
        m[1][0]
    yy : float
        m[1][1].
    yz : float
        m[1][2].
    zx : float
        m[2][0].
    zy : float
        m[2][1].
    zz : float
        m[2][2].

    Attributes
    ----------
    xx
    xy
    xz
    yx
    yy
    yz
    zx
    zy
    zz
    
    """
    cdef tpm_vec.M3 _m3

    def __cinit__(self):
        self._m3 = tpm_vec.m3I(1.0)

    def __init__(self, xx=1.0, xy=0.0, xz=0.0, yx=0.0, yy=1.0, yz=0.0,
                 zx=0.0, zy=0.0, zz=1.0):
        self._m3.m[0][0] = xx
        self._m3.m[0][1] = xy
        self._m3.m[0][2] = xz        
        self._m3.m[1][0] = yx
        self._m3.m[1][1] = yy
        self._m3.m[1][2] = yz
        self._m3.m[2][0] = zx
        self._m3.m[2][1] = zy
        self._m3.m[2][2] = zz 
        
    def __getxx(self):
        return self._m3.m[0][0]
    
    def __setxx(self, double xx):
        self._m3.m[0][0] = xx
        
    xx = property(__getxx, __setxx, doc="XX.")

    def __getxy(self):
        return self._m3.m[0][1]
    
    def __setxy(self, double xy):
        self._m3.m[0][1] = xy
        
    xy = property(__getxy, __setxy, doc="XY.")
    
    def __getxz(self):
        return self._m3.m[0][2]
    def __setxz(self, double xz):
        self._m3.m[1][2] = xz
        
    xz = property(__getxz, __setxz, doc="XZ.")
    
    def __getyx(self):
        return self._m3.m[1][0]
    
    def __setyx(self, double yx):
        self._m3.m[1][0] = yx
        
    yx = property(__getyx, __setyx, doc="YX.")        

    def __getyy(self):
        return self._m3.m[1][1]
    
    def __setyy(self, double yy):
        self._m3.m[1][1] = yy
        
    yy = property(__getyy, __setyy, doc="YY.")
    
    def __getyz(self):
        return self._m3.m[1][2]
    
    def __setyz(self, double yz):
        self._m3.m[1][2] = yz
        
    yz = property(__getyz, __setyz, doc="YZ.")
    
    def __getzx(self):
        return self._m3.m[2][0]
    
    def __setzx(self, double zx):
        self._m3.m[2][0] = zx
        
    zx = property(__getzx, __setzx, doc="ZX.")
    
    def __getzy(self):
        return self._m3.m[2][1]
    
    def __setzy(self, double zy):
        self._m3.m[2][1] = zy
        
    zy = property(__getzy, __setzy, doc="ZY.")
    
    def __getzz(self):
        return self._m3.m[2][2]
    
    def __setzz(self, double zz):
        self._m3.m[2][2] = zz
        
    zz = property(__getzz, __setzz, doc="ZZ.")

    cdef tpm_vec.M3 getM3(self):
        return self._m3

    cdef setM3(self, tpm_vec.M3 m3):
        self._m3 = m3

    def __str__(self):
        return self.__unicode__().encode("utf-8")
    
    def __unicode__(self):
        return unicode(tpm_vec.m3fmt(self._m3))

    def __sub__(M3 self, M3 other):
        # Cython doesn't distinguish between sub and rsub. Hence type
        # check on self.
        m3 = M3()
        m3.setM3(tpm_vec.m3diff(self.getM3(), other.getM3()))
        return m3

    def __add__(M3 self, M3 other):
        # Cython doesn't distinguish between add and radd. Hence type
        # check on self.
        m3 = M3()
        m3.setM3(tpm_vec.m3sum(self.getM3(), other.getM3()))
        return m3

    def __mul__(M3 self, double x):
        # Cython doesn't distinguish between mul and rmul. Hence type
        # check on self.
        m3 = M3()
        m3.setM3(tpm_vec.m3scale(self.getM3(), x))
        return m3

    def inv(self):
        """Inverse of the matrix.

        Returns
        -------
        m3 : tpm.M3
            Inverse matrix.
            
        """
        m3 = M3()
        m3.setM3(tpm_vec.m3inv(self.getM3()))
        return m3

    def m3m3(self, M3 other):
        """Product of 2 matrices.

        Returns
        -------
        m3 : tpm.M3
            Product.
            
        """
        m3 = M3()
        m3.setM3(tpm_vec.m3m3(self.getM3(), other.getM3()))
        return m3
    
    def m3v3(self, V3CP v3):
        """Product of an M3 matrix and a V3CP vector.

        Returns
        -------
        v : tpm.V3CP
            Product of matrix with Cartesian vector.
            
        """
        v = V3CP()
        v.setV3(tpm_vec.m3v3(self.getM3(), v3.getV3()))
        return v

    def m3v6(self, V6C v6):
        """Product of M3 matrix and V6C vector.

        Both position and velocity components are multiplied by M3.

        Returns
        -------
        v : tpm.V6C
            A V6C vector with position set to that obtained by
            multipying this matrix and the position component of the
            given vector, and the velocity set to that obtained by
            multiplying this matrix and the velocity component of the
            given vector.
            
        """
        v = V6C()
        v.setV6(tpm_vec.m3v6(self.getM3(), v6.getV6()))
        return v
       
    
def m3rx(theta):
   """A rotation matrix for rotation about X-axis.

   Parameters
   ----------
   theta : float
       Rotation angle in radians.

   Returns
   -------
   m3 : tpm.M3
       A rotation matrix about X-axis.

   Notes
   -----
   The rotation matrix::
   
       1      0          0 
       0 cos(theta)  sin(theta)
       0 -sin(theta) cos(theta)
   
   """
   m3 = M3()
   m3.setM3(tpm_vec.m3Rx(theta))
   return m3

def m3rxdot(theta, thetadot):
   """Derivative of rotation matrix for rotation about X-axis.

   Parameters
   ----------
   theta : float
       Rotation angle in radians.
   thetadot : float
       Rate of change of `theta` in radians/second.
     
   Returns
   -------
   m3 : tpm.M3
       A rotation matrix about X-axis.

   Notes
   -----
   The rotation matrix::
   
                 
                    0        0          0       
      thetadot *    0  -sin(theta) cos(theta)   
                    0  -cos(theta) -sin(theta)  
                  
   """
   m3 = M3()
   m3.setM3(tpm_vec.m3RxDot(theta, thetadot))
   return m3

def m3ry(theta):
   """A rotation matrix for rotation about Y-axis.

   Parameters
   ----------
   theta : float
       Rotation angle in radians.

   Returns
   -------
   m3 : tpm.M3
       A rotation matrix about Y-axis.

   Notes
   -----
   The rotation matrix::

       cos(theta)  0  -sin(theta)
             0     1        0
       sin(theta)  0   cos(theta)

   """
   m3 = M3()
   m3.setM3(tpm_vec.m3Ry(theta))
   return m3

def m3rydot(theta, thetadot):
   """Derivative of rotation matrix for rotation about Y-axis.

   Parameters
   ----------
   theta : float
       Rotation angle in radians.
   thetadot : float
       Rate of change of `theta` in radians/second.
     
   Returns
   -------
   m3 : tpm.M3
       A rotation matrix about Y-axis.

   Notes
   -----
   The rotation matrix::

                    -sin(theta) 0  -cos(theta)
      thetadot *         0      0       0  
                    cos(theta)  0  -sin(theta)

   """
   m3 = M3()
   m3.setM3(tpm_vec.m3RyDot(theta, thetadot))
   return m3

def m3rz(theta):
   """Rotation matrix for rotation about Z-axis.

   Parameters
   ----------
   theta : float
       Rotation angle in radians.

   Returns
   -------
   m3 : tpm.M3
       A rotation matrix about Z-axis.

   Notes
   -----
   The rotation matrix::

        cos(theta) sin(theta) 0
       -sin(theta) cos(theta) 0
             0          0     1
             
   """
   m3 = M3()
   m3.setM3(tpm_vec.m3Rz(theta))
   return m3

def m3rzdot(theta, thetadot):
   """Derivative of rotation matrix for rotation about Z-axis.

   Parameters
   ----------
   theta : float
       Rotation angle in radians.
   thetadot : float
       Rate of change of `theta` in radians/second.
     
   Returns
   -------
   m3 : tpm.M3
       A rotation matrix about Z-axis.

   Notes
   -----
   The rotation matrix::

                    -sin(theta)  cos(theta)  0
      thetadot *    -cos(theta) -sin(theta)  0
                          0            0     0

   """
   m3 = M3()
   m3.setM3(tpm_vec.m3RzDot(theta, thetadot))
   return m3


cdef class M6(object):
    """Class that wraps M6 structure.

    This is essential a 2x2 array of tpm.M3 matrices.

    Attributes
    ----------
    pp : tpm.M3
        m6[0][0].
    pv : tpm.M3
        m6[0][1].
    vp : tpm.M3
        m6[1][0].
    vv : tpm.M3
        m6[1][1]
        
    """
    cdef tpm_vec.M6 _m6

    def __cinit__(self):
        self._m6 = tpm_vec.m6I(1.0)
        
    def __init__(self):
        self._m6 = tpm_vec.m6I(1.0)

    cdef tpm_vec.M6 getM6(self):
        return self._m6

    cdef setM6(self, tpm_vec.M6 m6):
        self._m6 = m6
        
    def __getPP(self):
        pp = M3()
        pp.setM3(self._m6.m[0][0])
        return pp
    
    def __setPP(self, M3 m3):
        self._m6.m[0][0] = m3.getM3()

    pp = property(__getPP, __setPP, doc="PP component.")

    def __getPV(self):
        pv = M3()
        pv.setM3(self._m6.m[0][1])
        return pv
    
    def __setPV(self, M3 m3):
        self._m6.m[0][1] = m3.getM3()
        
    pv = property(__getPV, __setPV, doc="PV component.")
    
    def __getVP(self):
        vp = M3()
        vp.setM3(self._m6.m[1][0])
        return vp
    
    def __setVP(self, M3 m3):
        self._m6.m[1][0] = m3.getM3()
        
    vp = property(__getVP, __setVP, doc="VP component.")

    def __getVV(self):
        vv = M3()
        vv.setM3(self._m6.m[1][1])
        return vv
    
    def __setVV(self, M3 m3):
        self._m6.m[1][1] = m3.getM3()
        
    vv = property(__getVV, __setVV, doc="VV component.")

    def __add__(M6 self, M6 other):
        # Cython doesn't distinguish between add and radd. Hence type
        # check on self.
        m6 = M6()
        m6.setM6(tpm_vec.m6sum(self.getM6(), other.getM6()))
        return m6
    
    def __sub__(M6 self, M6 other):
        # Cython does not differentiate sub and rsub; hence typecheck.
        m6 = M6()
        m6.setM6(tpm_vec.m6diff(self.getM6(), other.getM6()))
        return m6

    def __mul__(M6 self, double x):
        # Cython doesn't distinguish between mul and rmul. Hence type
        # check on self.
        m6 = M6()
        m6.setM6(tpm_vec.m6scale(self.getM6(), x))
        return m6

    def __str__(self):
        return self.__unicode__().encode("utf-8")
    
    def __unicode__(self):
        return unicode(tpm_vec.m6fmt(self._m6))
    
    def inv(self):
        """Inverse of M6 matrix.

        Returns
        -------
        m : tpm.M6
            Inverse matrix.
            
        """
        m6 = M6()
        m6.setM6(tpm_vec.m6inv(self.getM6()))
        return m6

    def m6v3(self, V3CP v3):
        """Product of M6 matrix and V3CP vector.

        Returns
        -------
        v : tpm.V3CP
            Cartesian vector obtained by multiplying the PP component
            of this matrix with the given Cartesian vector.
            
        """
        v = V3CP()
        v.setV3(tpm_vec.m6v3(self.getM6(), v3.getV3()))
        return v

    def m6v6(self, V6C v6):
        """Product of M6 matrix and V6C vector.

        Returns
        -------
        v : tpm.V6C
            Cartesian vector obtained by multiplying this matrix with
            the given Cartesian vector.
        
        """
        v = V6C()
        v.setV6(tpm_vec.m6v6(self.getM6(), v6.getV6()))
        return v
        
        
def m6qx(x, xdot):
    """An M6 matrix for rotation about X-axis.

    Parameters
    ----------
    x : float
        Angle of rotation in radians.
    xdot : float
        Rate of change angle of rotation in radians/second.

    Returns
    -------
    m : tpm.M6
        An M6 matrix for rotating a V6 vector about the X-axis.
        
    """
    m6 = M6()
    m6.setM6(tpm_vec.m6Qx(x, xdot))
    return m6

def m6qy(y, ydot):
    """An M6 matrix for rotation about Y-axis.

    Parameters
    ----------
    x : float
        Angle of rotation in radians.
    xdot : float
        Rate of change of angle of rotation in radians/second.

    Returns
    -------
    m : tpm.M6
        An M6 matrix for rotating a V6 vector about the Y-axis.

    """
    m6 = M6()
    m6.setM6(tpm_vec.m6Qy(y, ydot))
    return m6

def m6qz(z, zdot):
    """An M6 matrix for rotation about Z-axis.

    Parameters
    ----------
    x : float
        Angle of rotation in radians.
    xdot : float
        Rate of change or angle of rotation in radians/second.

    Returns
    -------
    m : tpm.M6
        An M6 matrix for rotating a V6 vector about the Z-axis.

    """
    m6 = M6()
    m6.setM6(tpm_vec.m6Qz(z, zdot))
    return m6
