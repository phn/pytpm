/* file: $RCSfile: v3s2c.c,v $
** rcsid: $Id: v3s2c.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v3s2c.c,v $ - 3-vector spherical to cartesian
** *******************************************************************
*/

#include "vec.h"

/* some convenience macros */
#define X	(v3GetX(vc))
#define Y	(v3GetY(vc))
#define Z	(v3GetZ(vc))
#define R	(v3GetR(vs))
#define A	(v3GetAlpha(vs))
#define D	(v3GetDelta(vs))

V3
v3s2c(V3 vs)
{
    double rcosd;
    V3 vc;

    if (v3GetType(vs) == CARTESIAN) {
	return(vs);
    }

    vc = v3init(CARTESIAN);

    rcosd = R*cos(D);

    v3SetX(vc, rcosd*cos(A));
    v3SetY(vc, rcosd*sin(A));
    v3SetZ(vc, R*sin(D));

    return(vc);
}
