/* file: $RCSfile: v6r2cat.c,v $
** rcsid: $Id: v6r2cat.c,v 1.4 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: v6r2cat.c,v 1.4 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: v6r2cat.c,v $
** convert a cartesian state vector into a standard catalog entry
** this routine is the inverse of cat2v6r[12].c
** *******************************************************************


the inputs are:

	v6:	the 6-space state vector
	C:	number of days per century (tropical or julian)

the outputs are:
	r:	right ascension (radians)
	d:	declination (radians)
	rd:	proper motion in right ascension (arcseconds/cy)
	dd:	proper motion in declination (arcseconds/cy)
	px:	parallax in arcseconds
	rv:	radial velocity in km/s

** *******************************************************************
*/

#include "astro.h"

void
v6r2cat(double *r, double *d, double *rd, double *dd, double *px, double *rv, V6 v6, double C)
{
    double k = 86400.0 / (IAU_AU/1000);
    double ppx;	/* local copy */

    v6 = v6c2s(v6);
    *r = v6GetAlpha(v6);
    *d = v6GetDelta(v6);
    *rd = r2as(v6GetAlphaDot(v6)) * C;
    *dd = r2as(v6GetDeltaDot(v6)) * C;
    ppx = r2as(1 / v6mod(v6));
    *px = ppx;
    if (ppx > 0.001) {
	*rv = v6GetRDot(v6) / k;
    } else {
	*rv = 0;
    }

    return;
}
