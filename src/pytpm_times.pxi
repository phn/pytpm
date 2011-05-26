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
    valid_keys = ('r', 'h', 'dd', 'mm', 'ss')
    cdef _tpm_times.DMS _dms
    def __cinit__(self):
        self._dms.dd = 0.0
        self._dms.mm = 0.0
        self._dms.ss = 0.0

    def __init__(self, **kwargs):
        for key in kwargs:
            if key not in self.valid_keys:
                raise TypeError, "Invalid keyword: {0}".format(key)
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
        return unicode(_tpm_times.fmt_dms(self._dms))

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
        """Normalize components.

        Note: ``angle = (sign*dd) + (mm/60.0) + (ss/3600.0)`` and not
        ``sign * ( (dd) + (mm/60.0) + (ss/3600.0) )``. For negative
        numbers this gives different answers for the components when
        normalize is called. Similarly, for negative numbers, the angle
        will be incorrect if the components are separately set. In the
        first case, print statement does not have this problem.

          >>> dms = tpm.DMS(dd=-1.23)
          >>> dms.dd, dms.mm, dms.ss
          (-1.23, 0.0, 0.0)
          >>> print dms
          -01D 13' 47.999"
          >>> dms.normalize()
          >>> dms.dd, dms.mm, dms.ss
          (-2.0, 46.0, 12.00000000000017)
          >>> print dms
          -01D 13' 47.999"
          
        """
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
    valid_keys = ('r', 'dd', 'hh', 'mm', 'ss')
    cdef _tpm_times.HMS _hms
    def __cinit__(self):
        self._hms.hh = 0.0
        self._hms.mm = 0.0
        self._hms.ss = 0.0

    def __init__(self,**kwargs):
        for key in kwargs:
            if key not in self.valid_keys:
                raise TypeError, "Invalid keyword: {0}".format(key)
        if "r" in kwargs:
            self._hms = _tpm_times.r2hms(kwargs['r'])
        elif "dd" in kwargs:
            self._hms = _tpm_times.d2hms(kwargs['dd'])
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
    valid_keys = ('j','year','ydd','y','m','dd','hh','mm','ss')
    cdef _tpm_times.YMD _ymd
    def __cinit__(self):
        self._ymd.y = 2000
        self._ymd.m = 1
        self._ymd.dd = 0.0
        self._ymd.hms.hh = 0.0
        self._ymd.hms.mm = 0.0
        self._ymd.hms.ss = 0.0
        
    def __init__(self,**kwarg):
        for key in kwarg:
            if key not in self.valid_keys:
                raise TypeError, "Invalid keyword: {0}".format(key)
        if "j" in kwarg:
            self._ymd = _tpm_times.j2ymd(kwarg['j'])
        elif "year" in kwarg:
            self._ymd = _tpm_times.y2ymd(kwarg['year'])
        elif "ydd" in kwarg:
            # Must be tuple (integer year, double day)
            y,d = kwarg['ydd']
            self._ymd = _tpm_times.ydd2ymd(y,d)
        else:
            y = kwarg.get('y', 2000)
            assert type(y) == type(1), "Year must be an integer."
            self._ymd.y = y
            m = kwarg.get('m', 1)
            assert type(m) == type(1), "Month must be an integer."
            self._ymd.m = m
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
    valid_keys = ('j', 'year', 'dd', 'hh', 'mm', 'ss')
    cdef _tpm_times.JD _jd
    def __cinit__(self):
        self._jd.dd = 2451545.5
        self._jd.hms.hh = 0.0
        self._jd.hms.mm = 0.0
        self._jd.hms.ss = 0.0

    def __init__(self, **kwargs):
        for key in kwargs:
            if key not in self.valid_keys:
                raise TypeError, "Invalid keyword: {0}".format(key)
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
cpdef double byear2jd(double byear):
    """Convert Besselian year into a Julian date.

    :param byear: Besselian year.
    :type byear: float

    :return: Julian date corresponding to the given Besselian year.
    :rtype: float

    >>> tpm.byear2jd(1950.0)
    2433282.4234590498
    >>> tpm.byear2jd(2000.0)
    2451544.5333981365
    """
    return _tpm_times.BYEAR2JD(byear)
 
