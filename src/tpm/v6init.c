/* file: $RCSfile: v6init.c,v $
** rcsid: $Id: v6init.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: v6init.c,v $ - 6-vector initialization
** *******************************************************************
*/

#include "vec.h"

V6
v6init(int type)
{
    V6 v;

    if (type == SPHERICAL) {
	v6SetType(v, POLAR);
	v6SetR(v, 0.0);
	v6SetAlpha(v, 0.0);
	v6SetDelta(v, 0.0);
	v6SetRDot(v, 0.0);
	v6SetAlphaDot(v, 0.0);
	v6SetDeltaDot(v, 0.0);
    } else {
	v6SetType(v, CARTESIAN);
	v6SetX(v, 0.0);
	v6SetY(v, 0.0);
	v6SetZ(v, 0.0);
	v6SetXDot(v, 0.0);
	v6SetYDot(v, 0.0);
	v6SetZDot(v, 0.0);
    }

    return(v);
}
