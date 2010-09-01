/* file: $RCSfile: m6v6.c,v $
** rcsid: $Id: m6v6.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: m6v6.c,v $ - product of a 6-matrix and a 6-vector
** *******************************************************************
*/

#include "vec.h"

V6
m6v6(M6 m, V6 v1)
{
    V6 v2;

    if (v6GetType(v1) == SPHERICAL) {
	v1 = v6s2c(v1);
    }

    v2 = v6init(CARTESIAN);

    v2.v[0] = v3sum(m3v3(m.m[0][0], v1.v[0]), m3v3(m.m[0][1], v1.v[1]));
    v2.v[1] = v3sum(m3v3(m.m[1][0], v1.v[0]), m3v3(m.m[1][1], v1.v[1]));

    return(v2);
}