#double JD2BYEAR(double x)
cpdef double jd2byear(double jd):
    """Convert Julian date into a Besselian year.

    :param jd: Julian date.
    :type jd: float

    :return: Besselian year corresponding to the given Julian date.
    :rtype: float

    >>> tpm.jd2byear(tpm.B1950)
    1950.0
    >>> tpm.jd2byear(tpm.J2000)
    2000.0012775135656
    """
    return _tpm_times.JD2BYEAR(jd)
 
#double JYEAR2JD(double x)
cpdef double jyear2jd(double jyear):
    """Convert Julian year into a Julian date.

    :param jyear: Julian year.
    :type jyear: float

    :return: Julian date corresponding to the given Julian year.
    :rtype: float

    >>> tpm.jyear2jd(2000.0)
    2451545.0
    >>> tpm.jyear2jd(1950.0)
    2433282.5
    """
    return _tpm_times.JYEAR2JD(jyear)

#double JD2JYEAR(double x)
cpdef double jd2jyear(double jd):
    """Convert Julian date into Julian year.

    :param jd: Julian date.
    :type jd: float
    :return: Julian year corresponding to the given Juilan date.
    :rtype: float

    >>> tpm.jd2jyear(tpm.J2000)
    2000.0
    >>> tpm.jd2jyear(tpm.B1950)
    1949.9997904422992
    """
    return _tpm_times.JD2JYEAR(jd)

#JD jd_now(void)
cpdef JD jd_now():
    """Return current Julian date as a JD object.

    :return: Julian date as a ``JD`` object.
    :rtype: ``JD``
    
    This function is only accurate to the nearest second.
    """
    jd = JD()
    jd._jd = _tpm_times.jd_now()
    return jd

#double utc_now(void)
cpdef double utc_now():
    """Current UTC as a Julian date.

    :return: Julian date.
    :rtype: float
    
    This function is only accurate to the nearest second.
    """
    return _tpm_times.utc_now()

#double gcal2j(int y, int m, int d)
cpdef gcal2j(int y, int m, int dd):
    """Return Julian day number for the Gregorian calendar date.

    :param y: Year in the Gregorian calendar.
    :type y: integer
    :param m: Month in the Gregorian calendar.
    :type m: integer
    :param dd: Day in the Gregorian calendar.
    :type dd: integer

    :return: Julian date corresponding to the given date.
    :rtype: float

    >>> tpm.gcal2j(2000,1,1)
    2451545.0
    >>> tpm.gcal2j(2010,1,1)
    2455198.0
    >>> tpm.gcal2j(1950,1,1)
    2433283.0
    """
    return _tpm_times.gcal2j(y, m, dd)

#double jcal2j(int y, int m, int d)
cpdef double jcal2j(int y, int m, int dd):
    """Return Julian day number for the Julian calendar date.

    :param y: Year in the Julian calendar.
    :type y: integer
    :param m: Month in the Julian calendar.
    :type m: integer
    :param dd: Day in the Julian calendar.
    :type dd: integer

    :return: Julian date corresponding to the given date.
    :rtype: float

    >>> tpm.jcal2j(1950,1,1)
    2433296.0
    >>> tpm.jcal2j(2000,1,1)
    2451558.0
    >>> tpm.jcal2j(2010,1,1)
    2455211.0
    >>> tpm.jcal2j(1950,1,1)
    2433296.0
    """
    return _tpm_times.jcal2j(y, m, dd)

#void j2gcal(int *y, int *m, int *d, double j)
cpdef j2gcal(double j):
    """Convert Julian date into Gregorian calendar date.

    :param j: Julian date.
    :type j: float

    :return: A dictionary for the date in the Gregorian calendar. The
            keys in the dictionary are: 'y'=year, 'm'=month, 'dd'=day.
    :rtype: dict

    >>> tpm.j2gcal(tpm.J2000)
    {'dd': 1, 'm': 1, 'y': 2000}
    >>> tpm.j2gcal(tpm.B1950)
    {'dd': 31, 'm': 12, 'y': 1949}
    """
    cdef int y, m, d
    y = m = d = 0;
    _tpm_times.j2gcal(&y, &m, &d, j)
    return dict(y=y, m=m, dd=d)

