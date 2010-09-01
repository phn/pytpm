/* file: $RCSfile: aberrate.c,v $
** rcsid: $Id: aberrate.c 261 2007-10-19 19:07:02Z laidler $
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
** $RCSfile: aberrate.c,v $
** apply aberration of light to a state vector.
** *******************************************************************
*/

#include "astro.h"

V6
aberrate(V6 p, V6 e, int flag)
{
    double tau;

    tau = v6mod(p) / (IAU_C*(86400/IAU_AU)); 

    /* ensure cartesian vectors */
    p = v6s2c(p);
    e = v6s2c(e);

    if (flag > 0) {
	v6IncX(p, v6GetXDot(e) * tau);
	v6IncY(p, v6GetYDot(e) * tau);
	v6IncZ(p, v6GetZDot(e) * tau);
    } else {
	v6DecX(p, v6GetXDot(e) * tau);
	v6DecY(p, v6GetYDot(e) * tau);
	v6DecZ(p, v6GetZDot(e) * tau);
    }

    return(p);
}
