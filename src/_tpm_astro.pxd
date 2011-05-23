# -*- coding: utf-8 -*-

# Repeating tpm/vec.h definitions here; otherwise Cython says that V6
# etc are not declared.
cdef extern from "tpm/vec.h":
    # vec.h #includes v3, v6, m3 and m6.
    # From v3.h.
    struct s_v3:
        int type
        double v[3]

    ctypedef s_v3 V3

    # From v6.h.
    struct s_v6:
        V3 v[2]

    ctypedef s_v6 V6

    int POS
    int VEL

    # From m3.h.
    struct s_m3:
        double m[3][3]

    ctypedef s_m3 M3

    # From m6.h
    struct s_m6:
        M3 m[2][2]

    ctypedef s_m6 M6

cdef extern from "tpm/tpm.h":
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

cdef extern from "tpm/astro.h":
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


    
