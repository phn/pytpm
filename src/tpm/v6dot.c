/* file: $RCSfile: v6dot.c,v $
** rcsid: $Id: v6dot.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6dot.c,v $ - 6-vector dot product
** *******************************************************************
*/

#include "vec.h"

double
v6dot(V6 v1, V6 v2)
{
    double x = 0;

    if (v6GetType(v1) == SPHERICAL) {
	v1 = v6s2c(v1);
    }

    if (v6GetType(v2) == SPHERICAL) {
	v2 = v6s2c(v2);
    }

    x += v6GetX(v1) * v6GetX(v2);
    x += v6GetY(v1) * v6GetY(v2);
    x += v6GetZ(v1) * v6GetZ(v2);

    return(x);
}
