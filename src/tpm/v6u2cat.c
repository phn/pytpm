/* file: $RCSfile: v6u2cat.c,v $
** rcsid: $Id: v6u2cat.c,v 1.4 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: v6u2cat.c,v 1.4 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v6u2cat.c,v $
** convert a cartesian unit vector into a standard catalog entry
** this routine is the inverse of cat2v6u[12].c
** *******************************************************************


the inputs are:

	v6:	the 6-space unit vector
	C:	number of days per century (tropical or julian)

the outputs are:
	r:	right ascension (radians)
	d:	declination (radians)
	rd:	proper motion in right ascension (arcseconds/day)
	dd:	proper motion in declination (arcseconds/day)
	px:	parallax in arcseconds
	rv:	radial velocity in km/s

note: px must point to a valid parallax (e.g. the value supplied to
cat2v6u[12].c), which will be scaled by the length of the unit vector
being decoded.

** *******************************************************************
*/

#include "astro.h"

void
v6u2cat(double *r, double *d, double *rd, double *dd, double *px, double *rv, V6 v6, double C)
{
    double k;
    double ppx;	/* local value */

    k = C * 86400.0 / (IAU_AU/1000);

    v6 = v6c2s(v6);
    *r = v6GetAlpha(v6);
    *d = v6GetDelta(v6);
    *rd = v6GetAlphaDot(v6);
    *dd = v6GetDeltaDot(v6);
    ppx = *px / v6GetR(v6);
    *px = ppx;
    if (ppx > 0.001) {
	*rv = v6GetRDot(v6) / (k * ppx);
    } else {
	*rv = 0;
    }

    return;
}
