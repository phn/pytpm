# -*- coding: utf-8 -*-
# The following line must be present in the tpm.pyx file.
# cimport tpm_times 

M_PI = tpm_times.M_PI
MJD_0 = tpm_times.MJD_0
B1950 = tpm_times.B1950
J2000 = tpm_times.J2000
J1984 = tpm_times.J1984
CB = tpm_times.CB
CJ = tpm_times.CJ
SUNDAY  = tpm_times.SUNDAY 
MONDAY  = tpm_times.MONDAY
TUESDAY = tpm_times.TUESDAY
WEDNESDAY = tpm_times.WEDNESDAY
THURSDAY =  tpm_times.THURSDAY
FRIDAY  =   tpm_times.FRIDAY
SATURDAY =  tpm_times.SATURDAY 

cdef class DMS(object):
    """Angle in degrees, arc-minutes and arc-seconds.

    A class to represent angle in degrees, arc-minutes and
    arc-seconds. It can be initialized using angle in other units and
    can be converted into other units. It can be initialized with angle
    in radians, `r`, angle in hours, `h`, and also using degrees,
    arc-minutes and arc-seconds of the angle, `dd`, `mm` and `ss`,
    respectively. If `r` is given then its value is used, and others
    are ignored. If `h` is present, then it is preferred over `dd`,
    `mm` and `ss`. All of `dd`, `mm` and `ss` are used, if they are
    present.

    .. warning:: In this class, the negative sign is used for each part
                 of the angle separately. This is different from the
                 usual case in sexagesimal notation where the sign
                 applies to the whole angle. Also, after calling the
                 normalize method the sign gets assigned to the degrees
                 part. Hence this class is not recommended for use
                 outside PyTPM.
    
    Parameters
    ----------
    r : float, optional
        Angle in radians
    h : float, optional
        Angle in hours.
    dd : float, int, optional
        Angle in degrees, or the degrees part.
    mm : float, int, optional
        Angle in arc-minutes or the arc-minutes part of angle.
    ss : float, int, optional
        Angle in arc-seconds or the arc-seconds part of angle.

    Attributes
    ----------
    dd, mm, ss: float
        Degrees, arc-minutes and arc-seconds of the angle.

    """
    valid_keys = ('r', 'h', 'dd', 'mm', 'ss')
    cdef tpm_times.DMS _dms
    def __cinit__(self):
        self._dms.dd = 0.0
        self._dms.mm = 0.0
        self._dms.ss = 0.0

    def __init__(self, **kwargs):
        for key in kwargs:
            if key not in self.valid_keys:
                raise TypeError, "Invalid keyword: {0}".format(key)
        if "r" in kwargs:
            self._dms = tpm_times.r2dms(kwargs['r'])
        elif "h" in kwargs:
            self._dms = tpm_times.h2dms(kwargs['h'])
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
        cdef tpm_times.DMS dms
        return unicode(tpm_times.fmt_dms(self._dms))

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
        """Convert to an HMS object.

        Returns a tpm.HMS class containing the angle in this instance
        converted into hours, minutes and seconds.

        Returns
        -------
        hms : tpm.HMS
            A tpm.HMS object.
            
        """
        cdef tpm_times.HMS _hms
        _hms = tpm_times.dms2hms(self._dms)
        hms = HMS()
        hms._hms = _hms
        return hms

    def normalize(self):
        """Normalize components.

        Normalizes the arc-minutes and arc-seconds of the angle into
        the proper range. Note that after normalize the sign of the
        angle applies to the degrees part alone, and not to the whole
        angle.

        Don't use this class outside of PyTPM.

        Examples
        --------
        >>> from pytpm import tpm
        >>> dms = tpm.DMS(dd=-1.23)
        >>> dms.dd, dms.mm, dms.ss
        (-1.23, 0.0, 0.0)
        >>> print dms
        -01D 13' 47.999"
        >>> dms.normalize()
        >>> dms.dd, dms.mm, dms.ss
        (-2.0, 46.0, 12.00000000000017)

        Note that in the above case if we were to do dms.dd=-1.0,
        dms.mm=13 and dms.ss=48, we would get different results.

        >>> dms.dd = -1
        >>> dms.mm = 46.0
        >>> dms.ss = 12.0
        >>> print dms
        --> print(dms)
        -00D 13' 48.000"        
        """
        self._dms = tpm_times.dms2dms(self._dms)

    def to_degrees(self):
        """Return angle in decimal degrees.

        Angle in degrees, arc-minutes and arc-seconds is converted into
        decimal degrees.

        Returns
        -------
        dd : float
            Angle in degrees.

        """
        return tpm_times.dms2d(self._dms)

    def to_hours(self):
        """Return angle in decimal hours.

        Angle in degrees, arc-minutes and arc-seconds is converted into
        hours.

        Returns
        -------
        hh : float
            Angle in hours.
        
        """
        return tpm_times.dms2h(self._dms)

    def to_radians(self):
        """Return angle in radians.

        Angle in degrees, arc-minutes and arc-seconds is converted into
        radians.

        Returns
        -------
        r : float
            Angle in radians.
        
        """
        return tpm_times.dms2r(self._dms)

    
