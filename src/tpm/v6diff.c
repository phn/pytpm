/* file: $RCSfile: v6diff.c,v $
** rcsid: $Id: v6diff.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6diff.c,v $ - 6-vector difference
** *******************************************************************
*/

#include "vec.h"

V6
v6diff(V6 v1, V6 v2)
{
    if (v6GetType(v1) == SPHERICAL) {
	v1 = v6s2c(v1);
    }

    if (v6GetType(v2) == SPHERICAL) {
	v2 = v6s2c(v2);
    }

    v6DecX(v1, v6GetX(v2));
    v6DecY(v1, v6GetY(v2));
    v6DecZ(v1, v6GetZ(v2));
    v6DecXDot(v1, v6GetXDot(v2));
    v6DecYDot(v1, v6GetYDot(v2));
    v6DecZDot(v1, v6GetZDot(v2));

    return(v1);
}
