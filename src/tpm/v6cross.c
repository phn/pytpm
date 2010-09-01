/* file: $RCSfile: v6cross.c,v $
** rcsid: $Id: v6cross.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6cross.c,v $ - 6-vector cross product
** *******************************************************************
*/

#include "vec.h"

V6
v6cross(V6 v1, V6 v2)
{
    V6 v;

    if (v6GetType(v1) == SPHERICAL) {
	v1 = v6s2c(v1);
    }

    if (v6GetType(v2) == SPHERICAL) {
	v2 = v6s2c(v2);
    }

    v = v6init(CARTESIAN);

    v6SetX(v, v6GetY(v1) * v6GetZ(v2) - v6GetZ(v1) * v6GetY(v2));
    v6SetY(v, v6GetZ(v1) * v6GetX(v2) - v6GetX(v1) * v6GetZ(v2));
    v6SetZ(v, v6GetX(v1) * v6GetY(v2) - v6GetY(v1) * v6GetX(v2));

    return(v);
}