cdef class HMS(object):
    """Angle (or time) in hours, minutes and seconds.

    This can be initialized using angles in radians, `r`, degrees `dd`,
    and directly providing hours, `hh`, minutes `mm` and seconds `ss`.
    The keyword used in initialization is the first keyword in the
    following order of precedence: `r`, `dd` and then zero or more
    of `hh`, `mm` and `ss`.

    Parameters
    ----------
    r : float, optional
        Angle in radians
    dd : float, optional
        Angle in degrees.
    hh : float, int, optional
        Angle in hours, or the hours part.
    mm : float, int, optional
        Angle in minutes or the minutes part of angle.
    ss : float, int, optional
        Angle in seconds or the seconds part of angle.

    Attributes
    ----------
    hh, mm, ss: float
        hours, minutes and seconds of the angle.

    """
    valid_keys = ('r', 'dd', 'hh', 'mm', 'ss')
    cdef tpm_times.HMS _hms
    def __cinit__(self):
        self._hms.hh = 0.0
        self._hms.mm = 0.0
        self._hms.ss = 0.0

    def __init__(self,**kwargs):
        for key in kwargs:
            if key not in self.valid_keys:
                raise TypeError, "Invalid keyword: {0}".format(key)
        if "r" in kwargs:
            self._hms = tpm_times.r2hms(kwargs['r'])
        elif "dd" in kwargs:
            self._hms = tpm_times.d2hms(kwargs['dd'])
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
        cdef tpm_times.HMS hms
        hms = tpm_times.hms2hms(self._hms)
        s = tpm_times.fmt_hms(hms)
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
        """Convert to a DMS object.

        Returns a tpm.DMS class containing the angle/time in this
        instance converted into degrees, arc-minutes, and arc-seconds.

        Returns
        -------
        dms : tpm.DMS
            A tpm.DMS object.
            
        """
        cdef tpm_times.DMS _dms
        _dms = tpm_times.hms2dms(self._hms)
        dms = DMS()
        dms._dms = _dms
        return dms

    def normalize(self):
        """Normalize components.

        Normalizes the angle so that hours and minutes part are integer
        valued and the fractional part gets assigned to
        seconds. Similar to the case of `DMS`, the negative sign gets
        assigned to the hours part.

        Examples
        --------
        >>> from pytpm import tpm
        >>> h = tpm.HMS()
        >>> h.hh = 12.34
        >>> h.mm = 1.3
        >>> h.ss = 61.4
        >>> h
        {'mm': 1.3, 'ss': 61.399999999999999, 'hh': 12.34}
        >>> h.normalize()
        >>> h
        {'mm': 22.0, 'ss': 43.400000000001455, 'hh': 12.0}
        >>> h.hh = -12.34
        >>> h
        {'mm': 22.0, 'ss': 43.400000000001455, 'hh': -12.34}
        >>> h.normalize()
        >>> h
        {'mm': 2.0, 'ss': 19.400000000001967, 'hh': -12.0}
        
        """
        self._hms = tpm_times.hms2hms(self._hms)

    def to_hours(self):
        """Convert time into hours.

        Angle in hours, minutes and seconds is converted into hours.

        Returns
        -------
        h : float
            Angle in hours.
        
        """
        return tpm_times.hms2h(self._hms)

    def to_degrees(self):
        """Convert HMS into decimal degrees.

        Angle in hours, minutes and seconds is converted into degrees.

        Returns
        -------
        d : float
            Angle in degrees.
            
        """
        return tpm_times.hms2d(self._hms)

    def to_radians(self):
        """Convert HMS into radians.

        Angle in hours, minutes and seconds is converted into radians.

        Returns
        -------
        r : float
            Angle in radians.
        """
        return tpm_times.hms2r(self._hms)
    
    
