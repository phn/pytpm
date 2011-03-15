/* file: $RCSfile: cat2v6u2.c,v $
** rcsid: $Id: cat2v6u2.c,v 1.5 2003/09/03 20:19:12 jwp Exp $
** Copyright Jeffrey W Percival
** *******************************************************************
** Space Astronomy Laboratory
** University of Wisconsin
** 1150 University Avenue
** Madison, WI 53706 USA
** *******************************************************************
** Do not use this software without permission.
** Do not use this software without attribution.
** Do not remove or alter any of the lines above.
** *******************************************************************
*/
static char *rcsid = "$Id: cat2v6u2.c,v 1.5 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: cat2v6u2.c,v $
** convert a standard catalog entry into a cartesian unit vector.
** (cat2v6u1() does the same thing, in a visually more complicated way)
** the algorithm lets v6s2c() do all the work.
** *******************************************************************

the inputs are:
	r:	right ascension (radians)
	d:	declination (radians)
	rd:	proper motion in right ascension (arcseconds/cy)
	dd:	proper motion in declination (arcseconds/cy)
	px:	parallax in arcseconds
	rv:	radial velocity in km/s
	C:	number of days per century (tropical or julian)

** *******************************************************************
*/

#include "astro.h"

V6
cat2v6u2(double r, double d, double rd, double dd, double px, double rv, double C)
{
    double k;
    V6 v6;	/* the unit vector */

    k = 86400.0 * C / (IAU_AU/1000);

    v6 = v6init(SPHERICAL);
    v6SetR(v6, 1.0);
    v6SetAlpha(v6, r);
    v6SetDelta(v6, d);
    v6SetRDot(v6, k*rv*px);
    v6SetAlphaDot(v6, rd);
    v6SetDeltaDot(v6, dd);

    v6 = v6s2c(v6);

    return(v6);
}