#void j2jcal(int *y, int *m, int *d, double j)
cpdef j2jcal(double j):
    """Convert Julian date into Julian calendar date.

    :param j: Julian date.
    :type j: float

    :return: A dictionary for the date in the Julian calendar. The
            keys in the dictionary are: 'y'=year, 'm'=month, 'dd'=day.
    :rtype: dict

    >>> tpm.j2gcal(tpm.J2000)
    {'dd': 1, 'm': 1, 'y': 2000}
    >>> tpm.j2gcal(tpm.B1950)
    {'dd': 31, 'm': 12, 'y': 1949}
    """
    cdef int y, m, d
    y = m = d = 0;
    _tpm_times.j2jcal(&y, &m, &d, j)
    return dict(y=y, m=m, dd=d)

#double j2y(double j)
cpdef double j2y(double j):
    """Convert Julian date into Gregorian calendar year with fractional part.

    :param j: Julian date.
    :type j: float

    :return: Year, including fractional part, in the Gregorian calendar.
    :rtype: float

    >>> tpm.j2y(tpm.J2000)
    2000.0040983606557
    >>> tpm.j2y(tpm.J2000+366)
    2001.004109589041
    """
    return _tpm_times.j2y(j)

#double y2j(double y)
cpdef double y2j(double y):
    """Convert Gregorian calendar year with fractional part into Julian date.

    :param y: Gregorian calendar year with fractional part.
    :type y: float

    :return: Julian date.
    :rtype: float

    >>> tpm.y2j(2000.0040983606557)
    2451545.0
    >>> tpm.y2j(2001.004109589041)
    2451911.0
    >>> tpm.j2gcal(tpm.y2j(2001.004109589041))
    {'dd': 1, 'm': 1, 'y': 2001}
    """
    return _tpm_times.y2j(y)

#int j2dow(double j)
cpdef int j2dow(double j):
    """Return day of week for the given Gregorian calendar Julian date.

    :param j: Julian date (Gregorian calendar).
    :type j: float

    :return: Day of the week: 0 - Sunday, 6 - Saturday.
    :rtype: integer

    >>> j = tpm.gcal2j(2010,1,1)
    >>> tpm.fmt_y(tpm.j2y(j))
    'Fri Jan  1 12:00:00.000 2010'
    >>> tpm.j2dow(j)
    5
    """
    return _tpm_times.j2dow(j)

#int y2doy(int y)
cpdef int y2doy(int y):
    """Return number of days in the given Gregorian calendar year.

    :param y: Year in the Gregorian calendar.
    :type y: integer

    :return: Number of days in the year.
    :rtype: integer

    >>> tpm.y2doy(2000)
    366
    >>> tpm.y2doy(2001)
    365
    >>> tpm.y2doy(2002)
    365
    >>> tpm.y2doy(2003)
    365
    >>> tpm.y2doy(2004)
    366    
    """
    return _tpm_times.y2doy(y)

#char *fmt_alpha(double alpha)
cpdef char *fmt_alpha(double alpha):
    """Normalize and format angle in radians into a string: ' ##H ##M ##.###S'.

    :param alpha: Angle in radians.
    :type alpha: float

    :return: String of the form ' ##H ##M ##.###S'.
    :rtype: string

    This function normalizes the given angle in radians into the range
    [0,360) and then converts it into a string that represents
    angle/time in the 24-hour format. The angle is properly divided
    into hours, minutes and seconds.

    This is useful for formatting "longitudinal" angles, such as right
    ascension.

    >>> tpm.fmt_alpha(tpm.M_PI)
    ' 12H 00M 00.000S'
    >>> tpm.fmt_alpha(-tpm.M_PI)
    ' 12H 00M 00.000S'
    >>> tpm.fmt_alpha(2*tpm.M_PI)
    ' 00H 00M 00.000S'
    >>> tpm.fmt_alpha(tpm.M_PI/2.0)
    ' 06H 00M 00.000S'
    >>> tpm.fmt_alpha(-tpm.M_PI/2.0)
    ' 18H 00M 00.000S'
    >>> tpm.fmt_alpha(2*tpm.M_PI+(tpm.M_PI/12.0))
    ' 00H 59M 59.999S'
    >>> tpm.fmt_alpha(-(2*tpm.M_PI+(tpm.M_PI/12.0)))
    ' 23H 00M 00.000S'    
    """
    return _tpm_times.fmt_alpha(alpha)