cdef class YMD(object):
    """Class for representing data-time.

    Date and time is represented using (year, month, day, hours,
    minutes and seconds) in the Gregorian calendar. This can be
    initialized in several ways. If `j` is present then other are
    ignored. If `j` is not present then preference is given to `year`,
    and `jdd` in that order. If none of these are present then zero or
    more of the remaining arguments are used.

    Parameters
    ----------
    j : float, optional
        Julian date. The calendar date-time will be calculated from
        this.
    year : float, optional
        Year with fractional part.
    ydd : 2-element tuple of floats, optional
        Year and day of the year. Year is in the Gregorian calendar.
    y : int, optional
        Year.
    m : int, optional
        Month.
    dd : float, optional
        Day, which can have a fractional part.
    hh : float, optional
        Hour of the day.
    mm : float, optional
        Minute.
    ss : float, optional
        Second.

    Attributes
    ----------
    y : int
        Year.
    m : int
        Month.
    dd : float
        Day.
    hh : float
        Hour.
    mm : float
        Minute.
    ss : float
        Second.

    """
    valid_keys = ('j','year','ydd','y','m','dd','hh','mm','ss')
    cdef tpm_times.YMD _ymd
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
            self._ymd = tpm_times.j2ymd(kwarg['j'])
        elif "year" in kwarg:
            self._ymd = tpm_times.y2ymd(kwarg['year'])
        elif "ydd" in kwarg:
            # Must be tuple (integer year, double day)
            y,d = kwarg['ydd']
            self._ymd = tpm_times.ydd2ymd(y,d)
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
        cdef tpm_times.YMD ymd
        ymd = tpm_times.ymd2ymd(self._ymd)
        s = tpm_times.fmt_ymd(ymd)
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
        """Normalize YMD.

        The components `y`, `m`, `dd`, `hh`, `mm` and `ss` are
        normalized into their proper ranges.

        Examples
        --------
        >>> ymd = tpm.YMD(y=2010,m=3,dd=12.5,hh=12.25)
        >>> ymd
        {'mm': 0.0, 'dd': 12.5, 'm': 3, 'ss': 0.0, 'hh': 12.25, 'y': 2010}
        >>> ymd.normalize()
        >>> ymd
        {'mm': 14.0, 'dd': 13.0, 'm': 3, 'ss': 59.999986588954926, 'hh': 0.0, 'y': 2010}
                
        """
        self._ymd = tpm_times.ymd2ymd(self._ymd)

    def to_jd(self):
        """Convert into a tpm.JD object.

        Returns
        -------
        jd : tpm.JD
            Contains Julian date corresponding to the Calendar date.

        Examples
        --------
        >>> j = tpm.YMD(y=2000,m=1,dd=1,hh=12.0).to_jd()
        >>> j
        {'mm': 0.0, 'ss': 0.0, 'dd': 2451545.0, 'hh': 0.0}

        """
        cdef tpm_times.JD _jd
        _jd = tpm_times.ymd2jd(self._ymd)
        jd = JD()
        jd._jd = _jd
        return jd

    def to_j(self):
        """Convert YMD into scalar Julian date.

        Returns
        -------
        jd : float
            The Julian date corresponding to the Calendar date-time.

        Examples
        --------
        >>> tpm.YMD(y=2000,m=1,dd=1,hh=12.0).to_j()
        2451545.0
        
        """
        return tpm_times.ymd2j(self._ymd)
        
    def raw_str(self):
        """A string representation in the 'raw' format.

        Returns
        -------
        s : str
            A "raw" representation of the Calendar date-time.

        Examples
        --------
        >>> tpm.YMD(y=2000,m=1,dd=1,hh=12.0).raw_str()
        '2000 1 1 12 0 0'
        >>> tpm.YMD(y=2000,m=6,dd=1.34,hh=12.0,mm=12.678).raw_str()
        '2000 6 1.34 12 12.678 0'

        Printing or converting to str gives a nicely formatted string
        representation.
        
        >>> ymd = tpm.YMD(y=2000,m=1,dd=1,hh=12.0)
        >>> print ymd
        --> print(ymd)
        Sat Jan  1 12:00:00.000 2000
        >>> str(ymd)
        'Sat Jan  1 12:00:00.000 2000'

        """
        return tpm_times.fmt_ymd_raw(self._ymd)

    def doy(self):
        """Day of the year corresponding to the date-time.

        Returns
        -------
        doy : float
            Day of the year.

        Examples
        --------
        >>> tpm.YMD(y=2000,m=1,dd=1,hh=12.0).doy()
        1.5
        >>> tpm.YMD(y=2000,m=1,dd=1,hh=12.5).doy()
        1.5208333334885538
        
        """
        return tpm_times.ymd2dd(self._ymd)

    def to_year(self):
        """Convert date-time into a year number.

        Returns
        -------
        year : float
            Year number, i.e., year + (day / num. days).

        Examples
        --------
        >>> tpm.YMD(y=2000,m=1,dd=1).to_year()
        2000.0027322404371
        >>> 2000+(1/366.0)
        2000.0027322404371
        >>> tpm.YMD(y=2000,m=1,dd=1,hh=12.0).to_year()
        2000.0040983606557
        >>> 2000+(1/366.0+12/(24.0*366.0))
        2000.0040983606557
        
        """
        return tpm_times.ymd2y(self._ymd)

    
