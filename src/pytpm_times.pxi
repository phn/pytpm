# -*- coding: utf-8 -*-
# The following line must be present in the pytpm.pyx file.
# cimport _tpm_times 

M_PI = _tpm_times.M_PI
MJD_0 = _tpm_times.MJD_0
B1950 = _tpm_times.B1950
J2000 = _tpm_times.J2000
J1984 = _tpm_times.J1984
CB = _tpm_times.CB
CJ = _tpm_times.CJ
SUNDAY  = _tpm_times.SUNDAY 
MONDAY  = _tpm_times.MONDAY
TUESDAY = _tpm_times.TUESDAY
WEDNESDAY = _tpm_times.WEDNESDAY
THURSDAY =  _tpm_times.THURSDAY
FRIDAY  =   _tpm_times.FRIDAY
SATURDAY =  _tpm_times.SATURDAY 

cdef class DMS(object):
    cdef _tpm_times.DMS _dms
    def __cinit__(self):
        self._dms.dd = 0.0
        self._dms.mm = 0.0
        self._dms.ss = 0.0

    def __init__(self, **kwargs):
        if "r" in kwargs:
            self._dms = _tpm_times.r2dms(kwargs['r'])
        elif "h" in kwargs:
            self._dms = _tpm_times.h2dms(kwargs['h'])
        else:
            self._dms.dd = kwargs.get('dd',0.0)
            self._dms.mm = kwargs.get('mm',0.0) 
            self._dms.ss = kwargs.get('ss',0.0) 
        
    def __getdd(self):
        return self._dms.dd
    def __setdd(self,value):
        self._dms.dd = value
    dd = property(__getdd, __setdd,doc="Degrees.")

    def __getmm(self):
        return self._dms.mm
    def __setmm(self,value):
        self._dms.mm = value
    mm = property(__getmm, __setmm,doc="Minutes of arc.")

    def __getss(self):
        return self._dms.ss
    def __setss(self,value):
        self._dms.ss = value
    ss = property(__getss, __setss,doc="Seconds of arc.")

    def __repr__(self):
        d = {'dd':  self.dd, 'mm': self.mm, 'ss': self.ss}
        return repr(d)
    
    def __str__(self):
        return self.__unicode__().encode("utf-8")
    
    def __unicode__(self):
        cdef _tpm_times.DMS dms
        dms = _tpm_times.dms2dms(self._dms)
        return u"{0:+03.0f}\u00B0 {1:02.0f}' {2:06.3f}\"".format(
            dms.dd, dms.mm, dms.ss)

    def __add__(self, other):
        # Cython does not have __radd__ and the first parameter may not
        # be this object
        if isinstance(self, DMS) and isinstance(other, DMS):
            # return a new DMS object
            dms = self.__class__()
            dms.dd = self.dd + other.dd
            dms.mm = self.mm + other.mm
            dms.ss = self.ss + other.ss
            return dms
        else:
            raise TypeError, "Can only add two DMS values."

    def __sub__(self, other):
        # Cython does not have __rsub__ and the first parameter may not
        # be this object
        if isinstance(self, DMS) and isinstance(other, DMS):
            # return a new DMS object
            dms = self.__class__()
            dms.dd = self.dd - other.dd
            dms.mm = self.mm - other.mm
            dms.ss = self.ss - other.ss
            return dms
        else:
            raise TypeError, "Can only subtract two DMS values."

    def to_hms(self):
        """Convert to HMS object."""
        cdef _tpm_times.HMS _hms
        _hms = _tpm_times.dms2hms(self._dms)
        hms = HMS()
        hms._hms = _hms
        return hms

    def normalize(self):
        """Normalize components."""
        self._dms = _tpm_times.dms2dms(self._dms)

    def to_degrees(self):
        """Return angle in decimal degrees."""
        return _tpm_times.dms2d(self._dms)

    def to_hours(self):
        """Return angle in decimal hours."""
        return _tpm_times.dms2h(self._dms)

    def to_radians(self):
        """Return angle in radians."""
        return _tpm_times.dms2r(self._dms)

    
