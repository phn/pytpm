/* file: $RCSfile: proper_motion.c,v $
** rcsid: $Id: proper_motion.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: proper_motion.c,v $
** apply proper motion to a state vector
** *******************************************************************
*/

#include "astro.h"

V6
proper_motion(V6 v6, double t, double t0)
{
    double dt = (t - t0);
    /**********************************/
    /* add in the position derivative */
    /**********************************/

    if (v6GetType(v6) == SPHERICAL) {
	v6IncR(v6, v6GetRDot(v6) * dt);
	v6IncAlpha(v6, v6GetAlphaDot(v6) * dt);
	v6IncDelta(v6, v6GetDeltaDot(v6) * dt);
    } else {
	v6IncX(v6, v6GetXDot(v6) * dt);
	v6IncY(v6, v6GetYDot(v6) * dt);
	v6IncZ(v6, v6GetZDot(v6) * dt);
    }

    return(v6);
}