cdef class JD(object):
    """Class for Julian dates, with hours, minutes and seconds.

    This class represents a Julian date using a day part and hours,
    minutes and seconds. This can be initialized using several
    parameters. If multiple keyword arguments are given then one that
    gets used is based on this order: `j`, `year` and then zero or more
    of `dd`, `hh`, `mm` and `ss`.

    Parameters
    ----------
    j : float, optional
        Scalar Julian date.
    year : float, optional.
        Date-time as a year number. This is just
        (integer_year + day / num_of_days.)
    dd : float, optional
        Scalar Julian date or scalar Julian day number.
    hh : float, optional
        Hour of the day.
    mm : float, optional
        Minute.
    ss : float, optional
        Second.

    Attributes
    ----------
    dd : float
        The day part of the Julian date. This can also contain
        fractional part.
    hh : float
        Hour of the day.
    mm : float
        Minutes.
    ss : float
        Seconds.
    
    """
    valid_keys = ('j', 'year', 'dd', 'hh', 'mm', 'ss')
    cdef tpm_times.JD _jd
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
            self._jd = tpm_times.j2jd(kwargs['j'])
        elif "year" in kwargs:
            self._jd = tpm_times.y2jd(kwargs['year'])
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
        cdef tpm_times.JD jd
        jd = tpm_times.jd2jd(self._jd)
        s = tpm_times.fmt_jd(jd)
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
        """Normalize the JD structure.

        Normalize the components into their proper ranges and carry the
        fractional part of the date into seconds.

        Examples
        --------
        >>> j = tpm.JD(j=2451545.1234467)
        >>> j
        {'mm': 0.0, 'ss': 0.0, 'dd': 2451545.1234467002, 'hh': 0.0}
        >>> j.normalize()
        >>> j
        {'mm': 57.0, 'ss': 45.794894099235535, 'dd': 2451545.0, 'hh': 2.0}
        
        """
        self._jd = tpm_times.jd2jd(self._jd)

    def to_ymd(self):
        """Convert to YMD (Gregorian calendar).

        Returns
        -------
        ymd : tpm.YMD
            The Julian date is converted into Gregorian calendar date
            and returned as a tpm.YMD object.

        Examples
        --------
        >>> jd = tpm.JD(dd=2451545.0, hh=12.0)
        >>> ymd = jd.to_ymd()
        >>> ymd
        {'mm': 0.0, 'dd': 1.5, 'm': 1, 'ss': 0.0, 'hh': 12.0, 'y': 2000}

        """
        cdef tpm_times.YMD _ymd
        _ymd = tpm_times.jd2ymd(self._jd)
        ymd = YMD()
        ymd._ymd = _ymd
        return ymd

    def to_j(self):
        """Convert JD to a scalar Julian date.

        Returns
        -------
        j : float
            The scalar Julian date.

        Examples
        --------
        >>> jd = tpm.JD(dd=2451545.0, hh=12.0)
        >>> jd.to_j()
        2451545.5
        
        """
        return tpm_times.jd2j(self._jd)

    def to_year(self):
        """Convert JD into year (Gregorian calendar).

        Returns
        -------
        y : float
            Year with fractional part. This is just
            (integer_year + day/num_of_days).

        Examples
        --------
        >>> jd = tpm.JD(dd=2451545.0, hh=12.0)
        >>> jd.to_year()
        2000.0054644808743
        >>> 2000+(2/366.0)
        2000.0054644808743
            
        """
        return tpm_times.jd2y(self._jd)

    