cdef class HMS(object):
    cdef _tpm_times.HMS _hms
    def __cinit__(self):
        self._hms.hh = 0.0
        self._hms.mm = 0.0
        self._hms.ss = 0.0

    def __init__(self,**kwargs):
        if "r" in kwargs:
            self._hms = _tpm_times.r2hms(kwargs['r'])
        elif "d" in kwargs:
            self._hms = _tpm_times.d2hms(kwargs['d'])
        else:
            self._hms.hh = kwargs.get('hh',0.0)
            self._hms.mm = kwargs.get('mm',0.0) 
            self._hms.ss = kwargs.get('ss',0.0) 
        
    def __gethh(self):
        return self._hms.hh
    def __sethh(self,value):
        self._hms.hh = value
    hh = property(__gethh, __sethh,doc="Hours.")

    def __getmm(self):
        return self._hms.mm
    def __setmm(self,value):
        self._hms.mm = value
    mm = property(__getmm, __setmm,doc="Minutes.")

    def __getss(self):
        return self._hms.ss
    def __setss(self,value):
        self._hms.ss = value
    ss = property(__getss, __setss,doc="Seconds.")

    def __repr__(self):
        d = {'hh':  self.hh, 'mm': self.mm, 'ss': self.ss}
        return repr(d)
    
    def __str__(self):
        return self.__unicode__().encode("utf-8")
    
    def __unicode__(self):
        cdef _tpm_times.HMS hms
        hms = _tpm_times.hms2hms(self._hms)
        s = _tpm_times.fmt_hms(hms)
        return unicode(s)

    def __add__(self, other):
        # Cython does not have __rdd__ and the first parameter may not
        # be this object
        if isinstance(self, HMS) and isinstance(other, HMS):
            # return a new HMS object
            hms = self.__class__()
            hms.hh = self.hh + other.hh
            hms.mm = self.mm + other.mm
            hms.ss = self.ss + other.ss
            return hms
        else:
            raise TypeError, "Can only add two HMS values."

    def __sub__(self, other):
        # Cython does not have __rsub__ and the first parameter may not
        # be this object
        if isinstance(self, HMS) and isinstance(other, HMS):
            # return a new HMS object
            hms = self.__class__()
            hms.hh = self.hh - other.hh
            hms.mm = self.mm - other.mm
            hms.ss = self.ss - other.ss
            return hms
        else:
            raise TypeError, "Can only subtract two HMS values."

    def to_dms(self):
        cdef _tpm_times.DMS _dms
        _dms = _tpm_times.hms2dms(self._hms)
        dms = DMS()
        dms._dms = _dms
        return dms

    def normalize(self):
        """Normalize components."""
        self._hms = _tpm_times.hms2hms(self._hms)

    def to_hours(self):
        """Convert time into hours."""
        return _tpm_times.hms2h(self._hms)

    def to_degrees(self):
        """Convert HMS into decimal degrees."""
        return _tpm_times.hms2d(self._hms)

    def to_radians(self):
        """Convert HMS into radians."""
        return _tpm_times.hms2r(self._hms)
    
    
