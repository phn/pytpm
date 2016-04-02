cdef extern from "tpm/vec.h":
    ##############################
    ##### vec.h #####
    ##############################
    # vec.h #includes v3, v6, m3 and m6.
    # From v3.h.
    cdef struct s_v3:
        int type
        double v[3]

    ctypedef s_v3 V3

    # From v6.h.
    cdef struct s_v6:
        V3 v[2]

    ctypedef s_v6 V6

    int POS
    int VEL

    # From m3.h.
    cdef struct s_m3:
        double m[3][3]

    ctypedef s_m3 M3

    # From m6.h
    cdef struct s_m6:
        M3 m[2][2]

    ctypedef s_m6 M6

    int CARTESIAN
    int SPHERICAL
    int POLAR

    M3 m3I(double x)
    M3 m3O()
    M3 m3Rx(double x)
    M3 m3RxDot(double x, double xdot)
    M3 m3Ry(double y)
    M3 m3RyDot(double y, double ydot)
    M3 m3Rz(double z)
    M3 m3RzDot(double z, double zdot)
    M3 m3diff(M3 m1, M3 m2)
    M3 m3inv(M3 m)
    M3 m3m3(M3 m1, M3 m2)
    M3 m3scale(M3 m, double s)
    M3 m3sum(M3 m1, M3 m2)
    M6 m6I(double x)
    M6 m6O()
    M6 m6Qx(double x, double xdot)
    M6 m6Qy(double y, double ydot)
    M6 m6Qz(double z, double zdot)
    M6 m6diff(M6 m1, M6 m2)
    M6 m6inv(M6 m)
    M6 m6m6(M6 m1, M6 m2)
    M6 m6scale(M6 m, double s)
    M6 m6sum(M6 m1, M6 m2)
    V3 m3v3(M3 m, V3 v1)
    V3 m6v3(M6 m, V3 v)
    V3 v3c2s(V3 vc)
    V3 v3cross(V3 v1, V3 v2)
    V3 v3diff(V3 v1, V3 v2)
    V3 v3init(int type)
    V3 v3s2c(V3 vs)
    V3 v3scale(V3 v, double s)
    V3 v3sum(V3 v1, V3 v2)
    V3 v3unit(V3 v)
    V3 v62v3(V6 v6, double dt)
    V6 m3v6(M3 m, V6 v1)
    V6 m6v6(M6 m, V6 v1)
    V6 v32v6(V3 v3)
    V6 v6c2s(V6 vc)
    V6 v6cross(V6 v1, V6 v2)
    V6 v6diff(V6 v1, V6 v2)
    V6 v6init(int type)
    V6 v6s2c(V6 vs)
    V6 v6scale(V6 v, double s)
    V6 v6sum(V6 v1, V6 v2)
    V6 v6unit(V6 v)
    char *m3fmt(M3 m)
    char *m6fmt(M6 m)
    char *v3fmt(V3 v)
    char *v6fmt(V6 v)
    double v3alpha(V3 v)
    double v3delta(V3 v)
    double v3dot(V3 v1, V3 v2)
    double v3mod(V3 v)
    double v6alpha(V6 v)
    double v6delta(V6 v)
    double v6dot(V6 v1, V6 v2)
    double v6mod(V6 v)

cdef extern from "tpm/times.h":
    ##############################
    ##### times.h #####
    ##############################

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

cdef extern from "tpm/tpm.h":
    ##############################
    ##### tpm.h #####
    ##############################

    # State names
    int TPM_S00
    int TPM_S01
    int TPM_S02
    int TPM_S03
    int TPM_S04
    int TPM_S05
    int TPM_S06
    int TPM_S07
    int TPM_S08
    int TPM_S09
    int TPM_S10
    int TPM_S11
    int TPM_S12
    int TPM_S13
    int TPM_S14
    int TPM_S15
    int TPM_S16
    int TPM_S17
    int TPM_S18
    int TPM_S19
    int TPM_S20
    int TPM_S21
    int N_TPM_STATES
    
    int TPM_T00 
    int TPM_T01
    int TPM_T02
    int TPM_T03
    int TPM_T04
    int TPM_T05
    int TPM_T06
    int TPM_T07
    int TPM_T08
    int TPM_T09
    int TPM_T10
    int TPM_T11
    int TPM_T12
    int TPM_T13
    int TPM_T14
    int TPM_T15
    int N_TPM_TRANS

    struct s_target:
        char *name # char name[BUFSIZ]
        int state
        double epoch
        double equinox
        double position[2]
        double offset[2]
        double motion[2]
        double parallax
        double speed

    ctypedef s_target TPM_TARGET

    int TARGET_FK4
    int TARGET_FK5 
    int TARGET_ECL
    int TARGET_GAL 
    int TARGET_APP_HADEC 
    int TARGET_OBS_HADEC 
    int TARGET_APP_AZEL
    int TARGET_OBS_AZEL
    int TARGET_OBS_WHAM
    int TARGET_HADEC
    int TARGET_TOP_AZEL

    struct s_boresight:
        double epoch
        double position[2]
        double offset[2]
        double motion[2]

    ctypedef s_boresight TPM_BORESIGHT

    struct s_tstate:
        double utc
        double delta_at
        double delta_ut
        double lon
        double lat
        double alt
        double xpole
        double ypole
        double T
        double P
        double H
        double wavelength
        
        double tai
        double tdt
        double tdb

        double obliquity
        double nut_lon
        double nut_obl
        s_m3 nm
        s_m6 pm

        double ut1
        double gmst
        double gast
        double last

        s_v6 eb
        s_v6 eh
        s_v6 obs_m
        s_v6 obs_t
        s_v6 obs_s
        
        double refa
        double refb
        
    ctypedef s_tstate TPM_TSTATE

    int TPM_INIT
    int TPM_FAST
    int TPM_MEDIUM
    int TPM_SLOW
    int TPM_REFRACTION
    int TPM_ALL

    struct s_pmcell:
        int ptrans
        int pstate

    ctypedef s_pmcell TPM_PMCELL

