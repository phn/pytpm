/* file: $RCSfile: v3c2s.c,v $
** rcsid: $Id: v3c2s.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v3c2s.c,v $ - 3-vector cartesian to spherical
** *******************************************************************
*/

#include "vec.h"

/* some convenience macros */
#define R	(v3GetR(vs))
#define A	(v3GetAlpha(vs))
#define D	(v3GetDelta(vs))

V3
v3c2s(V3 vc)
{
    V3 vs;
    double x = v3GetX(vc);
    double y = v3GetY(vc);
    double z = v3GetZ(vc);

    if (v3GetType(vc) == SPHERICAL) {
	return(vc);
    }

    vs = v3init(SPHERICAL);

    v3SetR(vs, v3mod(vc));

    if (R == 0.0) {
	return(vs);
    }

    if (x == 0.0) {
	if (y < 0.0) {
	    v3SetAlpha(vs, -M_PI/2);
	} else if (y > 0.0) {
	    v3SetAlpha(vs, M_PI/2);
	}
    } else {
	v3SetAlpha(vs, atan2(y, x));
    }

    v3SetDelta(vs, atan2(z, sqrt(x*x + y*y)));

    return(vs);
}
