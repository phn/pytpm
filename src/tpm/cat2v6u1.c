/* file: $RCSfile: cat2v6u1.c,v $
** rcsid: $Id: cat2v6u1.c,v 1.5 2003/09/03 20:19:12 jwp Exp $
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
static char *rcsid = "$Id: cat2v6u1.c,v 1.5 2003/09/03 20:19:12 jwp Exp $";

/*
** *******************************************************************
** $RCSfile: cat2v6u1.c,v $
** convert a standard catalog entry into a cartesian unit vector.
** (cat2v6u2() does the same thing, in a visually simpler way)
** the algorithm is from yallop (AJ,97,274).
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
cat2v6u1(double r, double d, double rd, double dd, double px, double rv, double C)
{
    double k;
    V6 v6;	/* the unit vector */

    k = 86400.0 * C / (IAU_AU/1000);

    v6 = v6init(CARTESIAN);
    v6SetX(v6, cos(r)*cos(d));
    v6SetY(v6, sin(r)*cos(d));
    v6SetZ(v6, sin(d));
    v6SetXDot(v6, -rd*sin(r)*cos(d) - dd*cos(r)*sin(d));
    v6SetYDot(v6, rd*cos(r)*cos(d) - dd*sin(r)*sin(d));
    v6SetZDot(v6, dd*cos(d));
    v6IncXDot(v6, k*rv*px * v6GetX(v6));
    v6IncYDot(v6, k*rv*px * v6GetY(v6));
    v6IncZDot(v6, k*rv*px * v6GetZ(v6));

    return(v6);
}
