/* file: $RCSfile: v3init.c,v $
** rcsid: $Id: v3init.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v3init.c,v $ - 3-vector initialization
** *******************************************************************
*/

#include "vec.h"

V3
v3init(int type)
{
    V3 v;

    if (type == SPHERICAL) {
	v3SetType(v, SPHERICAL);
	v3SetR(v, 0.0);
	v3SetAlpha(v, 0.0);
	v3SetDelta(v, 0.0);
    } else {
	v3SetType(v, CARTESIAN);
	v3SetX(v, 0.0);
	v3SetY(v, 0.0);
	v3SetZ(v, 0.0);
    }

    return(v);
}
