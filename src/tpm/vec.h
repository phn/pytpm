/* file: $RCSfile: vec.h,v $
** rcsid: $Id: vec.h 261 2007-10-19 19:07:02Z laidler $
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
**********************************************************************
** $RCSfile: vec.h,v $ -
**********************************************************************
*/

#ifndef VEC_H
#define VEC_H

#include <math.h>
#ifndef M_PI
#define M_PI (3.14159265358979323846)
#endif

#define CARTESIAN	(0)
#define SPHERICAL	(1)
#define POLAR		(SPHERICAL)

/* define some short-cut macros */

/* these are repeated in times.h */
#ifndef TIMES_H
#define d2h(d)			((d)/15.0)
#define h2d(h)			((h)*15.0)
#define d2r(d)			((d)*(M_PI/180.0))
#define r2d(r)			((r)*(180.0/M_PI))
#define h2r(h)			((h)*(M_PI/12.0))
#define r2h(r)			((r)*(12.0/M_PI))
#define d2as(d)			((d)*3600.0)
#define as2d(x)			((x)/3600.0)
#define as2h(x)			(d2h(as2d(x)))
#define h2as(h)			(d2as(h2d(h)))
#define r2as(r)			(d2as(r2d(r)))
#define as2r(x)			(d2r(as2d(x)))
#endif

/* define 3-vectors */
#include "v3.h"

/* define 6-vectors */
#include "v6.h"

/* define 3-matrices */
#include "m3.h"

/* define 6-matrices */
#include "m6.h"

/* EXTERN_START */
extern M3 m3I(double x);
extern M3 m3O(void);
extern M3 m3Rx(double x);
extern M3 m3RxDot(double x, double xdot);
extern M3 m3Ry(double y);
extern M3 m3RyDot(double y, double ydot);
extern M3 m3Rz(double z);
extern M3 m3RzDot(double z, double zdot);
extern M3 m3diff(M3 m1, M3 m2);
extern M3 m3inv(M3 m);
extern M3 m3m3(M3 m1, M3 m2);
extern M3 m3scale(M3 m, double s);
extern M3 m3sum(M3 m1, M3 m2);
extern M6 m6I(double x);
extern M6 m6O(void);
extern M6 m6Qx(double x, double xdot);
extern M6 m6Qy(double y, double ydot);
extern M6 m6Qz(double z, double zdot);
extern M6 m6diff(M6 m1, M6 m2);
extern M6 m6inv(M6 m);
extern M6 m6m6(M6 m1, M6 m2);
extern M6 m6scale(M6 m, double s);
extern M6 m6sum(M6 m1, M6 m2);
extern V3 m3v3(M3 m, V3 v1);
extern V3 m6v3(M6 m, V3 v);
extern V3 v3c2s(V3 vc);
extern V3 v3cross(V3 v1, V3 v2);
extern V3 v3diff(V3 v1, V3 v2);
extern V3 v3init(int type);
extern V3 v3s2c(V3 vs);
extern V3 v3scale(V3 v, double s);
extern V3 v3sum(V3 v1, V3 v2);
extern V3 v3unit(V3 v);
extern V3 v62v3(V6 v6, double dt);
extern V6 m3v6(M3 m, V6 v1);
extern V6 m6v6(M6 m, V6 v1);
extern V6 v32v6(V3 v3);
extern V6 v6c2s(V6 vc);
extern V6 v6cross(V6 v1, V6 v2);
extern V6 v6diff(V6 v1, V6 v2);
extern V6 v6init(int type);
extern V6 v6s2c(V6 vs);
extern V6 v6scale(V6 v, double s);
extern V6 v6sum(V6 v1, V6 v2);
extern V6 v6unit(V6 v);
extern char *m3fmt(M3 m);
extern char *m6fmt(M6 m);
extern char *v3fmt(V3 v);
extern char *v6fmt(V6 v);
extern double v3alpha(V3 v);
extern double v3delta(V3 v);
extern double v3dot(V3 v1, V3 v2);
extern double v3mod(V3 v);
extern double v6alpha(V6 v);
extern double v6delta(V6 v);
extern double v6dot(V6 v1, V6 v2);
extern double v6mod(V6 v);
/* EXTERN_STOP */

#endif
