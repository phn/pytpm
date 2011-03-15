/* file: $RCSfile: v3dot.c,v $
** rcsid: $Id: v3dot.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v3dot.c,v $ - 3-vector dot product
** *******************************************************************
*/

#include "vec.h"

double
v3dot(V3 v1, V3 v2)
{
    double x = 0;

    if (v3GetType(v1) == SPHERICAL) {
	v1 = v3s2c(v1);
    }

    if (v3GetType(v2) == SPHERICAL) {
	v2 = v3s2c(v2);
    }

    x += v3GetX(v1) * v3GetX(v2);
    x += v3GetY(v1) * v3GetY(v2);
    x += v3GetZ(v1) * v3GetZ(v2);

    return(x);
}