#char *fmt_delta(double delta)
cpdef char* fmt_delta(double delta):
    """Normalize and format angle in radians into a string: ±###D ##' ##.###".

    :param alpha: Angle in radians.
    :type alpha: float

    :return: String of the form ±###D ##' ##.###".
    :rtype: string
    
    This function normalizes the given angle in radians into the range
    [-π/2, π/2] and then formats it into a string of the form
    ±###D ##\' ##.###", where each part of the string corresponds to
    degrees, arc-minutes and arc-seconds.

    This is useful for formatted output of "latitudinal" angles, such
    as declination.

    >>> tpm.fmt_delta(tpm.M_PI/2.0)
    '+90D 00\' 00.000"'
    >>> tpm.fmt_delta(-tpm.M_PI/2.0)
    '-90D 00\' 00.000"'
    >>> tpm.fmt_delta(tpm.M_PI/4.0)
    '+45D 00\' 00.000"'
    >>> tpm.fmt_delta(tpm.M_PI)
    '+00D 00\' 00.000"'
    >>> tpm.fmt_delta(-tpm.M_PI)
    '+00D 00\' 00.000"'
    """
    return _tpm_times.fmt_delta(delta)

#char *fmt_d(double d)
cpdef char *fmt_d(double d):
    """Format angle in degrees into a string: ±###D ##' ##.###".

    :param d: Angle in degrees.
    :type d: float

    :return: String of the form ±###D ##' ##.###".
    :rtype: string

    This function will format the given angle in degrees, into a string
    containing degrees, arc-minutes and arc-seconds. The angle is not
    normalized into any range, but is used as such.

    The degrees part can be two or three digits long.

    >>> tpm.fmt_d(1.234567)
    '+01D 14\' 04.441"'
    >>> tpm.fmt_d(256.9)
    '+256D 53\' 59.999"'
    >>> tpm.fmt_d(-256.9)
    '-256D 53\' 59.999"'
    >>> tpm.fmt_d(6.9)
    '+06D 54\' 00.000"'
    >>> tpm.fmt_d(-361)
    '-361D 00\' 00.000"'
    >>> tpm.fmt_d(720)
    '+720D 00\' 00.000"'
    """
    return _tpm_times.fmt_d(d)
    
#char *fmt_h(double h)
cpdef char *fmt_h(double h):
    """Format hours into a string: ±##H ##M ##.###S".

    :param d: Angle in hours.
    :type d: float

    :return: String of the form ±##H ##M ##.###S.
    :rtype: string

    This function will format the given angle in hours, into a string
    containing hours, minutes and seconds. The angle is not normalized
    into any range, but is used as such.

    >>> tpm.fmt_h(1.23456)
    ' 01H 14M 04.416S'
    >>> tpm.fmt_h(13.456)
    ' 13H 27M 21.599S'
    >>> tpm.fmt_h(-13.456)
    '-13H 27M 21.599S'
    >>> tpm.fmt_h(-133.456)
    '-133H 27M 21.599S'
    """
    return _tpm_times.fmt_h(h)

#char *fmt_j(double j)
cpdef char *fmt_j(double j):
    """Format Julian date into a string.

    :param j: Julian date.
    :type j: float

    :return: String of the form: JD ##H ##M ##.###S.
    :rtype: string

    This function takes a Julian date and returns a string that has a
    whole number Julian date and the fraction of the day expressed as
    hours, minutes and seconds in the 24-hour format.

    >>> tpm.fmt_j(tpm.J2000)
    ' 2451545  00H 00M 00.000S'
    >>> tpm.fmt_j(tpm.J2000+0.5)
    ' 2451545  12H 00M 00.000S'
    >>> tpm.fmt_j(tpm.J2000+0.75)
    ' 2451545  18H 00M 00.000S'
    >>> tpm.fmt_j(tpm.J2000+0.7)
    ' 2451545  16H 48M 00.000S'
    >>> tpm.fmt_j(tpm.J2000-0.7)
    ' 2451544  07H 11M 59.999S'
    """
    return _tpm_times.fmt_j(j)

#char *fmt_r(double r)
cpdef char* fmt_r(double r):
    """Format radians into a string with angle expressed as degrees.
    
    :param r: Angle in radians.
    :type r: float

    :return: String of the form: ±###D ##' ##.###".
    :rtype: string

    The function converts the angle given in radians into degrees and
    then return a string of the format ±###D ##' ##.###". The
    fractional part of the angle is converted into arc-minutes and
    arc-seconds, but otherwise no normalization is done.

    >>> tpm.fmt_r(1.0)
    '+57D 17\' 44.806"'
    >>> tpm.fmt_r(1.2345)
    '+70D 43\' 53.903"'
    >>> tpm.fmt_r(-2*tpm.M_PI)
    '-360D 00\' 00.000"'
    >>> tpm.fmt_r(-3*tpm.M_PI)
    '-540D 00\' 00.000"'
    >>> tpm.fmt_r(3*tpm.M_PI)
    '+540D 00\' 00.000"'
    """
    return _tpm_times.fmt_r(r)

