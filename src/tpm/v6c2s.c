/* file: $RCSfile: v6c2s.c,v $
** rcsid: $Id: v6c2s.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6c2s.c,v $ - 6-vector cartesian to spherical
** *******************************************************************
*/

#include "vec.h"

/* some convenience macros */
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
v6c2s(V6 vc)
{
    V6 vs;
    double r_cos_d;
    double sin_d;
    double x = v6GetX(vc);
    double y = v6GetY(vc);
    double z = v6GetZ(vc);

    if (v6GetType(vc) == SPHERICAL) {
	return(vc);
    }

    vs = v6init(SPHERICAL);

    v6SetR(vs, v6mod(vc));

    if (R == 0.0) {
	v6SetRDot(vs, XDOT);
	return(vs);
    }

    if (x == 0.0) {
	if (y < 0.0) {
	    v6SetAlpha(vs, -M_PI/2);
	} else if (y > 0.0) {
	    v6SetAlpha(vs, M_PI/2);
	}
    } else {
	v6SetAlpha(vs, atan2(y, x));
    }

    v6SetDelta(vs, atan2(z, sqrt(x*x + y*y)));

    sin_d = sin(D);

    if (cos(D) == 0.0) {
	v6SetRDot(vs, ZDOT / sin_d);
	if (cos(A) == 0.0) {
	    v6SetDeltaDot(vs, -YDOT/(R*sin_d*sin(A)));
	} else {
	    v6SetDeltaDot(vs, -XDOT/(R*sin_d*cos(A)));
	}
	return(vs);
    }

    r_cos_d = R*cos(D);

    v6SetRDot(vs, (x*XDOT + y*YDOT + z*ZDOT) / R);

    v6SetAlphaDot(vs, (x*YDOT - y*XDOT) / (r_cos_d*r_cos_d));

    v6SetDeltaDot(vs, ((ZDOT - RDOT*sin_d) / r_cos_d));

    return(vs);
}
