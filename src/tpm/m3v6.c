/* file: $RCSfile: m3v6.c,v $
** rcsid: $Id: m3v6.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3v6.c,v $ - product of a 3-matrix and a 6-vector.
** we define this operation to be multiplying both position and velocity
** components of the 6-vector by the matrix.
** *******************************************************************
*/

#include "vec.h"

V6
m3v6(M3 m, V6 v1)
{
    int row, col;
    V6 v2;

    if (v6GetType(v1) == SPHERICAL) {
	v1 = v6s2c(v1);
    }

    v2 = v6init(CARTESIAN);

    for (row = 0; row < 3; row++) {
	for (col = 0; col < 3; col++) {
	    v2.v[POS].v[row] += m.m[row][col] * v1.v[POS].v[col];
	    v2.v[VEL].v[row] += m.m[row][col] * v1.v[VEL].v[col];
	}
    }

    return(v2);
}