cdef class YMD(object):
    cdef _tpm_times.YMD _ymd
    def __cinit__(self):
        self._ymd.y = 2000
        self._ymd.m = 1
        self._ymd.dd = 0.0
        self._ymd.hms.hh = 0.0
        self._ymd.hms.mm = 0.0
        self._ymd.hms.ss = 0.0
        
    def __init__(self,**kwarg):
        if "j" in kwarg:
            self._ymd = _tpm_times.j2ymd(kwarg['j'])
        elif "year" in kwarg:
            self._ymd = _tpm_times.y2ymd(kwarg['year'])
        else:
            self._ymd.y = kwarg.get('y',2000)
            self._ymd.m = kwarg.get('m',1)
            self._ymd.dd = kwarg.get('dd',0)
            self._ymd.hms.hh = kwarg.get('hh',0.0) 
            self._ymd.hms.mm = kwarg.get('mm',0.0) 
            self._ymd.hms.ss = kwarg.get('ss',0.0)
        
    def __gety(self):
        return self._ymd.y
    def __sety(self,value):
        assert type(value) == type(1), "Year must be an integer."
        self._ymd.y = value
    y = property(__gety, __sety,doc="Year as an integer.")

    def __getm(self):
        return self._ymd.m
    def __setm(self,value):
        assert type(value) == type(1), "Month must be an integer."
        self._ymd.m = value
    m = property(__getm, __setm,doc="Month as an integer.")

    def __getdd(self):
        return self._ymd.dd
    def __setdd(self,value):
        self._ymd.dd = value
    dd = property(__getdd, __setdd,doc="Day as a float.")

    def __gethh(self):
        return self._ymd.hms.hh
    def __sethh(self,value):
        self._ymd.hms.hh = value
    hh = property(__gethh, __sethh,doc="Hours as a float.")

    def __getmm(self):
        return self._ymd.hms.mm
    def __setmm(self,value):
        self._ymd.hms.mm = value
    mm = property(__getmm, __setmm,doc="Minutes as a float.")

    def __getss(self):
        return self._ymd.hms.ss
    def __setss(self,value):
        self._ymd.hms.ss = value
    ss = property(__getss, __setss,doc="Seconds as a float.")

    def __repr__(self):
        ymd = dict(y=self.y, m=self.m, dd=self.dd, hh=self.hh,
                   mm=self.mm, ss=self.ss)
        return repr(ymd)

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        cdef _tpm_times.YMD ymd
        ymd = _tpm_times.ymd2ymd(self._ymd)
        s = _tpm_times.fmt_ymd(ymd)
        return unicode(s)

    def __sub__(self, other):
        # Cython does not have __rdd__ and the first parameter may not
        # be this object
        if isinstance(self, YMD) and isinstance(other, YMD):
            # return a new HMS object
            ymd = self.__class__()
            ymd.y = self.y - other.y
            ymd.m = self.m - other.m
            ymd.dd = self.dd - other.dd
            ymd.hh = self.hh - other.hh
            ymd.mm = self.mm - other.mm
            ymd.ss = self.ss - other.ss
            return ymd
        else:
            raise TypeError, "Can only subtract two YMD values."

    def normalize(self):
        """Normalize YMD."""
        self._ymd = _tpm_times.ymd2ymd(self._ymd)

    def to_jd(self):
        """Convert into YMD."""
        cdef _tpm_times.JD _jd
        _jd = _tpm_times.ymd2jd(self._ymd)
        jd = JD()
        jd._jd = _jd
        return jd

    def to_j(self):
        """Convert YMD into scalar Julian date."""
        return _tpm_times.ymd2j(self._ymd)
        
    def raw_str(self):
        """YMD string in the 'raw' format."""
        return _tpm_times.fmt_ymd_raw(self._ymd)

    def doy(self):
        """Day of the year corresponding to date in the YMD."""
        return _tpm_times.ymd2dd(self._ymd)

    def to_year(self):
        """Convert YMD into a year number."""
        return _tpm_times.ymd2y(self._ymd)

    
    
