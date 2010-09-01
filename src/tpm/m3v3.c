/* file: $RCSfile: m3v3.c,v $
** rcsid: $Id: m3v3.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m3v3.c,v $ - product of a 3-matrix and a 3-vector
** *******************************************************************
*/

#include "vec.h"

V3
m3v3(M3 m, V3 v1)
{
    int row, col;
    V3 v2;

    if (v3GetType(v1) == SPHERICAL) {
	v1 = v3s2c(v1);
    }

    v2 = v3init(CARTESIAN);

    for (row = 0; row < 3; row++) {
	for (col = 0; col < 3; col++) {
	    v2.v[row] += m.m[row][col] * v1.v[col];
	}
    }

    return(v2);
}