#char *fmt_y(double y)
cpdef char* fmt_y(double y):
    """Format years, including fractional part, into a string.

    :param y: Year, including fractional part.
    :type y: float

    :return: String of the form: AAA BBB DD HH:MM:SS.SSS YYYY,
             where AAA is the week day, BBB is the month and then the
             numbers that follow are indicate the day, the time in
             24-hour format and the year.
    :rtype: string

    >>> tpm.fmt_y(2000.0)
    'Fri Dec 31 00:00:00.000 1999'
    >>> tpm.fmt_y(2000.0+1.0/366)
    'Sat Jan  1 00:00:00.000 2000'
    >>> tpm.fmt_y(2000.0+1.25/366)
    'Sat Jan  1 06:00:00.000 2000'
    >>> tpm.fmt_y(2000.0+1.7/366)
    'Sat Jan  1 16:48:00.000 2000'
    >>> tpm.fmt_y(2001.0+32/365.0)
    'Thu Feb  1 00:00:00.000 2001'
    """
    return _tpm_times.fmt_y(y)

#double d2d(double d)
cpdef double d2d(double d):
    """Normalize angle in degrees into (-360, 360).

    :param d: Angle in degrees.
    :type d: float

    :return: Angle in degrees normalized into (-360, 360).
    :rtype: float
    
    >>> tpm.d2d(0.0)
    0.0
    >>> tpm.d2d(-360.0)
    0.0
    >>> tpm.d2d(360.0)
    0.0
    >>> tpm.d2d(361.0)
    1.0
    >>> tpm.d2d(-361.0)
    359.0
    """
    return _tpm_times.d2d(d)

#double h2h(double h)
cpdef double h2h(double h):
    """Normalize angle in hours into [0, 24).

    :param h: Angle in hours.
    :type h: float

    :return: Angle in hours normalized into [0, 24).
    :rtype: float

    >>> tpm.h2h(0.0)
    0.0
    >>> tpm.h2h(24.0)
    0.0
    >>> tpm.h2h(25.0)
    1.0
    >>> tpm.h2h(-25.0)
    23.0
    >>> tpm.h2h(-1)
    23.0
    >>> tpm.h2h(1)
    1.0
    """
    return _tpm_times.h2h(h)

#double r2r(double r)
cpdef double r2r(double r):
    """Normalize angle in radians into [0, 2π).

    :param r: Angle in radians.
    :type r: float

    :return: Angle in radians normalized into [0, 2π).
    :rtype: float

    >>> tpm.r2r(0.0)
    0.0
    >>> tpm.r2r(2*tpm.M_PI)
    0.0
    >>> tpm.r2r(tpm.M_PI)
    3.1415926535897931
    >>> tpm.r2r(-tpm.M_PI)
    3.1415926535897931
    >>> tpm.r2r(-2*tpm.M_PI)
    0.0
    >>> tpm.r2r(-tpm.M_PI/2.0)
    4.7123889803846897
    """
    return _tpm_times.r2r(r)

# In TPM the following are in vec.h and then redefined in
# times.h. I am including all of these in _tpm_times for
# convenience.
#define d2h(d)	
cpdef double d2h(double d):
    """Convert angle in degrees into hours.

    :param d: Angle in degrees.
    :type d: float

    :return: Angle in hours.
    :rtype: float

    >>> tpm.d2h(180.0)
    12.0
    >>> tpm.d2h(-180.0)
    -12.0
    >>> tpm.d2h(12.3456)
    0.82303999999999999
    """
    return _tpm_times.d2h(d)

#define h2d(h)	
cpdef double h2d(double h):
    """Convert angle in hours into degrees.

    :param h: Angle in hours.
    :type h: float

    :return: Angle in degrees.
    :rtype: float

    >>> tpm.h2d(12.0)
    180.0
    >>> tpm.h2d(-12.0)
    -180.0
    >>> tpm.h2d(-25)
    -375.0
    """
    return _tpm_times.h2d(h)

