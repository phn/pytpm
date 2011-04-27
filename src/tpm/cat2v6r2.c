/* file: $RCSfile: cat2v6r2.c,v $
** rcsid: $Id: cat2v6r2.c,v 1.5 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: cat2v6r2.c,v 1.5 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: cat2v6r2.c,v $
** convert a standard catalog entry into a cartesian unit vector.
** unlike cat2v6u1() and cat2v6u2(), this routine returns a true
** cartesian state vector, with components in AU and AU/day.
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
cat2v6r2(double r, double d, double rd, double dd, double px, double rv, double C)
{
    double k = 86400.0 / (IAU_AU/1000);
    V6 v6;	/* the state vector */

    v6 = v6init(SPHERICAL);
    if (px > 0.001) {
	v6SetR(v6, 1/as2r(px));
    } else {
	v6SetR(v6, 1e10);
    }
    v6SetAlpha(v6, r);
    v6SetDelta(v6, d);
    v6SetRDot(v6, k*rv);
    v6SetAlphaDot(v6, as2r(rd)/C);
    v6SetDeltaDot(v6, as2r(dd)/C);

    v6 = v6s2c(v6);

    return(v6);
}
