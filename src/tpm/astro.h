/* file: $RCSfile: astro.h,v $
** rcsid: $Id: astro.h 261 2007-10-19 19:07:02Z laidler $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/

/*
** *******************************************************************
** $RCSfile: astro.h,v $ - header file for general astronomy routines
** *******************************************************************
*/

#ifndef ASTRO_INCLUDE
#define ASTRO_INCLUDE

#include "misc.h"
#include "vec.h"
#include "times.h"

#include "tpm.h"

/*
**********************************************************************
** IAU (1976) System of Astronomical Constants
** from the Astronomical Almanac, 1984 p. K6 (SI units, MKS)
**********************************************************************
*/

/* Gaussian gravitational constant */
#define IAU_K	(0.01720209895)

/* distance of moon */
#define IAU_DM	(384400.0e3)

/* astronomical unit */
#define IAU_AU	(1.49597870e11)

/* speed of light */
#define IAU_C	(299792458.0)

/* radius of earth */
#define IAU_RE	(6378137.0)

/* radius of moon */
#define IAU_RM	(1738000.0)

/* flattening factor of earth */
#define IAU_F	(0.00335281)

/* constant of aberration */
#define IAU_KAPPA	(20.49552)

/* rotational velocity of the earth in radians/s */
#define IAU_W	(7.2921151467e-5)

/*
**********************************************************************
** end of IAU (1976) System of Astronomical Constants
** from the Astronomical Almanac, 1984 p. K6 (SI units, MKS)
**********************************************************************
*/

/* the equatorial location of the galactic pole in degrees */
#define GAL_RA	(192.25)
#define GAL_DEC	(27.4)
#define GAL_LON	(33.0)

/*
** definitions for FK4 and FK5 precession angles
** see Aoki et al., 1983, Astronomy and Astrophysics, 128, 263.
** the first four are FK4 angles (when in doubt, use PRECESS_KINOSHITA).
** the final one is the One True FK5 set of angles.
*/
#define PRECESS_NEWCOMB		(0)	/* aoki eqs 9a-c, ES 1961 */
#define PRECESS_ANDOYER		(1)	/* aoki eqs 8a-c, Andoyer 1911 */
#define PRECESS_KINOSHITA	(2)	/* aoki eqs 10a-c, Kinoshita 1975 */
#define PRECESS_LIESKE		(3)	/* aoki eqs 11a-c, Lieske 1967 */
#define PRECESS_FK4		(PRECESS_KINOSHITA)
#define PRECESS_FK5		(4)	/* ES 1992, Lieske 1979, 1977 */
/*
** flags to indicate whether the precession frames
** are inertial or not. See ES (1992), p. 182-183.
*/
#define PRECESS_INERTIAL	(0)
#define PRECESS_ROTATING	(1)

/* this structure defines a star datum */
typedef struct s_star {
	double a;	/* right ascension */
	double d;	/* declination */
	double m;	/* magnitude */
} STAR;

/* this structure defines a line segment between two stars */
typedef struct s_cons {
	double a1;	/* right ascension */
	double d1;	/* declination */
	double a2;	/* right ascension */
	double d2;	/* declination */
} CONS;

/* some simple transformations implemented as macros */

#define cat2v6(a,b,c,d,e,f,g)	cat2v6r2(a,b,c,d,e,f,g)
#define v62cat(a,b,c,d,e,f,g,h)	v6r2cat(a,b,c,d,e,f,g,h)

/* definitive time transformations */
#define et2tdt(et)	(et)
#define tai2tdt(tai)	((tai)+(32.184/86400))
#define tdt2et(tdt)	(tdt)
#define ut12et(ut1)	((ut1)+(delta_T(ut1)/86400))
#define utc2et(utc)	((utc)+(delta_ET(utc)/86400))
#define utc2tai(utc)	((utc)+(delta_AT(utc)/86400))
#define utc2tdt(utc)	((utc)+(delta_TT(utc)/86400))
#define utc2ut1(utc)	((utc)+(delta_UT(utc)/86400))

/* approximate time transformations */
#define et2ut1(et)	((et)-(delta_T(et)/86400))
#define et2utc(et)	((et)-(delta_ET(et)/86400))
#define tai2utc(tai)	((tai)-(delta_AT(tai)/86400))
#define tdt2tai(tdt)	((tdt)-(32.184/86400))
#define tdt2utc(tdt)	((tdt)-(delta_TT(tdt)/86400))
#define ut12utc(ut1)	((ut1)-(delta_UT(ut1)/86400))

/* derived time transformations */
#define et2tai(et)	(tdt2tai(et2tdt(et)))
#define et2tdb(et)	(tdt2tdb(et2tdt(et)))
#define tai2et(tai)	(tdt2et(tai2tdt(tai)))
#define tai2tdb(tai)	(tdt2tdb(tai2tdt(tai)))
#define tai2ut1(tai)	(et2ut1(tdt2et((tai2tdt(tai)))))
#define tdb2et(tdb)	(tdt2et(tdb2tdt(tdb)))
#define tdb2tai(tdb)	(tdt2tai(tdb2tdt(tdb)))
#define tdb2ut1(tdb)	(et2ut1(tdt2et(tdb2tdt(tdb))))
#define tdb2utc(tdb)	(tai2utc(tdt2tai(tdb2tdt(tdb))))
#define tdt2ut1(tdt)	(et2ut1(tdt2et(tdt)))
#define ut12tai(ut1)	(tdt2tai(et2tdt(ut12et(ut1))))
#define ut12tdb(ut1)	(tdt2tdb(et2tdt(ut12et(ut1))))
#define ut12tdt(ut1)	(et2tdt(ut12et(ut1)))
#define utc2tdb(utc)	(tdt2tdb(tai2tdt(utc2tai(utc))))