cdef class JD(object):
    cdef _tpm_times.JD _jd
    def __cinit__(self):
        self._jd.dd = 2451545.5
        self._jd.hms.hh = 0.0
        self._jd.hms.mm = 0.0
        self._jd.hms.ss = 0.0

    def __init__(self, **kwargs):
        if "j" in kwargs:
            self._jd = _tpm_times.j2jd(kwargs['j'])
        elif "year" in kwargs:
            self._jd = _tpm_times.y2jd(kwargs['year'])
        else:
            self._jd.dd = kwargs.get('dd',0.0)
            self._jd.hms.hh = kwargs.get('hh', 0.0)
            self._jd.hms.mm = kwargs.get('mm', 0.0)
            self._jd.hms.ss = kwargs.get('ss', 0.0)

    def __getdd(self):
        return self._jd.dd
    def __setdd(self,value):
        self._jd.dd = value
    dd = property(__getdd, __setdd,doc="Day as a float.")

    def __gethh(self):
        return self._jd.hms.hh
    def __sethh(self,value):
        self._jd.hms.hh = value
    hh = property(__gethh, __sethh,doc="Hours.")

    def __getmm(self):
        return self._jd.hms.mm
    def __setmm(self,value):
        self._jd.hms.mm = value
    mm = property(__getmm, __setmm,doc="Minutes.")

    def __getss(self):
        return self._jd.hms.ss
    def __setss(self,value):
        self._jd.hms.ss = value
    ss = property(__getss, __setss,doc="Seconds.")

    def __repr__(self):
        d = dict(dd=self.dd, hh=self.hh, mm=self.mm, ss=self.ss)
        return repr(d)

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        cdef _tpm_times.JD jd
        jd = _tpm_times.jd2jd(self._jd)
        s = _tpm_times.fmt_jd(jd)
        return unicode(s)

    def __add__(self, other):
        # Cython does not have __rdd__ and the first parameter may not
        # be this object
        if isinstance(self, JD) and isinstance(other, JD):
            # return a new JD object
            jd = self.__class__()
            jd.dd = self.dd + other.dd
            jd.hh = self.hh + other.hh
            jd.mm = self.mm + other.mm
            jd.ss = self.ss + other.ss
            return jd
        else:
            raise TypeError, "Can only add two JD values."

    def __sub__(self, other):
        # Cython does not have __rsub__ and the first parameter may not
        # be this object
        if isinstance(self, JD) and isinstance(other, JD):
            # return a new JD object
            jd = self.__class__()
            jd.dd = self.dd - other.dd
            jd.hh = self.hh - other.hh
            jd.mm = self.mm - other.mm
            jd.ss = self.ss - other.ss
            return jd
        else:
            raise TypeError, "Can only add two JD values."

    def normalize(self):
        """Normalize the JD structure."""
        self._jd = _tpm_times.jd2jd(self._jd)

    def to_ymd(self):
        """Convert to YMD (Gregorian calendar)."""
        cdef _tpm_times.YMD _ymd
        _ymd = _tpm_times.jd2ymd(self._jd)
        ymd = YMD()
        ymd._ymd = _ymd
        return ymd

    def to_j(self):
        """Convert JD to a Julian date."""
        return _tpm_times.jd2j(self._jd)

    def to_year(self):
        """Convert JD into year (Gregorian calendar)."""
        return _tpm_times.jd2y(self._jd)

    
#double BYEAR2JD(double x)
#cpdef double BYEAR2JD(double byear):
#    """Convert Besselian year into a Julian date."""
#    return _tpm_times.BYEAR2JD(byear)
# 
##double JD2BYEAR(double x)
#cpdef double JD2BYEAR(double jd):
#    """Convert Julian date into a Julian year."""
#    return _tpm_times.JD2BYEAR(jd)
# 
##double JYEAR2JD(double x)
##double JD2JYEAR(double x)
# 
##DMS d2dms(double d)
#cpdef DMS d2dms(double d):
#    return _tpm_times.d2dms(d)
# 
##DMS dms2dms(DMS dms)
#cpdef DMS dms2dms(DMS dms):
#    return DMS(_tpm_times.dms2dms(dms._dms))

#DMS hms2dms(HMS hms)
#HMS dms2hms(DMS dms)
#HMS h2hms(double h)
#HMS hms2hms(HMS hms)
#JD j2jd(double j)
#JD jd2jd(JD jd)
#JD jd_diff(JD jd1, JD jd2)
#JD jd_now(void)
#JD jd_sum(JD jd1, JD jd2)
#JD ymd2jd(YMD ymd)
#YMD jd2ymd(JD jd)
#YMD y2ymd(double y)
#YMD ydd2ymd(int y, double dd)
#YMD ymd2ymd(YMD ymd)
#char *fmt_alpha(double alpha)
cpdef char *fmt_alpha(double alpha):
    """Format angle as Right Ascension."""
    return _tpm_times.fmt_alpha(alpha)

#char *fmt_d(double d)
cpdef char *fmt_d(double d):
    """Format degrees into a string."""
    return _tpm_times.fmt_d(d)