def byear2jd(byear):
    """Convert Besselian year into a Julian date.

    Parameters
    ----------
    byear: float
        Besselian year.

    Returns
    -------
    j : float
        Julian date corresponding to the given Besselian year.

    Examples
    --------
    >>> tpm.byear2jd(1950.0)
    2433282.4234590498
    >>> tpm.byear2jd(2000.0)
    2451544.5333981365
    
    """
    return tpm_times.BYEAR2JD(byear)
 
def jd2byear(jd):
    """Convert Julian date into a Besselian year.

    Parameters
    ----------
    jd: float
        Julian date.

    Returns
    -------
    byear : float
        Besselian year corresponding to the given Julian date.

    Examples
    --------
    >>> tpm.jd2byear(tpm.B1950)
    1950.0
    >>> tpm.jd2byear(tpm.J2000)
    2000.0012775135656
    
    """
    return tpm_times.JD2BYEAR(jd)
 
def jyear2jd(jyear):
    """Convert Julian year into a Julian date.

    Parameters
    ----------
    jyear : float
        Julian year.

    Returns
    -------
    jd : float
        Julian date corresponding to the given Julian year.

    Examples
    --------
    >>> tpm.jyear2jd(2000.0)
    2451545.0
    >>> tpm.jyear2jd(1950.0)
    2433282.5
    
    """
    return tpm_times.JYEAR2JD(jyear)

def jd2jyear(jd):
    """Convert Julian date into Julian year.

    Parameters
    ----------
    jd : float
        Julian date.

    Returns
    -------
    jyear : float
        Julian year corresponding to the given Juilan date.

    Examples
    --------
    >>> tpm.jd2jyear(tpm.J2000)
    2000.0
    >>> tpm.jd2jyear(tpm.B1950)
    1949.9997904422992
    
    """
    return tpm_times.JD2JYEAR(jd)

def jd_now():
    """Return current Julian date as a JD object.

    This function is only accurate to the nearest second.

    Returns
    -------
    jd : tpm.JD
         Julian date as a ``JD`` object.

    """
    jd = JD()
    jd._jd = tpm_times.jd_now()
    return jd

def utc_now():
    """Current UTC as a Julian date.

    This function is only accurate to the nearest second.
    
    Returns
    -------
    jd : float
        Julian date.

    """
    return tpm_times.utc_now()

def gcal2j(int y, int m, int dd):
    """Return Julian day number for the Gregorian calendar date.

    Returns the Julian date for mid-night of the given date.
    
    Parameters
    ----------
    y : int
        Year in the Gregorian calendar.
    m : int
        Month in the Gregorian calendar.
    dd : int
        Day in the Gregorian calendar.

    Returns
    -------
    jd : float
        Julian date corresponding to the given date.

    Examples
    --------
    >>> tpm.gcal2j(2000,1,1)
    2451545.0
    >>> tpm.gcal2j(2010,1,1)
    2455198.0
    >>> tpm.gcal2j(1950,1,1)
    2433283.0
    
    """
    return tpm_times.gcal2j(y, m, dd)

def jcal2j(int y, int m, int dd):
    """Return Julian day number for the Julian calendar date.

    Returns the Julian date for mid-night of the given date.
    
    Parameters
    ----------
    y : int
        Year in the Julian calendar.
    m : int
        Month in the Julian calendar.
    dd : int
        Day in the Julian calendar.

    Returns
    -------
    jd : float
        Julian date corresponding to the given date.

    Examples
    --------
    >>> tpm.jcal2j(1950,1,1)
    2433296.0
    >>> tpm.jcal2j(2000,1,1)
    2451558.0
    >>> tpm.jcal2j(2010,1,1)
    2455211.0
    >>> tpm.jcal2j(1950,1,1)
    2433296.0
    
    """
    return tpm_times.jcal2j(y, m, dd)

cpdef j2gcal(double j):
    """Convert Julian date into Gregorian calendar date.

    Returns the year, month and day.

    Parameters
    ----------
    j : float
        Julian date.

    Returns
    -------
    d : dict
        A dictionary for the date in the Gregorian calendar. The
        keys in the dictionary are: 'y'=year, 'm'=month, 'dd'=day.

    Examples
    --------
    >>> tpm.j2gcal(tpm.J2000)
    {'dd': 1, 'm': 1, 'y': 2000}
    >>> tpm.j2gcal(tpm.B1950)
    {'dd': 31, 'm': 12, 'y': 1949}
    
    """
    cdef int y, m, d
    y = m = d = 0;
    tpm_times.j2gcal(&y, &m, &d, j)
    return dict(y=y, m=m, dd=d)