cdef extern from "tpm/astro.h":
    ##############################
    ##### astro.h #####
    ##############################

    double IAU_K
    double IAU_DM
    double IAU_AU
    double IAU_C
    double IAU_RE
    double IAU_RM
    double IAU_F
    double IAU_KAPPA
    double IAU_W
    double GAL_RA
    double GAL_DEC
    double GAL_LON
    int PRECESS_NEWCOMB
    int PRECESS_ANDOYER
    int PRECESS_KINOSHITA
    int PRECESS_LIESKE
    int PRECESS_FK4
    int PRECESS_FK5
    int PRECESS_INERTIAL
    int PRECESS_ROTATING
    
    struct s_star:
        double a
        double d
        double m

    ctypedef s_star STAR

    struct s_cons:
        double a1
        double d1
        double a2
        double d2

    ctypedef s_cons CONS

    # macros
    V6 cat2v6(double r, double d, double rd, double dd, double px, double rv, double C)
    void v62cat(double *r, double *d, double *rd, double *dd, double *px, double *rv, V6 v6, double C)
    
    double et2tdt(double et)
    double tai2tdt(double tai)
    double tdt2et(double tdt)
    double ut12et(double ut1)
    double utc2et(double utc)
    double utc2tai(double utc)
    double utc2tdt(double utc)
    double utc2ut1(double utc)
    
    double et2ut1(double et)  
    double et2utc(double et)  
    double tai2utc(double tai)
    double tdt2tai(double tdt)
    double tdt2utc(double tdt)
    double ut12utc(double ut1)

    double et2tai(double et)  
    double et2tdb(double et)  
    double tai2et(double tai) 
    double tai2tdb(double tai)
    double tai2ut1(double tai)
    #double tdb2et(double tdb) 
    #double tdb2tai(double tdb)
    #double tdb2ut1(double tdb)
    #double tdb2utc(double tdb)
    double tdt2ut1(double tdt)
    double ut12tai(double ut1)
    double ut12tdb(double ut1)
    double ut12tdt(double ut1)
    double utc2tdb(double utc)

    double et2ut(double ut) 
    double ut2et(double ut) 
    double ut2gmst(double ut)

    #Functions
    M6 precess_m(double j1, double j2, int pflag, int sflag)
    V6 aberrate(V6 p, V6 e, int flag)
    V6 azel2hadec(V6 v6, double latitude)
#    V6 barvel(double tdb)
    V6 cat2v6r1(double r, double d, double rd, double dd, double px, double rv, double C)
    V6 cat2v6r2(double r, double d, double rd, double dd, double px, double rv, double C)
    V6 cat2v6u1(double r, double d, double rd, double dd, double px, double rv, double C)
    V6 cat2v6u2(double r, double d, double rd, double dd, double px, double rv, double C)
    V6 ecl2equ(V6 v6, double obl)
    V6 ellab(double tdt, V6 star, int flag)
    V6 equ2ecl(V6 v6, double obl)
    V6 equ2gal(V6 v6)
    V6 eterms(double ep)
    V6 fk425(V6 v)
    V6 fk524(V6 v)
    V6 gal2equ(V6 v6)
    V6 geod2geoc(double lon, double lat, double alt)
    V6 hadec2azel(V6 v6, double latitude)
    V6 ldeflect(V6 s, V6 e, int flag)
    V6 precess(double j1, double j2, V6 v6, int pflag)
    V6 proper_motion(V6 v6, double t, double t0)
    char *tpm_state(int state)
    double delta_AT(double utc)
    double delta_ET(double utc)
    double delta_T(double ut1)
    double delta_TT(double utc)
    double delta_UT(double utc)
    double eccentricity(double tdt)
    double eccentricity_dot(double tdt)
    double obliquity(double tdt)
    double obliquity_dot(double tdt)    
    double refract(double zx, double refa, double refb, int flag)
    double refraction(double zobs, double lat, double alt, double T, double P, double rh, double wavelength, double eps)
    double solar_perigee(double tdt)
    double solar_perigee_dot(double tdt)
    double tdt2tdb(double tdt)
    double theta(double j1, double j2, int pflag)
    double thetadot(double j1, double j2, int pflag)
    double ut12gmst(double ut1)
    double zee(double j1, double j2, int pflag)
    double zeedot(double j1, double j2, int pflag)
    double zeta(double j1, double j2, int pflag)
    double zetadot(double j1, double j2, int pflag)
    int tpm(V6 *pvec, int s1, int s2, double ep, double eq, TPM_TSTATE *tstate)
    void atm(double r, double *n, double *dndr)
    void evp(double tdb, V6 *v6b, V6 *v6h)
    void nutations(double tdt, double *delta_phi, double *delta_eps)
    void refco(double lat, double alt, double T, double P, double rh, double wavelength, double eps, double *refa, double *refb)
    void tpm_data(TPM_TSTATE *p, int flags)
    void v6r2cat(double *r, double *d, double *rd, double *dd, double *px, double *rv, V6 v6, double C)
    void v6u2cat(double *r, double *d, double *rd, double *dd, double *px, double *rv, V6 v6, double C)

cdef extern from "tpm/misc.h":
    ##############################
    ##### misc.h #####
    ##############################

    int REAL
    int IMAG

    double trapzd(double (*func)(double), double a, double b, int n)
    double polint(double *xa, double *ya, int n, double x, double *dy)
    double qromb(double (*func)(double), double a, double b, double eps, int imax)