/* convenience time transformations */
#define et2ut(et)	(et2ut1(et))
#define ut2et(ut)	(ut12et(ut))
#define ut2gmst(ut)	(ut12gmst(ut))

/* EXTERN_START */
/*extern M3 eplane(V6 v1, V6 v2);
  extern M3 fplane(V6 v);
extern M3 nutate_m(double tdt);*/
extern M6 precess_m(double j1, double j2, int pflag, int sflag);
extern V6 aberrate(V6 p, V6 e, int flag);
/*extern V6 altaz(V6 object, V6 zenith);*/
extern V6 azel2hadec(V6 v6, double latitude);
/*extern V6 barvel(double tdb);*/
extern V6 cat2v6r1(double r, double d, double rd, double dd, double px, double rv, double C);
extern V6 cat2v6r2(double r, double d, double rd, double dd, double px, double rv, double C);
extern V6 cat2v6u1(double r, double d, double rd, double dd, double px, double rv, double C);
extern V6 cat2v6u2(double r, double d, double rd, double dd, double px, double rv, double C);
/*extern V6 com2cof(double et, V6 moon);*/
extern V6 ecl2equ(V6 v6, double obl);
extern V6 ellab(double tdt, V6 star, int flag);
extern V6 equ2ecl(V6 v6, double obl);
extern V6 equ2gal(V6 v6);
extern V6 eterms(double ep);
extern V6 fk425(V6 v);
extern V6 fk524(V6 v);
extern V6 gal2equ(V6 v6);
extern V6 geod2geoc(double lon, double lat, double alt);
/*extern V6 geoid(V6 position, V6 direction, double h0);*/
extern V6 hadec2azel(V6 v6, double latitude);
/*extern V6 hadec2radec(V6 v6, double last);
  extern V6 helvel(double tdb);*/
extern V6 ldeflect(V6 s, V6 e, int flag);
/*extern V6 lonlat(double ut1, V6 v);
  extern V6 nutate(double j, V6 v6, int dir);
  extern V6 observer(double tdb, double lon, double lat, double h);*/
extern V6 precess(double j1, double j2, V6 v6, int pflag);
extern V6 proper_motion(V6 v6, double t, double t0);
/*extern V6 radec2hadec(V6 v6, double last);
  extern V6 v2r(double v, double n, double a, double e);*/
extern char *tpm_state(int state);
/*extern double E2v(double E, double e);
  extern double M2E(double M, double e);
extern double ae2ha(double az, double el, double lat);
extern double ae2pa(double az, double el, double lat);*/
extern double delta_AT(double utc);
extern double delta_ET(double utc);
extern double delta_T(double ut1);
extern double delta_TT(double utc);
extern double delta_UT(double utc);
extern double eccentricity(double tdt);
extern double eccentricity_dot(double tdt);
/*extern double eq_equinox(double tdt);
  extern double eq_time(double tdt);*/
extern double func(double z);
/*extern double nut_longitude(double tdt);
  extern double nut_obliquity(double tdt);
  extern double obj2lha(V6 object, V6 obs);*/
extern double obliquity(double tdt);
extern double obliquity_dot(double tdt);
extern double refract(double zx, double refa, double refb, int flag);
extern double refraction(double zobs, double lat, double alt, double T, double P, double rh, double lambda, double eps);
/*extern double shadow_altitude(V3 E, V3 G, V3 T, double height);
  extern double shadow_distance(V3 E, V3 G, V3 T, double height);*/
extern double solar_perigee(double tdt);
extern double solar_perigee_dot(double tdt);
/*extern double tdb2tdt(double tdb);*/
extern double tdt2tdb(double tdt);
extern double theta(double j1, double j2, int pflag);
extern double thetadot(double j1, double j2, int pflag);
extern double ut12gmst(double ut1);
/*extern double zd2airmass(double zd);*/
extern double zee(double j1, double j2, int pflag);
extern double zeedot(double j1, double j2, int pflag);
extern double zeta(double j1, double j2, int pflag);
extern double zetadot(double j1, double j2, int pflag);
/*extern int n_cons_data(void);
  extern int n_star_data(void);*/
extern int tpm(V6 *pvec, int s1, int s2, double ep, double eq, TPM_TSTATE *tstate);
extern void atm(double r, double *n, double *dndr);
/*extern void draw_saturn(V3 z);*/
extern void evp(double tdb, V6 *v6b, V6 *v6h);
/*extern void geoc2geod(double *lon, double *lat, double *h, V6 g);*/
extern void nutations(double tdt, double *delta_phi, double *delta_eps);
extern void refco(double lat, double alt, double T, double P, double rh, double lambda, double eps, double *refa, double *refb);
extern void tpm_data(TPM_TSTATE *p, int flags);
/*extern void tpm_status(FILE *fp, TPM_TSTATE *p);*/
extern void v6r2cat(double *r, double *d, double *rd, double *dd, double *px, double *rv, V6 v6, double C);
extern void v6u2cat(double *r, double *d, double *rd, double *dd, double *px, double *rv, V6 v6, double C);
/* EXTERN_STOP */

#endif