cpdef j2jcal(double j):
    """Convert Julian date into Julian calendar date.

    Returns the year, month and day.

    Parameters
    ----------
    j : float
        Julian date.

    Returns
    -------
    d : dict
        A dictionary for the date in the Julian calendar. The
        keys in the dictionary are: 'y'=year, 'm'=month, 'dd'=day.

    Examples
    --------
    >>> tpm.j2jcal(tpm.J2000)
    {'dd': 19, 'm': 12, 'y': 1999}
    >>> tpm.j2jcal(tpm.B1950)
    {'dd': 18, 'm': 12, 'y': 1949}

    """
    cdef int y, m, d
    y = m = d = 0;
    tpm_times.j2jcal(&y, &m, &d, j)
    return dict(y=y, m=m, dd=d)

def j2y(j):
    """Convert Julian date into Gregorian calendar year with fractional part.

    Parameters
    ----------
    j : float
        Julian date

    Returns
    -------
    year : float
        Year, including fractional part, in the Gregorian
    calendar. This is just (integer_year + day / num_of_days.)

    Examples
    --------
    >>> tpm.j2y(tpm.J2000)
    2000.0040983606557
    >>> 2000+(1.5/366)
    2000.0040983606557
    >>> tpm.j2y(tpm.J2000+366)
    2001.004109589041
    
    """
    return tpm_times.j2y(j)

def y2j(y):
    """Convert Gregorian calendar year with fractional part into Julian date.

    Parameters
    ----------
    y : float
        Gregorian calendar year with fractional part.

    Returns
    -------
    j : float
        Julian date.

    Examples
    --------
    >>> tpm.y2j(2000.0040983606557)
    2451545.0
    >>> tpm.y2j(2001.004109589041)
    2451911.0
    >>> tpm.j2gcal(tpm.y2j(2001.004109589041))
    {'dd': 1, 'm': 1, 'y': 2001}
    
    """
    return tpm_times.y2j(y)

def j2dow(j):
    """Return day of week for the given Julian date.

    Parameters
    ----------
    j : float
        Julian date (Gregorian calendar).

    Returns
    -------
    dow : int
        Day of the week: 0 - Sunday, 6 - Saturday.

    Examples
    --------
    >>> j = tpm.gcal2j(2010,1,1)
    >>> tpm.fmt_y(tpm.j2y(j))
    'Fri Jan  1 12:00:00.000 2010'
    >>> tpm.j2dow(j)
    5
    
    """
    return tpm_times.j2dow(j)

def y2doy(int y):
    """Return number of days in the given Gregorian calendar year.

    Parameters
    ----------
    y : int
        Year in the Gregorian calendar.

    Returns
    -------
    doy : int
        Number of days in the year.

    Examples
    --------
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
    return tpm_times.y2doy(y)

cpdef char *fmt_alpha(double alpha):
    """Normalize and format angle in radians into a str: ' ##H ##M ##.###S'.

    Parameters
    ----------
    alpha : float
        Angle in radians.

    Returns
    -------
    fmts : str
        String of the form ' ##H ##M ##.###S'.

    Notes
    -----
    This function normalizes the given angle in radians into the range
    [0,360) and then converts it into a string that represents
    angle/time in the 24-hour format. The angle is properly divided
    into hours, minutes and seconds.

    This is useful for formatting "longitudinal" angles, such as right
    ascension.

    Examples
    --------
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
    return tpm_times.fmt_alpha(alpha)

cpdef char* fmt_delta(double delta):
    """Normalize and format angle in radians into a str: ±###D ##' ##.###".

    Parameters
    ----------
    alpha : float
        Angle in radians.

    Return
    ------
    fmts : str
         String of the form ±###D ##' ##.###".

    Notes
    -----
    This function normalizes the given angle in radians into the range
    [-π/2, π/2] and then formats it into a string of the form
    ±###D ##\' ##.###", where each part of the string corresponds to
    degrees, arc-minutes and arc-seconds.

    This is useful for formatted output of "latitudinal" angles, such
    as declination.

    Examples
    --------
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
    return tpm_times.fmt_delta(delta)

cpdef char *fmt_d(double d):
    """Format angle in degrees into a string: ±###D ##' ##.###".

    Parameters
    ----------
    d : float
        Angle in degrees.

    Returns
    -------
    fmts : str
        String of the form ±###D ##' ##.###".

    Notes
    -----
    This function will format the given angle in degrees, into a string
    containing degrees, arc-minutes and arc-seconds. The angle is not
    normalized into any range, but is used as such.

    The degrees part can be two or three digits long.

    Examples
    --------
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
    return tpm_times.fmt_d(d)
    
