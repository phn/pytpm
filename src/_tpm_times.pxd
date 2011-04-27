# -*- coding: utf-8 -*-
cdef extern from "tpm/times.h":

    # Constants
    cdef double M_PI
    cdef double MJD_0
    cdef double B1950
    cdef double J2000
    cdef double J1984
    cdef double CB
    cdef double CJ
    cdef double SUNDAY
    cdef double MONDAY
    cdef double TUESDAY
    cdef double WEDNESDAY
    cdef double THURSDAY
    cdef double FRIDAY
    cdef double SATURDAY

    # degree, minute, second
    cdef struct s_dms:
        double dd
        double mm
        double ss
        
    ctypedef s_dms DMS
    
    # hour, minute, second */
    cdef struct s_hms:
        double hh
        double mm
        double ss
            
    ctypedef s_hms HMS
     
    # year, month, day
    cdef struct s_ymd:
        int y
        int m
        double dd
        HMS hms
            
    ctypedef s_ymd YMD
     
    # Julian day 
    cdef struct s_jd:
        double dd       # day part 
        HMS hms         # fractional part
            
    ctypedef s_jd JD

    double BYEAR2JD(double x)
    double JD2BYEAR(double x)
    double JYEAR2JD(double x)
    double JD2JYEAR(double x)

    # In TPM the following are in vec.h and then redefined in
    # times.h. I am including these in _tpm_times for convenience.
    double d2h(double d)	
    double h2d(double h)	
    double d2r(double d)	
    double r2d(double r)	
    double h2r(double h)	
    double r2h(double r)	
    double d2as(double d)	
    double as2d(double x)	
    double as2h(double x)	
    double h2as(double h)	
    double r2as(double r)	
    double as2r(double x)	

    DMS d2dms(double d)
    DMS dms2dms(DMS dms)
    DMS hms2dms(HMS hms)
    HMS dms2hms(DMS dms)
    HMS h2hms(double h)
    HMS hms2hms(HMS hms)
    JD j2jd(double j)
    JD jd2jd(JD jd)
    JD jd_now()
    JD ymd2jd(YMD ymd)
    YMD jd2ymd(JD jd)
    YMD y2ymd(double y)
    YMD ydd2ymd(int y, double dd)
    YMD ymd2ymd(YMD ymd)
    char *fmt_alpha(double alpha)
    char *fmt_d(double d)
    char *fmt_delta(double delta)
    char *fmt_h(double h)
    char *fmt_j(double j)
    char *fmt_ymd(YMD ymd)
    char *fmt_ymd_raw(YMD ymd)
    double d2d(double d)
    double dms2d(DMS dms)
    double gcal2j(int y, int m, int d)
    double h2h(double h)
    double hms2h(HMS hms)
    double jcal2j(int y, int m, int d)
    double jd2j(JD jd)
    double r2r(double r)
    double utc_now()
    double ymd2dd(YMD ymd)
    double ymd2rdb(YMD ymd)
    double ymd2y(YMD ymd)
    int j2dow(double j)
    int y2doy(int y)
    void j2gcal(int *y, int *m, int *d, double j)
    void j2jcal(int *y, int *m, int *d, double j)

    HMS d2hms(double d)
    double dms2h(DMS dms)
    double dms2r(DMS dms)
    char *fmt_dms(DMS dms)
    char *fmt_hms(HMS hms)
    char *fmt_jd(JD jd)
    char *fmt_r(double r)
    char *fmt_y(double y)
    DMS h2dms(double h)
    double hms2d(HMS hms)
    double hms2r(HMS hms)
    double j2j(double j)
    double j2y(double j)
    YMD j2ymd(double j)
    double jd2y(JD jd)
    DMS r2dms(double r)
    HMS r2hms(double r)
    double y2j(double y)
    JD y2jd(double y)
    double y2y(double y)
    double ymd2j(YMD ymd)