#define d2r(d)	
cpdef double d2r(double d):
    """Convert angle in degrees into degrees.

    :param d: Angle in degrees.
    :type d: float

    :return: Angle in radians.
    :rtype: float

    >>> tpm.d2r(180.0)
    3.1415926535897931
    >>> tpm.d2r(-180.0)
    -3.1415926535897931
    >>> tpm.d2r(361.0)
    6.3006385996995293
    """
    return _tpm_times.d2r(d)

#define r2d(r)	
cpdef double r2d(double r):
    """Convert angle in radians into degrees.

    :param r: Angle in radians.
    :type r: float

    :return: Angle in degrees.
    :rtype: float

    >>> tpm.r2d(tpm.M_PI)
    180.0
    >>> tpm.r2d(tpm.M_PI/4.0)
    45.0
    >>> tpm.r2d(-tpm.M_PI/4.0)
    -45.0
    >>> tpm.r2d(-2*tpm.M_PI)
    -360.0
    """
    return _tpm_times.r2d(r)

#define h2r(h)	
cpdef double h2r(double h):
    """Convert angle in hours into radians.

    :param h: Angle in hours.
    :type h: float

    :return: Angle in radians.
    :rtype: float

    >>> tpm.h2r(12.0)
    3.1415926535897931
    >>> tpm.h2r(-12.0)
    -3.1415926535897931
    """
    return _tpm_times.h2r(h)

#define r2h(r)	
cpdef double r2h(double r):
    """COnvert angle in radians into hours.

    :param r: Angle in radians.
    :type r: float

    :return: Angle in hours.
    :rtype: float

    >>> tpm.r2h(tpm.M_PI)
    12.0
    >>> tpm.r2h(-tpm.M_PI)
    -12.0
    """
    return _tpm_times.r2h(r)

#define d2as(d)	
cpdef double d2as(double d):
    """Convert angle in degrees into arc-seconds.

    :param d: Angle in degrees.
    :type d: float

    :return: Angle in arc-seconds.
    :rtype: float

   >>> tpm.d2as(1.0)
   3600.0
   >>> tpm.d2as(-1.0)
   -3600.0
    """
    return _tpm_times.d2as(d)

#define as2d(x)	
cpdef double as2d(double arcs):
    """Convert angle in arc-seconds into degrees.

    :param arcs: Angle in arc-seconds.
    :type arcs: float

    :return: Angle in degrees.
    :rtype: float

    >>> tpm.as2d(3600.0)
    1.0
    >>> tpm.as2d(-3600.0)
    -1.0
    """
    return _tpm_times.as2d(arcs)

#define as2h(x)	
cpdef double as2h(double arcs):
    """Convert angle in arc-seconds into hours.

    :param arcs: Angle in arc-seconds.
    :type arcs: float

    :return: Angle in hours.
    :rtype: float

    >>> tpm.as2h(3600.0*180.0)
    12.0
    >>> tpm.as2h(-3600.0*180.0)
    -12.0
    """
    return _tpm_times.as2h(arcs)

#define h2as(h)	
cpdef double h2as(double h):
    """Convert angle in hours into arc-seconds.

    :param h: Angle in hours.
    :type h: float

    :return: Angle in arc-seconds.
    :rtype: float

    >>> tpm.h2as(12.0)
    648000.0
    >>> tpm.h2as(-12.0)
    -648000.0
    """
    return _tpm_times.h2as(h)

#define r2as(r)	
cpdef double r2as(double r):
    """Convert angle in radians into arc-seconds.

    :param r: Angle in radians.
    :type r: float

    :return: Angle in arc-seconds.
    :rtype: float

    >>> tpm.r2as(tpm.M_PI)
    648000.0
    >>> tpm.r2as(-tpm.M_PI)
    -648000.0
    """
    return _tpm_times.r2as(r)

#define as2r(x)	
cpdef double as2r(double arcs):
    """Convert angle in arc-seconds into radians.

    :param arcs: Angle in arc-seconds.
    :type arcs: float

    :return: Angle in radians.
    :rtype: float

    >>> tpm.as2r(3600.0*180.0)
    3.1415926535897931
    >>> tpm.as2r(-3600.0*180.0)
    -3.1415926535897931
    """
    return _tpm_times.as2r(arcs)