cpdef char *fmt_h(double h):
    """Format hours into a string: ±##H ##M ##.###S".

    Parameters
    ----------
    d : float
        Angle in hours.

    Returns
    -------
    fmts : str
        String of the form ±##H ##M ##.###S.

    Notes
    -----
    This function will format the given angle in hours, into a string
    containing hours, minutes and seconds. The angle is not normalized
    into any range, but is used as such.

    Examples
    --------
    >>> tpm.fmt_h(1.23456)
    ' 01H 14M 04.416S'
    >>> tpm.fmt_h(13.456)
    ' 13H 27M 21.599S'
    >>> tpm.fmt_h(-13.456)
    '-13H 27M 21.599S'
    >>> tpm.fmt_h(-133.456)
    '-133H 27M 21.599S'
    
    """
    return tpm_times.fmt_h(h)

cpdef char *fmt_j(double j):
    """Format Julian date into a string.

    Parameters
    ----------
    j : float
        Julian date.

    Returns
    -------
    fmts : str
        String of the form: JD ##H ##M ##.###S.

    Notes
    -----
    This function takes a Julian date and returns a string that has a
    whole number Julian date and the fraction of the day expressed as
    hours, minutes and seconds in the 24-hour format.

    Examples
    --------
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
    return tpm_times.fmt_j(j)

cpdef char* fmt_r(double r):
    """Format radians into a string with angle expressed as degrees.

    Parameters
    ----------
    r : float
        Angle in radians.

    Returns
    -------
    fmts : str
        String of the form: ±###D ##' ##.###".

    Notes
    -----
    The function converts the angle given in radians into degrees and
    then return a string of the format ±###D ##' ##.###". The
    fractional part of the angle is converted into arc-minutes and
    arc-seconds, but otherwise no normalization is done.

    Examples
    --------
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
    return tpm_times.fmt_r(r)

cpdef char* fmt_y(double y):
    """Format years, including fractional part, into a string.

    Parameters
    ----------
    y : float
        Year, including fractional part.

    Returns
    -------
    fmts : str
        String of the form: AAA BBB DD HH:MM:SS.SSS YYYY, where AAA is
        the week day, BBB is the month and then the numbers that follow
        are indicate the day, the time in 24-hour format and the year.

    Examples
    --------
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
    return tpm_times.fmt_y(y)

def d2d(d):
    """Normalize angle in degrees into (-360, 360).

    Parameters
    ----------
    d : float
        Angle in degrees.

    Returns
    -------
    d : float
        Angle in degrees normalized into (-360, 360).

    Examples
    --------
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
    return tpm_times.d2d(d)

def h2h(h):
    """Normalize angle in hours into [0, 24).

    Parameters
    ----------
    h : float
        Angle in hours.

    Returns
    -------
    h : float
        Angle in hours normalized into [0, 24).

    Examples
    --------
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
    return tpm_times.h2h(h)

def r2r(r):
    """Normalize angle in radians into [0, 2π).

    Parameters
    ----------
    r : float
        Angle in radians.

    Returns
    -------
    r : float
        Angle in radians normalized into [0, 2π).

    Examples
    --------
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
    return tpm_times.r2r(r)

# In TPM the following are in vec.h and then redefined in
# times.h. I am including all of these in tpm_times for
# convenience.
def d2h(d):
    """Convert angle in degrees into hours.

    Parameters
    ----------
    d : float
        Angle in degrees.

    Returns
    -------
    h : float
        Angle in hours.

    Examples
    --------
    >>> tpm.d2h(180.0)
    12.0
    >>> tpm.d2h(-180.0)
    -12.0
    >>> tpm.d2h(12.3456)
    0.82303999999999999
    
    """
    return tpm_times.d2h(d)

def h2d(h):
    """Convert angle in hours into degrees.

    Parameters
    ----------
    h : float
        Angle in hours.

    Returns
    -------
    d : float
        Angle in degrees.

    Examples
    --------
    >>> tpm.h2d(12.0)
    180.0
    >>> tpm.h2d(-12.0)
    -180.0
    >>> tpm.h2d(-25)
    -375.0
    
    """
    return tpm_times.h2d(h)