#char *fmt_delta(double delta)
cpdef char* fmt_delta(double delta):
    """Format radians as declination."""
    return _tpm_times.fmt_delta(delta)
    
#char *fmt_h(double h)
cpdef char *fmt_h(double h):
    """Format hours into a string."""
    return _tpm_times.fmt_h(h)

#char *fmt_j(double j)
cpdef char *fmt_j(double j):
    """Format Julian date into a string."""
    return _tpm_times.fmt_j(j)

#char *fmt_ymd(YMD ymd)
#char *fmt_ymd_raw(YMD ymd)
#double d2d(double d)
cpdef double d2d(double d):
    """Normalize angle in degrees into (-360, 360)."""
    return _tpm_times.d2d(d)

#double dms2d(DMS dms)
#double gcal2j(int y, int m, int d)
#double h2h(double h)
cpdef double h2h(double h):
    return _tpm_times.h2h(h)

#double hms2h(HMS hms)
#double jcal2j(int y, int m, int d)
#double jd2j(JD jd)
#double r2r(double r)
cpdef double r2r(double r):
    return _tpm_times.r2r(r)

#double utc_now(void)
#double ymd2dd(YMD ymd)
#double ymd2rdb(YMD ymd)
#double ymd2y(YMD ymd)
#int argv2dms(DMS *dms, char *argv[], int argnum, int cooked)
#int argv2hms(HMS *hms, char *argv[], int argnum, int cooked)
#int argv2ymd(YMD *ymd, char *argv[], int argnum, int cooked)
#int j2dow(double j)
#int y2doy(int y)
#void j2gcal(int *y, int *m, int *d, double j)
#void j2jcal(int *y, int *m, int *d, double j)
# 
#DMS d2hms(double d)
#double dms2h(DMS dms)
#double dms2r(DMS dms)
#char *fmt_dms(DMS dms)
#cpdef char* fmt_dms(DMS dms):
#    return _tpm_times.fmt_dms(dms._dms)
#char *fmt_hms(HMS hms)
#cpdef char *fmt_hms (HMS hms):
#    return _tpm_times.fmt_hms(hms._hms)
#char *fmt_jd(JD jd)
#char *fmt_r(double r)
#char *fmt_y(double y)
#DMS h2dms(double h)
#double hms2d(HMS hms)
#double hms2r(HMS hms)
#double j2j(double j)
#double j2y(double j)
cpdef double j2y(double j):
    return _tpm_times.j2y(j)

#double j2ymd(double j)
#double jd2y(JD jd)
#DMS r2dms(double r)
#HMS r2hms(double r)
#double y2j(double y)
cpdef double y2j(double y):
    return _tpm_times.y2j(y)

#JD y2jd(double y)
#double y2y(double y)
#double ymd2j(YMD ymd)
#YMD ymd_diff(YMD ymd1, YMD ymd2)

# In TPM the following are in vec.h and then redefined in
# times.h. I am including all of these in _tpm_times for
# convenience.
#define d2h(d)	
cpdef double d2h(double d):
    return _tpm_times.d2h(d)
#define h2d(h)	
cpdef double h2d(double h):
    return _tpm_times.h2d(h)
#define d2r(d)	
cpdef double d2r(double d):
    return _tpm_times.d2r(d)
#define r2d(r)	
cpdef double r2d(double r):
    return _tpm_times.r2d(r)
#define h2r(h)	
cpdef double h2r(double h):
    return _tpm_times.h2r(h)
#define r2h(r)	
cpdef double r2h(double r):
    return _tpm_times.r2h(r)
#define d2as(d)	
cpdef double d2as(double d):
    return _tpm_times.d2as(d)
#define as2d(x)	
cpdef double as2d(double x):
    return _tpm_times.as2d(x)
#define as2h(x)	
cpdef double as2h(double x):
    return _tpm_times.as2h(x)
#define h2as(h)	
cpdef double h2as(double h):
    return _tpm_times.h2as(h)
#define r2as(r)	
cpdef double r2as(double r):
    return _tpm_times.r2as(r)
#define as2r(x)	
cpdef double as2r(double x):
    return _tpm_times.as2r(x)
