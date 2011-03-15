/* file: $RCSfile: v6mod.c,v $
** rcsid: $Id: v6mod.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6mod.c,v $ - 6-vector modulus
** *******************************************************************
*/

#include "vec.h"

double
v6mod(V6 v)
{
    double x = 0.0;

    if (v6GetType(v) == SPHERICAL) {
	x = fabs(v6GetR(v));
    } else {
	x += v6GetX(v) * v6GetX(v);
	x += v6GetY(v) * v6GetY(v);
	x += v6GetZ(v) * v6GetZ(v);
	x = sqrt(x);
    }

    return(x);
}