def d2r(d):
    """Convert angle in degrees into degrees.

    Parameters
    ----------
    d : float
        Angle in degrees.

    Returns
    -------
    d : float
        Angle in radians.

    Examples
    --------
    >>> tpm.d2r(180.0)
    3.1415926535897931
    >>> tpm.d2r(-180.0)
    -3.1415926535897931
    >>> tpm.d2r(361.0)
    6.3006385996995293
    
    """
    return tpm_times.d2r(d)

def r2d(r):
    """Convert angle in radians into degrees.

    Parameters
    ----------
    r : float
        Angle in radians.

    Returns
    -------
    d : float
        Angle in degrees.

    Examples
    --------
    >>> tpm.r2d(tpm.M_PI)
    180.0
    >>> tpm.r2d(tpm.M_PI/4.0)
    45.0
    >>> tpm.r2d(-tpm.M_PI/4.0)
    -45.0
    >>> tpm.r2d(-2*tpm.M_PI)
    -360.0
    
    """
    return tpm_times.r2d(r)

def h2r(h):
    """Convert angle in hours into radians.

    Parameters
    ----------
    h : float
        Angle in hours.

    Returns
    -------
    r : float
        Angle in radians.

    Examples
    --------
    >>> tpm.h2r(12.0)
    3.1415926535897931
    >>> tpm.h2r(-12.0)
    -3.1415926535897931
    
    """
    return tpm_times.h2r(h)

def r2h(r):
    """Convert angle in radians into hours.

    Parameters
    ----------
    r : float
        Angle in radians.

    Returns
    -------
    h : float
        Angle in hours.

    Examples
    --------
    >>> tpm.r2h(tpm.M_PI)
    12.0
    >>> tpm.r2h(-tpm.M_PI)
    -12.0
    
    """
    return tpm_times.r2h(r)

def d2as(d):
    """Convert angle in degrees into arc-seconds.

    Parameters
    ----------
    d : float
        Angle in degrees.

    Returns
    -------
    arcs : float
        Angle in arc-seconds.

    Examples
    --------
    >>> tpm.d2as(1.0)
    3600.0
    >>> tpm.d2as(-1.0)
    -3600.0
    
    """
    return tpm_times.d2as(d)

def as2d(arcs):
    """Convert angle in arc-seconds into degrees.

    Parameters
    ----------
    arcs : float
        Angle in arc-seconds.

    Returns
    -------
    d : float
        Angle in degrees.

    Examples
    --------
    >>> tpm.as2d(3600.0)
    1.0
    >>> tpm.as2d(-3600.0)
    -1.0
    
    """
    return tpm_times.as2d(arcs)

def as2h(arcs):
    """Convert angle in arc-seconds into hours.

    Parameters
    ----------
    arcs : float
        Angle in arc-seconds.

    Returns
    -------
    h : float
        Angle in hours.

    Examples
    --------
    >>> tpm.as2h(3600.0*180.0)
    12.0
    >>> tpm.as2h(-3600.0*180.0)
    -12.0
    
    """
    return tpm_times.as2h(arcs)

def h2as(h):
    """Convert angle in hours into arc-seconds.

    Parameters
    ----------
    h : float
        Angle in hours.

    Returns
    -------
    arcs : float
        Angle in arc-seconds.

    Examples
    --------
    >>> tpm.h2as(12.0)
    648000.0
    >>> tpm.h2as(-12.0)
    -648000.0
    
    """
    return tpm_times.h2as(h)

def r2as(r):
    """Convert angle in radians into arc-seconds.

    Parameters
    ----------
    r : float
        Angle in radians.

    Returns
    -------
    arcs : float
        Angle in arc-seconds.

    Examples
    --------
    >>> tpm.r2as(tpm.M_PI)
    648000.0
    >>> tpm.r2as(-tpm.M_PI)
    -648000.0
    """
    return tpm_times.r2as(r)

def as2r(arcs):
    """Convert angle in arc-seconds into radians.

    Parameters
    ----------
    arcs : float
        Angle in arc-seconds.

    Returns
    -------
    r : float
        Angle in radians.

    Examples
    --------
    >>> tpm.as2r(3600.0*180.0)
    3.1415926535897931
    >>> tpm.as2r(-3600.0*180.0)
    -3.1415926535897931
    
    """
    return tpm_times.as2r(arcs)
