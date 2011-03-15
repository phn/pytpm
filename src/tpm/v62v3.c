/* file: $RCSfile: v62v3.c,v $
** rcsid: $Id: v62v3.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v62v3.c,v $ - downgrade a 6-vector to a 3-vector by adding space motion
** *******************************************************************
*/

#include "vec.h"

V3
v62v3(V6 v6, double dt)
{
    V3 v3;

    if (v6GetType(v6) == SPHERICAL) {
	v6 = v6s2c(v6);
    }

    v3 = v3init(CARTESIAN);
    v3SetX(v3, v6GetX(v6) + v6GetXDot(v6) * dt);
    v3SetY(v3, v6GetY(v6) + v6GetYDot(v6) * dt);
    v3SetZ(v3, v6GetZ(v6) + v6GetZDot(v6) * dt);

    return(v3);
}
