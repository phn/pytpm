/* file: $RCSfile: v6s2c.c,v $
** rcsid: $Id: v6s2c.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6s2c.c,v $ - 6-vector spherical to cartesian
** *******************************************************************
*/

#include "vec.h"

/* some convenience macros */
#define X	(v6GetX(vc))
#define Y	(v6GetY(vc))
#define Z	(v6GetZ(vc))
#define XDOT	(v6GetXDot(vc))
#define YDOT	(v6GetYDot(vc))
#define ZDOT	(v6GetZDot(vc))
#define R	(v6GetR(vs))
#define A	(v6GetAlpha(vs))
#define D	(v6GetDelta(vs))
#define RDOT	(v6GetRDot(vs))
#define ADOT	(v6GetAlphaDot(vs))
#define DDOT	(v6GetDeltaDot(vs))

V6
v6s2c(V6 vs)
{
    double cos_a;
    double cos_d;
    double sin_a;
    double sin_d;
    V6 vc;

    if (v6GetType(vs) == CARTESIAN) {
	return(vs);
    }

    vc = v6init(CARTESIAN);

    cos_a = cos(A);
    cos_d = cos(D);
    sin_a = sin(A);
    sin_d = sin(D);

    /* the standard transformation */
    v6SetX(vc, R*cos_d*cos_a);
    v6SetY(vc, R*cos_d*sin_a);
    v6SetZ(vc, R*sin_d);

    /* the first derivative of the standard transformation */
    v6SetXDot(vc, -R*(cos_d*sin_a*ADOT + sin_d*cos_a*DDOT) + RDOT*cos_d*cos_a);
    v6SetYDot(vc,  R*(cos_d*cos_a*ADOT - sin_d*sin_a*DDOT) + RDOT*cos_d*sin_a);
    v6SetZDot(vc,  R*cos_d*DDOT + RDOT*sin_d);

    return(vc);
}
